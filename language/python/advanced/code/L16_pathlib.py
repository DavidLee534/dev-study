# [문법] pathlib — 경로 다루기
#
# 실행: python L16_pathlib.py
#
# 문자열로 경로를 이어 붙이는 대신 Path 객체를 쓴다.


from pathlib import Path

here = Path(__file__).resolve().parent
print("이 폴더 =", here)

sample = here / "sample_path.txt"
sample.write_text("리코\n", encoding="utf-8")
print("존재?", sample.exists())
print("내용 =", sample.read_text(encoding="utf-8").strip())

sample.unlink()  # 삭제
print("삭제 후 존재?", sample.exists())
