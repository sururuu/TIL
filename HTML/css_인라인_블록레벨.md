## 인라인/블록 레벨 요소

### 대표적인 인라인 레벨 요소

> span / a / img / input, label / b, em, i, stron 등



### 대표적인 블록 레벨 요소

> div / ul, ol, li / p / hr / form 등



## **display

### display : inline

- 줄 바꿈이 일어나지 않는 행의 일부 요소
- `content 너비만큼` 가로폭을 차지한다.
- ** `width, height, margin-top, margin-bottom`을 지정할 수 없다.
- 상하여백은 line-height로 지정



### display : block

- 줄바꿈이 일어나는 요소
- `화면 크기 전체`의 가로폭을 차지한다.
- 블록 레벨 요소 안에 인랑니 레벨 요소가 들어갈 수 있음. 
- `기본 너비의 100%`, 100%의 너비를 가질 수 없다면 margin을 주기 떄문 



### display inline-block

- block과 inline레벨 요소의 특징을 모두 같는다.
- inline처럼 한 줄에 표시 가능
- block처럼 `width`,`height`,`margin` 속성을 모두 지정할 수 있다. 