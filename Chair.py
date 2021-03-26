class Chair:
    def __init__(self, x, y, table):
        self.x = x         # x cor
        self.y = y         # y cor
        self.table = table # table instance that this chair is around
        self.taken = False # no one sitting on the table 