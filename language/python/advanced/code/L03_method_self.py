# [문법] 메서드와 self
#
# 실행: python L03_method_self.py
#
# self = 호출한 그 객체 자신. 메서드 첫 매개변수로 꼭 받는다.
# 호출할 때는 p.introduce() 처럼 self 를 직접 안 넘긴다.


class Penguin:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"나는 {self.name}")

    def shout(self, word):
        print(f"{self.name}: {word}!")


p = Penguin("리코")
p.introduce()
p.shout("BANG")
