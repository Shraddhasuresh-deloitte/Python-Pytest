class StringClass:
    def __init__(self, demo):
        self.demo = demo

    def lis(self):
        return list(self.demo)

    def length(self):
        return len(self.demo)


class PairsPossible(StringClass):
    def pair(self, test_list):
        res = [(n, object1) for idx, n in enumerate(test_list) for object1 in test_list[idx + 1:]]
        print(res)


n = input("Enter a string :")
object1 = StringClass(n)


h = object1.lis()
object2 = PairsPossible(object1)
object2.pair(h)
