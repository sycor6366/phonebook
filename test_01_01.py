import pickle
# l = [1,2,3]
# a = pickle.dumps(l)
# print(a)
# b = pickle.loads(a)
# print(b)


# d = {'name':'zhangsan','age':18}
# a = pickle.dumps(d)
# print(a)
# b = pickle.loads(a)
# print(b)


# class test:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
# R = pickle.dumps(test)
# print(R)
# print(pickle.loads(R))
# aa = test(name='zhangsan',age=18)
# r = pickle.dumps(aa)
# print(r)
# print(pickle.loads(r))

L = [1,2,3]
with open(('d://L.dat'),'wb') as f:
    pickle.dump(L,f)
with open('d://L.dat','rb') as f:
    print(pickle.load(f))


class Record:
    def __init__(self,name,phone_number):
        self.name = name
        self.phone_number = phone_number

with open('d:/Record.dat','wb') as f:
    pickle.dump(Record,f)
with open('d:/Record.dat','rb') as  f:
    print(pickle.load(f))

record = Record('zhangsan','131313131')
with open('d:/record.dat','wb') as f:
    pickle.dump(record,f)
with open('d:/record.dat','rb') as f:
    print(pickle.load(f))





