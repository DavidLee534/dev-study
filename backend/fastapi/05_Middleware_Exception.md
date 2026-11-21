<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../assets/sections/banner-cs-dark.svg" />
  <img src="../../assets/sections/banner-cs.svg" width="100%" alt="Backend" />
</picture>

# 05. 미들웨어와 예외

**요청 전후 처리와 공통 에러 응답을 맞춘다.**

<p>
  <img src="https://img.shields.io/badge/Chapter-05-0F172A?style=flat-square" alt="Chapter 05" />
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

미들웨어는 바깥 층, `exception_handler`는 실패 계약의 허브다.  
Nest Filter/Interceptor·Spring Advice와 같은 문제를 푼다.

대응: Spring **[04](../spring/04_Validation_Exception.md)** · Nest **[05](../nestjs/05_Exception_Interceptor.md)**

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../assets/sections/section-contents-dark.svg" />
  <img src="../../assets/sections/section-contents.svg" width="100%" alt="Contents" />
</picture>

| # | 주제 | 한 줄 |
| :--- | :--- | :--- |
| 01 | Middleware | 요청 전후 |
| 02 | exception_handler | 공통 에러 |
| 03 | HTTPException | 의도한 실패 |
| 04 | 로깅·CORS | 운영 감각 |

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../assets/sections/section-concept-dark.svg" />
  <img src="../../assets/sections/section-concept.svg" width="100%" alt="Concept" />
</picture>

### 01. Middleware

**모든 요청의 바깥에서 전후 처리를 한다.**

#### 직관

건물 정문이다.  
들어오고 나가는 모든 손님을 기록하거나 헤더를 붙인다.

#### 핵심 성질

| 개념 | 내용 |
| :--- | :--- |
| ASGI 미들웨어 | 요청·응답 래핑 |
| 측정·로깅 | 지연 시간, request id |
| Depends와 층 | 미들웨어는 더 바깥 |

- **쓰임**: 공통 헤더, 타이밍, 간단한 차단

---

### 02. exception_handler

**예외 타입별로 표준 JSON을 돌린다.**

#### 직관

민원 창구다.  
검증 실패·도메인 실패·미처리 예외를 각각의 양식으로 정리한다.

#### 핵심 성질

| 개념 | 내용 |
| :--- | :--- |
| `@app.exception_handler` | 타입 → 응답 |
| RequestValidationError | Pydantic 422 커스터마이즈 |
| 내부 정보 마스킹 | 5xx에 스택 노출 금지 |

- **쓰임**: 클라이언트와 맞춘 에러 바디

---

### 03. HTTPException

**의도한 HTTP 오류를 던진다.**

#### 직관

안내 방송이다.  
없면 404, 권한 없으면 403.

#### 핵심 성질

| 개념 | 내용 |
| :--- | :--- |
| `status_code` / `detail` | 상태와 메시지 |
| 핸들러와 협력 | 최종 포맷은 handler가 정리 가능 |
| 업무 예외 매핑 | 도메인 예외 → HTTPException |

- **쓰임**: 경로·서비스에서의 의도된 거절

---

### 04. 로깅·CORS

**관측과 브라우저 접근 정책을 붙인다.**

#### 직관

CCTV와 출입 명부다.  
CORS는 브라우저가 다른 출처 API를 호출할 때의 규칙이다.

#### 핵심 성질

| 개념 | 내용 |
| :--- | :--- |
| 구조화 로그 | request id, path, status |
| `CORSMiddleware` | allow_origins 등 |
| 운영 | 너무 넓은 `*` 는 개발용 감각 |

- **쓰임**: SPA 프론트 연동, 장애 추적

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../assets/sections/section-summary-dark.svg" />
  <img src="../../assets/sections/section-summary.svg" width="100%" alt="Summary" />
</picture>

### 무엇을 먼저 떠올릴까

| 상황 | 후보 |
| :--- | :--- |
| 모든 요청 공통 | Middleware |
| 에러 JSON | exception_handler |
| 의도한 4xx | HTTPException |
| 브라우저 호출 | CORS |

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../assets/sections/section-next-dark.svg" />
  <img src="../../assets/sections/section-next.svg" width="100%" alt="Next Chapter" />
</picture>

다음 장: **[06. 테스트](06_Testing.md)** — TestClient와 의존성 오버라이드
