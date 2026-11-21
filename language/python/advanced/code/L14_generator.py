# [문법] 제너레이터 (yield)
#
# 실행: python L14_generator.py
#
# return 대신 yield 를 쓰면 값을 하나씩 만들어 내는 제너레이터가 된다.
# 한꺼번에 리스트를 안 만들어도 되어 메모리를 아낀다.


def countdown(n):
    while n > 0:
        yield n
        n -= 1


for x in countdown(3):
    print(x)  # 3 2 1


# 제너레이터 식: (식 for ... )
squares = (n * n for n in range(1, 4))
print(list(squares))  # [1, 4, 9]
