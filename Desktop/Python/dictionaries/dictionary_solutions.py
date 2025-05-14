# Easy 1
def invert_dictionary(dictionary):
    inverted={}
    for key,value in dictionary.items():
        inverted[value]=key
    return inverted



# Easy 2
def merge_dictionaries(dict1,dict2):
    merged={}
    for key,value in dict1.items():
        merged[key]=value
    for key,value in dict2.items():
        merged[key]=value
    return merged



# Medium 1
def word_frequencies(text):
    word_count={}
    text=text.lower()
    words=text.split()
    for word in words:
        if word in word_count:
            word_count[word]+=1
        else:
            word_count[word]=1
    
    return word_count



# Medium 2
def add_contact(contact_book, name, phone=None, email=None, address=None):
    contact_details={}
    
    if phone is not None:
        contact_details['phone']=phone
    if email is not None:
        contact_details['email']=email
    if address is not None:
        contact_details['address']=address
    if name in contact_book:
        contact_book[name].update(contact_details)
    else:
        contact_book[name]=contact_details


# Hard 1
def transform_grades(grades):
    result={}
    for student, student_grades in grades.items():
        if student_grades:
            average=sum(student_grades)/len(student_grades)
            highest=max(student_grades)
            lowest=min(student_grades)
        else:
            average=highest=lowest=0 
        result[student]={
            'average':average,
            'highest':highest,
            'lowest':lowest
        }
    return result

# Hard 2
def generate_tree(paths):
    tree={}
    for path in paths:
        parts=path.split('/')
        current_level=tree
        for part in parts:
            if part not in current_level:
                current_level[part]={}
            current_level=current_level[part]
    return tree


#Test Cases:

# Easy 1:
print(invert_dictionary({"a": 1, "b": 2, "c": 3}))  # Should return {1: "a", 2: "b", 3: "c"}

# Easy 2:
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
print(merge_dictionaries(dict1, dict2))  # Should return {"a": 1, "b": 3, "c": 4}

# Medum 1:
text = "the quick brown fox jumps over the lazy dog"
print(word_frequencies(text))
# Should return {"the": 2, "quick": 1, "brown": 1, "fox": 1, "jumps": 1, "over": 1, "lazy": 1, "dog": 1}

# Medium 2:
contacts = {}
add_contact(contacts, "Alice", phone="123-456-7890", email="alice@example.com")
add_contact(contacts, "Bob", phone="987-654-3210")
add_contact(contacts, "Alice", address="123 Main St")  # Updates Alice's info

print(contacts)
# Should return:
# {
#   "Alice": {"phone": "123-456-7890", "email": "alice@example.com", "address": "123 Main St"},
#   "Bob": {"phone": "987-654-3210"}
# }

# Hard 1:
grades = {
    "Alice": [85, 90, 95],
    "Bob": [70, 80, 90],
    "Charlie": [90, 92, 93]
}

print(transform_grades(grades))
# Should return:
# {
#   "Alice": {"average": 90.0, "highest": 95, "lowest": 85},
#   "Bob": {"average": 80.0, "highest": 90, "lowest": 70},
#   "Charlie": {"average": 91.67, "highest": 93, "lowest": 90}
# }

# Hard 2:
paths = [
    "folder1/file1.txt",
    "folder1/folder2/file2.txt",
    "folder3/file3.txt"
]

print(generate_tree(paths))
# Should return:
# {
#   "folder1": {
#     "file1.txt": {},
#     "folder2": {
#       "file2.txt": {}
#     }
#   },
#   "folder3": {
#     "file3.txt": {}
#   }
# }
