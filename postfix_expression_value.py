def do_operation(operand1, operand2, operator):
    # eval("1+2+3") = 6
    return eval(operand1 + operator + operand2)

def postfix_evalute(expression):
    operands = []
    operators = "*/+-"

    # to calculate postfix notation we have to traverse from left to right
    for character in expression:
        if character.isdigit():
            operands.append(character)
        elif character in operators:
            operand2 = operands.pop()
            operand1 = operands.pop()

            # if character is an operator then work with previous two values and store the result in stack
            result = do_operation(operand1, operand2, character)
            operands.append(str(result))

    result = operands.pop()
    return result

print(postfix_evalute("132*+"))

