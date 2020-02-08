
def change_list_to_nine(index, data_list):

    for j in range(index, len(data_list)):
        data_list[j] = 9
    return data_list

def check_tidy(number):
    digit_list = [int(x) for x in str(number)]

    found = False
    while not found:
        found = True
        for j in range(0, len(digit_list)-1):
            if digit_list[j] > digit_list[j+1]:
                found = False
                digit_list[j] = digit_list[j] - 1
                digit_list = change_list_to_nine(j+1, digit_list)
                break
    
    digit_list = [str(i) for i in digit_list] 
    return int(''.join(digit_list))


with open('B-large-practice.in', 'r') as input_file:
    t = int(input_file.readline())
    out_file = open('B-large-out.out', 'w')
    for k in range(1, t+1):
        out_file.write("CASE #{}: {}\n".format(k, check_tidy(int(input_file.readline()))))