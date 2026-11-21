<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../assets/sections/banner-cs-dark.svg" />
  <img src="../../assets/sections/banner-cs.svg" width="100%" alt="Backend" />
</picture>

# 05. 예외와 인터셉터

**실패를 공통 응답으로 돌리고, 로깅·변환을 가로지른다.**

<p>
  <img src="https://img.shields.io/badge/Chapter-05-0F172A?style=flat-square" alt="Chapter 05" />
  &nbsp;
  <img src="https://img.shields.io/badge/Track-NestJS-334155?style=flat-square" alt="NestJS" />
  &nbsp;
  <img src="https://img.shields.io/badge/Status-Ready-16A34A?style=flat-square" alt="Ready" />
</p>

</div>

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../assets/sections/section-goals-dark.svg" />
  <img src="../../assets/sections/section-goals.svg" width="100%" alt="Learning Goals" />
</picture>

Nest의 Exception Filter는 Spring `@ControllerAdvice`에, Interceptor는 AOP·응답 래핑에 가깝다.  
미들웨어와의 **실행 순서**만 구분하면 디버깅이 쉬워진다.

대응: Spring **[04. 검증과 예외](../spring/04_Validation_Exception.md)**

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../assets/sections/section-contents-dark.svg" />
  <img src="../../assets/sections/section-contents.svg" width="100%" alt="Contents" />
</picture>

| # | 주제 | 한 줄 |
| :--- | :--- | :--- |
| 01 | Exception Filter | 공통 에러 응답 |
| 02 | HttpException | 의도한 실패 |
| 03 | Interceptor | 로깅·변환 |
| 04 | 미들웨어와의 차이 | 실행 순서 |

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../assets/sections/section-concept-dark.svg" />
  <img src="../../assets/sections/section-concept.svg" width="100%" alt="Concept" />
</picture>

### 01. Exception Filter

**예외를 잡아 표준 JSON으로 바꾼다.**

#### 직관

민원 창구다.  
어디서 터지든 같은 양식의 답변을 돌려준다.

#### 핵심 성질

| 개념 | 내용 |
| :--- | :--- |
| `@Catch` | 잡을 예외 타입 |
| `ExceptionFilter` | `catch`에서 응답 작성 |
| 전역 필터 | 앱 전체에 일관된 에러 바디 |

- **쓰임**: 필드 오류·NotFound·내부 오류 포맷 통일

---

### 02. HttpException

**의도한 HTTP 실패를 던진다.**

#### 직관

안내 방송이다.  
“리소스 없음”은 404, “권한 없음”은 403으로 명시한다.

#### 핵심 성질

| 개념 | 내용 |
| :--- | :--- |
| `NotFoundException` 등 | 상태 코드가 박힌 예외 |
| 메시지·객체 | 클라이언트에 줄 detail |
| 필터와의 관계 | 필터가 최종 바디 형태로 정리 |

- **쓰임**: 서비스/가드에서 의도된 거절

---

### 03. Interceptor

**핸들러 전후에 끼어 로깅·캐시·응답 래핑을 한다.**

#### 직관

통역·기록 담당이다.  
들어가기 전 스톱워치를 켜고, 나온 결과를 `{ data }`로 감쌀 수 있다.

#### 핵심 성질

| 개념 | 내용 |
| :--- | :--- |
| `NestInterceptor` | `intercept` + `next.handle()` |
| RxJS | 스트림으로 응답 가공 |
| 용도 | 로깅, timeout, 변환 |

- **쓰임**: 공통 응답 envelope, 성능 로그

---

### 04. 미들웨어와의 차이

**같은 “중간”이라도 걸리는 층이 다르다.**

#### 직관

건물 정문(미들웨어) vs 사무실 안 절차(가드·인터셉터·파이프)다.

#### 핵심 성질

| 단계 | 감각 |
| :--- | :--- |
| Middleware | Express/Fastify에 가까운 바깥층 |
| Guard | 인증·인가 게이트 |
| Interceptor | 핸들러 전후 AOP |
| Pipe | 인자 변환·검증 |
| Exception Filter | 예외가 난 뒤 응답으로 변환 (체인 한 칸이 아님) |

- **쓰임**: “왜 가드 로그가 안 찍히지?” → 미들웨어에서 이미 끝났는지 확인

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../assets/sections/section-summary-dark.svg" />
  <img src="../../assets/sections/section-summary.svg" width="100%" alt="Summary" />
</picture>

### 무엇을 먼저 떠올릴까

| 상황 | 후보 |
| :--- | :--- |
| 에러 JSON 통일 | Exception Filter |
| 의도한 4xx | HttpException |
| 응답 래핑·로깅 | Interceptor |
| 순서 혼란 | Middleware vs Guard 표 |

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../assets/sections/section-next-dark.svg" />
  <img src="../../assets/sections/section-next.svg" width="100%" alt="Next Chapter" />
</picture>

다음 장: **[06. 테스트](06_Testing.md)** — TestingModule과 e2e
