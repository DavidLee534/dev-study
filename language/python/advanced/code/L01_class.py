# [문법] 클래스와 객체
#
# 실행: python L01_class.py
#
# 클래스 = 설계도 / 객체 = 설계도로 만든 실체


class Penguin:
    pass  # 일단 비어 있는 클래스


p1 = Penguin()
p2 = Penguin()

p1.name = "스키퍼"
p2.name = "코왈스키"

print(p1.name)
print(p2.name)
