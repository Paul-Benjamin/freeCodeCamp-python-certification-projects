def arithmetic_arranger(problems, calculate=False):
    space = '    '
    nl = '\n'
    allowed_op = ['+', '-']

    list_ = [i.split() for i in problems]
    straightend_list_ = [item for sublist in list_ for item in sublist]

    calculated_result = []

    num1 = []
    op = []
    num2 = []

    for i in range(len(straightend_list_) - 1):
        if not straightend_list_[i + 1].isdigit():
            num1.append(straightend_list_[i])
        elif not straightend_list_[i].isdigit():
            op.append(straightend_list_[i])

    for i in range(len(straightend_list_)):
        if not straightend_list_[i - 1].isdigit():
            num2.append(straightend_list_[i])


    num1_isdigit = all([i.isdigit() for i in num1])
    num2_isdigit = all([i.isdigit() for i in num2])

    num1_length = all([len(i) <= 4 for i in num1])
    num2_length = all([len(i) <= 4 for i in num2])

    op_check = all([True if i in allowed_op else False for i in op])

    if len(problems) > 5:
        return "Error: Too many problems."
    elif not num1_isdigit or not num2_isdigit:
        return "Error: Numbers must only contain digits."
    elif not op_check:
        return "Error: Operator must be '+' or '-'."
    elif not num1_length or not num2_length:
        return "Error: Numbers cannot be more than four digits."
    else:
        for i in range(len(straightend_list_)-1):
            if straightend_list_[i+1] == "+":
                calculated_result.append(int(straightend_list_[i]) + int(straightend_list_[i+2]))
            elif straightend_list_[i+1] == "-":
                calculated_result.append(int(straightend_list_[i]) - int(straightend_list_[i+2]))

    calculated_result = [str(i) for i in calculated_result]
    
    output = ""

    loop_first_line = ""
    loop_second_line = ""
    loop_linebreak = ""
    loop_result = ""

    lb_length1 = []
    lb_length2 = []
    final_lb_len = []

    for i in range(len(problems)):
        for j in range(1):
            lb_length1.append(len(list_[i][0]))
            lb_length2.append(len(list_[i][j+2]))
            if lb_length1[i] > lb_length2[i]:
                final_lb_len.append(lb_length1[i] + 2)
            else:
                final_lb_len.append(lb_length2[i] + 2)
            loop_first_line += list_[i][0].rjust(final_lb_len[i]) + space 
            loop_second_line += list_[i][j+1] + list_[i][j+2].rjust(final_lb_len[i]-1) + space 
            loop_result += calculated_result[i].rjust(final_lb_len[i]) + space
            loop_linebreak += "-" * (final_lb_len[i]) + space


    
    loop_first_line = loop_first_line.rstrip()
    loop_second_line = loop_second_line.rstrip()
    loop_result = loop_result.rstrip()
    loop_linebreak = loop_linebreak.rstrip()


    if calculate:
       output = loop_first_line + nl + loop_second_line + nl + loop_linebreak + nl + loop_result
    else:
       output = loop_first_line + nl + loop_second_line + nl + loop_linebreak
    
    return output