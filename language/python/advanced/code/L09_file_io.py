# [문법] 파일 입출력
#
# 실행: python L09_file_io.py
#
# open 으로 열고, with 를 쓰면 끝나면 자동으로 닫힌다.
# "w" 쓰기, "r" 읽기, "a" 이어쓰기.


path = "penguin_note.txt"

with open(path, "w", encoding="utf-8") as f:
    f.write("스키퍼\n")
    f.write("코왈스키\n")

with open(path, "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

# 정리: 예제용 파일 삭제
import os

os.remove(path)
print("파일 삭제 완료")
