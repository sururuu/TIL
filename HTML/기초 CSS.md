## 기초 CSS

> 크기 단위(상대)

- PX
- %
- em : 배수단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐.
- rem : 최상위 요소(html)의 사이즈를 기준으로 배수 단위를 가짐.
- Viewport 기준 단위
- - vw, vh, vmin,vmax



> CSS 문서표현

- 변헝 서테(<strong>, <em> -> 강조 의미)
- color, background-image, background-color
- 목록 꾸미기



> Box model 구성(margin)

1. Margin : 테두리 바깥의 외부 여백, 배경색 지정 x
2. Border : 테두리 영역
3. Padding : 테두리 안쪽의 내부 여백, 요소에 적용된 배경의 컬러/이미지느느 패딩까지 적용
4. Content : 실제 내용이 위치 

![image-20200310235938836](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200310235938836.png)

```css
.margin{
 margin-top : 10px;
 margin-right : 20px;
 margin-bottom : 30px;
 margin-left : 40px;
}
```



> Box model 구성(padding)



![](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200311000326725.png)





```css
.margin-padding{
    margin:10px;
    padding:39px;
}
```



> Box model 구성(margin/padding)

 : Shorthand를 통해서 표현 가능. 

![image-20200311000510255](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200311000510255.png)

```css
.margin-1{
 margin:10px;
}

.margin-2{
 margin:10px20px;
}

.margin-3{
 margin:10px20px30px;
}

.margin-4{
 margin:10px20px30px40px
}
```



> Box  model 구성(border)

: Shorthand를 통해서 표현 가능. 



```css
.border{
 border-width : 2px;
 border-style : dashed;
 border-color : black;
}

.border{
 border:2pxdashedblack;
}
```



> box-sizing

- 기본적으로 모든 요소의 `box - sizing`은 `content-box'

- - padding 을 제외한 순수 contents영역만을 box로 지정
- 일반적으로 영역을 볼때는 border까지의 너비를 100px보는 것을 원함

- - box-sizing을 border-box

