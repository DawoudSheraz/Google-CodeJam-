
def get_new_str(input_str):
    output_str = ""
    prev_value = int(input_str[0])
    output_str+=('(' * prev_value ) + str(prev_value)
    for count in range(1, len(input_str)):
        current = int(input_str[count])
        if current>prev_value:
            output_str+= ('(' * (current-prev_value)) + str(current)
        elif current<prev_value:
            output_str+= (')'* abs(prev_value-current)) + str(current)
        elif current==prev_value:
            output_str+=str(current)
        prev_value = current
    output_str+=')'* (prev_value)
    return output_str

test_cases = int(input())

for test in range(0, test_cases):
    data_str = input()
    out = get_new_str(data_str)
    print("Case #{}: {}".format(test+1, out))