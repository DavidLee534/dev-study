<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../assets/sections/banner-cs-dark.svg" />
  <img src="../../assets/sections/banner-cs.svg" width="100%" alt="Backend" />
</picture>

# 02. Pydantic 검증

**스키마로 입력을 검증하고, 출력 계약과 문서를 같이 얻는다.**

<p>
  <img src="https://img.shields.io/badge/Chapter-02-0F172A?style=flat-square" alt="Chapter 02" />
  &nbsp;
  <img src="https://img.shields.io/badge/Track-FastAPI-334155?style=flat-square" alt="FastAPI" />
  &nbsp;
  <img src="https://img.shields.io/badge/Status-Ready-16A34A?style=flat-square" alt="Ready" />
</p>

</div>

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../assets/sections/section-goals-dark.svg" />
  <img src="../../assets/sections/section-goals.svg" width="100%" alt="Learning Goals" />
</picture>

FastAPI의 검증은 Pydantic 모델이 중심이다.  
Spring Bean Validation·Nest ValidationPipe와 같은 “입구 계약”이다.

대응: Spring **[04](../spring/04_검증과예외.md)** · Nest **[02](../nestjs/02_컨트롤러와파이프.md)**

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../assets/sections/section-contents-dark.svg" />
  <img src="../../assets/sections/section-contents.svg" width="100%" alt="Contents" />
</picture>

| # | 주제 | 한 줄 |
| :--- | :--- | :--- |
| 01 | BaseModel | 스키마 |
| 02 | Field / 제약 | 검증 규칙 |
| 03 | 응답 모델 | 출력 계약 |
| 04 | OpenAPI 자동 문서 | 문서화 이득 |

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../assets/sections/section-concept-dark.svg" />
  <img src="../../assets/sections/section-concept.svg" width="100%" alt="Concept" />
</picture>

### 01. BaseModel

**요청·응답 형태를 타입 있는 모델로 선언한다.**

#### 직관

양식 용지다.  
필드 이름과 타입이 칸이다.

#### 핵심 성질

| 개념 | 내용 |
| :--- | :--- |
| `BaseModel` | 파싱·검증·직렬화 |
| 타입 힌트 | `str`, `EmailStr`, nested model |
| 요청 바디 | 엔드포인트 인자 타입으로 선언 |

- **쓰임**: JSON 바디를 안전한 객체로 받기

---

### 02. Field / 제약

**필수·길이·범위·설명을 필드에 붙인다.**

#### 직관

필수 칸·글자 수 제한이다.  
틀리면 422와 함께 어느 필드인지 알려 준다.

#### 핵심 성질

| 개념 | 내용 |
| :--- | :--- |
| `Field(...)` | default, ge/le, min_length, description |
| 커스텀 validator | 교차 필드 규칙 |
| 422 Unprocessable Entity | 검증 실패의 기본 상태 |

- **쓰임**: 형식 검증. 업무 규칙(재고 없음)과는 층을 나눈다.

---

### 03. 응답 모델

**내보낼 필드를 `response_model`로 제한한다.**

#### 직관

공개용 명함이다.  
내부 객체에 비밀번호 해시가 있어도 응답 모델에 없으면 안 나간다.

#### 핵심 성질

| 개념 | 내용 |
| :--- | :--- |
| `response_model` | 출력 필터·문서 스키마 |
| 입력/출력 모델 분리 | CreateDto vs PublicDto |
| `model_config` | from_attributes 등 ORM 연동 |

- **쓰임**: 오버노출 방지, 클라이언트 계약 고정

---

### 04. OpenAPI 자동 문서

**스키마가 곧 Swagger/ReDoc 문서가 된다.**

#### 직관

메뉴판 자동 인쇄다.  
모델·경로·예제가 `/docs`에 나타난다.

#### 핵심 성질

| 개념 | 내용 |
| :--- | :--- |
| `/docs` · `/redoc` | 대화형·가독형 문서 |
| 스키마 동기화 | 코드 변경이 문서에 반영 |
| 설명 보강 | Field description, summary |

- **쓰임**: 프론트·외부 팀과 계약 공유 (SpringDoc과 같은 자리)

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../assets/sections/section-summary-dark.svg" />
  <img src="../../assets/sections/section-summary.svg" width="100%" alt="Summary" />
</picture>

### 무엇을 먼저 떠올릴까

| 상황 | 후보 |
| :--- | :--- |
| 바디 형태 | BaseModel |
| 필수·범위 | Field |
| 비밀번호 노출 위험 | response_model 분리 |
| 팀 공유 | OpenAPI `/docs` |

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../assets/sections/section-next-dark.svg" />
  <img src="../../assets/sections/section-next.svg" width="100%" alt="Next Chapter" />
</picture>

다음 장: **[03. SQLAlchemy](03_SQLAlchemy.md)** — 엔진·세션·ORM
