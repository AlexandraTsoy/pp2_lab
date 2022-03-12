br= input()
i = 0
while "[]" in br or "()" in br or "{}" in br:
    if "()" in br:
        br = br.replace("()", "")
    if "[]" in br:
        br = br.replace("[]", "")
    if "{}" in br:
        br = br.replace("{}", "")
    i += 1
if len(br) > 0:
    print("No")
else:
    print("Yes")