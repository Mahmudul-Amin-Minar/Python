def do_operation(operand1, operand2, operator):
    return eval(operand1 + operator + operand2)

def prefix_evaluation(expression):
    operands = []
    operators = "*/+-"

    # for prefix notation we have traverse form right to left
    for character in expression[::-1]:
        if character.isdigit():
            operands.append(character)

        elif character in operators:
            operand2 = operands.pop()
            operand1 = operands.pop()

            result = do_operation(operand1, operand2, character)
            operands.append(str(result))
    result = operands.pop()
    return result

print(prefix_evaluation("*+132"))