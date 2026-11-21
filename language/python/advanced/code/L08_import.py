# [문법] 모듈 / import
#
# 실행: python L08_import.py
#
# 다른 파일·표준 라이브러리의 기능을 가져온다.
# import 모듈 / from 모듈 import 이름


import math
from random import choice

print(math.sqrt(16))          # 4.0
print(math.pi)

penguins = ["스키퍼", "코왈스키", "리코", "프라이빗"]
print(f"오늘의 펭귄: {choice(penguins)}")
