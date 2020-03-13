## css

Cascading Style Sheets

> HTML은 문서의 구조화 CSS는 스타일을 정의.



> CSS 기본 사용법

**Selector(셀렉터) : h1

```css
h1{color:blue; font-size:15px;}
```



> CSS정의방법

- 인라인 : 해당 태그에 직접 style 속성을 활용

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>mySite</title>
</head>
<body>
    <h1 style="color:blue;font-size:100px">This is my site</h1>
</body>
</html>
```



- 내부참조 : HTML파일 내에 <style>태그에 지정

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>mySite</title>
    <style>
    h1{
        color : blue;
        font-size:100px    
    </style>
</head>
<body>
    <h1>This is my site</h1>
</body>
</html>
```



- 외부참조 : 외부CSS 파일을 <head>내 <link>를 통해 불러오기

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>mySite</title>
    <link rel="sylesheet" href="mystyle.css">
</head>
<body>
    <h1>This is my site</h1>
</body>
</html>
```

```css
h1 {
	color : blue;
	font-size:20px
}
```



> 선택자 

- HTML 문서에서 `특정한 요소`를 선택하여 스타일링 하기 위해서는 반드시 선택자라는 개념이 필요하다.
- 기초 선택자
- 고급선택자

- - 자손 선택자, 직계자손 선택자
  - 형제, 인접형제 선택자, 전체선택자
- 의사 클래스



> CSS 상속

- CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속한다.

- - 속성(프로퍼티) 중에는 상속이 되는 것과 되지 않는 것들이 있다.
  - 상속 되는 것 

  - - EX) Text관련 요소(font, color, text-align,visibility)등
  - 상독 되지 않는 것
  - - EX) Box model(with,height,margin등), position(position,top/right등)관련요소



> CSS적용 우선순위(cascading order)

- 중요도 (importance)

- - !important
- 우선순위(Specificity)
- - 인라인/id선택자/class선택자/요소  선택자
- 소스순서

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        h3{ color : violet !important;}
        p { color: green;}
        .blue { color : blue;}
        .skyblue {color : skyblue;}
        #red { color : red;}
    </style>
</head>
<body>
    <p>1</p> # green
    <p class="blue">2</p> #blue
    <P class="blue skyblue">3</P> #skyblue
    <p class="skyblue blue">4</p> #skyblue
    <p id = 'red' class='blue'>5</p> #red
    <h3 id='red' class='blue' >6</h3> #violet
    <p id='red' class="blue" style="color: yellow;">7</p> #yellow
    <h3 id='red' class="blue" style="color: yellow;">8</h3> #violet
</body>
</html>
```
