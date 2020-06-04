#无参数方法调用
def no_number():
    print()
no_number()  #调用时没有参数，打印为空

#有参数方法调用
def have_number():
    a=1
    b=a+2
    print(a,b)
have_number()  #调用时有参数，打印方法里定义的a，b的值

##return无值方法调用例
def have_return(a3=10):
    if a3==10:
        return
    else:
        a3!=10
        return
print(have_return()) #1.打印调用的方法，return无返回值时传递默认值参数none而不是空

##return有值和无值方法调用例
def have2_return(a3=9):
    if a3==10:
        return True
    else:
        a3!=10
        return False
        i=10
        print(i)
print(have2_return()) #2.return有返回值时正常传递返回参数,并且不执行return后面的代码
