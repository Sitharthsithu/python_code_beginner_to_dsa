s = "{[]}" 
k = []

for ch in s:
    print(ch)
    if ch in "({[":
        k.append(ch)
    elif ch in ")}]":
        if not k:
            print("Invalid")
            break
        top = k.pop()
        if (ch == ")" and top != "(") or (ch == "}" and top != "{") or (ch == "]" and top != "["):
            print("Invalid")
            break
else:
    if not k:
        print("Valid")
    else:
        print("Invalid")
