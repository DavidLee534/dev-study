<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/banner-cs-dark.svg" />
  <img src="../assets/sections/banner-cs.svg" width="100%" alt="AI / ML" />
</picture>

# 01. 학습의 감각

**모델·데이터·손실로 배우는 일의 뼈대를 잡는다.**

<p>
  <img src="https://img.shields.io/badge/Chapter-01-0F172A?style=flat-square" alt="Chapter 01" />
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

머신러닝은 규칙을 손으로 다 적는 대신, **데이터로 규칙을 맞추는** 일에 가깝다.  
코드는 뼈대를 보여 주는 짧은 예시일 뿐, 라이브러리 튜토리얼이 목표는 아니다.

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/section-contents-dark.svg" />
  <img src="../assets/sections/section-contents.svg" width="100%" alt="Contents" />
</picture>

| # | 주제 | 한 줄 |
| :--- | :--- | :--- |
| 01 | 지도 / 비지도 | 정답 유무 |
| 02 | 모델과 파라미터 | 무엇을 맞추는가 |
| 03 | 손실(loss) | 틀린 정도 |
| 04 | 학습 루프 | 맞추고 고치기 |

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/section-concept-dark.svg" />
  <img src="../assets/sections/section-concept.svg" width="100%" alt="Concept" />
</picture>

### 01. 지도 / 비지도

**정답(라벨)이 있으면 지도, 없으면 비지도에 가깝다.**

#### 직관

문제집에 답이 있으면 채점하며 배우고(지도),  
비슷한 것끼리만 묶는 정리(비지도)다.

#### 핵심 성질

| 구분 | 감각 | 예 |
| :--- | :--- | :--- |
| 지도 | 입력 → 정답 | 스팸 분류, 가격 예측 |
| 비지도 | 구조·군집 | 고객 군집, 토픽 |
| 강화 | 보상으로 행동 | 게임·추천 일부 |

```python
# 지도: (x, y) 쌍
X = [[1.0], [2.0], [3.0]]
y = [2.0, 4.0, 6.0]  # 정답(라벨)
```

---

### 02. 모델과 파라미터

**모델은 입력을 출력으로 바꾸는 틀, 파라미터는 그 안의 조절 나사.**

#### 직관

저울의 눈금이다.  
틀(모델)은 같고, 나사(가중치)를 돌려 맞춘다.

#### 핵심 성질

| 개념 | 내용 |
| :--- | :--- |
| 가설/모델 | `y ≈ f(x; θ)` |
| 파라미터 θ | 학습으로 바뀌는 값 |
| 하이퍼파라미터 | 학습률 등, 보통 사람이 고름 |

```python
# 아주 단순한 선형 모델: y_hat = w * x + b
def predict(x, w, b):
    return w * x + b
```

---

### 03. 손실(loss)

**틀리면 얼마나 틀렸는지 숫자로 만든 것.**

#### 직관

채점표의 감점이다.  
감점이 줄어들도록 나사를 돌린다.

#### 핵심 성질

| 개념 | 내용 |
| :--- | :--- |
| MSE 등 | 회귀에서 흔한 제곱 오차 |
| 교차 엔트로피 | 분류에서 흔함 |
| 작을수록 | (보통) 더 잘 맞춤 |

```python
def mse(y_true, y_pred):
    errs = [(yt - yp) ** 2 for yt, yp in zip(y_true, y_pred)]
    return sum(errs) / len(errs)

print(mse([2, 4, 6], [2.1, 3.9, 6.2]))
```

---

### 04. 학습 루프

**예측 → 손실 → 파라미터 수정**을 반복한다.

#### 직관

연습·채점·교정 반복이다.

#### 핵심 성질

| 단계 | 내용 |
| :--- | :--- |
| forward | 예측 |
| loss | 틀린 정도 |
| update | 경사 등으로 θ 수정 |

```python
# 개념용 1차원 경사하강 (라이브러리 없이)
w, b, lr = 0.0, 0.0, 0.1
xs, ys = [1.0, 2.0, 3.0], [2.0, 4.0, 6.0]
for _ in range(200):
    preds = [w * x + b for x in xs]
    # 단순화한 기울기 감각
    dw = sum(2 * (p - y) * x for p, y, x in zip(preds, ys, xs)) / len(xs)
    db = sum(2 * (p - y) for p, y in zip(preds, ys)) / len(xs)
    w -= lr * dw
    b -= lr * db
print(round(w, 2), round(b, 2))  # w≈2, b≈0 근처
```

- **쓰임**: “학습한다”를 마법이 아니라 **손실을 줄이는 반복**으로 말할 때

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/section-summary-dark.svg" />
  <img src="../assets/sections/section-summary.svg" width="100%" alt="Summary" />
</picture>

### 무엇을 먼저 떠올릴까

| 상황 | 후보 |
| :--- | :--- |
| 정답 있음/없음 | 지도 / 비지도 |
| 무엇을 바꾸나 | 파라미터 |
| 얼마나 틀렸나 | 손실 |
| 어떻게 나아지나 | 학습 루프 |

<br />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/sections/section-next-dark.svg" />
  <img src="../assets/sections/section-next.svg" width="100%" alt="Next Chapter" />
</picture>

다음 장: **[02. 평가와 데이터](02_Eval_Data.md)** — 나눈 데이터와 지표
