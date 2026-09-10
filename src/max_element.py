def max_element(l):
    m = l[0]        # first element is the max element

    for i in l:
        if i>m:     # whenever an element is greater than m, assign that element to m
            m = i 
    
    return m


l = [4, 2, 8, 9, 2, 1, 5, 7, 10, 3, 6]
maximum = max_element(l)

print(maximum)
    