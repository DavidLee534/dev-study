# [문법] tuple — 튜플
#
# 실행: python L12_tuple.py
#
# 리스트와 비슷하지만 불변(추가/수정/삭제 불가).
# (값, 값) 또는 콤마만으로 만든다.

point = (3, 4)
print(point[0], point[1])

# 값 교환에 자주 쓴다
a, b = 1, 2
a, b = b, a
print(a, b)  # 2 1
