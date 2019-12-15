

def convert_to_int(list): 
    s = [str(i) for i in list] 
    return int("".join(s)) 
      

def find_data_pair(value):

    out_list = []
    for j in range(0, len(value)):

        if value[j]==4:
            value[j] = value[j] - 1
            out_list.append(1)
        else:
            out_list.append(0)
    return convert_to_int(out_list), convert_to_int(value)
 
t = int(input())

data_list = []
for j in range(1, t+1):
    data_list.append(input())

for count in range(0,len(data_list)):
    a,b = find_data_pair([int(x) for x in data_list[count]])
    print("CASE #{}: {} {}".format(count+1,a,b))


