import datetime

prompt = input("""
1. 출결 사항
2. 결석 기록
3. 출결 상세보기
원하는 기능의 번호를 입력하세요 : """)

dt = datetime.datetime.now()
# repeat = ("수업1", "수업2", "수업3")
# classes = {"수업1":{"name":"한국어정보처리", "file":"attend1.txt"},
#             "수업2":{"name":"교양독일어중급","file":"attend2.txt"},                       
#             "수업3":{"name":"소설창작연습","file":"attend3.txt"}
# }
classes = {"name":["한국어정보처리", "교양독일어중급", "소설창작연습"],
            "file":["attend1.txt", "attend2.txt", "attend3.txt"]}

if prompt == '1':
    for r in range(3) :
        with open(classes.get("file")[r], 'r', encoding="utf-8") as f :
            lines = f.readlines()
            print(f"{classes.get('name')[r]} 수업은 총 {len(lines)}회 결석하셨습니다. 남은 결석 횟수는 {10-len(lines)}회입니다.")    
    # with open(classes.get("수업1").get("file"), 'r', encoding="utf-8") as f :
    #     lines = f.readlines()
    #     print(f"한국어정보처리 수업은 총 {len(lines)}회 결석하셨습니다. 남은 결석 횟수는 {10-len(lines)}회입니다.")
    # with open('attend2.txt', 'r', encoding="utf-8") as f :
    #     lines = f.readlines()
    #     print(f"교양독일어중급 수업은 총 {len(lines)}회 결석하셨습니다. 남은 결석 횟수는 {10-len(lines)}회입니다.")
    # with open('attend3.txt', 'r', encoding="utf-8") as f :
    #     lines = f.readlines()
    #     print(f"소설창작연습 수업은 총 {len(lines)}회 결석하셨습니다. 남은 결석 횟수는 {10-len(lines)}회입니다.")
elif prompt == '2':
    absence = input(f"""
    1. {classes.get("name")[0]}
    2. {classes.get("name")[1]}
    3. {classes.get("name")[2]}
    결석한 과목 번호를 입력하세요 : """)
  
    if absence == '1' :
        with open(classes.get("file")[0], 'a', encoding="utf-8") as f :
            f.write(f"{classes.get('name')[0]} 수업에 {dt.month}월 {dt.day}일 결석했습니다.\n")
    elif absence == '2' :
        with open(classes.get("file")[1], 'a', encoding="utf-8") as f :
            f.write(f"{classes.get('name')[1]} 수업에 {dt.month}월 {dt.day}일 결석했습니다.\n")
    elif absence == '3' :
        with open(classes.get("file")[2], 'a', encoding="utf-8") as f :
            f.write(f"{classes.get('name')[2]} 수업에 {dt.month}월 {dt.day}일 결석했습니다.\n")
    else :
        print("과목 번호를 잘못 입력하셨습니다.")
elif prompt == '3':
    list = list(classes.get("file"))
    # list = ('attend1.txt', 'attend2.txt', 'attend3.txt')
    text = ""
    for l in list :
        with open(l, 'r', encoding="utf-8") as f :
            lines = f.readlines()
            for line in lines :
                text += line
    print(text)

else :
    print("잘못된 명령어를 입력하셨습니다.")