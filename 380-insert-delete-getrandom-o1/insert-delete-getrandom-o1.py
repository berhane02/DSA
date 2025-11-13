class RandomizedSet:

    def __init__(self):
        self.num_map = {}
        self.list_num = []

    def insert(self, val: int) -> bool:
        res = val not in self.num_map
        if res:
            self.num_map[val]=len(self.list_num)
            self.list_num.append(val)
        return res

    def remove(self, val: int) -> bool:
        res = val in self.num_map
        if res:
            indx = self.num_map[val]
            last_val = self.list_num[-1]
            self.list_num[indx] = last_val
            self.num_map[last_val] = indx
            self.list_num.pop()
            del self.num_map[val]
        return res

    def getRandom(self) -> int:
        return random.choice(self.list_num)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()