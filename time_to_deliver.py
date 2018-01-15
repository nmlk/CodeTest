def  time_to_deliver(num_packages, delivery_sequence):
    drones = set([x.split("-")[0] for x in delivery_sequence])
    pos = {d:1 for d in drones}
    
    total_time = 0
    trip_time  = 0
    prev_drone = delivery_sequence[0].split('-')[0]
    
    for s in delivery_sequence:
        this_drone = s.split('-')[0]
        this_pos = int(s.split('-')[1])
        
        if this_drone == prev_drone:
            trip_time = this_pos - pos[this_drone] +1
            total_time += trip_time
            pos[this_drone] = this_pos
        else:
            trip_time = max(this_pos-pos[this_drone] +1-trip_time,1)
            total_time += trip_time
            pos[this_drone] = this_pos
        
        prev_drone = this_drone
    
    return total_time
