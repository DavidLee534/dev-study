# Python 심화

| 문서 | 내용 | 코드 |
|------|------|------|
| [basics.md](basics.md) | 변수, 제어문, 자료구조, 함수 (`L01` ~ `L17`) | [`basics/code/`](basics/code/) |
| [advanced.md](advanced.md) | 클래스 ~ venv/pip (`L01` ~ `L18`) | [`advanced/code/`](advanced/code/) |

한 코드 파일 = 한 문법. 자세한 설명은 각 `.py` 주석에 있다.

기초 다음에 이어서 공부한다. 번호는 `L01_`부터 다시 시작한다.

```bash
cd language/python/advanced/code
python L01_class.py
```

---

## L01 · 클래스·객체

클래스 = 설계도, 객체 = 만든 실체.

→ [`advanced/code/L01_class.py`](advanced/code/L01_class.py)

## L02 · \_\_init\_\_

객체를 만들 때 자동 호출되는 생성자.

→ [`advanced/code/L02_init.py`](advanced/code/L02_init.py)

## L03 · 메서드 / self

`self`는 그 객체 자신. 메서드 첫 매개변수로 받는다.

→ [`advanced/code/L03_method_self.py`](advanced/code/L03_method_self.py)

## L04 · 상속

`class 자식(부모):`으로 부모 기능을 물려받는다.

→ [`advanced/code/L04_inheritance.py`](advanced/code/L04_inheritance.py)

## L05 · 예외 처리

`try` / `except` / `finally`.

→ [`advanced/code/L05_exception.py`](advanced/code/L05_exception.py)

## L06 · 리스트 컴프리헨션

`[식 for 변수 in iterable]`로 리스트를 짧게 만든다.

→ [`advanced/code/L06_comprehension.py`](advanced/code/L06_comprehension.py)

## L07 · lambda

이름 없는 짧은 함수. `sorted`의 `key` 등에 자주 쓴다.

→ [`advanced/code/L07_lambda.py`](advanced/code/L07_lambda.py)

## L08 · 모듈 / import

다른 모듈·표준 라이브러리를 가져온다.

→ [`advanced/code/L08_import.py`](advanced/code/L08_import.py)

## L09 · 파일 입출력

`with open(...)`으로 읽고 쓴다. 끝나면 자동으로 닫힌다.

→ [`advanced/code/L09_file_io.py`](advanced/code/L09_file_io.py)

## L10 · 타입 힌트

`이름: 타입`, `-> 반환타입`. 실행을 막지는 않는다.

→ [`advanced/code/L10_type_hint.py`](advanced/code/L10_type_hint.py)

## L11 · \*args / \*\*kwargs

남는 위치 인자·키워드 인자를 묶어서 받는다.

→ [`advanced/code/L11_args_kwargs.py`](advanced/code/L11_args_kwargs.py)

## L12 · 데코레이터

`@데코레이터`로 함수를 감싸 기능을 추가한다.

→ [`advanced/code/L12_decorator.py`](advanced/code/L12_decorator.py)

## L13 · dataclass

데이터용 클래스를 짧게 만든다. (Java `record`와 비슷)

→ [`advanced/code/L13_dataclass.py`](advanced/code/L13_dataclass.py)

## L14 · 제너레이터

`yield`로 값을 하나씩 만든다.

→ [`advanced/code/L14_generator.py`](advanced/code/L14_generator.py)

## L15 · enumerate / zip

인덱스와 함께 순회, 여러 시퀀스를 나란히 묶기.

→ [`advanced/code/L15_enumerate_zip.py`](advanced/code/L15_enumerate_zip.py)

## L16 · pathlib

경로를 `Path`로 다룬다.

→ [`advanced/code/L16_pathlib.py`](advanced/code/L16_pathlib.py)

## L17 · json

딕셔너리 ↔ JSON 문자열.

→ [`advanced/code/L17_json.py`](advanced/code/L17_json.py)

## L18 · venv / pip

프로젝트별 가상환경과 패키지 설치. (명령은 파일 주석 참고)

→ [`advanced/code/L18_venv_pip.py`](advanced/code/L18_venv_pip.py)
