
from datetime import datetime, timedelta


def custom_data(date_string):
    return datetime.strptime(date_string, "%H:%M")

def find_buses(source_departure_list, second_source_arrival_list):

    buses_count = len(source_departure_list)
    source_departure_list.sort()
    second_source_arrival_list.sort()
    for index1, source_departure in enumerate(source_departure_list):
        for index2, source_arrival in enumerate(second_source_arrival_list):
            if source_departure >= source_arrival:
                source_departure_list.pop(index1)
                second_source_arrival_list.pop(index2)
                return find_buses(source_departure_list, second_source_arrival_list)
    return buses_count

input_file = open('B-large-practice.in', 'r')
out_file = open('out-large.out', 'w')
t= int(input_file.readline())

for case in range(1, t+1):
    turnaround_time = int(input_file.readline())
    a_trips_departure_list = []
    b_trips_departure_list = []
    a_trips_arrival_list = []
    b_trips_arrival_list = []
    trips_a, trips_b = input_file.readline().split()
    trips_a, trips_b = int(trips_a), int(trips_b)

    for count in range(0, trips_a):
        trip = input_file.readline()
        a_trips_departure_list.append(custom_data(trip.split()[0]))
        a_trips_arrival_list.append(custom_data(trip.split()[1]) + timedelta(minutes=turnaround_time))
    
    for count in range(0, trips_b):
        trip = input_file.readline()
        b_trips_departure_list.append(custom_data(trip.split()[0]))
        b_trips_arrival_list.append(custom_data(trip.split()[1])+ timedelta(minutes=turnaround_time))

    if trips_a==0 or trips_b==0:
        out_file.write("CASE #{}: {} {}\n".format(case, trips_a, trips_b))
    else:
        buses_a = find_buses(a_trips_departure_list, b_trips_arrival_list)
        buses_b = find_buses(b_trips_departure_list, a_trips_arrival_list)
        out_file.write("CASE #{}: {} {}\n".format(case, buses_a, buses_b))
