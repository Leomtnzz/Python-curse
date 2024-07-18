name='Dave'

# def greeting(name):
#      color='blue'
#      print(color)
#      print(name)
     #print(firstname)

#greeting('John')
count=1

def another():
    color='blue'
    global count
    count+=3
    print(count)
    def greeting(name):
        nonlocal color
        color+='Red'
        print(color)
        print(name)
    greeting('Dave')

another()