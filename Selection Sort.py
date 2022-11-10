from random import randint


class selectionSort:
    def __init__(self, size):
        self.size = size
        self.array = []
        self.random = 0
        self.solvedArr = []
        count = 0
        while count != self.size:
            self.random = randint(1, self.size)
            if self.random in self.array:
                pass
            else:
                self.array.append(self.random)
                count += 1

    def sort(self):
        tmp = self.array.copy()
        for i in range(self.size):
            self.solvedArr.append(min(self.array))
            self.array.remove(min(self.array))
        self.array = tmp


test = selectionSort(4)
test.sort()
print(test.array)
print(test.solvedArr)