<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../assets/sections/banner-cs-dark.svg" />
  <img src="../../assets/sections/banner-cs.svg" width="100%" alt="Backend" />
</picture>

# 04. 검증과 예외

**잘못된 입력을 걸러 내고, 실패를 일관된 응답으로 돌린다.**

<p>
  <img src="https://img.shields.io/badge/Chapter-04-0F172A?style=flat-square" alt="Chapter 04" />
  &nbsp;
  <img src="https://img.shields.io/badge/Track-Spring_Boot-334155?style=flat-square" alt="Spring_Boot" />
  &nbsp;
  <img src="https://img.shields.io/badge/Status-Ready-16A34A?style=flat-square" alt="Ready" />
</p>

</div>

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../assets/sections/section-goals-dark.svg" />
  <img src="../../assets/sections/section-goals.svg" width="100%" alt="Learning Goals" />
</picture>

API는 성공 경로만 있는 것이 아니다.  
**무엇이 잘못됐는지**를 클라이언트와 같은 말로 약속하는 일이 검증·예외 처리다.

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../assets/sections/section-contents-dark.svg" />
  <img src="../../assets/sections/section-contents.svg" width="100%" alt="Contents" />
</picture>

| # | 주제 | 한 줄 |
| :--- | :--- | :--- |
| 01 | @Valid / Bean Validation | 입력 검증 |
| 02 | 예외 계층 | 비즈니스·시스템 구분 |
| 03 | @ControllerAdvice | 공통 예외 처리 |
| 04 | Problem Detail / 에러 바디 | 클라이언트와 계약 |

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../assets/sections/section-concept-dark.svg" />
  <img src="../../assets/sections/section-concept.svg" width="100%" alt="Concept" />
</picture>

### 01. @Valid / Bean Validation

**요청 DTO에 규칙을 붙여, 컨트롤러 입구에서 걸러 낸다.**

#### 직관

접수 양식의 필수 칸 표시다.  
이름·이메일이 비면 접수 창구에서 되돌려 보낸다.

#### 핵심 성질

| 개념 | 내용 |
| :--- | :--- |
| `@NotNull` / `@Size` / `@Email` 등 | 필드 제약 |
| `@Valid` / `@Validated` | 검증 트리거 |
| `BindingResult` | 검증 결과를 직접 받을 때 |
| 그룹 | 생성/수정처럼 규칙 묶음 |

- **쓰임**: 400 Bad Request로 “형식·필수” 오류를 빨리 돌려줄 때

> 검증은 **문법·형식**에 가깝고, “재고가 없다” 같은 업무 실패와는 층을 나눈다.

---

### 02. 예외 계층

**의도한 실패와 예상 밖 실패를 다른 종류로 나눈다.**

#### 직관

안내 방송과 화재 경보다.  
“좌석이 없다”는 안내(비즈니스), “서버가 죽었다”는 경보(시스템)다.

#### 핵심 성질

| 구분 | 감각 |
| :--- | :--- |
| 비즈니스 예외 | 도메인 규칙 위반, 보통 4xx |
| 시스템/인프라 예외 | DB 다운, 타임아웃, 보통 5xx |
| 체크 vs 언체크 | 팀 컨벤션. Spring에선 런타임 예외가 흔함 |
| 예외를 흐름 제어로 남용 | 가독성·성능 모두 해칠 수 있음 |

- **쓰임**: 서비스에서 “없을 때”를 `Optional`/예외 중 무엇으로 표현할지 정할 때

> 예외 메시지에 **내부 스택·SQL**을 그대로 노출하지 않는다.

---

### 03. @ControllerAdvice

**컨트롤러마다 try-catch를 두지 않고 공통 변환기를 둔다.**

#### 직관

민원 창구 하나다.  
각 부서가 민원을 창구로 넘기면, 창구가 표준 답변 양식으로 돌려준다.

#### 핵심 성질

| 개념 | 내용 |
| :--- | :--- |
| `@RestControllerAdvice` | 전역(또는 패키지 범위) 예외 핸들러 |
| `@ExceptionHandler` | 예외 타입별 응답 매핑 |
| 우선순위 | 더 구체적인 핸들러가 먼저 |
| 로깅 위치 | 여기서 수준을 나누어 남기기 좋음 |

- **쓰임**: 검증 실패·NotFound·권한 오류를 한곳에서 JSON으로 맞출 때

> Advice는 “숨기는 곳”이 아니라 **응답 계약의 허브**다.

---

### 04. Problem Detail / 에러 바디

**에러도 API 계약의 일부로 설계한다.**

#### 직관

영수증 뒷면의 약관이다.  
코드·메시지·필드 오류 목록이 약속된 칸에 들어간다.

#### 핵심 성질

| 개념 | 내용 |
| :--- | :--- |
| 공통 필드 | `code`, `message`, `timestamp`, `path` 등 |
| RFC 7807 Problem Details | `type` / `title` / `status` / `detail` 관례 |
| 필드 오류 배열 | 검증 실패 시 어느 칸이 문제인지 |
| 상태 코드 일치 | 바디의 status와 HTTP status를 맞춤 |

- **쓰임**: 프론트·모바일·다른 서비스가 같은 파서로 에러를 처리할 때

> 성공 응답만 OpenAPI에 적지 말고, **실패 스키마**도 문서에 남긴다.

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../assets/sections/section-summary-dark.svg" />
  <img src="../../assets/sections/section-summary.svg" width="100%" alt="Summary" />
</picture>

### 무엇을 먼저 떠올릴까

| 상황 | 후보 |
| :--- | :--- |
| 필수값 누락 | Bean Validation → 400 |
| 리소스 없음 | 비즈니스 예외 → 404 |
| 권한 없음 | 인가 실패 → 403 (다음 장) |
| 스택이 클라이언트에 보일 때 | Advice에서 마스킹 |

좋은 API는 성공뿐 아니라 **실패를 예측 가능하게** 만든다.

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../assets/sections/section-next-dark.svg" />
  <img src="../../assets/sections/section-next.svg" width="100%" alt="Next Chapter" />
</picture>

다음 장: **[05. 인증·인가](05_Authz.md)** — 누구인지, 무엇을 할 수 있는지
