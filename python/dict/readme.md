# DICT



- 챗봇을 통해 어학사전 검색 기능 활용하기
- 프롬프트로 표제어를 입력받은 다음, 이를 네이버 사전 url에 부착하여 결과를 검색한다.
- 검색된 결과를 크롤링 하여 사용자에게 보여준다.
- 크롤링에는 BeautifulSoup기능을 사용했다.
- 안타깝게도 네이버가 사전 기능을 저작권 문제로 사용하지 못하게 해두어 결과를 성공적으로 가져올 수가 없었다.



## 필요 패키지

- import requests
- pip install bs4
- from bs4 import BeautifulSoup