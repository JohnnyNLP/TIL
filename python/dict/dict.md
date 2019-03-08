# 챗봇 기능에 사전 검색 기능 추가

- 네이버 사전의 경우 핸드폰으로 매번 앱을 시작하고 사전 탭을 찾아 들어가야 하는 번거로움이 있었다.
- 만약 telegram 챗봇에서 '사전 keyword' 형태로 별도의 앱 실행 없이 바로 사전을 이용할 수 있다면 어떨까?
- 이전에 배웠던 웹 크롤링 기술을 이용하여 네이버 사전에서 해당 표제어에 대한 검색 결과를 가져오는 것이 이번 프로젝트의 목표이다.



## 코드 작성

- 코드 작성 부분의 상당부분은 web_crawling.md를 참조하였다.

![1551787866773](assets/1551787866773.png)

- query= 이하 부분에 검색 키워드가 들어가는 점에 착안하여 변수 설정을 다음과 같이 한다.

```python
url = 'https://dict.naver.com/dekodict/#/search?query='
word = '사전'
```

![1551787849510](assets/1551787849510.png)

- 사전 검색 결과를 담고 있는 html 문서의 css selector는 다음과 같았다.

```python
#searchPage_entry > ul > li:nth-child(1) > ul > li:nth-child(1) > p > span
```

- 위 두 정보를 종합하여 최종적으로 작성된 코드는 다음과 같다.

```python
import requests
from bs4 import BeautifulSoup

url = 'https://dict.naver.com/dekodict/#/search?query='
word = '사전'

res = requests.get(url+word)
print(res.status_code)
soup = BeautifulSoup(res.text, 'html.parser')
result = soup.find_all('#searchPage_entry > ul > li:nth-child(1) > ul > li:nth-child(1) > p > span')
print(result)
```

> 200
>
> []

## 문제 당면

- 그러나 어쩐 이유에선지 자꾸만 결과가 빈 리스트로 출력되는 걸 알 수 있었다.
- 네트워크 연결 문제인가 해서 res.status_code로 확인해보아도 200번이 리턴되어왔다.
- 이 부분에 대한 해결은 차차 해나가도록 하겠다.



## 재도전

- 사전 페이지를 페이지 소스 보기로 조회해보니 다음과 같이 되어 있었다.

> ![1552013990868](assets/1552013990868.png)

- 문제 해결의 실마리가 조금 보이는 듯하다.
- 해당 사전 페이지는 직접 검색 결과 태그를 가지고 있는 것이 아니라 태그를 지니고 있는 다른 참조주소를 가져와서 보여주고 있는 것 같았다.
- 눈에 띄는 부분은 window.appChunks 라는 객체인데, 딕셔너리 형태로 각종 url을 전달하는 것을 볼 수 있다. 이를 통해 짐작컨데, 사전을 사용하는 API에게 json 형태로 요청을 보내는 게 아닐까 싶다.
- ssl.pstatic.net이라는 주소에 착안하여 pstatic을 검색해보니 naver api와 관련된 것이 확실해 보였다.
- 그러던 중 네이버 developer 포럼에서 이와 유사하게 어학사전 정보를 가져오고 싶다는 문의글을 발견하였다.

> 해당 url : https://developers.naver.com/forum/posts/9711

- 문제는 사전 기능은 저작권 이슈 때문에 접근이 제한되어 있다는 것이었다.
- 이로 인해 나의 사전 프로젝트는 허무하게 좌절되고 말았다.



## 대안

- 아쉽게도 직접 구현하지는 못하지만, 검색 중에 독한사전을 독자적으로 구축한 프로그램을 제공하고 있는 사이트를 발견했다.

> 해당 url : https://german.kr

- 사전을 좀더 유용하고 편리하게 사용하려는 사람이 제법 있다는 데에 공감대를 느끼며 이번 프로젝트를 정리하도록 하겠다.