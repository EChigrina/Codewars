import sys

def brain_luck(code, input):
    output = ""
    input = list(input)
    
    len_code = len(code)
    data_arr = [0]*30
    data_pointer = 0
    code_pointer = 0

    loop_start_pointer = []
    while code_pointer < len_code:
        instruction = code[code_pointer]
        if instruction == '.':
            output += chr(data_arr[data_pointer])
        elif instruction == ',':
            if len(input) != 0:
                data_arr[data_pointer] = ord(input.pop(0))
        elif instruction == '>':
            data_pointer += 1
        elif instruction == '<':
            data_pointer -= 1
        elif instruction == '+':
            data_arr[data_pointer] += 1
            if data_arr[data_pointer] == 256:
                data_arr[data_pointer] = 0
        elif instruction == '-':
            data_arr[data_pointer] -= 1
            if data_arr[data_pointer] == -1:
                data_arr[data_pointer] = 255
        elif instruction == '[':
            if data_arr[data_pointer] == 0:
                pair_bracket = True
                for i in range(code_pointer + 1, len_code):
                    if code[i] == '[':
                        pair_bracket = False
                    elif code[i] == ']' and not pair_bracket:
                        pair_bracket = True
                    elif code[i] == ']' and pair_bracket:
                        break
                code_pointer = i
            else:
                loop_start_pointer.append(code_pointer)
        elif instruction == ']':
            if data_arr[data_pointer] != 0:
                code_pointer = loop_start_pointer[len(loop_start_pointer) - 1]
            else:
                loop_start_pointer.pop()
        code_pointer += 1   
    return output
