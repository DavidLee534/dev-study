# [문법] enumerate / zip
#
# 실행: python L15_enumerate_zip.py
#
# enumerate: 인덱스와 값을 같이
# zip: 여러 시퀀스를 나란히 묶기


names = ["스키퍼", "코왈스키", "프라이빗"]

for i, name in enumerate(names):
    print(f"{i}: {name}")

ranks = [1, 2, 3]
for name, rank in zip(names, ranks):
    print(f"{name} → 서열 {rank}")
