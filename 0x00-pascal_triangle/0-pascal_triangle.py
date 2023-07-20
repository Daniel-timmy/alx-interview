#!/usr/bin/python3
"""returns a list of lists of integers
representing the Pascal’s triangle of n"""


def pascal_triangle(n):
    """
    pascal triangle
    :param n: number of levels in the triangle
    :return:  list of lists of integers
    representing the Pascal’s triangle
    or an empty list if n<=0
    """
    triangle = []

    # return (trianlgle if n <= 0)
    if n <= 0:
        return triangle
    for i in range(n):
        temp_list = []

        for j in range(i+1):
            if j == 0 or j == i:
                temp_list.append(1)
            else:
                temp_list.append(triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(temp_list)
        return triangle

