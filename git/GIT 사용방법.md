[TOC]

# GIT 사용방법

------



## 1. git init

- git bash를 실행시키고 로컬 저장소에서 git init 명령어를 수행한다.
- 앞으로 해당 .git 폴더가 설치된 경로 상에서 git 작업을 수행할 수 있다.



## 2. git add

- git add . 명령어는 현재 디렉토리의 모든 변경사항을 반영시키겠다는 의미이다.
- git add '특정 파일명'을 통해 원하는 파일만 변경사항을 적용시킬 수 있다.



## 3. git commit

- git commit -m "메모" 명령어는 지금까지 add된 파일들을 .git 폴더에 반영시키는 명령어이다.
- commit까지 마쳤다면 변경사항이 로컬 저장소에 반영된 상태이며, 이 상태에서 push 하지 않으면 git hub에는 반영되지 않는다.



## 4. git remote

- git remote add origin "해당 repository url" 명령어는 변경사항을 저장하고 싶은 원격 저장소를 설정하는 명령어이다.
- 만약 한번 추가했다면 다시 수행하지 않아도 된다.



## 5. git push

- git push 단계까지 적용시켜야만 자기가 변경한 내용들이 github에 안정적으로 저장된다.
- git push -u origin master 명령어는 현재 설정한 github 저장소의 master branch에다 파일을 저장하겠다는 명령어이다.
- -u 라는 옵션을 추가할 시, 2회차부터는 git push 까지만 수행하여도 이후의 수행 내용이 자동으로  기억된다.



## 6. Git의 역할

- 버전 관리
  - 바뀐 내용에 대한 기록을 log로 남길 수 있다.
  - 기존의 저장이 git의 commit에 해당.
  - 기능을 하나 변경했을 때마다 commit을 해준 뒤 log를 남긴다.
  - 변경 사항을 모아뒀다가 한번에 commit 하기보다는 그때그때 해주는 게 좋다.
- 기본 프로세스
  - 작업 -> add
  - 커밋 목록 생성 -> commit 
  - 저장된 commit -> push 
  - github에 저장

