def dp(n, m, board):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    ans = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if board[i - 1][j - 1]:
                dp[i][j] = min(min(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1]) + 1
            ans = max(ans, dp[i][j])
    return ans

def solution(board):
    n = len(board)
    m = len(board[0])
    square_len = dp(n, m, board)
    return square_len * square_len
