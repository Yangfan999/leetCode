def uniquePaths(self, m: int, n: int) -> int:
    A = [1 for _ in range(n)]
    for row in range(1, m):
        for col in range(1, n):
            A[col] += A[col-1]
    return A[n-1]

def uniquePaths(self, m: int, n: int) -> int:
    A = [[1 for i in range(m)] for _ in range(n)]
    for row in range(1, n):
        for col in range(1, m):
            A[row][col] = A[row][col-1] + A[row-1][col]
    return A[n-1][m-1]