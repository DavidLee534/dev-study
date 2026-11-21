<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/banner-cs-dark.svg" />
  <img src="../assets/sections/banner-cs.svg" width="100%" alt="Tools" />
</picture>

# 05. IDE와 디버깅

**에디터·브레이크포인트·로그로 원인을 좁힌다.**

<p>
  <img src="https://img.shields.io/badge/Chapter-05-0F172A?style=flat-square" alt="Chapter 05" />
  &nbsp;
  <img src="https://img.shields.io/badge/Track-Tools_Collab-334155?style=flat-square" alt="Tools_Collab" />
  &nbsp;
  <img src="https://img.shields.io/badge/Status-Ready-16A34A?style=flat-square" alt="Ready" />
</p>

</div>

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/section-goals-dark.svg" />
  <img src="../assets/sections/section-goals.svg" width="100%" alt="Learning Goals" />
</picture>

막히면 코드를 더 쓰기 전에 **어디서 빗나갔는지**를 본다.  
IDE와 디버깅은 그 길을 짧게 만드는 도구다.

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/section-contents-dark.svg" />
  <img src="../assets/sections/section-contents.svg" width="100%" alt="Contents" />
</picture>

| # | 주제 | 한 줄 |
| :--- | :--- | :--- |
| 01 | IDE 역할 | 탐색·실행 |
| 02 | 브레이크포인트 | 멈춰 보기 |
| 03 | 로그 | 흔적 읽기 |
| 04 | 재현 | 같은 조건 |

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/section-concept-dark.svg" />
  <img src="../assets/sections/section-concept.svg" width="100%" alt="Concept" />
</picture>

### 01. IDE 역할

**코드를 읽고, 찾고, 실행하고, 고치는 작업대.**

#### 직관

정비소 리프트다.  
부품(심볼)을 찾고, 엔진(앱)을 돌리며, 볼트를 조인다.

#### 핵심 성질

| 기능 | 쓰임 |
| :--- | :--- |
| 검색·참조 | 정의로 이동, 사용처 찾기 |
| 실행 구성 | 디버그/런 설정 |
| 린트·포맷 | 리뷰 전에 기계가 할 일 |
| Git 연동 | diff·커밋 UI |

- **쓰임**: “파일 이름이 기억 안 날 때”부터 “테스트 한 개만 돌릴 때”

---

### 02. 브레이크포인트

**의심 줄에서 실행을 멈추고 상태를 본다.**

#### 직관

CCTV 일시정지다.  
그 순간의 변수·콜스택을 확인한다.

#### 핵심 성질

| 개념 | 내용 |
| :--- | :--- |
| breakpoint | 멈출 위치 |
| step over / into | 다음 줄 / 함수 안으로 |
| watch | 관심 식 추적 |
| 조건부 BP | 특정 값일 때만 멈춤 |

- **쓰임**: “여기 들어오나?”, “이 값이 왜 null이지?”

> `print`만으로도 되지만, 멈추면 **호출 경로**까지 같이 보인다.

---

### 03. 로그

**시간이 지나며 남긴 흔적.**

#### 직관

항해 일지다.  
언제·어디서·무엇을 했는지 레벨을 나눠 적는다.

#### 핵심 성질

| 개념 | 내용 |
| :--- | :--- |
| level | debug / info / warn / error |
| 구조화 | request id, user id 등 키 |
| 민감정보 | 토큰·비밀번호 금지 |
| 과다 로그 | 신호 대 잡음이 나빠짐 |

- **쓰임**: 재현 어려운 운영 이슈, 비동기·분산 추적

---

### 04. 재현

**같은 조건으로 다시 일어나게 한다.**

#### 직관

실험 노트다.  
입력·환경·버전을 고정해야 “고쳤다”를 말할 수 있다.

#### 핵심 성질

| 개념 | 내용 |
| :--- | :--- |
| 최소 재현 | 관련된 것만 남긴 사례 |
| 환경 | OS, 브랜치, 설정, 데이터 |
| 테스트로 고정 | 회귀를 막는 자동 검사 |

- **쓰임**: 이슈 작성, 리뷰어·미래 나에게 넘길 때

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/section-summary-dark.svg" />
  <img src="../assets/sections/section-summary.svg" width="100%" alt="Summary" />
</picture>

### 무엇을 먼저 떠올릴까

| 상황 | 후보 |
| :--- | :--- |
| 심볼 찾기 | IDE 탐색 |
| 값·경로 확인 | 브레이크포인트 |
| 운영·비동기 | 로그 |
| “내 PC에선 됨” | 재현 조건 고정 |

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/section-next-dark.svg" />
  <img src="../assets/sections/section-next.svg" width="100%" alt="Next Chapter" />
</picture>

다음 장: **[06. 협업 습관](06_Collab_Habits.md)** — 작은 PR과 CI로 속도를 유지한다
