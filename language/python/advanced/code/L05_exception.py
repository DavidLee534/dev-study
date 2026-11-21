# [문법] 예외 처리 try / except / finally
#
# 실행: python L05_exception.py
#
# try 에서 시도 → except 에서 잡음 → finally 는 항상 실행.


try:
    nums = [1, 2, 3]
    print(nums[10])
except IndexError as e:
    print(f"인덱스 오류: {e}")

try:
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    print("연산 오류: 0으로 나눌 수 없음")
finally:
    print("finally: 예외 여부와 관계없이 실행")

print("프로그램 계속 진행")
