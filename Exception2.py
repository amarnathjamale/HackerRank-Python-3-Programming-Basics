def FORLoop():
    # Write your code here
    n = int(input())
    l1 = []
    for i in range(n):
        elements = int(input())
        l1.append(elements)
    print(l1)
    
    iter1 = iter(l1)
    
    while True:
        print(next(iter1))
