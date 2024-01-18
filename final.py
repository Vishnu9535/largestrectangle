from typing import List

def add_unique_numbers(matrix):
    max_row_length = max(len(row) for row in matrix)
    used_numbers = set()

    for row in matrix:
        while len(row) < max_row_length:
            unique_number = find_unique_number(used_numbers, matrix)
            row.append(unique_number)
            used_numbers.add(unique_number)

    return matrix

def find_unique_number(used_numbers, matrix):
    number = 1
    while number in used_numbers or any(number in row for row in matrix):
        number += 1
    return number

def largest_rectangle(matrix: List[List[int]]) -> tuple:
    matrix = add_unique_numbers(matrix)
    if not matrix or not matrix[0]:
        return None, 0

    rows, cols = len(matrix), len(matrix[0])
    max_area = 0
    max_number = None
    heights = [[0]*cols for _ in range(rows)]

    for num in set(num for row in matrix for num in row):
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == num:
                    heights[i][j] = heights[i-1][j] + 1 if i > 0 else 1
                else:
                    heights[i][j] = 0

        for i in range(rows):
            stack = [-1]
            for j in range(cols):
                while stack[-1] != -1 and heights[i][stack[-1]] >= heights[i][j]:
                    h = heights[i][stack.pop()]
                    w = j - stack[-1] - 1
                    if h != w and h * w > max_area:
                        max_area = h * w
                        max_number = num
                stack.append(j)

            while stack[-1] != -1:
                h = heights[i][stack.pop()]
                w = cols - stack[-1] - 1
                if h != w and h * w > max_area:
                    max_area = h * w
                    max_number = num

    return max_number, max_area

matrix_example = [
    [1, 1, 1, 0, 1, -9],
    [1, 1, 1, 1, 2, -9],
    [1, 1, 1, 1, 2, -9],
    [1, 0, 0, 0, 5, -9],
    [5, 0, 0, 0, 5],
]
# result = largest_rectangle(matrix_example)
assert largest_rectangle(matrix_example) == (1, 8)
# print(f"Largest rectangle is formed by number {result[0]} with area {result[1]}")