# Easy 1
def filter_even_numbers(numbers):
    result=[]
    for num in numbers:
        if num%2==0:
            result.append(num)
        
    return list(result)


# Easy 2
def merge_sorted_lists(list1, list2):
    merged=list1+list2
    merged=sorted(merged)
    return merged

# Medium 1
def generate_matrix(n, m):
    mat=[]
    for i in range(n):
        row=[]
        for j in range(m):
            row.append(i*j)
        mat.append(row)
    return mat

# Medium 2
def transpose_matrix(matrix):
    transposed=[]
    rows=len(matrix)
    columns=len(matrix[0])
    for j in range(columns):
        new_row=[]
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)
    return transposed


# Hard 1
def find_peaks(numbers):
    peaks=[]
    if numbers[0]>numbers[1]:
        peaks.append(numbers[0])
    for i in range(1,len(numbers)-1):
        if numbers[i]>numbers[i-1] and numbers[i]>numbers[i+1]:
            peaks.append(i)
    return peaks


# Hard 2
def rotate_list(numbers, k):
    n=len(numbers)
    k=k%n
    rotated=[]
    for i in range(n-k,n):
        rotated.append(numbers[i])
    for i in range(n-k):
        rotated.append(numbers[i])

    return rotated


#Test Cases:

# Easy 1:
print(filter_even_numbers([1, 2, 3, 4, 5, 6]))  # Should return [2, 4, 6]
print(filter_even_numbers([1, 3, 5]))  # Should return []


# Easy 2:
print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  # Should return [1, 2, 3, 4, 5, 6]
print(merge_sorted_lists([1, 2, 3], [4, 5, 6]))  # Should return [1, 2, 3, 4, 5, 6]

# Medum 1:
print(generate_matrix(3, 3))
# Should return:
# [
#   [0, 0, 0],
#   [0, 1, 2],
#   [0, 2, 4]
# ]


# Medium 2:
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(transpose_matrix(matrix))
# Should return:
# [
#   [1, 4],
#   [2, 5],
#   [3, 6]
# ]

# Hard 1:
print(find_peaks([1, 3, 2, 3, 5, 4, 3, 2, 3, 1]))  # Should return [1, 4, 8]

# Hard 2:
print(rotate_list([1, 2, 3, 4, 5], 2))  # Should return [4, 5, 1, 2, 3]
print(rotate_list([1, 2, 3], 4))  # Should return [3, 1, 2]
