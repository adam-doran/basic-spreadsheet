from src.observer import Observer

class Cell(Observer):
    def __init__(self, sheet, formula, val=0):
        super().__init__()
        self.sheet = sheet
        self.val = val
        self.formula = formula

    def __str__(self) -> str:
        return str(self.val)

    def set_formula(self, formula):
        # unsubscribe from cells referenced by current formula
        if self.formula:
            for cell in self.formula.references:
                self.sheet.data[cell].unsubscribe(self)

        # subscribe to cells referenced by current formula
        self.formula = formula
        for cell in formula.references:
            self.sheet.data[cell].subscribe(self)

        # evaluate formula
        self.update()

    def eval_formula(self)-> int | float:
        cell_map = dict((k, self.sheet.data[k].val) for k in self.formula.references)
        return self.formula.eval(cell_map)

    def update(self):
        new_val = self.eval_formula()
        # don't bother notifying observers if value hasn't changed
        if self.val != new_val:
            self.val = new_val
            self.notify_observers()

    def notify_observers(self):
        for obs in self._observers:
            obs.update() 

    def subscribe(self, observer: Observer):
        self._observers.add(observer)

    def unsubscribe(self, observer: Observer):
        self._observers.remove(observer)
