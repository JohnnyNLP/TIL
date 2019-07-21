#가위바위보

import random

while(True):
    human = input('가위, 바위, 보 중 하나를 선택해주세요.')
    if (human in ['가위', '바위', '보']) :
        wintable = {'가위':'보', '바위':'가위', '보':'바위'}
        computer = random.choice(['가위', '바위', '보'])
        if (computer == wintable[human]):
            print('이겼습니다.')
        elif (computer == human) :
            print('비겼습니다.')
        else : print('졌습니다.')
        print('인간이 낸 것 :', human, '\n컴퓨터가 낸 것 :', computer)
        if not input('press any key'):
            break
    else :
        print ('올바른 패를 내주세요, 휴먼')
        raise ValueError
