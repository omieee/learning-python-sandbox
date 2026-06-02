def return_age(age):
    return age

age = "alph12"

print(return_age(age))

'''
The above is not wrong as per say language pov if you consider it as python 
the intution or motivation for typing is to make sure the code is more redable
and also it is possible less error prone as it is sytax above is correct but
for sure you don't want age to be alphanumeric ... hence type hinting

does it really follow rules like it will start throwing error while running 
NO NO it as the name says is hinting in IDE through tools like pylance say says
hey bro this literal "alpha123" doesn't look like an int please fix it, with a proper
redline to catch your eye. as you can see the below thing will run. but ide
will warn
'''

def type_hinted_age(age: int) -> int:
    return age

print(type_hinted_age(10))

print(type_hinted_age("alpha123"))


'''
Lets move to some collections
bellow function was thought that a user will always pass a integer list or a 
numerical list but users can pass string and things will fall apart and this time
we will get an error during runtime when we pass a string
'''

def square_list(alist):
    return_list = []
    for i in alist:
        return_list.append(i ** 2)
    return return_list

print(square_list([1,2,3]))
print(square_list("alpha"))#This will throw error. it's not user fault it's eng. fault


def square_list_by_a_senior_eng(alist: list[int]) -> list[int]:
    return_list = []
    for i in alist:
        return_list.append(i ** 2)
    return return_list

print(square_list_by_a_senior_eng([1,2,3]))
print(square_list_by_a_senior_eng("alpha"))#This will throw error, string is not a list[int]


def greet_user(name: str) -> str:
    return f"Hello, {name}"


def word_count(words: list[str]) -> dict[str, int]:
    counts: dict[str, int] = {}

    for word in words:
        counts[word] = counts.get(word, 0) + 1

    return counts