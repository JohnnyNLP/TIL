# Servlet



## 자바 웹 어플리케이션

- WAS에 설치되어 동작하는 어플리케이션
- HTML, CSS, 이미지, 자바로 작성된 클래스(servlet, package, interface 등), 각종 설정 파일 등이 포함된다.
- 인터넷에서 사용하는 쇼핑몰 사이트 등이 웹 어플리케이션이다.



### 구조

- WAS에 의해 동작하는 웹 어플리케이션은 특정 파일 구조를 따른다.
- 이와 같은 tree 구조를 확인하려면 워크스페이스 내 .metadata > .plugins > org.eclipse.wst.server.core > tmp0 > wtpwebapps > 해당 package로 들어가면 볼 수 있다.



#### WEB-INF 폴더

- 반드시 있어야 하는 폴더.
- **web.xml**이라는 파일이 존재 (배포 기술자. servlet 3.0 미만에서는 필수, 이후는 어노테이션 사용)
- lib 폴더 -> jar 파일들 수록
- classes 폴더 -> java 패키지, class들 포함



#### Resources 폴더

- 각종 폴더, 이미지, 리소스들
- html, css, java-script 등(프론트 기반)이 수록



## servlet이란?

- 자바 웹 어플리케이션의 구성요소 중 동적인 처리를 하는 프로그램의 역할

- WAS에서 동작하는 Java 클래스

- HttpServlet 클래스를 상속받아야 한다.

- 서블릿과 JSP로부터 최상의 결과를 얻으려면, 웹 페이지를 개발할 때 이 두가지를 조화롭게 사용하는 것이 좋다.

  ex) 웹 페이지를 구성하는 화면은 JSP로, 복잡한 프로그래밍은 서블릿으로 구현

- 동적 구성이라고 하는 이유는, 이미 만들어져 있는 페이지를 클라이언트에게 제공(html)하는 것이 아니라, 요청이 들어왔을 시에만 필요한 정보를 제공한다는 점에서 그러하다.



## servlet 작성하기

1. 3.0 이상

- web.xml 파일을 사용하지 않고 자바 어노테이션을 사용한다.

  ex) @WebServlet("/helloservlet")

- 단 spring과 같은 프레임워크를 사용할 때는 3.0 이상이라 하더라도 web.xml 파일이 필요할 수 있다.

- 어노테이션을 적용하면 URL이 다음과 같이 설정되는 것을 알 수 있다.

> ip주소:포트번호/패키지명/맵핑값
>
> localhost:8081/practice/helloservlet



2. 3.0 미만

- web.xml 파일에 mapping 해주어야 한다.
- 맵핑 양식은 다음과 같다.

```markup
<servlet>
        <description></description>
        <display-name>실제 서블릿명</display-name>
        <servlet-name>실제 서블릿명</servlet-name>
        <servlet-class>패키지명.실제 서블릿명</servlet-class>
    </servlet>
    <servlet-mapping>
        <servlet-name>실제 서블릿명</servlet-name>
        <url-pattern>/원하는 맵핑 주소/url-pattern>
    </servlet-mapping>
```