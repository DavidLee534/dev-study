<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/banner-cs-dark.svg" />
  <img src="../assets/sections/banner-cs.svg" width="100%" alt="AI / ML" />
</picture>

# 04. LLM과 프롬프트

**큰 언어 모델에 맥락을 주고 답을 받는 방식을 본다.**

<p>
  <img src="https://img.shields.io/badge/Chapter-04-0F172A?style=flat-square" alt="Chapter 04" />
  &nbsp;
  <img src="https://img.shields.io/badge/Track-AI_ML-334155?style=flat-square" alt="AI_ML" />
  &nbsp;
  <img src="https://img.shields.io/badge/Status-Ready-16A34A?style=flat-square" alt="Ready" />
</p>

</div>

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/section-goals-dark.svg" />
  <img src="../assets/sections/section-goals.svg" width="100%" alt="Learning Goals" />
</picture>

LLM은 “다음 토큰을 고르는” 거대한 모델이다.  
앱에서는 **프롬프트·컨텍스트·샘플링**으로 동작을 조종한다.

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/section-contents-dark.svg" />
  <img src="../assets/sections/section-contents.svg" width="100%" alt="Contents" />
</picture>

| # | 주제 | 한 줄 |
| :--- | :--- | :--- |
| 01 | LLM이란 | 다음 토큰 예측 |
| 02 | 토큰·컨텍스트 | 입력 한도 |
| 03 | 프롬프트 | 지시와 예시 |
| 04 | 온도·샘플링 | 답의 흔들림 |

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/section-concept-dark.svg" />
  <img src="../assets/sections/section-concept.svg" width="100%" alt="Concept" />
</picture>

### 01. LLM이란

**대규모로 학습된 언어 모델. 문맥 다음 말을 고른다.**

#### 직관

자동완성이다.  
다만 창이 매우 크고, 지시·도구와 결합하면 앱이 된다.

#### 핵심 성질

| 개념 | 내용 |
| :--- | :--- |
| 생성 | 한 토큰씩(또는 묶음으로) 이어 씀 |
| 사전학습 | 광역 텍스트로 패턴 학습 |
| 한계 | 최신·사내 지식은 없을 수 있음 → RAG |

---

### 02. 토큰·컨텍스트

**모델이 한 번에 보는 입력+출력 예산.**

#### 직관

책상 크기다.  
지시·문서·대화 기록이 책상을 채운다.

```python
# 의사 토큰 수 (실제는 tokenizer 사용)
def rough_tokens(text: str) -> int:
    return max(1, len(text) // 4)

prompt = "Summarize these docs: " + ("lorem " * 200)
print(rough_tokens(prompt))
```

---

### 03. 프롬프트

**역할·지시·예시·입력 형식을 글로 준다.**

#### 직관

업무 브리핑이다.  
모호하면 모호한 답이 나온다.

```python
system = "You are a concise API docs assistant. Answer in Korean."
user = "Explain what a 401 status means in one sentence."
messages = [
    {"role": "system", "content": system},
    {"role": "user", "content": user},
]
# client.chat.completions.create(model="...", messages=messages)
```

#### 핵심 성질

| 기법 | 감각 |
| :--- | :--- |
| 지시 명확화 | 형식·톤·금지 |
| few-shot | 짧은 예시 |
| 구조화 출력 | JSON 스키마 등 |

---

### 04. 온도·샘플링

**같은 프롬프트라도 답을 얼마나 흔들 것인가.**

#### 직관

주사위 편향이다.  
낮으면 보수적, 높으면 다양(또는 엉뚱).

```python
# API 호출 시 흔히 넘기는 파라미터 감각
params = {"temperature": 0.2, "max_tokens": 256}
# 분류·추출 → 낮은 temperature
# 아이디어 발산 → 조금 높이기
```

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/section-summary-dark.svg" />
  <img src="../assets/sections/section-summary.svg" width="100%" alt="Summary" />
</picture>

### 무엇을 먼저 떠올릴까

| 상황 | 후보 |
| :--- | :--- |
| 답이 횡설수설 | 지시·예시 보강 |
| 입력이 잘림 | 토큰·컨텍스트 |
| 결과가 들쭉날쭉 | temperature |
| 회사 문서 필요 | 다음 장 RAG |

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/section-next-dark.svg" />
  <img src="../assets/sections/section-next.svg" width="100%" alt="Next Chapter" />
</picture>

다음 장: **[05. RAG](05_RAG.md)** — 검색한 근거로 생성
