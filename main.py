import re

data = """
park 950101-1234567
lee  890212-3456789
"""

pat = re.compile("(\d{6})[-]\d{7}") # 주어진 텍스트에서 "6자리 숫자 - 7자리 숫자" 형식을 가진 패턴
print(pat.sub("\g<1>-*******", data)) # 첫번째 그룹(\d{6})뒤에 '-*******' 문자로 대체 