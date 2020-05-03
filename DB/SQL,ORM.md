## Django 에서 sqlite 작성하기

- django app 

  - `django_extensions` 설치
  - csv 파일에 맞춰 `models.py` 작성 및 `migrate`

- `db.sqlite3` 활용 및 데이터 반영

  - sqlite3 실행

  ```bash
  $ ls
  db.sqlite3 manage.py ----
  $ sqlite3 db.sqlite3
  ```

- csv 파일 data 업로드

  ```sqlite
  sqlite> .tables
  sqlite> .mode csv
  sqlite> .import users.csv user_user
  sqlite> SELECT COUNT(*) FROM users_user;
  1000
  ```

- 확인

  - sqlite3 에서 스키마 확인

  ```sqlite
  sqlite> .schema users_user
  ```

  

## SQL / ORM

### TABLE 생성

- django

    ```python
    # django
    class User(models.Model):
        first_name = models.CharField(max_length=10)
        last_name = models.CharField(max_length=10)
        age = models.IntegerField()
        country = models.CharField(max_length=10)
        phone = models.CharField(max_length=15)
        balance = models.IntegerField()
    # python manage.py makemigrations
    # python manage.py migrate
    ```

- SQL
    - sql.sqlite3에 동일하게 테이블 생성

        ```sql
        --sql
        sqlite> .tables
        sqlite> .schema users.user
        sqlite> .read users_user.sql  파일로 테이블 만들어서 가져오기
        ```

### 기본 CRUD 로직

1. 모든 user 레코드 조회

   ```python
   # orm
   user = User.objects.all()
   type(users)
   # => django.db.models.query.QuerySet
   # queryset만 sql문 출력 가능
   ```

      ```sql
   -- sql
   sqlite> SELECT * FROM users_user;
      ```

2. user 레코드 생성

   ```python
   # orm
   User.objects.create(
   	first_name='구름',
   	last_name='김',
   	age=100,
   	country='제주도',
   	phone='010-1110-222',
   	balance = 1000000000
   	)
   ```

   ```sql
   -- sql
   sqlite> INSERT INTO users_user ('first_name','lst_name','age','country','phone','balnce')
   VALUES ('근제','성',20,'서울','010-222-3333',10000000000);
   ```

3. 해당 user 레코드 조회

   ```python
   # orm
   User.objects.get(id=100)
   User.objects.get(pk=100)
   # get 은 쿼리 결과가 반드시 하나여야 한다.
   ```

      ```sql
   -- sql
   sqlite> SELECT * FROM users_user WHERE id=100
      ```

4. 해당 user 레코드 수정

   ```python
   # orm
   user = User.objects.get(id=100)
   user.last_name='성'
   user.save()
   ```

      ```sql
   -- sql
   sqlite> UPDATE users_user SET last_name='최' WHERE id=100
      ```

5. 해당 user 레코드 삭제

   ```python
   # orm
   User.objects.get(id=101).delete()
   ```
```
   
      ```sql
   -- sql
   sqlite> DELETE FROM users_user WHERE id=102;
```

### 조건에 따른 쿼리문

1. 전체 인원 수

   ```python
   # orm
   User.objects.count()
   ```

      ```sql
   -- sql
   sqlite> SELECT COUNT(id) FROM users_user;
   COUNT(id)
   100
      ```

2. 나이가 30인 사람의 이름

   ```python
   # orm
   User.objects.filter(age=30)
   #=> <QuerySet [<User: User object (5)>, <User: User object (57)>, <User: User object (60)>]>
   
   User.objects.filter(age=30).values('first_name')
   #=> <QuerySet [{'first_name': '영환'}, {'first_name': '보람'}, {'first_name': '은영'}]>
   
   type(User.objects.filter(age=30).values('first_name')[0])  
   #=> dict
   
   print(User.objects.filter(age=30).values('first_name').query)  
   #=> SELECT "users_user"."first_name" FROM "users_user" WHERE "users_user"."age" = 30
   
   user.objects.filter(age=30).values('first_name')
   ```

      ```sql
   -- sql
   SELECT first_name FROM users_user
   WHERE age=30;
      ```

3. 나이가 30살 이상인 사람의 인원 수

   대소관계

   1. `__gte`: >=

   2. `__gt`: >

   3. `__lte`: <=

   4. `__lt` : <

   ```python
   # orm
   User.objects.filter(age__gte=30).count()
   ```

   ```sql
   --sql
   SELECT COUNT(*) FROM users_user
   WHERE age>=30;
   ```

   

4. 나이가 30이면서 성이 김씨인 사람의 인원 수

   ```python
   # orm
   User.objects.filter(age=30).filter(last_name='김').count()
   User.objects.filter(age=30, last_name='김').count()
   ```

      ```sql
   -- sql
   SELECT COUNT(*) FROM user_user
   WHERE age=30 AND last_name = '김';
      ```
	- OR 연산을 하기 위해서는 Q 오브젝트가 필요하다.
	
	  ```sql
	  from django.db.models import Q
	  User.objects.filter(Q(age=30) | Q(last_name='김')).count()
	  ```


5. 지역번호가 02인 사람의 인원 수

  > i prefix는 case-insensitive의 의미를 지닌다. 

  ```
  iexact, contains, icontains, startswith, istartswith, endswith, iendswith
  ```

  ```python
  # orm
  User.objects.filter(phone__startswith='02-').count()
  ```

     ```sql
  -- sql
  SELECT COUNT(*) FROM users_user
  WHERE phone LIKE '02-%';
     ```

6. 거주 지역이 강원도이면서 성이 황씨인 사람의 이름

   ```python
   # orm
   User.objects.filter()
```
   
      ```sql
   -- sql
      ```



### 정렬 및 LIMIT, OFFSET

1. 나이가 많은 사람 10명

   ```python
   # orm
   User.objects.order_by('-age')[:10]
   ```

      ```sql
   -- sql
   SELECT * FROM users_user
   ORDER BY age DESC
   LIMIT 10;
      ```

2. 잔액이 적은 사람 10명

   ```python
   # orm
   User.objects.order_by('balance')[:10]
   ```

      ```sql
   -- sql
   SELECT * FROM users_user
   ORDER BY balance ASC
   LIMIT 10;
      ```

3. 성, 이름 내림차순 순으로 5번째 있는 사람

      ```python
   # orm
   User.objects.order_by('-last_name','-first_name')[4]
```
   
      ```sql
   -- sql
   SELECT * FROM users_user
   ORDER BY last_name DESC, first_name DESC
   LIMIT 1 OFFSET 4;
      ```



### 표현식

> 표현식을 위해서는 [aggregate]([https://docs.djangoproject.com/en/2.2/topics/db/aggregation/](https://docs.djangoproject.com/en/2.2/topics/db/aggregation/)) 를 알아야한다.

1. 전체 평균 나이

   ```python
   # orm
   from django.db.models import Avg
   User.objects.aggregate(Avg('age'))
   ```

      ```sql
   -- sql
   SELECT AVG(age) FROM users_user;
      ```

2. 김씨의 평균 나이

   ```python
   # orm
   from django.db.models import Avg
   user.objects.filter(last_name="김").aggregate(Aave('age'))
   ```

      ```sql
   -- sql
   SELECT AVG(age) FROM users_user
   WHERE last_name = '김';
      ```

3. 계좌 잔액 중 가장 높은 값

   ```python
   # orm
   from django.db.models import Max
   User.objects.aggregate(Max('balance'))
   ```

      ```sql
   -- sql
   Select max(balace) FROM users_user;
      ```

4. 계좌 잔액 총액

      ```python
   # orm
   from django.db.models import Sum
user.objects.aggregate(Sum('balance'))
   ```
   
      ```sql
   -- sql
   SELECT SUM(balance) FROM users_user;
      ```



### Group by

> annotate는 개별 item에 추가 필드를 구성한다.

1. 지역별 인원 수

   ```python
   # orm
   User.objects.values('country')
from django.db.models import Count
   User.objects.values('country').annotate(Count('country'))
   ```
   
   ```sql
   -- sql
   SELECT country ,COUNT(country) FROM users_user
   GROUP BY country;
   ```