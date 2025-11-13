class Spreadsheet:
    def __init__(self, rows):
        self.rows = rows
        self.cells = {}  # store cell values like {"A1": 10, "B2": 15}

    def setCell(self, cell, value):
        self.cells[cell] = value

    def resetCell(self, cell):
        if cell in self.cells:
            del self.cells[cell]

    def getValue(self, formula):
        # Formula looks like "=A1+B2" or "=5+7"
        formula = formula[1:]  # remove "="
        x, y = formula.split('+')

        def get_val(token):
            # check if it's a number
            if token.isdigit():
                return int(token)
            # else it's a cell name
            return self.cells.get(token, 0)

        return get_val(x) + get_val(y)


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)