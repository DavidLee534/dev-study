# [문법] __init__ — 생성자
#
# 실행: python L02_init.py
#
# 객체를 만들 때 자동 호출된다. 초기값을 넣을 때 쓴다.


class Penguin:
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank


p = Penguin("스키퍼", 1)
print(f"{p.name} / 서열 {p.rank}")
