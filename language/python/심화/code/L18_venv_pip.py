# [문법] venv / pip (가상환경·패키지)
#
# 실행: python L18_venv_pip.py
#
# 프로젝트마다 패키지를 격리할 때 venv 를 쓴다.
# pip 로 라이브러리를 설치·목록 확인한다.
#
# --- 터미널에서 (참고) ---
#   python -m venv .venv
#   # Windows PowerShell:
#   .\.venv\Scripts\Activate.ps1
#   python -m pip install requests
#   python -m pip list
#   deactivate
#
# 아래는 "지금 이 인터프리터" 정보를 확인하는 예제이다.

import sys

print("Python =", sys.version.split()[0])
print("실행 파일 =", sys.executable)
print("가상환경?", sys.prefix != sys.base_prefix)
