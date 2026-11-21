<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/banner-cs-dark.svg" />
  <img src="../assets/sections/banner-cs.svg" width="100%" alt="Tools" />
</picture>

# 06. 협업 습관

**작은 PR·컨벤션·CI로 팀 속도를 유지한다.**

<p>
  <img src="https://img.shields.io/badge/Chapter-06-0F172A?style=flat-square" alt="Chapter 06" />
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

도구보다 **습관**이 병목을 가른다.  
리뷰 가능한 크기, 기계가 할 검사, 다음 사람을 배려하는 마무리가 핵심이다.

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/section-contents-dark.svg" />
  <img src="../assets/sections/section-contents.svg" width="100%" alt="Contents" />
</picture>

| # | 주제 | 한 줄 |
| :--- | :--- | :--- |
| 01 | 작은 PR | 리뷰 가능 크기 |
| 02 | 컨벤션 | 이름·포맷 |
| 03 | CI 초록 | 자동 검사 |
| 04 | 핸드오프 | 다음 사람 배려 |

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/section-concept-dark.svg" />
  <img src="../assets/sections/section-concept.svg" width="100%" alt="Concept" />
</picture>

### 01. 작은 PR

**한 번에 리뷰·되돌리기 쉬운 크기.**

#### 직관

한 접시 요리다.  
코스 전체를 한 접시에 올리면 검수도, 반품도 어렵다.

#### 핵심 성질

| 개념 | 내용 |
| :--- | :--- |
| 범위 | 한 이슈·한 의도 |
| 크기 | 수백 줄이 기본 상한 감각(팀마다 다름) |
| 쪼개기 | 리팩터와 기능 변경 분리 |

- **쓰임**: “리뷰가 안 도는” 거대 PR을 나눌 때

---

### 02. 컨벤션

**이름·포맷·커밋 메시지를 맞춘다.**

#### 직관

표지판 글씨체다.  
내용보다 먼저 “같은 언어”를 쓰면 리뷰가 스타일 논쟁에 안 빠진다.

#### 핵심 성질

| 개념 | 내용 |
| :--- | :--- |
| 포맷터·린트 | 기계가 맞출 것 |
| 브랜치·커밋 규칙 | `feat`/`fix` 등 |
| 코드 스타일 가이드 | 팀이 합의한 읽기 규칙 |

- **쓰임**: nit 코멘트를 줄일 때

---

### 03. CI 초록

**푸시·PR마다 자동으로 도는 검사.**

#### 직관

출고 전 자동 검사기다.  
초록이면 “기본 문은 통과” 신호다.

#### 핵심 성질

| 개념 | 내용 |
| :--- | :--- |
| 테스트·린트·빌드 | 흔한 파이프 |
| 실패 시 | 머지 전 고치기 |
| 로컬 재현 | CI만 맹신하지 말고 같은 명령을 로컬에서 실행 |

- **쓰임**: 회귀 방지, 리뷰어 시간 절약

> 빨간 CI를 “나중에”로 미루면 본선이 금방 썩는다.

---

### 04. 핸드오프

**다음 사람(미래 나 포함)이 이어받기 쉽게 남긴다.**

#### 직관

교대 인수인계다.  
열린 TODO, 위험, 검증 방법을 PR·이슈에 적는다.

#### 핵심 성질

| 개념 | 내용 |
| :--- | :--- |
| PR 설명 | 의도·리스크·확인 방법 |
| 미완료 | 이슈로 남기기 |
| 시크릿 | 문서·코드에 안 남기기 |

- **쓰임**: 휴가 전, 큰 기능 중간 머지, 온콜 인수

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/section-summary-dark.svg" />
  <img src="../assets/sections/section-summary.svg" width="100%" alt="Summary" />
</picture>

### 무엇을 먼저 떠올릴까

| 상황 | 후보 |
| :--- | :--- |
| 리뷰 적체 | 작은 PR |
| 스타일 논쟁 | 컨벤션·린트 |
| 회귀 | CI |
| 인수인계 | 핸드오프 메모 |

Tools 트랙 본문은 여기까지다.  
도구 이름보다 **팀과 맞추는 습관**이 남으면 충분하다.

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/section-next-dark.svg" />
  <img src="../assets/sections/section-next.svg" width="100%" alt="Related tracks" />
</picture>

Tools 트랙 Ready.  
목록: **[tools/README.md](README.md)** · AI 트랙: **[ai/](../ai/README.md)**
