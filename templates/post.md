---
title: 글 제목
date: YYYY-MM-DD
category: spring
tags: [Spring, JPA]
languages: [java, sql]
summary: 이 글에서 다루는 내용을 한두 문장으로 적습니다.
---

# 글 제목

## 들어가며

왜 이 내용을 공부했는지, 어떤 문제를 겪었는지 적습니다.

## 내용

### 1. 개념

핵심 개념을 정리합니다.

### 2. 코드로 보기

글 안에 바로 코드를 적어도 되고, `code/` 폴더 파일을 링크해도 됩니다.

#### Java

```java
public class Example {
    public static void main(String[] args) {
        System.out.println("hello");
    }
}
```

#### SQL

```sql
select m.id, m.name, c.name as category
from menu m
join category c on c.id = m.category_id
where m.status = 'ACTIVE';
```

#### 다른 언어 예시

````md
```javascript
console.log('hello');
```

```python
print('hello')
```

```bash
./gradlew test
```
````

관련 전체 코드: [`code/java/...`](../code/java/)

### 3. 삽질과 해결

막혔던 지점과 해결 방법을 적습니다.

## 정리

- 핵심 포인트 1
- 핵심 포인트 2

## 참고

- 문서 / 강의 / 이슈 링크
