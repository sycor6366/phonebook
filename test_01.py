# aa = []
# def add (**date):
#     aa.append({'name':name,'tel':tel,'id':id})
# def dell (**date):
#     for i in range(len(aa)):
#         if aa[i]['name'] == name and aa[i]['id'] == id and len(aa) >= 0:
#             aa.pop(i)
# def select(**date):
#     for i in range(len(aa)):
#         if aa[i]['name'] == name and aa[i]['id'] == str(id):
#             print(aa[i])
# def update(newname = '',newtel='',**date):
#     for i in range(len(aa)):
#         if aa[i]['name'] == name and aa[i]['id'] == id:
#             aa[i]['name'] = newname
#             aa[i]['tel'] = newtel
# q = 1
# while q == 1:
#     print(aa)
#     ss = int(input('1,增加，2，删除，3，查询，4，改,5,退出:', ))
#     if ss == 1:
#         name = input('name:',)
#         tel = input('tel:',)
#         id = input('id:',)
#         add(name = name ,tel =tel,id = id)
#     elif ss ==2:
#         name = input('name:',)
#         id = input('id:',)
#         dell(name = name ,id = id)
#     elif ss ==3 :
#         name = input('name:',)
#         id = input('id:',)
#         select(name = name ,id = id)
#     elif ss ==4:
#         name = input('name:',)
#         id = input('id:',)
#         new_name = input('new_name:',)
#         new_tel = input('new_tel:',)
#         # date ={'name':name,'id':id}
#         update(newname=new_name,newtel=new_tel,name=name,id=id)
#     elif ss ==5:
#         print(88)
#         q = 2
#     else:
#         print(88)
#         q = 2


class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry :
            print('Ahhh...')
            self.hungry = False
        else:
            print('NO,thanks')
class SongBird(Bird):
    def __init__(self):
        # super().__init__()
        self.sound = 'DSFSDF'
    def sing(self):
        print(self.sound)
sb = SongBird()
sb.sing()
sb.eat()
sb.eat()


