def Color(A, C, i):
    if i == len(A) - 1:  # Python uses 0-based indexing, so n-1 is the last index
        k = 0
        # Compute largest color value occurring in the coloring
        for j in range(len(A)):
            k = max(k, C[j])
        return k
    else:
        bestValue = float('inf')
        # Try all valid options of assigning a color to the next vertex, number i+1
        for x in range(1, len(A) + 1):  # Colors from 1 to n
            freeColor = True
            # Check if color x does not yet appear on a neighbor j of vertex i+1
            for j in A[i+1]:  # Assuming A[i+1] contains the neighbors of vertex i+1
                if C[j - 1] == x:
                    freeColor = False
                    break
            if freeColor:
                C[i+1] = x
                # print(bestValue)
                bestValue = min(bestValue, Color(A, C, i+1))
                C[i+1] = 0
        return bestValue
    

A = [[3,4], [3,4,5,6], [1,4,6], [1,2,3], [2, 5], [2,3,5]]
C = [1,2,0,0,0,0]
print(Color(A, C, 1))