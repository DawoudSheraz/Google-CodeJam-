
SWITCH_CHAR = {
    'J': 'C',
    'C': 'J'
}

def get_output(outdata):
    if isinstance(outdata, str):
        return "IMPOSSIBLE"
    elif isinstance(outdata, list):
        new_list = sorted(outdata, key=lambda tup: tup[1])
        out_str = ''
        for each in new_list:
            out_str +=each[0]
        return out_str

def find_schedule(activities):
    last_parent = 'J'
    activity_before_switch = None
    out_list = [(last_parent, activities[0][2])]
    for count in range(1, len(activities)):
        current_activity = activities[count]
        last_activity = activities[count-1]
        if current_activity[0] >= last_activity[1]:
            out_list.append((last_parent, current_activity[2]))
        elif current_activity[0] < last_activity[1]:
            if not activity_before_switch or activity_before_switch[1] <= current_activity[0]:
                activity_before_switch = last_activity
                last_parent = SWITCH_CHAR[last_parent]
                out_list.append((last_parent, current_activity[2]))
            else:
                return "IMPOSSIBLE"
    return out_list

test_case = int(input())

for j in range(0, test_case):
    count = int(input())
    activities = []
    for i in range(0, count):
        out = input()
        out = out.split()
        out = (int(out[0]), int(out[1]), i+1)
        activities.append(out)
    sorted_act = (sorted(activities, key= lambda tup:tup[0]))
    sch = find_schedule(sorted_act)
    print("Case #{}: {}".format(j+1, get_output(sch)))