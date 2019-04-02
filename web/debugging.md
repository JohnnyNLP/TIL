# Debugging

- 크롬 개발자 도구를 이용해 각 엘리먼트들의 html, css 정보들을 알 수 있다.
- computed 탭 -> 해당 엘리먼트에 적용된 최종 style 확인 가능
- 순서와 상관 없이 style selector에는 우선순위가 존재하며, 동일 엘리먼트에 여러 스타일이 적용되고 있을 때 우선 순위대로 반영한다.
- inline > internal > external
- id > class > tag
- 개발자 도구를 이용하면 임시적으로 html, css 정보를 변경하여 변경 사항을 테스트해볼 수 있다.