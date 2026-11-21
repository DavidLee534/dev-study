# [문법] set — 집합
#
# 실행: python L14_set.py
#
# 중복 없음. 순서 보장하지 않음. Java HashSet 과 비슷.

tags = {"python", "java", "python"}  # python 한 번만
tags.add("spring")

print(len(tags))
print("java" in tags)

for tag in tags:
    print(tag)
