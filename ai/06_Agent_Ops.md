<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/banner-cs-dark.svg" />
  <img src="../assets/sections/banner-cs.svg" width="100%" alt="AI / ML" />
</picture>

# 06. 에이전트와 운영

**도구를 쓰는 에이전트와 평가·비용·안전을 한곳에 둔다.**

<p>
  <img src="https://img.shields.io/badge/Chapter-06-0F172A?style=flat-square" alt="Chapter 06" />
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

채팅 한 방이 끝이 아니다.  
도구를 호출하는 **에이전트 루프**와, 품질·돈·안전을 보는 **운영**이 따라온다.

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/section-contents-dark.svg" />
  <img src="../assets/sections/section-contents.svg" width="100%" alt="Contents" />
</picture>

| # | 주제 | 한 줄 |
| :--- | :--- | :--- |
| 01 | 도구 호출 | 함수·API |
| 02 | 에이전트 루프 | 계획·실행 |
| 03 | 평가 | 품질 측정 |
| 04 | 비용·안전 | 운영 감각 |

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/section-concept-dark.svg" />
  <img src="../assets/sections/section-concept.svg" width="100%" alt="Concept" />
</picture>

### 01. 도구 호출

**모델이 “함수를 고르고 인자를 채우면” 앱이 실행한다.**

#### 직관

비서가 전화·캘린더 API를 대신 누르는 일이다.

```python
def get_weather(city: str) -> str:
    return f"Weather in {city}: cloudy"  # 실제로는 API

tools = {
    "get_weather": get_weather,
}

# 모델이 고른 호출 (의사)
call = {"name": "get_weather", "arguments": {"city": "Seoul"}}
result = tools[call["name"]](**call["arguments"])
print(result)
```

---

### 02. 에이전트 루프

**생각(또는 결정) → 도구 → 관찰 → 다시 결정**을 반복한다.

#### 직관

심부름 체크리스트다.  
끝날 때까지 한 걸음씩 도구를 쓴다.

```python
def agent_loop(goal, decide, tools, max_steps=5):
    obs = None
    for _ in range(max_steps):
        action = decide(goal, obs)
        if action["type"] == "final":
            return action["answer"]
        obs = tools[action["name"]](**action.get("arguments", {}))
    return "step limit"
```

#### 핵심 성질

| 개념 | 내용 |
| :--- | :--- |
| step limit | 무한 루프 방지 |
| 권한 | 위험한 도구는 화이트리스트 |
| 관측 | 도구 결과를 다시 컨텍스트에 |

---

### 03. 평가

**데모 한 방이 아니라 회귀 가능한 측정.**

#### 직관

시험 세트다.  
고정 질문·기대 행동으로 바뀌었는지 본다.

```python
cases = [
    {"q": "서울 날씨?", "expect_tool": "get_weather"},
]
# 의사: 모델이 고른 도구 이름과 기대를 비교
chosen = ["get_weather"]  # 실제로는 모델 출력에서 추출
score = sum(
    1 for c, name in zip(cases, chosen) if c["expect_tool"] == name
) / len(cases)
print(score)
```

#### 핵심 성질

| 개념 | 내용 |
| :--- | :--- |
| offline eval | 저장된 케이스 |
| online | 사용자 피드백·가드레일 |
| LLM-as-judge | 보조 지표 (편향 주의) |

---

### 04. 비용·안전

**토큰·호출·데이터 유출을 운영 지표로 본다.**

#### 직관

택시 미터기와 출입 통제다.

#### 핵심 성질

| 개념 | 내용 |
| :--- | :--- |
| 토큰·$/요청 | 컨텍스트·모델 크기 |
| 캐시·작은 모델 | 비용 절감 |
| 시크릿·PII | 프롬프트·로그에 금지 |
| 인간 승인 | 결제·삭제 등 고위험 행동 |

```python
def estimate_cost(tokens: int, price_per_1k: float = 0.002) -> float:
    return tokens / 1000 * price_per_1k

print(estimate_cost(3500))
```

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/section-summary-dark.svg" />
  <img src="../assets/sections/section-summary.svg" width="100%" alt="Summary" />
</picture>

### 무엇을 먼저 떠올릴까

| 상황 | 후보 |
| :--- | :--- |
| API/DB 필요 | 도구 호출 |
| 다단계 일 | 에이전트 루프 + step limit |
| 품질 회귀 | 평가 세트 |
| 청구서·유출 | 비용·안전 |

AI 트랙 본문은 여기까지다.  
코드는 **감각을 고정하는 최소 예시**이고, 프로덕션 SDK는 그때의 문서를 따르면 된다.

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/section-next-dark.svg" />
  <img src="../assets/sections/section-next.svg" width="100%" alt="Related tracks" />
</picture>

AI 트랙 Ready.  
목록: **[ai/README.md](README.md)** · 협업: **[tools/](../tools/README.md)**
