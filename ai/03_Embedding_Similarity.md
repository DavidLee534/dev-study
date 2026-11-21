<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/banner-cs-dark.svg" />
  <img src="../assets/sections/banner-cs.svg" width="100%" alt="AI / ML" />
</picture>

# 03. 임베딩과 유사도

**텍스트·이미지를 벡터로 두고 가까운 것을 찾는다.**

<p>
  <img src="https://img.shields.io/badge/Chapter-03-0F172A?style=flat-square" alt="Chapter 03" />
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

문자 그대로 비교하면 “왕”과 “여왕”이 멀다.  
임베딩은 **의미 가까운 것을 가까운 점**으로 두는 표현이다.

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/section-contents-dark.svg" />
  <img src="../assets/sections/section-contents.svg" width="100%" alt="Contents" />
</picture>

| # | 주제 | 한 줄 |
| :--- | :--- | :--- |
| 01 | 벡터 공간 | 점으로 표현 |
| 02 | 유사도 | 거리·코사인 |
| 03 | 임베딩 모델 | 의미 압축 |
| 04 | 검색 쓰임 | 추천·매칭 |

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/section-concept-dark.svg" />
  <img src="../assets/sections/section-concept.svg" width="100%" alt="Concept" />
</picture>

### 01. 벡터 공간

**각 항목을 숫자 목록(벡터)으로 둔다.**

#### 직관

지도 좌표다.  
가까우면 비슷하다고 본다.

```python
# 장난감 임베딩 (실제는 모델이 수백 차원으로 만듦)
emb = {
    "cat": [0.9, 0.1],
    "dog": [0.8, 0.2],
    "car": [0.1, 0.9],
}
```

---

### 02. 유사도

**두 벡터가 얼마나 같은 방향을 보는가.**

#### 직관

화살표 각도다.  
코사인 유사도는 길이보다 방향에 초점인 경우가 많다.

```python
import math

def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))
    return dot / (na * nb)

print(round(cosine([0.9, 0.1], [0.8, 0.2]), 3))
print(round(cosine([0.9, 0.1], [0.1, 0.9]), 3))
```

---

### 03. 임베딩 모델

**문장·이미지를 벡터로 바꿔 주는 모델.**

#### 직관

번역기 대신 “의미 GPS”다.

#### 핵심 성질

| 개념 | 내용 |
| :--- | :--- |
| 문장 임베딩 | 검색·클러스터에 흔함 |
| 차원 | 보통 수백~수천 |
| 같은 모델 | 비교·인덱스에 동일 모델 사용 |

```python
# 의사코드: 실제로는 OpenAI / sentence-transformers 등
# vec = embed("penguin likes fish")
# → [0.02, -0.11, ...]
```

---

### 04. 검색 쓰임

**쿼리 벡터와 가까운 문서를 고른다.**

#### 직관

도서관에서 “비슷한 책” 찾기.

```python
def most_similar(query, store):
    return max(store, key=lambda k: cosine(query, store[k]))

q = [0.85, 0.15]
print(most_similar(q, emb))  # 위 §01 emb 필요 · dog 또는 cat
```

- **쓰임**: 의미 검색, 추천, RAG의 검색 단계

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/section-summary-dark.svg" />
  <img src="../assets/sections/section-summary.svg" width="100%" alt="Summary" />
</picture>

### 무엇을 먼저 떠올릴까

| 상황 | 후보 |
| :--- | :--- |
| 의미 비교 | 임베딩 |
| 가까운 항목 | 코사인 등 유사도 |
| 문서 찾기 | 벡터 검색 |

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/section-next-dark.svg" />
  <img src="../assets/sections/section-next.svg" width="100%" alt="Next Chapter" />
</picture>

다음 장: **[04. LLM과 프롬프트](04_LLM_Prompt.md)** — 토큰과 지시
