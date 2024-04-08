import sys

infix = sys.stdin.readline()

result = ""
stack = []
operators = ["*", "+", "/", "-"]
parenthesis = ["(", ")"]

priority_out = dict()
priority_in = dict()

priority_out["("] = 99
priority_out[")"] = 98
priority_out["+"] = 2
priority_out["-"] = 2
priority_out["*"] = 50
priority_out["/"] = 50

priority_in["("] = 1
priority_in["+"] = 2
priority_in["-"] = 2
priority_in["*"] = 50
priority_in["/"] = 50


# operand 일 때는 문자열에 붙여주기
# operator 이면? ->
# stack 에 넣어줘야 됨
# 어떤 규칙으로 넣고 빼야할까?
# 만약 ) 이면 ( 나올 때까지 전부 결과에 붙여주기
# 넣기 전에 우선 스택의 맨 위에 있는 operator 과 중요도 비교
# 만약 새로 넣는 operator 의 중요도가 더 높으면 우선 pass 하고 스택 위에 넣기
# 새로 넣는 게 더 작다? 그러면 넣기 전에 아래 수행
# 본인보다 크거나 같은 오퍼레이터를 전부 꺼내서 수행 (priority in)

for i in range(len(infix)):
    curr = infix[i]
    if (curr in operators) or (curr in parenthesis):
        if len(stack) == 0:
            stack.append(curr)
        elif i == len(infix) - 1:
            stack.append(curr)
            while stack:
                l = stack.pop()
                if l != "(" and l != ")":
                    result += l
        # 오른쪽 괄호인 경우
        elif curr == ")":
            while True:
                last_op = stack.pop()
                if last_op == "(":
                    break
                result += last_op
        else:
            last_op_priority = priority_in.get(stack[-1])
            curr_op_priority = priority_out.get(curr)
            if curr_op_priority > last_op_priority:
                stack.append(curr)
            else:
                last_op_priority_in = priority_in.get(stack[-1])
                curr_op_priority_in = priority_in.get(curr)
                while True:
                    if last_op_priority_in < curr_op_priority_in:
                        break
                    l = stack.pop()
                    result += l
                    if len(stack) == 0:
                        break
                    last_op_priority_in = priority_in.get(stack[-1])
                stack.append(curr)
    else:
        result += curr
while stack:
    l = stack.pop()
    if l != "(" and l != ")":
        result += l

print(result.replace("\n", ""))