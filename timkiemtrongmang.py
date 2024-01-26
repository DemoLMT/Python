def search_element(arr, x):
    if x in arr:
        return "YES"
    else:
        return "NO"
n,x  = map(int,input().split())
arr=list(map(int, input().split()*5))
print(search_element(arr, x))