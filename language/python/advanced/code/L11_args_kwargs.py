# [문법] *args / **kwargs
#
# 실행: python L11_args_kwargs.py
#
# *args   → 남는 위치 인자를 튜플로
# **kwargs → 남는 키워드 인자를 딕셔너리로


def demo(a, *args, **kwargs):
    print("a =", a)
    print("args =", args)
    print("kwargs =", kwargs)


demo(1, 2, 3, name="스키퍼", rank=1)


def total(*nums):
    return sum(nums)


print("합 =", total(1, 2, 3, 4))
