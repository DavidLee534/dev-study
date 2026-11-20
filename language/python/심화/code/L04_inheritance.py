# [문법] 상속
#
# 실행: python L04_inheritance.py
#
# class 자식(부모): 으로 부모의 속성과 메서드를 물려받는다.


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name}이(가) 소리친다")


class Penguin(Animal):
    def slide(self):
        print(f"{self.name}이(가) 미끄러진다")


p = Penguin("프라이빗")
p.speak()   # 부모 메서드
p.slide()   # 자식 메서드
