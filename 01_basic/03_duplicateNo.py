arr = [2,4,1,3,2,1,5]

for idx in range(len(arr)):
    for secIdx in range(idx + 1, len(arr)):
        if(arr[secIdx] == arr[idx]):
            print(arr[idx])

