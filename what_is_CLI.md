[TOC]

# CLI

> : Command Line Interface (<-> GUI)

- 글씨(명령어)만 입력해서 조작하는 방식
- 유닉스 shell, CP/M, DOS 등등이 이 방식을 사용



## 명령어 (리눅스)

- ls : 현재 디렉토리의 내용들을 나열
- cd : 현재 작업하는 디렉토리를 변경
- mkdir : 새로운 디렉토리 생성
- echo : 문자열 출력
- rm : 파일 지우기
- exit : 터미널 종료
- vi : 파일 에디터를 실행
  - i : insert 모드로 변경
  - esc : command 모드로 변경
    - w : 현재 파일명으로 저장
    - w [파일명] : 해당 파일명으로 저장
    - wq : 변경사항을 저장하고 종료
    - wq! : 저장하고 강제 종료
    - q : 저장하지 않고 종료
    - q! : 강제 종료
    - f [파일명] : 해당 파일명으로 변경
    - $ : 파일의 맨 끝줄로 이동
  - a : 현재 커서 바로 다음에 삽입
  - o : 현재 줄 다음 위치에 삽입
  - x : 커서가 위치한 곳의 글자 1개 삭제
  - dw : 커서가 위치한 곳에서부터 띄어쓰기한 부분까지 단어 삭제
  - dd : 커서가 위치한 곳의 한 줄 삭제
  - u : 방금 수행한 명령 취소
  - yy : 현재 줄 버퍼로 복사 (ctrl+c)
  - p : 현재 커서 바로 아래 줄에 붙여넣기 (ctrl+v)
  - dd : 행 잘라내기 (ctrl+x)
  - k, j, h, l : 각각 커서 위치 상하좌우로 이동
  - 0 : 커서가 있는 줄의 맨 앞
  - $ : 커서가 있는 줄의 맨 뒤
  - ( : 현재 문장의 맨 처음
  - ) : 현재 문장의 맨 끝
  - { : 현재 문단의 처음
  - } : 현재 문단의 끝
  - 숫자 -  : 숫자만큼 윗 줄로 이동
  - 숫자 + :  숫자만큼 아랫 줄로 이동
  - G : 파일의 맨 끝으로 이동
  - r : 한 문자만 변경
  - cc : 커서가 있는 줄의 내용 변경
- cat : 파일 내용 출력



## Chocolatey

- 윈도우에 걸맞은 프로그램 -> 나중에 한번 사용해 볼것
- choco install git -y ... git 설치 가능
- choco install python --version 3.6.7 ... python 설치 가능



## Git bash를 이용해 프로그램 실행하기

- vscode를 설치하면 code 명령어를 사용할 수 있다.

```bash
cd Desktop/
mkdir local_python
cd local_python/
code .
```

- vscode가 현재 폴더를 기준으로 실행된다.
- 실행된 vscode에서 ctrl + `
- terminal의 플러스 버튼을 누른 뒤에 customize => git bash 설정
- default shell 이 bash로 변경된다.

![1551058110110](assets/1551058110110.png)

> 적용된 상태

```BASH
$ touch browser.py
```

- 파이썬 파일 생성
- Recommendation에 따라 Python과 Linter Extension을 설치해준다

- Korean Langauge Pack Extension을 설치하면 한국말 설정으로 바꿀 수 있다.



## Python에서 코드 작성하기

```python
import webbrowser

url = "https://search.naver.com/search.naver?query="
keyword = ["아이유", "itzy", "위너", "빅백"]
for k in keyword :
    webbrowser.open(url+k)
```

위 코드를 browser.py에 작성하고 bash에서

```bash
$ python browser.py
```

로 실행하면 각 keyword가 입력된 검색창 4개가 실행된다.

