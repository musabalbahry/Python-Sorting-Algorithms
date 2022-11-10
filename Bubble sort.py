from random import randint


class bubbleSort:
    def __init__(self, size):
        self.size = size
        self.array = []
        self.sorted = self.array
        self.random = 0
        self.count = 0
        self.done = False
        self.equal = 0
        while self.count != self.size:
            random = randint(1, self.size)
            if random in self.array:
                pass
            else:
                self.array.append(random)
                self.count += 1

    def sort(self):
        while self.done != True:
            self.equal = False
            for i in range(self.size):
                if i == self.size:
                    pass
                else:
                    if self.sorted[i] > [self.tmp]:
                        self.equal += 1
                        if self.equal == self.size:
                            self.done = True
                    else:
                        self.sorted[i], self.sorted[i + 1] = self.sorted[i+1], self.sorted[i]


new = bubbleSort(1000)
print(new.array)
new.array.sort()
print(new.sorted)
