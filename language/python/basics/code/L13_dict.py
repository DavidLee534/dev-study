# [문법] dict — 딕셔너리
#
# 실행: python L13_dict.py
#
# 키 → 값. Java 의 Map / HashMap 과 같다.

ages = {
    "스키퍼": 25,
    "코왈스키": 30,
}

ages["스키퍼"] = 26          # 수정
ages["프라이빗"] = 20        # 추가

print(ages["스키퍼"])
print("코왈스키" in ages)    # 키 있는지

for name, age in ages.items():
    print(f"{name} → {age}")
