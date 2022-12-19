
from collections import defaultdict
from src.cell import Cell
from src.formula import Formula

class Spreadsheet:
    def __init__(self):
        self.data = defaultdict(self._cell_factory)

    def _cell_factory(self) -> Cell:
        return Cell(self,  formula=Formula(''))

    # returns value in cell
    def get_cell_value(self, cell: str) -> int | float:
        return self.data[cell].val
    
    def set_cell_value(self, cell: str, value: object):
        formula = Formula(value)
        # check if new formula introduces a cycle
        if self.detect_cycle(cell, formula):
            raise RecursionError("Cyclic reference detected in formula")

        self.data[cell].set_formula(Formula(value))

    def detect_cycle(self, start: str, formula: Formula) -> bool:
        stack = [formula]
        while stack:
            f = stack.pop()
            for reference in f.references:
                stack.append(
                    self.data[reference].formula
                )
                if reference == start:
                    return True
        return False


        

if __name__ == '__main__':
    s = Spreadsheet()

    s.set_cell_value('A1', '7')
    s.set_cell_value('A2','3')

    print(s.get_cell_value('A1'))
    s.set_cell_value('A3', '=A2/A1')
    print(s.get_cell_value('A3'))

    s.set_cell_value('A4', '=A1+A2+A3')
    print(s.get_cell_value('A4'))

    # # s.set_cell_value('A1','A4')
