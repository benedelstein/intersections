from intersection import crashes_at_n_way_given_my_direction
import matplotlib.pyplot as plt
import numpy as np
import sys

## how many crashes will occur given each destination index in the intersection?
# some directions are more dangerous than others, it seems if you are going substantially across the intersection (dest = n/2) then you have higher probability of getting hit
def generate_graph(num_ways):
    hits_by_destination = []
    hit_rates = []
    non_hits = []
    indices = range(1,num_ways) # my end direction
    for i in indices:
        (hits, total) = crashes_at_n_way_given_my_direction(num_ways,i)
        hits_by_destination.append(hits)
        hit_rates.append(hits / total)
        non_hits.append((num_ways-1)**2 - hits)
        no_crashes_eqn = (num_ways-i) + (num_ways-i-1)**2 + (i-1)*(i-2)
        print("match?", no_crashes_eqn == (num_ways-1)**2-hits)

    sum_rates = sum([x/(num_ways-1) for x in hit_rates])
    print(sum_rates)
    plt.figure(1)
    scaled_indices = [translate(x,1,num_ways-1, 0, 1) for x in indices]
    z = np.polyfit(scaled_indices,hits_by_destination,2)
    print(z)
    p = np.poly1d(z)
    xp = np.linspace(0, 1, 20)

    ax1 = plt.subplot(221)
    plt.plot(scaled_indices, hits_by_destination)
    plt.plot(xp,p(xp),'.',label='quadratic fit')
    plt.axhline(y=(num_ways-1)**2, color='r', linestyle='-',label='maximum number of crashes')
    plt.legend()

    ax1.set_ylim([0,(num_ways-1)**2 * 1.2])

    z1 = np.polyfit(scaled_indices, hit_rates,2)
    p1 = np.poly1d(z1)
    ax1.set(ylabel="number of crashes")
    plt.suptitle(f"number of crashes vs. car A destination index at {num_ways}-way intersection")
    ax2 = plt.subplot(223)
    ax2.set(xlabel="dest. index normalized from 0-1")
    ax2.set(ylabel="crash rate")
    plt.plot(scaled_indices, hit_rates)
    plt.plot(xp,p1(xp),'.')
    print(z1)

    print("index of max crashes:", indices[np.argmax(hits_by_destination)]) # add 1 because the array starts at index 1
    # print("total hits:",sum(hits_by_destination))

    # non-normalized values
    plt.subplot(222)
    plt.plot(indices,hits_by_destination)
    ax4 = plt.subplot(224)
    ax4.set(xlabel="dest. index")
    plt.plot(indices,hit_rates)

    plt.show()


def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

generate_graph(int(sys.argv[1]))
# generate_graph(50)