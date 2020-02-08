
def find_path(data_str):
    out_str=''
    for each in data_str:
        if each=='E':
            out_str+='S'
        elif each=='S':
            out_str+='E'
    return out_str


t = int(input())

data_list = []
for j in range(0,t):
    input()
    data_list.append(input())

for count in range(1, len(data_list)+1):
    val = find_path(data_list[count-1])
    print("CASE #{}: {}".format(count, val))
