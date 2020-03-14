## css

> css position

- `static` : 디폴트 값(기준위치)(기본 값)

- - *기본적인 요소의 배치 순서에 따름(좌측상단)
  - 부노 요소 내에서 배치될 떄는 부모 요소의 위치를 기준으로 배치
- 좌표 프로퍼티(top, bottom, left, right)를 사용하여 이동 가능(음수값도 가능)

- - `relative`(상대위치) : static 위치를 기준으로 이동
  - `absolute`(절대위치) : *static이 아닌 가장 가까이 있는 부모/조상 요소를 기준으로 이동!
  - `fixed`(절대위치) : 부모 요소와 관계 없이 브라우저를 기준으로 이동
  - - 스크롤시에도 항상 같은 곳에 위치

> css float 속성

- Float는 요소를 일반적인 흐름에서 벗어나도록 하는 속성 중 하나

- - ** 반드시 clear속성을 통해 초기화가 필요!




> float가 발생 시키는 문제 

- 자식요소의 float속성으로 인해 부모 영역의 높이가 사라지는 문제
- clear한 요소의 margin이 제대로 표현이 되지 않는 문제

 

> 해결방안

- **가상 요소 선택자를 활용한 방법

  ```html
  .clearfix::after{
   content:'';
   display:block;
   clear : both;
  }
  # 비어있는 내용으로 block을 만들고 그것을 clear한다. 
  ```

  