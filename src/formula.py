import re

"""
    Simple formula parser that supports basic arithmetic operations on integers and references to other cells
    Anything more advanced is assumed outside scope of the problem
"""

class Formula:
    def __init__(self, formula: object, sup_ops=['+','-','*','/']):
        self._references = []
        self.formula = self.format_formula(formula)
        self.supported_operations = '|'.join(map(re.escape, sup_ops))
        self.extract_references()
    
    def __str__(self):
        return self.formula

    def format_formula(self, formula):
        formula = str(formula).lstrip('=')
        formula = formula.replace(' ', '')
        return formula

    def extract_references(self):
        split_form = re.split(self.supported_operations, self.formula)
        for arg in split_form:
            # naively assume that all non-numeric arguments must be cell references
            if not arg.isnumeric() and arg != '': 
                if not arg.isalnum():
                    raise ValueError("Unsupported characters in cell name")
                self._references.append(arg)
    
    def eval(self,params):
        if self.formula == '':
            return 0
        return eval(self.formula, params)

    @property
    def references(self):
        return self._references

if __name__ == '__main__':
    f = Formula('A1+A2-64+A3+9')
    print(f.references)