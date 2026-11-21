# [문법] if / elif / else
#
# 실행: python L08_if.py
#
# 들여쓰기(스페이스 4칸)로 블록을 구분한다. { } 는 없다.

score = 75

if score >= 90:
    print("등급: A")
elif score >= 80:
    print("등급: B")
elif score >= 60:
    print("등급: C")  # ← 여기
else:
    print("등급: F")
