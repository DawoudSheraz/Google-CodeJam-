

def find_optimal_engine(engine_query_indices_list, to_skip=''):

    min_index_dict = {key:min(engine_query_indices_list[key]) for key in engine_query_indices_list.keys() if key!=to_skip}
    
    values=list(min_index_dict.values())
    keys=list(min_index_dict.keys())
    if values == []:
        return None
    max_value = max(values)
    max_value_index = max(idx for idx, val in enumerate(values) if val == max_value) 

    return keys[max_value_index]

def saving_the_universe(search_engines, query_list):

    engine_hit_count_dict = {key:0 for key in search_engines}
    engine_query_indices_list = {key:[] for key in search_engines}
    number_of_switches = 0

    for count, each in enumerate(query_list):
        engine_hit_count_dict[each] +=1
        engine_query_indices_list[each].append(count)
    
    if 0 in engine_hit_count_dict.values():
            return number_of_switches
    
    engine_query_indices_list = {key:engine_query_indices_list[key] for key in engine_query_indices_list.keys()}
    current_engine = find_optimal_engine(engine_query_indices_list)
    for each in query_list:
        
        if each == current_engine:
            number_of_switches += 1
            if 0 in engine_hit_count_dict.values():
                current_engine = None
            else:
                current_engine = find_optimal_engine(engine_query_indices_list, current_engine)

        engine_hit_count_dict[each] -= 1
        engine_query_indices_list[each].pop(0)
        if engine_query_indices_list[each] == []:
            del engine_query_indices_list[each]
    
    return number_of_switches


input_file = open('A-large-practice.in', 'r')
out_file = open('out-large.out', 'w')

t = int(input_file.readline())

search_engines = []

query_list = []

for k in range(1, t+1):
    search_engines = []
    query_list = []
    engines_count = int(input_file.readline())
    for count in range(0, engines_count):
        search_engines.append(input_file.readline())
    query_count = int(input_file.readline())
    for count in range(0, query_count):
        query_list.append(input_file.readline())
    
    out_file.write("CASE #{}: {}\n".format(k, 0 if query_count==0 else saving_the_universe(search_engines, query_list)))