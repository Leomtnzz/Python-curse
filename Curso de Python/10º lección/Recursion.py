# def add_one(num):
#     if (num>=9):
#         return num+1
    
#     total=num+1
#     print(total)

#     return add_one(total)
# mynewtotal=add_one(9)
# print(mynewtotal)


num=input('Enter your number\n')
num=int(num)  
while num<=9:  
    if num==4:
        print('Not today buddy')
    else:print(num+1)
    break
