# Dev Blog

티스토리처럼 **개발 공부 글**을 올리고, 코드 예제도 함께 남기는 저장소입니다.

## 글 목록

| 날짜 | 제목 | 카테고리 | 언어 |
| :--- | :--- | :--- | :--- |
| 2026-11-20 | [깃허브에 공부 글을 남기는 이유](./posts/spring/2026-11-20-프로필-readme와-학습-블로그.md) | spring | java |

## 구조

```text
posts/          공부 글 (티스토리처럼 장문)
  spring/
  java/
  cs/
  infra/
code/           실행·참고용 소스 코드
  java/
  javascript/
  typescript/
  python/
  sql/
  bash/
drafts/         작성 중인 글
templates/      새 글 템플릿
```

## 새 글 + 코드 작성법

1. `templates/post.md` 복사 → `posts/카테고리/YYYY-MM-DD-제목.md`
2. 글 본문에 코드 블록 작성 (언어 이름 필수)

````md
```java
System.out.println("hello");
```

```python
print("hello")
```
````

3. 코드가 길면 `code/언어/주제/`에 `.java`, `.py` 등으로 저장 후 글에서 링크
4. README 글 목록에 행 추가
5. 커밋

```bash
git add posts code README.md
git commit -m "post: JPA N+1 정리"
git push
```

## frontmatter 예시

```yaml
---
title: JPA N+1 문제 정리
date: 2026-11-20
category: spring
tags: [JPA, Hibernate]
languages: [java, sql]
summary: N+1이 생기는 이유와 fetch join 해결을 정리합니다.
---
```

`languages`에 사용한 프로그래밍 언어를 적어두면 나중에 찾기 쉽습니다.
