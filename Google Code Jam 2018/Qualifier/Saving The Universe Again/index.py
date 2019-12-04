

def calculate_damage(instructions):

    damageLevel = 1
    totalDamage = 0
    for each in instructions:
        if each == 'S':
            totalDamage = totalDamage + damageLevel
        elif each == 'C':
            damageLevel = damageLevel * 2
    
    return totalDamage

def find_cs_pattern(instruction):
    
    for count in range(len(instruction)-1, 0, -1):
        if instruction[count] == 'S' and instruction[count-1] == 'C':
            return count


def swap(instruction, index):
    ins_list = list(instruction)

    ins_list[index], ins_list[index-1] = ins_list[index-1], ins_list[index]

    return ''.join(ins_list)

def save_the_world(defense, instruction):
    
    original_damage = calculate_damage(instruction)
    if original_damage <= defense:
        return 0
    original_instruction = instruction
    total_swaps = 0

    while True:
        index = find_cs_pattern(instruction)
        if not index:
            break
        instruction = swap(instruction, index)
        new_damage = calculate_damage(instruction)
        total_swaps = total_swaps + 1
        if new_damage <= defense:
            return total_swaps
    
    if total_swaps != 0 and calculate_damage(instruction) <= defense:
        return total_swaps
    return 'IMPOSSIBLE'


t= int(input())
data_list = []
for k in range(0, t):
    data_list.append(input())

for count in range(0, len(data_list)):
    defense, instruction = data_list[count].split()
    output = save_the_world(int(defense), instruction)
    print('CASE #%s: %s' % (count + 1, output))




