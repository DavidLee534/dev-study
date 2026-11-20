# [문법] lambda — 이름 없는 짧은 함수
#
# 실행: python L07_lambda.py
#
# lambda 매개변수: 식
# map / filter / sorted 의 key 에 자주 쓴다.


add = lambda a, b: a + b
print(add(3, 5))

nums = [3, 1, 4, 1, 5]
print(sorted(nums, key=lambda n: -n))  # 큰 수부터

names = ["리코", "스키퍼", "프라이빗"]
print(sorted(names, key=lambda s: len(s)))  # 짧은 이름부터
