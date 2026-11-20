# [문법] list — 리스트
#
# 실행: python L11_list.py
#
# 순서가 있는 가변 목록. 인덱스는 0부터.
# Java 의 ArrayList 와 비슷하다.

names = ["스키퍼", "코왈스키", "리코"]

print(names[0])       # 스키퍼
print(len(names))     # 3

names.append("프라이빗")  # 끝에 추가
names.remove("리코")      # 값으로 삭제

print(names)
