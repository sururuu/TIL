## 표 (Table)

> `tr` (table row): 행

> `td`(table data) : 데이터 셀

> `th`(table heading) : 제목셀

> `tr` 태그 밑에 `td `혹은` th` 태그 사용!

```html
<table> <!--전체를 담고 있는 표-->
	<tr> <!--각 행-->
		<th>나이</th> <!--각 열의 제목을 담은 제목 셀-->
		<th>직업</th>
		<th>이름</th>
	</tr>
	<tr>
		<td>23</td> <!--데이터를 담은 데이터 셀-->
		<td>학생</td>
		<td>김00</td>
	</tr>
	<tr>
		<td>24</td>
		<td>직장인</td>
		<td>이00</td>
	</tr>
</table>
```



> 테이블 태그의 속성

- `rowspan` = '숫자' 는 숫자 만큼 행 방향으로 셀을 병합
- `colspan` = '숫자' 는 숫자 만큼 열 방향으로 셀을 병합





## 목록(List)

> 순서 없는 목록 `li`

: `<ul>`은 리스트의 항목을 감싸는 태그, `<li>`는 리스트에 나열할 항목을 담는 태그

```html
<ul>
    <li>침대</li>
    <li>배개</li>
</ul>
```



> 순서 있는 목록 

: `<ul>`이 `<ol>`로  변경 

```html
<ol>
    <ul>
        1교시
    </ul>
    <ul>
        2교시
    </ul>
</ol>
```



> 중첩 리스트

```html
<h3>
    오늘 할일
</h3>
<ul>
    <li>강의 듣기
    	<ol>
            <li>python</li>
            <li>web</li>
        </ol>
    </li>
</ul>
#- 강의듣기
	1. python
	2. web
```



## 목록 태그의 속성

#### ol 태그

```html
#start = '숫자' 는 리스트가 시작하는 숫자를 지정.
<ol start='3'>
    <li>국어</li>
    <li>수학</li>
</ol>
# 3. 국어
  4. 수학
```



```html
#type = '문자' 는 시작하는 문자를 지정. (ex, a,A,i,1 등)
<ol type="i">	
	<li>1</li>
	<li>2</li>
</ol>
## i. 1
   ii. 2
<ol type="I">	
	<li>1</li>
	<li>2</li>
</ol>
<ol type="a">	
	<li>1</li>
	<li>2</li>
</ol>
## a. 1
<ol type="A">	
	<li>1</li>
	<li>2</li>
</ol>
<ol type="1">	
	<li>1</li>
	<li>2</li>
</ol>
```



```html
#reversed 순서를 반대로 시작
<ol reversed>
    <li>국어</li>
    <li>수학</li>
</ol>
# 2. 국어
  1. 수학
```



#### li 태그

```html
# value = '숫자' 는 해당하는 리스트 아이템 번호를 지정
<ol>	
	<li value="3">국어</li>
	<li>수학</li>
	<li value="7">영어</li>
</ol>
# 3. 국어
  4. 수학
  7. 영어
```

