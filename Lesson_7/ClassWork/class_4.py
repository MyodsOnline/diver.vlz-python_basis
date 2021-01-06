class Iter:
    def __init__(self, start=0):
        self.i = start - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i <= 5:
            return self.i
        else:
            raise StopIteration

a = Iter(start=1)
for el in a:
    print(el)