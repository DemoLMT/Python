def find_second_largest(arr):
    arr.sort(reverse=True)
    for i in range(0, len(arr)):
        if arr[i] < arr[0]:
            return arr[i]
    return "NOT FOUND"
n = int(input())
arr = list(map(int, input().split()*n))
print(find_second_largest(arr))