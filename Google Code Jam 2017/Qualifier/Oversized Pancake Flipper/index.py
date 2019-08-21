

def validate_if_all_pancakes_happy(pancakes_list):

    all_happy = True
    for each in pancakes_list:
        if each == '-':
            all_happy = False
            break
    
    return all_happy


def get_first_blank_face_index_from_right(pancakes_list):

    index= len(pancakes_list) - 1
    for k in range(len(pancakes_list)-1, -1, -1):
        if pancakes_list[k] == '-':
            index = k
            break
    return index


def validate_flip_possible(pancakes_list, start_index, flip_count):

    if ((start_index +1) - flip_count) >= 0:
        return True
    return False 


def flip_consecutive_pancakes(pancakes_list, start_index, consecutive_count):

    for count in range(start_index, start_index - consecutive_count, -1):
        pancakes_list[count] = '+' if pancakes_list[count] == '-' else '-'


def oversized_pancake_flipper(pancakes_list, flip_count):
    number_of_flips = 0

    if(validate_if_all_pancakes_happy(pancakes_list)):
        return 0
    
    while True:

        if validate_if_all_pancakes_happy(pancakes_list):
            break
        flip_index = get_first_blank_face_index_from_right(pancakes_list)
        if validate_flip_possible(pancakes_list, flip_index, flip_count):
            flip_consecutive_pancakes(pancakes_list, flip_index, flip_count)
            number_of_flips +=1
        else:
            break
    
    if not validate_if_all_pancakes_happy(pancakes_list):
        return 'IMPOSSIBLE'
    return number_of_flips


with open('A-large-practice.in', 'r') as input_file:
    output_file = open('out-large.out', 'w')
    t = int(input_file.readline().strip())
    for j in range(1, t+1):
        input_data = input_file.readline()
        input_data = input_data.split()
        output_file.write("CASE #{}: {}\n".format(j, oversized_pancake_flipper(list(input_data[0]), int(input_data[1]))))
