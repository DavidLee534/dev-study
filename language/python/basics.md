# Python 기초

| 문서 | 내용 | 코드 |
|------|------|------|
| [basics.md](basics.md) | 변수, 제어문, 자료구조, 함수 (`L01` ~ `L17`) | [`basics/code/`](basics/code/) |
| [advanced.md](advanced.md) | 클래스 ~ venv/pip (`L01` ~ `L18`) | [`advanced/code/`](advanced/code/) |

한 코드 파일 = 한 문법. 자세한 설명은 각 `.py` 주석에 있다.

예제 이름은 마다가스카 펭귄(**스키퍼**, **코왈스키**, **프라이빗**, **리코**)을 쓴다.

```bash
cd language/python/basics/code
python L01_print.py
```

---

## L01 · print

콘솔 출력. `end=` 로 줄바꿈을 바꿀 수 있다.

→ [`basics/code/L01_print.py`](basics/code/L01_print.py)

## L02 · 변수

`이름 = 값`. 타입을 적지 않아도 된다.

→ [`basics/code/L02_variables.py`](basics/code/L02_variables.py)

## L03 · 기본 타입

`int`, `float`, `bool`, `str`. `type()`으로 확인.

→ [`basics/code/L03_types.py`](basics/code/L03_types.py)

## L04 · 문자열

`'...'` / `"..."`. `f"..."`으로 변수를 넣는다.

→ [`basics/code/L04_string.py`](basics/code/L04_string.py)

## L05 · 산술 연산자

`+ - * / // % **`. `/`는 실수, `//`는 정수 나눗셈.

→ [`basics/code/L05_arithmetic.py`](basics/code/L05_arithmetic.py)

## L06 · 비교 연산자

`== != > >= < <=` → 결과는 `bool`.

→ [`basics/code/L06_comparison.py`](basics/code/L06_comparison.py)

## L07 · 논리 연산자

`and` / `or` / `not`.

→ [`basics/code/L07_logical.py`](basics/code/L07_logical.py)

## L08 · if / elif / else

들여쓰기로 블록을 구분한다. `{ }` 없음.

→ [`basics/code/L08_if.py`](basics/code/L08_if.py)

## L09 · for

`for 변수 in iterable`. `range(n)`은 0 ~ n-1.

→ [`basics/code/L09_for.py`](basics/code/L09_for.py)

## L10 · while

조건이 True인 동안 반복.

→ [`basics/code/L10_while.py`](basics/code/L10_while.py)

## L11 · list

순서가 있는 가변 목록. Java `ArrayList`와 비슷.

→ [`basics/code/L11_list.py`](basics/code/L11_list.py)

## L12 · tuple

불변 시퀀스. 값 교환에 자주 쓴다.

→ [`basics/code/L12_tuple.py`](basics/code/L12_tuple.py)

## L13 · dict

키 → 값. Java `Map`과 같다.

→ [`basics/code/L13_dict.py`](basics/code/L13_dict.py)

## L14 · set

중복 없는 집합.

→ [`basics/code/L14_set.py`](basics/code/L14_set.py)

## L15 · 함수

`def 이름():`으로 정의 후 호출.

→ [`basics/code/L15_function.py`](basics/code/L15_function.py)

## L16 · 매개변수

호출할 때 넘기는 입력값.

→ [`basics/code/L16_parameters.py`](basics/code/L16_parameters.py)

## L17 · return

결과를 돌려준다. 없으면 `None`.

→ [`basics/code/L17_return.py`](basics/code/L17_return.py)
