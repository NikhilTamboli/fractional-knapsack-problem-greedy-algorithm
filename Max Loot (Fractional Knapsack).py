# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    bits = []
    i=0
    for v in values:
        bits.append(v/weights[i])
        i += 1 
    # bits.sort()
    # bits = bits[::-1]
    # print(bits)
    # while capacity>0 and len(bits)>0:
    #     maxi = bits.index(max(bits))
    #     if weights[maxi] <= capacity:
    #         capacity -= weights[maxi]
    #         value += values[maxi]
    #         bits.remove(bits[maxi])
    #     else:
    #         value += capacity*bits[maxi]
    #         capacity=0
    
    for i in range(len(values)):
        maxi = bits.index(max(bits))
        if capacity == 0:
            return value
        a = min(weights[maxi], capacity)
        value += a*bits[maxi]
        capacity -= a 
        weights[maxi] -= a 
        bits[maxi] = 0
    
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
