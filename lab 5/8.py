import re
text = "ZhantoreSvanov"
print(re.findall('[A-Z][^A-Z]*', text))