# [문법] dataclass
#
# 실행: python L13_dataclass.py
#
# 데이터 보관용 클래스를 짧게 만든다.
# __init__, __repr__, __eq__ 등을 자동 생성. (Java record 와 비슷)


from dataclasses import dataclass


@dataclass
class Penguin:
    name: str
    rank: int


p1 = Penguin("스키퍼", 1)
p2 = Penguin("스키퍼", 1)

print(p1)                 # Penguin(name='스키퍼', rank=1)
print(p1.name, p1.rank)
print("equals?", p1 == p2)  # True
