class MyList:
    def __init__(self, data=None):
        if data is None:
            self.lst = []
        else:
            self.lst = data

    def my_append(self, item):
        self.lst = self.lst + [item]
        return self.lst

    def my_pop(self):
        if len(self.lst) == 0:
            return "List is empty!"
        self.lst = self.lst[:-1]
        return self.lst

    def my_delete(self, index):
        if index >= len(self.lst):
            return "Index too big!"
        self.lst = self.lst[:index] + self.lst[index+1:]
        return self.lst
