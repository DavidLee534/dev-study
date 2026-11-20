# [문법] return — 반환값
#
# 실행: python L17_return.py
#
# return 으로 결과를 돌려준다. 안 쓰면 None 이 반환된다.


def add(a, b):
    return a + b


total = add(3, 5)
print(f"합 = {total}")
print(f"두 배 = {add(7, 7)}")
