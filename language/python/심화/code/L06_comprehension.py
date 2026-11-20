# [문법] 리스트 컴프리헨션
#
# 실행: python L06_comprehension.py
#
# [식 for 변수 in iterable] 로 리스트를 짧게 만든다.
# 조건은 if 로 붙인다.


nums = [1, 2, 3, 4, 5, 6]

squares = [n * n for n in nums]
evens = [n for n in nums if n % 2 == 0]
labels = [f"n={n}" for n in nums if n > 3]

print(squares)  # [1, 4, 9, 16, 25, 36]
print(evens)    # [2, 4, 6]
print(labels)
