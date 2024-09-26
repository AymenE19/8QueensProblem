N=8
L = [0] * N  # Initialize the list to hold the positions of queens

def place(k, i):
    # returns True if Queen is placed at k-th row and i-th column otherwise return False
    for j in range(k):
        if L[j] == i or abs(L[j] - i) == abs(j - k):
            return False
    return True

def NQueens(k, n):
    #using backtracking, this procedure prints all possible combinations of solutions
    for i in range(n):
        if place(k, i):
            L[k] = i  # Place the queen at column i in row k
            if k == n - 1:
                print([x + 1 for x in L[0:n]])  # Print the solution
            else:
                NQueens(k + 1, n)  

NQueens(0, N)  