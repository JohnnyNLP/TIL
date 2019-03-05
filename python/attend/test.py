classes = {"수업1":{"name":"한국어정보처리", "file":"attend1.txt"},
            "수업2":{"name":"교양독일어중급","file":"attend2.txt"},                       
            "수업3":{"name":"소설창작연습","file":"attend3.txt"}
}
print(classes.get("name"))
test = f"{classes.get('수업1').get('name')}"
print(test)

classess = {"name":["한국어정보처리", "교양독일어중급", "소설창작연습"],
            "file":["attend1.txt", "attend2.txt", "attend3.txt"]}
print(classess.get("name")[1])
print(len(classess.get("name")))

for i in range(3) :
    print(i)