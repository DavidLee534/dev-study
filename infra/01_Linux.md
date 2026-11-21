<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/banner-cs-dark.svg" />
  <img src="../assets/sections/banner-cs.svg" width="100%" alt="Infra" />
</picture>

# 01. Linux와 서버

**앱이 돌아가는 머신의 기본 감각을 잡는다.**

<p>
  <img src="https://img.shields.io/badge/Chapter-01-0F172A?style=flat-square" alt="Chapter 01" />
  &nbsp;
  <img src="https://img.shields.io/badge/Track-Infra_DevOps-334155?style=flat-square" alt="Infra_DevOps" />
  &nbsp;
  <img src="https://img.shields.io/badge/Status-Ready-16A34A?style=flat-square" alt="Ready" />
</p>

</div>

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/section-goals-dark.svg" />
  <img src="../assets/sections/section-goals.svg" width="100%" alt="Learning Goals" />
</picture>

인프라의 출발점은 “서버에 무엇이 살아 있는가”다.  
프로세스, 파일, 권한, 서비스 단위를 알면 Docker·클라우드도 같은 말로 읽힌다.

관련: CS **[03. 운영체제](../cs/03_Operating_Systems.md)**

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/section-contents-dark.svg" />
  <img src="../assets/sections/section-contents.svg" width="100%" alt="Contents" />
</picture>

| # | 주제 | 한 줄 |
| :--- | :--- | :--- |
| 01 | 프로세스 | 실행 단위 |
| 02 | 파일·경로 | 어디에 있는가 |
| 03 | 사용자·권한 | 누가 무엇을 |
| 04 | 서비스 | 켜 두고 관리 |

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/section-concept-dark.svg" />
  <img src="../assets/sections/section-concept.svg" width="100%" alt="Concept" />
</picture>

### 01. 프로세스

**실행 중인 프로그램 한 덩어리다. PID로 구분한다.**

#### 직관

식당의 “주문 처리 중” 테이블이다.  
메뉴(바이너리)와 달리, 지금 돌아가는 자리가 프로세스다.

#### 핵심 성질

| 개념 | 내용 |
| :--- | :--- |
| PID | 프로세스 식별자 |
| 부모/자식 | 프로세스가 프로세스를 띄움 |
| CPU · 메모리 | 동시에 나눠 쓰는 자원 |
| 종료 코드 | 정상/실패를 숫자로 남김 |

- **쓰임**: “서버가 죽었다”를 프로세스 생존·재시작으로 분해할 때

> 포트에 바인딩한 프로세스가 곧 “이 머신에서 API가 살아 있다”의 실체다.

---

### 02. 파일·경로

**설정·로그·바이너리·데이터가 어디에 있는지부터 본다.**

#### 직관

창고 주소다.  
앱은 코드만이 아니라 설정 파일과 로그 경로에 묶여 있다.

#### 핵심 성질

| 개념 | 내용 |
| :--- | :--- |
| 절대/상대 경로 | `/`부터 vs 현재 위치 기준 |
| 설정 | env 파일, `/etc`, 앱 설정 디렉터리 |
| 로그 | 표준출력·파일·저널 |
| 디스크 | 용량·inode·마운트 |

- **쓰임**: “로컬에선 되는데 서버에선 안 됨” — 경로·권한·마운트부터

> 컨테이너도 결국 **파일시스템 뷰**를 잘라 보여 주는 것이다.

---

### 03. 사용자·권한

**누가 실행하고, 어떤 파일에 손댈 수 있는지 가른다.**

#### 직관

열쇠와 출입증이다.  
root는 만능에 가깝고, 앱 전용 유저는 피해 범위를 줄인다.

#### 핵심 성질

| 개념 | 내용 |
| :--- | :--- |
| user / group | 소유·소속 |
| rwx | 읽기·쓰기·실행 |
| sudo | 임시 승격 |
| 시크릿 | 키·토큰은 권한·유출 경로를 함께 본다 |

- **쓰임**: 배포 계정, CI 러너, 컨테이너 USER를 정할 때

> 편하다고 root로 돌리면, 침해 한 번에 머신 전체가 열린다.

---

### 04. 서비스

**부팅 후에도 유지되는 단위로 앱을 관리한다.**

#### 직관

상시 근무 스케줄이다.  
수동으로 바이너리를 켜 두는 대신, 서비스로 시작·재시작·로그를 묶는다.

#### 핵심 성질

| 개념 | 내용 |
| :--- | :--- |
| systemd unit 등 | 시작 명령, 의존성, 재시작 정책 |
| enable / start | 부팅 등록 vs 지금 실행 |
| 상태 | active, failed, inactive 등 |
| 로그 연결 | journal / 파일 경로 |

- **쓰임**: VM·베어메탈에 데몬을 올릴 때, 컨테이너 orchestration 이전 단계

> Docker·K8s도 “원하는 상태(desired state)”를 유지한다는 점에서 서비스와 같은 감각이다.

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/section-summary-dark.svg" />
  <img src="../assets/sections/section-summary.svg" width="100%" alt="Summary" />
</picture>

### 무엇을 먼저 떠올릴까

| 상황 | 후보 |
| :--- | :--- |
| API가 응답 없음 | 프로세스·포트 |
| 설정이 안 먹음 | 경로·권한 |
| 보안 걱정 | 실행 유저·시크릿 |
| 재부팅 후 안 뜸 | 서비스 enable |

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/section-next-dark.svg" />
  <img src="../assets/sections/section-next.svg" width="100%" alt="Next Chapter" />
</picture>

다음 장: **[02. 네트워크와 엣지](02_Network_Edge.md)** — 요청이 앱에 닿기까지의 길
