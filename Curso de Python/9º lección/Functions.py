def hello_world():
    print('Hello world!')
#hello_world()

def sum(num1,num2):
    print(num1+num2)
# sum(3,2)
# sum(3,27)
# sum(100,3) 
#a=(5)
def sum(num1=0,num2=0):
    if (type (num1)) is not int or (type (num2)) is not int:
        return 0
    return(num1+num2)
total=sum(1,6)
#print(total)


def multiple_items(*args):
    print(args)
    print(type(args))

# multiple_items('Dave','Sara','John')


def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))
mult_named_items(First='Dave',Last='Gray')