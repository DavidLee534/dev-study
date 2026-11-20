# [문법] for 반복문
#
# 실행: python L09_for.py
#
# for 변수 in iterable:  형태로 순회한다.
# range(n) → 0 부터 n-1 까지

for i in range(5):
    print(i)  # 0 1 2 3 4

penguins = ["스키퍼", "코왈스키", "프라이빗"]
for name in penguins:
    print(name)
