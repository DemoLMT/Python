def find_longest_subarray(arr, n, k):
    max_length = 0
    prefix_sum = 0
    remainder_index = {0: -1}

    for i in range(n):
        prefix_sum = (prefix_sum + arr[i]) % k
        if prefix_sum in remainder_index:
            max_length = max(max_length, i - remainder_index[prefix_sum])
        else:
            remainder_index[prefix_sum] = i

    return max_length

n, k = map(int, input().split())
arr = list(map(int, input().split()))
print(find_longest_subarray(arr, n, k))
