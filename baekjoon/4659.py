import sys

def contains_aeiou(text):
    return text.__contains__("a") or text.__contains__("e") or text.__contains__("i") or text.__contains__("o") or text.__contains__("u")

def continued_letter_check(text):
    cnt = 0
    is_v = False
    last_let = ""
    for let in text:
        if contains_aeiou(let):
            if is_v:
                cnt += 1
                if cnt >= 3:
                    return False
            else:
                is_v = True
                cnt = 1
        else:
            if not is_v:
                cnt += 1
                if cnt >= 3:
                    return False
            else:
                is_v = False
                cnt = 1

        if let == last_let and let not in ["o", "e"]:
            return False
        last_let = let
    return True


while True:
    txt = sys.stdin.readline().replace("\n", "")
    if txt == "end":
        break

    if contains_aeiou(txt) and continued_letter_check(txt):
        print("<"+txt+"> is acceptable.")
    else:
        print("<"+txt+"> is not acceptable.")