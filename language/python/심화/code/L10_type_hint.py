# [문법] 타입 힌트
#
# 실행: python L10_type_hint.py
#
# 이름: 타입 으로 기대 타입을 적는다. 실행을 막지는 않고, 읽기·도구 검사에 도움.


def introduce(name: str, age: int) -> str:
    return f"{name} / {age}세"


msg: str = introduce("스키퍼", 25)
print(msg)

scores: list[int] = [90, 80, 70]
print(scores)
