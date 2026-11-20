# [문법] 데코레이터 (@)
#
# 실행: python L12_decorator.py
#
# 함수를 감싸서 기능을 추가한다.
# @데코레이터 는 함수 = 데코레이터(함수) 와 같다.


def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"호출: {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


@log_call
def greet(name):
    print(f"안녕, {name}")


greet("코왈스키")
