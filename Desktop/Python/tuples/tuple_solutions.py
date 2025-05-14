# Easy 1
def swap_pairs(input_tuple):
    result=[]
    i=0
    while i<(len(input_tuple)-1):
        result.append(input_tuple[i+1])
        result.append(input_tuple[i])
        i+=2
    if len(input_tuple)%2!=0:
        result.append(input_tuple[-1])
    return tuple(result)

# Easy 2
def get_stats(input_list):
    total=sum(input_list)
    average=total/len(input_list)
    return (min(input_list),max(input_list),total,average)

# Medium 1
from collections import namedtuple
Student=namedtuple('Student',['name','age','grades'])

def top_student(students):
    top=students[0]
    top_average=sum(top.grades)/len(top.grades)
    for student in students[1:]:
        avg_grade=sum(student.grades)/len(student.grades)
        if top_average<avg_grade:
            top=student
            top_average=avg_grade
    return top

# Medium 2
def count_coordinate_occurrences(coordinates):
    count_dictionary ={}
    for coordinate in coordinates:
        if coordinate in count_dictionary:
                count_dictionary[coordinate]+=1
        else:
            count_dictionary[coordinate]=1
    return count_dictionary

# Hard 1


# Hard 2


#Test Cases:

# Easy 1:
print(swap_pairs((1, 2, 3, 4)))  # Should return (2, 1, 4, 3)
print(swap_pairs((1, 2, 3)))  # Should return (2, 1, 3)

# Easy 2:
print(get_stats([1, 2, 3, 4, 5]))  # Should return (1, 5, 15, 3.0)

# Medum 1:

alice = Student("Alice", 20, (85, 90, 95))
bob = Student("Bob", 19, (70, 80, 90))
charlie = Student("Charlie", 21, (90, 92, 93))

print(top_student([alice, bob, charlie]))  # Should return the charlie Student tuple

# Medium 2:
coords = [(1, 2), (3, 4), (1, 2), (5, 6), (3, 4), (1, 2)]
print(count_coordinate_occurrences(coords))
# Should return {(1, 2): 3, (3, 4): 2, (5, 6): 1}

# Hard 1:


# Hard 2:
