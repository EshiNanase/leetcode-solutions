class RandomizedSet:

    def __init__(self):
        self.set = list()

    def insert(self, val: int) -> bool:
        if not val in self.set:
            self.set.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.set:
            self.set.remove(val)
            return True
        return False
        
    def getRandom(self) -> int:
        import random
        return random.choice(self.set)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()