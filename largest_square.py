# def largest_square(bin_array:list[list[int]]) -> int:
#     n = len(bin_array)
#     m =len(bin_array[0])
#     dp =[[0]*m for _ in range(n)]
#     max_num = 0
#     bottom_right = (-1, -1)
#     for i in range(n):
#         for j in range(m):
#             if bin_array[i][j] == 0:
#                 continue
#             left = right = diag = 0
#             if i > 0:left = dp[i -1][j]
#             if j > 0:right = dp[i][j-1]
#             if (i > 0) and (j > 0) : diag = dp[i -1][j -1]
            
#             dp[i][j] = min([left , right, diag]) + 1
            
#             max_num = max(max_num , dp[i][j])
#             if dp[i][j] > max_num:
#                 max_size = dp[i][j]
#                 bottom_right = (i , j)
            
#     if max_num == 0:
#         return 0 , []
    
#     br_x , br_y = bottom_right
#     top_left_x , top_left_y = br_x - max_num + 1, br_y - max_num + 1
    
#     largest_square_matrix =  [
#         bin_array[i][top_left_y:br_y + 1] for i in range (top_left_x , br_x + 1)
#     ]
#     return max_num , largest_square_matrix



def largest_square(bin_array: list[list[int]]) -> tuple[int, list[list[int]]]:
    if not bin_array or not bin_array[0]:  # Edge case: Empty matrix
        return 0, []
    
    n = len(bin_array)
    m = len(bin_array[0])  # Correcting matrix dimensions
    
    dp = [[0] * m for _ in range(n)]  # Initialize DP table
    max_size = 0
    bottom_right = (-1, -1)  # To track bottom-right position of largest square

    for i in range(n):
        for j in range(m):
            if bin_array[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1  # First row and column take direct values
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                
                # Update max square size and bottom-right position
                if dp[i][j] > max_size:
                    max_size = dp[i][j]
                    bottom_right = (i, j)

    # Extract the largest square matrix
    if max_size == 0:
        return 0, []

    br_x, br_y = bottom_right  # Bottom-right coordinates
    top_left_x, top_left_y = br_x - max_size + 1, br_y - max_size + 1  # Top-left coordinates

    # Extract the submatrix
    largest_square_matrix = [
        bin_array[i][top_left_y: br_y + 1] for i in range(top_left_x, br_x + 1)
    ]
    for i in dp:
        print(i)
    return max_size, largest_square_matrix


# Example Usage
if __name__ == "__main__":
    arr =  [[0, 1, 1, 0, 1],
            [1, 1, 0, 1, 0],
            [1, 1, 1, 1, 0],
            [1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0]]
    
    size, square_matrix = largest_square(arr)
    print("Largest Square Size:", size)
    print("Largest Square Submatrix:")
    for row in square_matrix:
        print(row)
