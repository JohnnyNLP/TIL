# 웹 크롤링 예제

```bash
$ pip install requests
```

requests를 인스톨한 뒤에 python에 다음 코드를 작성한다.

```python
import requests

res = requests.get("https://naver.com")
print(res.status_code)
```

> <Response [200]>



#### 	* http status code란?

- 모든 http 응답은 상태코드가 함께 전송된다.
  - 1xx (조건부 실행)
  - 2xx (성공)
  - 3xx (리다이렉션 완료)
  - 4xx (요청 오류) (클라이언트 잘못) ex) 404 (not found)
  - 5xx (서버 오류) (개발자 잘못)



따라서 Response [200]은 응답이 성공했다는 것을 의미한다.

```python
print(res.text)
```

> naver html 문서 전체가 반환된다.

즉, 원하는 페이지의 html 문서를 가져와 필요한 정보만 추출할 수 있게 된다.



BeautifulSoup을 이용한 코스피 지수 가져오기

```bash
pip install bs4
```

BeautifulSoup 패키지를 설치한다.



```python
import requests
from bs4 import BeautifulSoup

res = requests.get("https://finance.naver.com/sise/")
# print(res.text)

html = BeautifulSoup(res.text, 'html.parser')
# print(html)
kospi = html.select_one('#KOSPI_now') # 웹 검사 페이지의 copy selector를 이용한다.
print(kospi.text)
```

> 2,234.00

- select의 반환값은 list이다.
- select_one의 반환값은 하나의 태그 전체이다.
- 이렇게 반환된 태그에 .text 를 붙여주면 내용물만 출력된다.



### 네이버 실시간 검색어 가져오기



![1551071339978](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1551071339978.png)

- 우리가 필요로 하는 데이터를 담고 있는 태그를 검사한다.



```python
import requests
from bs4 import BeautifulSoup

url = "https://www.naver.com"
res = requests.get(url)
html = BeautifulSoup(res.text, 'html.parser')
searchrank = html.select_one('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul:nth-child(5) > li:nth-child(1) > a.ah_a > span.ah_k')
print(searchrank.text)
```

> 히든프라이스



### 네이버 실시간 검색어 20위까지 가져오기



![1551072041563](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1551072041563.png)

- 마찬가지로 해당하는 데이터들이 포함되어 있는 태그를 조사한다.

```python
import requests
from bs4 import BeautifulSoup

url = "https://www.naver.com"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
silgum = soup.select(".ah_list .ah_l .ah_item .ah_a .ah_k")
		#select는 태그가 여러 개일 경우에 리스트 값을 리턴한다.
for k in silgum:
    print(k.text)
```

> 히든프라이스
> 2019 아카데미 시상식
> ...
> 부라더
> 삼성라이온즈



### 환율 정보 가져오기

```python
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/marketindex/?tabSel=exchange#tab_section"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
dol_rate = soup.select_one("#exchangeList > li:nth-child(1) > a.head.usd > div > span.value")
en_rate = soup.select_one("#exchangeList > li:nth-child(2) > a.head.jpy > div > span.value")

print("미국 환율은 {0}원이고 \n엔화 환율은 {1}원입니다." .format(dol_rate.text,en_rate.text))
```

> 미국 환율은 1,121.00원이고 
> 엔화 환율은 1,012.83원입니다.

- 만약 copy selector가 너무 길다면 태그 검사를 통해 코드를 간결하게 만들 수도 있다.

```python
dol_rate = soup.select_one("#exchangeList li a.usd .head_info .value")
en_rate = soup.select_one("#exchangeList li a.jpy .head_info .value")
```

- 대신 부모태그를 건너뛰고 자식태그로 갈 수는 없으므로 최종 태그에서부터 하나씩 차례로 올라가야 정확하게 값을 가져올 수 있다.



### 환율 변동폭도 추가해보자

```python
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/marketindex/?tabSel=exchange#tab_section"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
dol_rate = soup.select_one("a.usd .head_info .value").text
dol_change = soup.select_one("a.usd .head_info .change").text
en_rate = soup.select_one("a.jpy .head_info .value").text
en_change = soup.select_one("a.jpy .head_info .change").text

print("미국 환율은 {0}원이고 \n엔화 환율은 {1}원입니다.\n변동폭은 각각 {2}원, {3}원입니다." .format(dol_rate, en_rate, dol_change, en_change))
```

> 미국 환율은 1,121.10원이고 
> 엔화 환율은 1,013.01원입니다. 
> 변동폭은 각각  3.90원,  1.83원입니다.



### 주의사항

![1551075142923](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1551075142923.png)

- iframe 태그는 웹 페이지 두 개(html태그)를 동시에 보여주고 싶을 때 사용하는데, iframe을 이용하고 있는 태그는 이러한 방식으로는 즉각적으로 가져올 수 없다.

- R Selenium은 페이지 로딩이 끝날 때까지 기다리기 때문에 이러한 것도 반영하여 가져올 수 있지만,  request같은 경우 최초 요청 시를 기준으로 하기 때문에 이러한 문제가 생기는 것,

  - 페이지 리로딩이 발생하는 경우
  - 새로고침 없이 계속해서 데이터가 갱신되는 경우

  

![1551075371607](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1551075371607.png)

> 출처 : https://www.slideshare.net/wangwonLee/2018-datayanolja-moreeffectivewebcrawling