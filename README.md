<div align="center">

# Dev Study

**개발 공부 노트를 주제별로 정리하는 저장소**

언어 / 프레임워크 / 인프라 / CS까지, 이해한 내용을 교재처럼 남깁니다.

<p>
  <img src="https://img.shields.io/badge/Format-Study_Notes-0F172A?style=flat-square" alt="Study Notes" />
  &nbsp;
  <img src="https://img.shields.io/badge/Focus-Concepts_First-EA580C?style=flat-square" alt="Concepts First" />
  &nbsp;
  <img src="https://img.shields.io/badge/Track-Computer_Science-334155?style=flat-square" alt="Computer Science" />
</p>

<p>
  <img src="https://img.shields.io/badge/Java-21-EA580C?style=flat-square" alt="Java" />
  &nbsp;
  <img src="https://img.shields.io/badge/Python-3-16A34A?style=flat-square" alt="Python" />
  &nbsp;
  <img src="https://img.shields.io/badge/CS-Lecture_Notes-0F172A?style=flat-square" alt="CS Lecture Notes" />
</p>

</div>

<br />

## 공부 범위

### Language
- Java, Kotlin, JavaScript, TypeScript, Python, Go, Rust, C/C++, Swift 등
- 문법, 타입 시스템, 메모리/동시성, 표준 라이브러리

### Frontend
- HTML, CSS, 반응형 UI
- React, Next.js, Vue, Angular
- 상태 관리, 라우팅, 접근성, 성능 최적화
- 테스트 (Jest, Playwright, Cypress)

### Backend
- Spring Boot, Node.js, NestJS, FastAPI, Django, Express
- REST / GraphQL API 설계
- 인증/인가 (Session, JWT, OAuth)
- 캐싱, 메시징, 배치, 비동기 처리

→ 교재형 노트: **[backend/](backend/README.md)** (Spring · NestJS · FastAPI 병렬 Ready)

### Database
- PostgreSQL, MySQL, MongoDB, Redis
- SQL / NoSQL 모델링
- 인덱스, 트랜잭션, 락, 쿼리 최적화
- ORM / Query Builder (JPA, Prisma 등)

### Mobile
- Android, iOS, React Native, Flutter
- 앱 아키텍처, 로컬 저장소, 푸시, 배포

### Infra / DevOps
- Linux, 네트워크, 서버 구성
- Docker, Kubernetes
- CI/CD (GitHub Actions 등)
- AWS / GCP / Azure 기초
- 모니터링, 로깅, 장애 대응

### Computer Science
- 자료구조, 알고리즘
- 운영체제, 네트워크, HTTP
- 데이터베이스 이론
- 소프트웨어 공학, 설계 패턴, 클린 코드

→ 교재형 노트: **[cs/](cs/README.md)**

### AI / ML
- 고전 ML 감각 (학습·평가·임베딩)
- LLM, 프롬프트, RAG, 에이전트
- 평가·비용·안전 운영 감각

→ 교재형 노트: **[ai/](ai/README.md)** (ML · LLM Ready, Python 스니펫)

### Tools / Collaboration
- Git, GitHub, PR 워크플로
- IDE / 디버깅 / 테스트 도구
- 문서화, 코드 리뷰, 협업 프로세스

→ 교재형 노트: **[tools/](tools/README.md)** (협업 Ready)

### Security / Quality
- 웹 보안 기초 (XSS, CSRF, SQL Injection)
- 입력 검증, 시크릿 관리
- 테스트 전략, 코드 품질, 리팩터링

## 폴더 구조

```text
dev-study/
├── language/    # 언어 (Java, TS, Python …)
├── frontend/    # UI, React, Next.js …
├── backend/     # API, 서버 프레임워크
├── database/    # SQL/NoSQL, 인덱스, ORM
├── mobile/      # Android, iOS, RN, Flutter
├── infra/       # Docker, K8s, CI/CD, 클라우드
├── cs/          # 자료구조, OS, 네트워크, 설계
├── ai/          # ML · LLM · RAG · 에이전트
├── tools/       # Git, PR, 리뷰, 협업 교재
└── security/    # 보안, 테스트, 품질

```

주제 안에서 필요하면 하위 폴더를 더 나눕니다.  
예: `language/python/`, `cs/01_자료구조.md`

## 이 저장소를 쓰는 방식

1. 주제를 하나 정하고 위 폴더에 둡니다.
2. 이해한 내용과 코드를 문서로 정리합니다.
3. 커밋해서 기록으로 남깁니다.

```bash
git add .
git commit -m "study: 주제 정리"
git push
```

## 기록 원칙

- 완벽하지 않아도 됩니다. **오늘 이해한 것**을 남깁니다.
- 가능하면 **문제 → 원인 → 해결 → 코드** 순서로 적습니다.
- 짧은 메모보다, 나중에 다시 읽을 수 있는 설명을 남깁니다.

## 프로필

GitHub 프로필: [DavidLee534](https://github.com/DavidLee534)
