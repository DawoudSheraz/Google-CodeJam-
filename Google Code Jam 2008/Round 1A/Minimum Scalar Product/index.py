

def minimum_scalar_product(list_1, list_2, length):

    list_1.sort()
    list_2 = sorted(list_2, reverse=True)
    min_product = 0

    for k in range(0, length):
        min_product += (list_1[k] * list_2[k])
    
    return min_product


input_file = open('A-large-practice.in', 'r')
out_file = open('out-large.out', 'w')

t = int(input_file.readline())

for count in range(1, t+1):
    list_length = int(input_file.readline())
    list_1 = input_file.readline().split()
    list_2 = input_file.readline().split()
    list_1 = [int(k) for k in list_1]
    list_2 = [int(k) for k in list_2]
    out_file.write("CASE #{}: {}\n".format(count, minimum_scalar_product(list_1, list_2, list_length)))