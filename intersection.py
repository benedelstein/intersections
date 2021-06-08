import sys

def will_crash(num_ways, my_end, other_start, other_end):
    my_start = 0 # always define my start position as 0    
    if other_start == my_start or my_start == my_end or other_start == other_end or my_end >= num_ways or other_end >= num_ways or other_start >= num_ways:
        raise Exception("invalid inputs")

    # if other_end is 0, set it to num_ways to simplify (basically like saying 0 degrees = 360 degrees)
    if other_end == 0:
        other_end = num_ways

    if my_end == other_end:
        return True # always crashes if they end up in the same road, no matter the start position
    elif other_end < my_end:
        if other_start < my_end: # has to be <, not <=, because car must cross intersection to turn left
            return False
        else:
            return True
    else: # other_end > my_end
        if other_start < my_end:
            return True
        else: # other_start >= my_end.  can do >= here because car is turning right and won't cross
            return False # if other car starts where I end, and is not crossing over to a lower index, no crash

    # redundant to previous checks, never gets run
    # if other_start >= my_end:
    #     if other_end > other_start:
    #         return False # other can can also sneak to the right here
    #     else:
    #         return True # crash
    
    print(f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!unhandled scenario: {my_end} {other_start} {other_end}!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    # return False

# if len(sys.argv) > 1: # first argument is script name
#     n = int(sys.argv[1])
# else:
#     n = 5
# num_hits = 0 # counter
# total_scenarios = (n-1)**3 # I have n-1 possible end positions, the other driver has n-1 possible start positions, and for each start pos, n-1 possible end positions
# total_scenarios_sanity_check = 0

# for my_end in range(1,n): # my end cant be 0 (no u turns yet)
#     for other_start in range(1,n): # other car can't start at 0
#         for other_end in list(range(other_start)) + list(range(other_start+1,n)): # other cant start where they end
#             try:
#                 is_crash = will_crash(n,my_end,other_start,other_end)
#             except:
#                 # print(f"invalid scenario: {my_end} {other_start} {other_end}")
#                 continue # invalid input combos. this is inefficient O(n^3), maybe we can speed it up later by excluding certin numbers from the for loop range
#             total_scenarios_sanity_check += 1
#             if is_crash:
#                     num_hits+=1

# print("hits:", num_hits)
# print("hit rate:", (num_hits/total_scenarios))

# print(total_scenarios_sanity_check)

def crashes_at_n_way_intersection(n):
    num_hits = 0 # counter
    total_scenarios = (n-1)**3 # I have n-1 possible end positions, the other driver has n-1 possible start positions, and for each start pos, n-1 possible end positions
    total_scenarios_sanity_check = 0

    for my_end in range(1,n): # my end cant be 0 (no u turns yet)
        for other_start in range(1,n): # other car can't start at 0
            for other_end in list(range(other_start)) + list(range(other_start+1,n)): # other cant start where they end
                try:
                    is_crash = will_crash(n,my_end,other_start,other_end)
                except:
                    # print(f"invalid scenario: {my_end} {other_start} {other_end}")
                    continue # invalid input combos. this is inefficient O(n^3), maybe we can speed it up later by excluding certin numbers from the for loop range
                total_scenarios_sanity_check += 1
                if is_crash:
                        num_hits+=1

    return (num_hits,total_scenarios)

def crashes_at_n_way_given_my_direction(n,my_end):
    num_hits = 0
    total_scenarios = (n-1)**2 # this is just for one given end position, so squared not cubed
    for other_start in range(1,n):
        for other_end in list(range(other_start)) + list(range(other_start+1,n)):
            try:
                is_crash = will_crash(n,my_end,other_start,other_end)
            except:
                continue # invalid input combos
            if is_crash:
                    num_hits+=1
    return (num_hits, total_scenarios)

def crashes_given_other_start(n,other_start):
    num_hits = 0
    total_scenarios = (n-1)**2
    for other_end in list(range(other_start)) + list(range(other_start+1,n)): # other cant start where they end
        for my_end in range(1,n): #can't end at 0
            try:
                is_crash = will_crash(n,my_end,other_start,other_end)
            except:
                continue # invalid input combos
            if is_crash:
                    num_hits+=1
    return (num_hits,total_scenarios)

if len(sys.argv) == 2:
    print(crashes_at_n_way_intersection(int(sys.argv[1])))
elif len(sys.argv) > 2:
    print(crashes_at_n_way_given_my_direction( int(sys.argv[1]), int(sys.argv[2]) ) )



def will_crash_with_u_turns(num_ways, my_end, other_start, other_end):
    my_start = 0 # always define my start position as 0    
    if other_start == my_start or my_end >= num_ways or other_end >= num_ways or other_start >= num_ways:
        raise Exception("invalid inputs")

    # if other_end is 0, set it to num_ways to simplify (basically like saying 0 degrees = 360 degrees)
    if other_end == 0:
        other_end = num_ways

    if my_end == other_end:
        return True # always crashes if they end up in the same road, no matter the start position
    elif other_end < my_end:
        if other_start < my_end: # has to be <, not <=, because car must cross intersection to turn left
            return False
        else:
            return True
    else: # other_end > my_end
        if other_start < my_end:
            return True
        else: # other_start >= my_end.  can do >= here because car is turning right and won't cross
            return False # if other car starts where I end, and is not crossing over to a lower index, no crash
