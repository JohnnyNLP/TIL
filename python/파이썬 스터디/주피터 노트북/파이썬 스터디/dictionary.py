'''
wintable = {
   'scissor' : 'paper',
   'rock' : 'scissor',
   'paper' : 'rock',
}

#print(wintable['scissor']);

def rsp(mine, yours):
    if mine == yours:
        return 'draw'
    elif wintable[mine] == yours:
        return 'win'
    else :
        return 'lose'
    
print(rsp('scissor', 'rock'))
print(rsp('rock', 'rock'))
print(rsp('rock', 'scissor'))
'''

'''
ages = {'aa':25, 'bb':23, 'cc':21}
for key in ages.keys():
    print('{}의 나이는 {}입니다.'.format(key,ages[key]))
for key in ages:
    print('{}의 나이는 {}입니다.'.format(key,ages[key]))
for key,value in ages.items():
    print('{}의 나이는 {}입니다.'.format(key,value))
'''

tuple1 = (1, 2, 3)
print(tuple1)
tuple2 = 1, 2, 3
print(tuple2)
