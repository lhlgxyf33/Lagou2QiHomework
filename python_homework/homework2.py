import yaml
class Animal:
    def __init__(self,name,color,age,sex):
        self.name = name
        self.color = color
        self.age = age
        self.sex =sex
    def shout(self):
        pass
    def run(self):
        pass

class Cat(Animal):
    def __init__(self,name,color,age,sex,maofa='短毛'):
        self.maofa = maofa
        Animal.__init__(self,name,color,age,sex)
    def catchingmice(self):
        return (f"姓名 : {self.name},颜色 : {self.color},年龄 : {self.age},性别 : {self.sex} ,毛发 : {self.maofa},捉到了老鼠")
    def maomao_shout(self,value):
        self.value=value

class Dog(Animal):
    def __init__(self,name,color,age,sex,maofa='长毛'):
        self.maofa = maofa
        Animal.__init__(self,name,color,age,sex)
    def watchhouse(self):
        return
    def wangwang_shout(self,value):
        self.value = value

#调用猫捉老鼠、狗看家方法
# maomao=Cat("benben","white",2,"female")
# print(maomao.catchingmice())
# gougou = Dog("doudou", "black", 6, "male")
# gougou.watchhouse()
# print(f"姓名 : {gougou.name},颜色 : {gougou.color},年龄 : {gougou.age},性别 : {gougou.sex} ,毛发 : {gougou.maofa}")
# #猫叫
# maomao.maomao_shout("喵喵！")
# print(maomao.value)
# #狗叫
# gougou.wangwang_shout("汪汪！")
# print(gougou.value)

if __name__== "__main__":
    with open("animal_data.yml",encoding='utf-8') as f:
        datas=yaml.safe_load(f)
    dw=datas['default']
    dw_name=dw['name']
    dw_color=dw['color']
    dw_age=dw['age']
    dw_sex=dw['sex']
    dw_maofa=['maofa']
    maomao = Cat(dw_name,dw_color,dw_age,dw_sex)
    gougou = Dog(dw_name,dw_color,dw_age,dw_sex)
    print(maomao.catchingmice())
    print(gougou.watchhouse())