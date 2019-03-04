import datetime

prompt = input("""
1. 출결 사항
2. 결석 기록
3. 출결 상세보기
원하는 기능의 번호를 입력하세요 : """)

dt = datetime.datetime.now()

if prompt == '1':
    with open('attend1.txt', 'r', encoding="utf-8") as f :
        lines = f.readlines()
        print(f"한국어정보처리 수업은 총 {len(lines)}회 결석하셨습니다. 남은 결석 횟수는 {10-len(lines)}회입니다.")
    with open('attend2.txt', 'r', encoding="utf-8") as f :
        lines = f.readlines()
        print(f"교양독일어중급 수업은 총 {len(lines)}회 결석하셨습니다. 남은 결석 횟수는 {10-len(lines)}회입니다.")
    with open('attend3.txt', 'r', encoding="utf-8") as f :
        lines = f.readlines()
        print(f"소설창작연습 수업은 총 {len(lines)}회 결석하셨습니다. 남은 결석 횟수는 {10-len(lines)}회입니다.")
        # for line in lines :
        #     print(line)
elif prompt == '2':
    absence = input("""
    1. 한국어정보처리
    2. 교양독일어중급
    3. 소설창작연습
    결석한 과목 번호를 입력하세요 : """)
    if absence == '1' :
        with open('attend1.txt', 'a', encoding="utf-8") as f :
            f.write(f"한국어정보처리 수업에 {dt.month}월 {dt.day}일 결석했습니다.\n")
    elif absence == '2' :
        with open('attend2.txt', 'a', encoding="utf-8") as f :
            f.write(f"교양독일어중급 수업에 {dt.month}월 {dt.day}일 결석했습니다.\n")
    elif absence == '3' :
        with open('attend3.txt', 'a', encoding="utf-8") as f :
            f.write(f"소설창작연습 수업에 {dt.month}월 {dt.day}일 결석했습니다.\n")
    else :
        print("과목 번호를 잘못 입력하셨습니다.")
elif prompt == '3':
    list = ('attend1.txt', 'attend2.txt', 'attend3.txt')
    text = ""
    for l in list :
        with open(l, 'r', encoding="utf-8") as f :
            lines = f.readlines()
            for line in lines :
                text += line
    print(text)

else :
    print("잘못된 명령어를 입력하셨습니다.")