# 制作一个可以处理字符串运算的运算器（当然还不支持括号）
Q = input("What's your mathematical problem(English):")

# 1版本对于number operate 两个concentrate_1函数进行优化
# 2版本处理了运算优先级的问题
# 3版本已经解决有关 5 * -9此类问题 在后面的备注中记作bug1


def calculate_1(n):
    """
    在只允许输入0到9数字和运算符号的基础上（允许有空格）
    计算字符串n所描述数学问题的值,可以适用于 + - * / ** // (如果需要 %也可 补充上条件语句即可）
    """

    def clear_1(n):
        """
        清除字符串中的空格
        """
        char_1 = ""
        for char in n:
            if char == " ":
                continue
            else:
                char_1 += char
        return char_1

    def number_concentrate_1(n):
        """
        将n中的数字初步制作成一个列表(但是没有考虑bug1)
        """
        l = n + "."
        if l[0] == "-":
            l = '0' + l
        number = []
        i = 0
        j = 0
        t = 0
        Flag = False
        while i <= len(l) - 1:
            if Flag == True:
                t = i
            if "0" <= l[i] <= "9":
                Flag = False
                j += 1
            else:
                Flag = True
                char = ""
                if j > 0:
                    for h in l[t:t + j]:
                        char += h
                    number.append(char)
                j = 0
            i += 1
        return number

    def operating_concentrate_1(n):
        """
        将n中的运算符号初步制作一个列表（但是没有考虑bug1)
        """
        l = n + "5"
        if l[0] == "-":
            l = '0' + l
        operate = []
        i = 0
        j = 0
        t = 0
        Flag = False
        while i <= len(l) - 1:
            if Flag == True:
                t = i
            if "0" <= l[i] <= "9":
                Flag = True
                char = ""
                if j > 0:
                    for h in l[t:t + j]:
                        char += h
                    operate.append(char)
                j = 0
            else:
                Flag = False
                j += 1
            i += 1

        return operate

    def number_operate_concentrate_2(n):
        """
        进一步得到正确列表 修复bug1 即使得代表负号的“-”成为数值的一部分，而不被认作运算符
        """
        num = number_concentrate_1(n)
        operate = operating_concentrate_1(n)
        g = 0
        while g <= len(operate) - 1:
            if operate[g] == "+-":
                operate = operate[:g] + ["+"] + operate[g + 1:]
                num = num[:g+1] + ["-"+num[g+1]] + num[g +2:]
            elif operate[g] == "--":
                operate = operate[:g] + ["-"] + operate[g + 1:]
                num = num[:g+1] + ["-"+num[g+1]] + num[g +2:]
            elif operate[g] == "*-":
                operate = operate[:g] + ["*"] + operate[g + 1:]
                num = num[:g+1] + ["-"+num[g+1]] + num[g +2:]
            elif operate[g] == "/-":
                operate = operate[:g] + ["/"] + operate[g + 1:]
                num = num[:g+1] + ["-"+num[g+1]] + num[g +2:]
            elif operate[g] == "//-":
                operate = operate[:g] + ["//"] + operate[g + 1:]
                num = num[:g+1] + ["-"+num[g+1]] + num[g +2:]
            elif operate[g] == "**-":
                operate = operate[:g] + ["**"] + operate[g + 1:]
                num = num[:g+1] + ["-"+num[g+1]] + num[g +2:]
            g += 1
        return num, operate

    n = clear_1(n)
    if n[0] == "-":
        n = "0" + n  # 方便我们后续的讨论 第一个数字如果是负数就看作0减去这个数包括后面连在一起的比加法优先级高的运算
    num, operate = number_operate_concentrate_2(n)
    m = len(operate) - 1
    k = 0
    t = 0

    # 先优先进行**运算 且符合右结合运算规律
    while m >= 0:
        if operate[m] == "**":
            a = float(num[m]) ** float(num[m+1])
            if m == len(operate) - 1:
                num = num[:m]+[str(a)]
                operate = operate[:m]
            else:
                num = num[:m] + [str(a)] + num[m+2:]
                operate = operate[:m] + operate[m+1:]
        m = m - 1

    # 下一步考虑 *;/;// 这些满足左结合运算规律
    while k <= len(operate) - 1:
        if operate[k] == "*":
            a = float(num[k]) * float(num[k+1])
            num = num[:k] + [str(a)] + num[k+2:]
            operate = operate[:k] + operate[k+1:]
            continue
        elif operate[k] == "/":
            a = float(num[k]) / float(num[k+1])
            num = num[:k] + [str(a)] + num[k+2:]
            operate = operate[:k] + operate[k+1:]
            continue
        elif operate[k] == "//":
            a = float(num[k]) // float(num[k+1])
            num = num[:k] + [str(a)] + num[k+2:]
            operate = operate[:k] + operate[k+1:]
            continue
        k = k + 1

    # 再一步考虑 + - 运算
    while t <= len(operate) - 1:
        if operate[t] == "+":
            a = float(num[t]) + float(num[t+1])
            num = num[:t] + [str(a)] + num[t+2:]
            operate = operate[:t] + operate[t+1:]
            continue
        elif operate[t] == "-":
            a = float(num[t]) - float(num[t+1])
            num = num[:t] + [str(a)] + num[t+2:]
            operate = operate[:t] + operate[t+1:]
            continue
        t = t + 1
    answer = num[0]
    return answer

A = calculate_1(Q)
print("Your mathematical problem's answer is", A)

# 2*3 output 6.0
# 7-5 output 2.0
# 9 - 6/3 + 2*5 output 17.0
