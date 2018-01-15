def min_cost(num_days, demands, max_capacity, shipping_cost, price, overnight_cost):
    count_ice_cream = float('inf')
    count_day = 1
    cost1 = []
    
    for i in demands:
        storage_cost = i*count_day*overnight_cost
        
        if count_ice_cream + i<= max_capacity and storage_cost < shipping_cost:
            cost1.append(storage_cost)
            count_ice_cream += i
            count_day +=1
        else:
            cost1.append(shipping_cost)
            count_ice_cream = i
            count_day = 1
            
            
    demands.reverse()
    count_ice_cream = float('inf')
    cost2 = []
    
    for i in demands:
        storage_cost += count_ice_cream*overnight_cost
        
        if count_ice_cream + i<= max_capacity and storage_cost < shipping_cost:
            cost2.append(storage_cost)
            count_ice_cream += i
        else:
            cost2.append(shipping_cost)
            storage_cost = 0
            count_ice_cream = i

    cost1.insert(0,0)
    cost2.insert(0,0)

    def accumu(lis):
        total = 0
        for x in lis:
            total += x
            yield total
        
    accum_cost1 = list(accumu(cost1))
    accum_cost2 = list(accumu(cost2))
    accum_cost2.reverse()

    accum_cost = [a + b for a, b in zip(accum_cost1, accum_cost2)]

    shipping_storage = min(accum_cost)
    total_cost = shipping_storage + sum(demands)*price

    return total_cost
