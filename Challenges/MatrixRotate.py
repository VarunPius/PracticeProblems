def matrix(n, m, li): 
  
    # Counter Variable 
    ctr = 0
    while(ctr < 2 * n-1): 
        #print(" "*abs(n-ctr-1), end="") 
        lst = [] 
  
        # Iterate [0, m] 
        for i in range(m): 
  
                # Iterate [0, n] 
            for j in range(n): 
  
                # Diagonal Elements 
                # Condition 
                if i + j == ctr: 
  
                    # Appending the 
                    # Diagonal Elements 
                    lst.append(li[i][j]) 
  
        # Printing reversed Diagonal 
        # Elements 
        print(lst)
        lst.reverse() 

        #print(*lst) 
        ctr += 1
  
  
# Driver Code 
  
# Dimensions of Matrix 
n = 8
m = n 
  
# Given matrix 
li = [[4, 5, 6, 9, 8, 7, 1, 4], 
      [1, 5, 9, 7, 5, 3, 1, 6], 
      [7, 5, 3, 1, 5, 9, 8, 0], 
      [6, 5, 4, 7, 8, 9, 3, 7], 
      [3, 5, 6, 4, 8, 9, 2, 1], 
      [3, 1, 6, 4, 7, 9, 5, 0], 
      [8, 0, 7, 2, 3, 1, 0, 8], 
      [7, 5, 3, 1, 5, 9, 8, 5]] 
  
# Function Call 
matrix(n, m, li) 




