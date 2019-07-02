
import re

# 예시 1
# data = """
# park 800906-1049118
# kim  700905-1059119
# """

# pat = re.compile("(\d{6})[-]\d{7}")
# print(pat.sub("\g<1>-*******", data))


# 예시 2
# text = "에러 1122 : 레퍼런스 오류\n 에러 1033: 아규먼트 오류"
# regex = re.compile("에러 1033")
# mo = regex.search(text)
# if mo != None :
#     print(mo.group())
#     print(mo.span())


# 예시 3
text = '문의사항이 있으면 032-232-3245로 연락주시기 바랍니다.'
regex = re.compile(r'\d{2,3}-\d{3,4}-\d{4}')
matchobj = regex.search(text)
phonenumber = matchobj.group()
print(phonenumber)
#r은 뒤에 나온 '\ << 얘를 혼동하지 않도록 문자 그대로 해석하라는 의미


# 예시 4
text = '문의사항이 있으면 032-232-3245로 연락주시기 바랍니다.'
regex = re.compile(r'(\d{2,3})-(\d{3,4}-\d{4})')
matchobj = regex.search(text)
areaCode = matchobj.group(1)
num = matchobj.group(2)
fullNum = matchobj.group()
print(areaCode, num)
