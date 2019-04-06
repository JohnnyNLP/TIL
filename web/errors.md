# errors



## javax.servlet 임포트 오류

> ![1554550942312](assets/1554550942312.png)

- 이클립스에서 서블릿을 생성하자 다음과 같은 오류가 발생하였다.
- 프로젝트 내부에 서블릿을 인식하는 라이브러리가 설정되지 않으면 이와 같은 오류가 발생한다.
- 해결 방법은 다음과 같다.

> 프로젝트 우클릭 -> Build Path -> Configure Build Path -> libraries 탭 -> Add Library -> Server Runtime -> Apache Tomcat v8.0

- 서블릿은 서버와의 통신이 가능해야하기 때문에 서버를 제공하는 WAS의 라이브러리가 등록돼있어야만 이를 사용할 수 있는 것으로 보인다.

