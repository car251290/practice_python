def triplets(a,b,c):
    #Complete the triplets function in the editor below. It must return the number of distinct triplets that can be formed from the given arrays.
    #triplets has the following parameter(s):
    #a, b, c: three arrays of integers .
    
    # The idea is to sort the arrays and then iterate through the middle array, b. For each element in b, we count the number of elements in a that are less than or equal to it and the number of elements in c that are less than or equal to it. The number of triplets that can be formed with b[i] as the middle element is the product of these two counts. We sum this product over all elements in b to get the total number of triplets.
    # sort the arrays a.b.c and remove duplicates
    # set the indices for the arrays to 0
    a = sorted(set(a))
    b = sorted(set(b))
    c = sorted(set(c))
    # initialize the indices for the arrays
    ai = 0
    bi = 0
    ci = 0
    # initialize the count of triplets
    ans = 0
    # while we haven't reached the end of b
    while bi < len(b):
        # find the number of elements in a that are less than or equal to b[bi]
        while ai < len(a) and a[ai] <= b[bi]:
            ai += 1
        # find the number of elements in c that are less than or equal to b[bi]
        while ci < len(c) and c[ci] <= b[bi]:
            ci += 1
        # increment the count of triplets
        ans += ai * ci
        # increment the index for b
        bi += 1
        #   return the count of triplets
    return ans

        
        



