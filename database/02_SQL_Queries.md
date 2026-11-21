<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/banner-cs-dark.svg" />
  <img src="../assets/sections/banner-cs.svg" width="100%" alt="Database" />
</picture>

# 02. SQL 조회

**필요한 행과 열만 골라, 관계를 이어 답을 만든다.**

<p>
  <img src="https://img.shields.io/badge/Chapter-02-0F172A?style=flat-square" alt="Chapter 02" />
  &nbsp;
  <img src="https://img.shields.io/badge/Track-Database-334155?style=flat-square" alt="Database" />
  &nbsp;
  <img src="https://img.shields.io/badge/Status-Ready-16A34A?style=flat-square" alt="Ready" />
</p>

</div>

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/section-goals-dark.svg" />
  <img src="../assets/sections/section-goals.svg" width="100%" alt="Learning Goals" />
</picture>

이 장에서는 SQL의 **조회(SELECT)** 를 중심으로 본다.  
(쓰기는 INSERT/UPDATE 등, 스키마는 DDL이다.)  
SELECT → 필터 → 조인 → 집계 순서로 읽으면 대부분의 조회가 풀린다.

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/section-contents-dark.svg" />
  <img src="../assets/sections/section-contents.svg" width="100%" alt="Contents" />
</picture>

| # | 주제 | 한 줄 |
| :--- | :--- | :--- |
| 01 | SELECT · WHERE | 고르기 |
| 02 | JOIN | 이어 붙이기 |
| 03 | GROUP BY | 묶기 |
| 04 | 정렬·제한 | 페이지 |

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/section-concept-dark.svg" />
  <img src="../assets/sections/section-concept.svg" width="100%" alt="Concept" />
</picture>

### 01. SELECT · WHERE

**보고 싶은 열을 고르고, 조건으로 행을 줄인다.**

#### 직관

창고에서 “파란 상자만, 라벨만 읽어 와”다.

#### 핵심 성질

| 개념 | 내용 |
| :--- | :--- |
| `SELECT` | 투영(열 선택) |
| `WHERE` | 선택(행 필터) |
| `NULL` | “모름”. `=`가 아니라 `IS NULL` |
| 술어 | 인덱스가 탈 수 있는 형태가 유리 |

- **쓰임**: 목록 API, 관리 화면 필터

> `WHERE`에 함수로 열을 감싸면(`WHERE YEAR(created_at)=2026`) 인덱스 활용이 어려워질 수 있다.

---

### 02. JOIN

**키로 표를 이어 한 결과처럼 본다.**

#### 직관

회원 명부와 주문 장부를 회원 번호로 맞추는 일이다.

#### 핵심 성질

| 종류 | 감각 |
| :--- | :--- |
| INNER | 양쪽에 맞는 것만 |
| LEFT | 왼쪽은 지키고 오른쪽은 없으면 NULL |
| 다중 조인 | 단계마다 “무엇을 기준으로 붙였는지” |
| 중복 행 | 1:N 조인 후 행이 늘어남 |

- **쓰임**: 상세 조회, 리포트, ORM `join`의 실체

> 조인 결과가 예상보다 많으면, 관계가 1:N인데 집계 없이 붙인 경우가 많다.

---

### 03. GROUP BY

**같은 가방에 넣고 숫자를 센다.**

#### 직관

부서별로 인원·합계를 집계하는 회의 자료다.

#### 핵심 성질

| 개념 | 내용 |
| :--- | :--- |
| `GROUP BY` | 그룹 키 |
| 집계 함수 | `COUNT`, `SUM`, `AVG`, … |
| `HAVING` | 집계 결과 필터 |
| SELECT 규칙 | 표준적으로는 그룹 키 또는 집계만 (방언·설정에 예외 있음) |

- **쓰임**: 대시보드, “사용자당 주문 수”

> `COUNT(*)`와 `COUNT(col)`은 NULL 취급이 다르다.

---

### 04. 정렬·제한

**보여줄 순과 양을 정한다.**

#### 직관

대기표 정렬과 “앞에서 N명만”이다.

#### 핵심 성질

| 개념 | 내용 |
| :--- | :--- |
| `ORDER BY` | 정렬. 인덱스와 맞으면 유리 |
| `LIMIT` / `FETCH` | 개수 제한 |
| offset 페이지 | 깊어질수록 비용 큼 |
| keyset 페이지 | “이전 마지막 키 다음”이 안정적 |

- **쓰임**: 피드, 관리자 표, 무한 스크롤

> `ORDER BY` 없는 `LIMIT`은 순서가 보장되지 않는다.

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/section-summary-dark.svg" />
  <img src="../assets/sections/section-summary.svg" width="100%" alt="Summary" />
</picture>

### 무엇을 먼저 떠올릴까

| 상황 | 후보 |
| :--- | :--- |
| 조건 목록 | WHERE |
| 표 둘 이상 | JOIN |
| 합계·건수 | GROUP BY |
| 다음 페이지 | LIMIT + 안정적 정렬 |

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/section-next-dark.svg" />
  <img src="../assets/sections/section-next.svg" width="100%" alt="Next Chapter" />
</picture>

다음 장: **[03. 인덱스와 실행 계획](03_Indexes_Plans.md)** — 빠르게 찾아가게 만드는 길
