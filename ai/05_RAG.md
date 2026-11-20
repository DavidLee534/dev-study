<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/banner-cs-dark.svg" />
  <img src="../assets/sections/banner-cs.svg" width="100%" alt="AI / ML" />
</picture>

# 05. RAG

**검색으로 근거를 붙인 뒤 생성한다.**

<p>
  <img src="https://img.shields.io/badge/Chapter-05-0F172A?style=flat-square" alt="Chapter 05" />
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

LLM만 물으면 모르는 내용을 **지어낼** 수 있다.  
RAG는 **관련 문서를 찾아 프롬프트에 실어** 근거 있는 답을 유도한다.

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/section-contents-dark.svg" />
  <img src="../assets/sections/section-contents.svg" width="100%" alt="Contents" />
</picture>

| # | 주제 | 한 줄 |
| :--- | :--- | :--- |
| 01 | 검색 + 생성 | RAG 흐름 |
| 02 | 청크·인덱스 | 문서 자르기 |
| 03 | 검색 품질 | 넣을 근거 |
| 04 | 환각 | 없는 말 |

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/section-concept-dark.svg" />
  <img src="../assets/sections/section-concept.svg" width="100%" alt="Concept" />
</picture>

### 01. 검색 + 생성

**Retrieve → Augment → Generate.**

#### 직관

시험 중 오픈북이다.  
책을 펼쳐 해당 문단을 보고 답을 쓴다.

```python
def rag_answer(question: str, search, generate):
    docs = search(question, k=3)          # Retrieve
    context = "\n---\n".join(docs)        # Augment
    prompt = f"근거:\n{context}\n\n질문: {question}\n근거에만 기대어 답하라."
    return generate(prompt)               # Generate
```

---

### 02. 청크·인덱스

**문서를 조각 내어 벡터(또는 키워드) 인덱스에 넣는다.**

#### 직관

책을 쪽수 단위로 복사해 서랍에 넣는 일이다.

#### 핵심 성질

| 개념 | 내용 |
| :--- | :--- |
| chunk | 토큰/문단 단위 조각 |
| overlap | 경계 문장 유실 완화 |
| index | 유사도 검색용 저장소 |

```python
def chunk(text: str, size: int = 100, overlap: int = 20):
    """예시는 글자 단위. 실무는 토큰/문단 기준으로 자른다."""
    out, i = [], 0
    while i < len(text):
        out.append(text[i : i + size])
        if i + size >= len(text):
            break
        i += max(1, size - overlap)
    return out

print(chunk("abcdefghijklmnopqrstuvwxyz", size=10, overlap=2))
```

---

### 03. 검색 품질

**잘못된 조각을 넣으면 답이 빗나간다.**

#### 직관

오픈북인데 엉뚱한 페이지를 펼친 상태.

#### 핵심 성질

| 개념 | 내용 |
| :--- | :--- |
| top-k | 몇 조각을 넣을지 |
| 하이브리드 | 키워드 + 벡터 |
| 재순위 | 한번 더 걸러 품질↑ |

```python
def search(query, store, k=2):
    # 키워드 포함만 (벡터 검색 감각은 03장). store: {id: text}
    hits = [t for t in store.values() if query.lower() in t.lower()]
    return hits[:k] or list(store.values())[:k]
```

---

### 04. 환각

**근거에 없는 내용을 자신 있게 말하는 현상.**

#### 직관

빈칸을 메우느라 소설을 쓰는 일이다.

#### 핵심 성질

| 완화 | 내용 |
| :--- | :--- |
| 근거 강제 | “모르면 모른다” 지시 |
| 인용 | 조각 id를 답에 포함 |
| 평가 | 샘플 질문으로 회귀 테스트 |

```python
guard = (
    "아래 근거에 없는 내용은 추측하지 말고 "
    "'근거 부족'이라고 답하라."
)
```

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/section-summary-dark.svg" />
  <img src="../assets/sections/section-summary.svg" width="100%" alt="Summary" />
</picture>

### 무엇을 먼저 떠올릴까

| 상황 | 후보 |
| :--- | :--- |
| 사내 문서 Q&A | RAG |
| 답이 동떨어짐 | 검색·청크 품질 |
| 없는 말 | 환각 가드·인용 |

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/section-next-dark.svg" />
  <img src="../assets/sections/section-next.svg" width="100%" alt="Next Chapter" />
</picture>

다음 장: **[06. 에이전트와 운영](06_에이전트와운영.md)** — 도구·평가·비용
