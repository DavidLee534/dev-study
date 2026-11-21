# [문법] json
#
# 실행: python L17_json.py
#
# 딕셔너리 ↔ JSON 문자열 변환. API·설정 파일에 자주 쓴다.


import json

data = {
    "leader": "스키퍼",
    "members": ["코왈스키", "리코", "프라이빗"],
    "ready": True,
}

text = json.dumps(data, ensure_ascii=False, indent=2)
print(text)

parsed = json.loads(text)
print("리더 =", parsed["leader"])
print("멤버 수 =", len(parsed["members"]))
