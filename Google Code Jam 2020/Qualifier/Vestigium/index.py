
def find_trace(matrix, size):
    sum=0
    for count in range(0, size):
        sum += matrix[count][count]
    return sum

def find_repeating_rows(matrix, size):
    count = 0 
    for k in range(0, size):
        set_list = set(matrix[k])
        if len(set_list)!= len(matrix[k]):
            count+=1
    return count

def find_repeating_cols(matrix, size):
    t_matrix = list(map(list, zip(*matrix)))
    return find_repeating_rows(t_matrix, size)

test_cases = int(input())

for case in range(0, test_cases):
    matrix = []
    size = int(input())
    for i in range(0, size):
        data_list = input()
        data_list = data_list.split(' ')
        data_list = [int(k) for k in data_list]
        matrix.append(data_list)
    trace = find_trace(matrix, size)
    no_rows = find_repeating_rows(matrix, size)
    no_cols = find_repeating_cols(matrix, size)
    print("Case #{}: {} {} {}".format(case+1, trace, no_rows, no_cols))