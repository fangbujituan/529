苏联的解体
brand = ['李宁','耐克','阿迪']
slogn = ['a','b','c']
#
# dict1 = {'李宁':'a','耐克':'b','阿迪':'c'}
dict1 = {}
dict1 = dict1.fromkeys(range(32),"wode")
for x in dict1.keys():
    print(x)

for x in dict1.values():
    print(x)

for x in dict1.items():
    print(x)