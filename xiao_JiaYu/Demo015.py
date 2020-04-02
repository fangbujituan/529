'''
* 内容：定制元组
*
* data ：2019.06.26
* @author：fangbu
'''
class CountList:
    def __init__(self, *args):
        self.values = [x for x in args]
        self.count = {}.fromkeys(range(len(self.values)),0)
    def __len__(self):
        return len(self.values)
    def __getitem__(self, key):
        self.count[key] += 1
        return self.values[key]

c = CountList(7,8,9,10,11)
print(c[1])
print(c.count)