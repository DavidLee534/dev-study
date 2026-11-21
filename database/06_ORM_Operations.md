<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/banner-cs-dark.svg" />
  <img src="../assets/sections/banner-cs.svg" width="100%" alt="Database" />
</picture>

# 06. ORM과 운영

**객체로 다루되, SQL·스키마 변경·성능 함정을 시야에 둔다.**

<p>
  <img src="https://img.shields.io/badge/Chapter-06-0F172A?style=flat-square" alt="Chapter 06" />
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

ORM은 SQL을 숨기는 마법이 아니라 **매핑 계층**이다.  
프레임워크별 API는 Backend 트랙에 두고, 여기서는 공통 함정과 운영을 본다.

관련: Backend **[Spring JPA](../backend/spring/03_JPA_Persistence.md)** · **[Nest ORM](../backend/nestjs/03_ORM_DB.md)** · **[SQLAlchemy](../backend/fastapi/03_SQLAlchemy.md)**

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/section-contents-dark.svg" />
  <img src="../assets/sections/section-contents.svg" width="100%" alt="Contents" />
</picture>

| # | 주제 | 한 줄 |
| :--- | :--- | :--- |
| 01 | 매핑 | 객체 ↔ 표 |
| 02 | N+1 | 쿼리 폭탄 |
| 03 | 마이그레이션 | 스키마 변경 |
| 04 | 운영 감각 | 백업·관측 |

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/section-concept-dark.svg" />
  <img src="../assets/sections/section-concept.svg" width="100%" alt="Concept" />
</picture>

### 01. 매핑

**클래스 필드와 표 열을 이어 준다.**

#### 직관

통역기다.  
앱은 객체를 말하고, DB는 행을 말한다.

#### 핵심 성질

| 개념 | 내용 |
| :--- | :--- |
| Entity / Model | 표에 대응하는 타입 |
| Unit of Work | 변경 추적 후 한꺼번에 SQL |
| Lazy / Eager | 연관 로딩 시점 |
| 원시 SQL | 복잡한 쿼리는 도망치지 말고 드러내기 |

- **쓰임**: CRUD 기본 경로

> ORM이 만든 SQL을 한 번도 안 보면, 프로덕션에서 처음 본다.

---

### 02. N+1

**목록 N개를 가져온 뒤, 건마다 추가 쿼리가 나간다.**

#### 직관

명단을 받은 뒤 사람마다 다시 전화하는 일이다.  
한 번에 “같이 가져와”가 해결인 경우가 많다.

#### 핵심 성질

| 개념 | 내용 |
| :--- | :--- |
| N+1 | 1 + N번 왕복 |
| fetch join / eager | 한 쿼리(또는 소수)로 묶기 |
| 배치 로딩 | 묶음으로 추가 조회 |
| 증상 | 목록 API 지연, 로그에 같은 SELECT 반복 |

- **쓰임**: 연관이 있는 리스트 화면

> “로컬에선 빠른데 데이터가 늘면 죽음” — N+1·풀스캔 단골이다.

---

### 03. 마이그레이션

**스키마 변경을 코드처럼 버전으로 남긴다.**

#### 직관

DB에도 커밋 히스토리가 필요하다.  
손으로 프로덕션만 고치면 환경마다 어긋난다.

#### 핵심 성질

| 개념 | 내용 |
| :--- | :--- |
| migration | up/down 또는 전진 전용 스크립트 |
| 호환 | 앱 배포와 스키마 순서(확장→배포→정리) |
| 잠금 | 긴 ALTER는 서비스에 영향 |
| 데이터 백필 | 열 추가 후 값 채우기 |

- **쓰임**: Flyway, Liquibase, Alembic, Prisma migrate 등

> “컬럼 드롭”은 되돌리기 어렵다. **읽지 않음 → 배포 → 삭제** 단계가 안전하다.

---

### 04. 운영 감각

**백업, 느린 쿼리, 연결 수를 본다.**

#### 직관

창고 CCTV와 재고 실사다.  
장애 전에 신호를 보고, 장애 후엔 복구할 복사본이 있어야 한다.

#### 핵심 성질

| 개념 | 내용 |
| :--- | :--- |
| backup / PITR | 백업·시점 복구 가능 여부 |
| 커넥션 풀 | 앱·DB 사이 연결 한도 |
| 슬로우 로그 | 인덱스·쿼리 개선 입력 |
| 권한 | 앱 계정은 최소 권한 |

- **쓰임**: 온콜, 용량 계획, 배포 전 체크

> 스키마가 좋아도 백업·복구가 없으면 운영이 아니다. **복구 연습**이 운영이다.

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/section-summary-dark.svg" />
  <img src="../assets/sections/section-summary.svg" width="100%" alt="Summary" />
</picture>

### 무엇을 먼저 떠올릴까

| 상황 | 후보 |
| :--- | :--- |
| 객체로 CRUD | ORM 매핑 |
| 목록이 유난히 느림 | N+1 · EXPLAIN |
| 스키마 변경 | migration + 호환 순서 |
| 장애 대비 | 백업 · 풀 · 슬로우 로그 |

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/section-next-dark.svg" />
  <img src="../assets/sections/section-next.svg" width="100%" alt="Next Chapter" />
</picture>

Database 트랙 Ready.  
다음으로 비어 있는 트랙 예: **[frontend/](../frontend/README.md)** · **[security/](../security/README.md)** · **[mobile/](../mobile/README.md)**
