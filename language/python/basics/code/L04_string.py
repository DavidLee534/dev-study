# [문법] 문자열 (str)
#
# 실행: python L04_string.py
#
# 작은따옴표 '...' 또는 큰따옴표 "..." 둘 다 가능.
# f"..." 로 변수 mid 에 넣을 수 있다 (f-string).

name = "스키퍼"
msg = '헬로'

# f-string: { } 안에 변수/식
print(f"{name} 안녕")
print(f"길이 = {len(name)}")

# 이어 붙이기
print(msg + ", " + name)
