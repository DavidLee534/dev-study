<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/banner-cs-dark.svg" />
  <img src="../assets/sections/banner-cs.svg" width="100%" alt="Tools" />
</picture>

# 04. 이슈와 문서

**할 일과 결정을 이슈·문서로 남긴다.**

<p>
  <img src="https://img.shields.io/badge/Chapter-04-0F172A?style=flat-square" alt="Chapter 04" />
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

코드만 있으면 “왜 이렇게 됐는지”가 사라진다.  
이슈와 문서는 **작업 단위와 결정**을 팀에 남기는 기록이다.

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/section-contents-dark.svg" />
  <img src="../assets/sections/section-contents.svg" width="100%" alt="Contents" />
</picture>

| # | 주제 | 한 줄 |
| :--- | :--- | :--- |
| 01 | 이슈 | 작업 단위 |
| 02 | README | 입구 문서 |
| 03 | ADR / 결정 기록 | 왜 이렇게 |
| 04 | Changelog 감각 | 무엇이 바뀌었나 |

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/section-concept-dark.svg" />
  <img src="../assets/sections/section-concept.svg" width="100%" alt="Concept" />
</picture>

### 01. 이슈

**할 일·버그·질문을 추적 가능한 단위로 연다.**

#### 직관

작업 지시서다.  
제목·재현·기대 결과·수락 기준이 있으면 핸드오프가 쉬워진다.

#### 핵심 성질

| 개념 | 내용 |
| :--- | :--- |
| 버그 이슈 | 재현 절차·환경·기대/실제 |
| 기능 이슈 | 목표·범위 밖(Non-goals)·수락 조건 |
| 라벨·마일스톤 | 분류와 일정 감각 |
| 이슈 ↔ PR | 닫을 때 연결 (`Fixes #…`) |

- **쓰임**: “말로만 있던 일”을 보드에 올릴 때

---

### 02. README

**저장소 입구. 처음 온 사람이 살 길을 찾게 한다.**

#### 직관

건물 안내판이다.  
무엇인지, 어떻게 실행하는지, 어디로 더 가면 되는지.

#### 핵심 성질

| 넣을 것 | 내용 |
| :--- | :--- |
| What | 이 레포가 하는 일 |
| How | 설치·실행·테스트 |
| Where | 문서·이슈·기여 방법 |
| Don’t | 비밀키·내부망 전제만 잔뜩 |

- **쓰임**: 온보딩, 오픈소스, 팀 내부 레포 입구

---

### 03. ADR / 결정 기록

**나중에 “왜?”에 답할 짧은 결정 메모.**

#### 직관

회의록의 ‘결정’ 칸만 모은 것이다.  
옵션·선택·결과(트레이드오프)를 남긴다.

#### 핵심 성질

| 개념 | 내용 |
| :--- | :--- |
| ADR | Architecture Decision Record |
| 짧은 형식 | Context → Decision → Consequences |
| 언제 | 되돌리기 비싼 선택 (DB, 인증, 배포) |

- **쓰임**: “그때 왜 Nest였지?”를 반년 뒤에 물을 때

---

### 04. Changelog 감각

**사용자·팀이 체감하는 변화 목록.**

#### 직관

릴리스 노트다.  
추가·수정·깨짐(Breaking)을 구분해 적는다.

#### 핵심 성질

| 구분 | 내용 |
| :--- | :--- |
| Added / Fixed / Changed | 흔한 분류 |
| Breaking | 업그레이드 주의 |
| 커밋 ≠ Changelog | 사용자 언어로 다시 쓰기 |

- **쓰임**: 버전 태그, 배포 공지

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/section-summary-dark.svg" />
  <img src="../assets/sections/section-summary.svg" width="100%" alt="Summary" />
</picture>

### 무엇을 먼저 떠올릴까

| 상황 | 후보 |
| :--- | :--- |
| 할 일 추적 | 이슈 |
| 레포 입구 | README |
| 큰 기술 선택 | ADR |
| 배포 공지 | Changelog |

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/section-next-dark.svg" />
  <img src="../assets/sections/section-next.svg" width="100%" alt="Next Chapter" />
</picture>

다음 장: **[05. IDE와 디버깅](05_IDE_Debugging.md)** — 멈춰 보고 흔적을 읽는다
