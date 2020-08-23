x = int(input())
list_of_number = list(map(int,input().split()))
range_of_window = int(input())
for i in range(x-range_of_window+1):
    maximum = max(list_of_number[i:i+4])
    print(maximum,end=" ")