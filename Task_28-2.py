'''Дана квадратная матрица чисел, некоторые клеточки содержат
отрицательные числа, туда нельзя заходить.
Ваша задача построить оптимальный путь из произвольной точки в
произвольную точку.
Оптимальность пути определяется суммой клеточек от начальной точки до
конечной включительно.
Вы можете двигаться вправо, влево, вверх, вниз, не вылезая за границы
матрицы, не заходя на клеточки с отрицательными числами.
Например:
matrix = [[1, 2, 3],
[ 4, -1, 6],
[ 7, 8, 9]]
Оптимальным маршрутом из точки (0,0) в точку (2,2) будет путь:
(0,0),(0,1),(0,2),(1,2),(2,2) «длиной» 21. '''


def is_valid_move(matrix, visited, row, col):
    n = len(matrix)
    return 0 <= row < n and 0 <= col < n and not visited[row][col] and matrix[row][col] >= 0


def find_optimal_path(matrix, start, end):
    n = len(matrix)
    visited = [[False for _ in range(n)] for _ in range(n)]
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(row, col):
        if (row, col) == end:
            return matrix[row][col]

        visited[row][col] = True
        best_path_sum = float('inf')

        for dr, dc in moves:
            new_row, new_col = row + dr, col + dc
            if is_valid_move(matrix, visited, new_row, new_col):
                path_sum = dfs(new_row, new_col)
                if path_sum != float('inf'):
                    best_path_sum = min(best_path_sum, matrix[row][col] + path_sum)

        visited[row][col] = False
        return best_path_sum

    return dfs(start[0], start[1])


matrix = [
    [-1, -2, -3],
    [-4, 0, -6],
    [-7, -8, -9]
]
start_point = (1, 0)
end_point = (2, 2)

print(find_optimal_path(matrix, start_point, end_point))
