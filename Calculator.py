from math import*
x=float(input('enter:'))
y=float(input('enter:'))
class calculator():
    def __init__(self):
        '''calculator'''
class math_operation(calculator):
    def sum(self):
        print('sum of two digits')
        print(x+y)
    def sub(self):
        print('subtraction of two digit')
        print(x-y)
    def mul(self):
        print('multiplicatin of two digit')
        print(x*y)
    def div(self):
        print('division of two digits')
        print(x/y)
    def pow(self):
        print('power of first digit over second')
        print(pow(x,y))
    def squir_root(self):
        import math
        print('squir root of the digits')
        print('squirroot of first digit',math.sqrt(x))
        print('squirroot of second digit',math.sqrt(y))
class trigonometry(calculator):
        '''trigonometry solutions'''
        def sin(self):
            import math
            print('sin of first digit',math.sin(x))
            print('sin of second digit',math.sin(y))
        def cos(self):
            import math
            print('cos of first digit',math.cos(x))
            print('cos of second digit',math.cos(y))
        def tan(self):
            import math
            print('tan of first digit',math.tan(x))
            print('tan of second digit',math.tan(y))
class logorithm(calculator):
    def log(self):
        import math
        print('logorithm solutions')
        print('log of first digit',math.log(x))
        print('log of second digit',math.log(y))
obj1=math_operation()
obj2=trigonometry()
obj3=logorithm()

while True:
    op=input('enter the operator:')
    if op=='+':
        obj1.sum()
    elif op=='-':
        obj1.sub()
    elif op=='*':
        obj1.mul()
    elif op=='/':
        obj1.div()
    elif op=='**':
        obj1.pow()
    elif op=='root':
        obj1.squir_root()
    elif op=='sin':
        obj2.sin()
    elif op=='cos':
        obj2.cos()
    elif op=='tan':
        obj2.tan()
    elif op=='log':
        obj3.log()
    else:
        print('you have entered wrong operator')
    break    
input('press any key to exit:')
        
