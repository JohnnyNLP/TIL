#quiz 3 6-1
from datetime import datetime, date, time

# 날짜를 입력받는다.
str1 = input('"19960109"와 같은 형태로 날짜를 입력하세요>')
dt1 = datetime.strptime(str1, "%Y%m%d")

# 현재 날짜와 비교한다.
dt2 = datetime.now().replace(hour=0, minute=0, second=0)
delta = dt2 - dt1

# 현재와 며칠 전/후인지 출력한다.
print(delta.days)