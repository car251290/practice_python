def rotLeft(a, d):
    # Write your code here
    a_len = len(a)
    b_len = a_len - d
    for i in range(d):
        a.append(a[i])
    for i in range(a_len):
        a[i] = a[i+d]
    a = a[:a_len]
    return a


    
   # return a[d:] + a[:d]