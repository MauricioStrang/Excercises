import math

"#1. First Python code :D"

def boolean_to_string(b):
    return "True" if b else "False"


"#2. Still learning Syntaxis"
"Create a function which translates a given DNA string into RNA."

def dna_to_rna(dna):
    rna = []
    for x in dna:
        if x == "T":
            rna.append("U")
        else:
            rna.append(x)
    rna_string = "".join(rna)
    return rna_string


"#3. Bad day but still trying some Python"
"This one is pretty easy"

def greet(name, owner):
    if name == owner:
        return 	'Hello boss'
    else:
        return 'Hello guest'


def litres(time):
    ans = time * 0.5
    return math.floor(ans)



def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"


# def digitize(n):
#     string = str(n.reverse())
#     arrayed = []
#     for x in string:
#         arrayed.append(x)
#     return arrayed


# print(digitize(869))


#WRONG
def count_by(x, n):
    result = []
    for i in range(1,n+1):
        result.append(x * i)
    return result


#WRONG
def count_positives_sum_negatives(arr):
    positives = 0
    negatives = 0
    for x in arr:
        if x > 0:
            positives +=1
        elif x < 0:
            negatives += x
        else:
            print("0 found")
    result = [positives, negatives]
    if positives == 0 and negatives == 0:
        return []
    else:
        return result




def get_grade(s1, s2, s3):
    average = (s1 + s2 + s3) // 3
    if average < 60:
        return 'F'
    elif average < 70:
        return 'D'
    elif average < 80:
        return 'C'
    elif average < 90:
        return 'B'
    else: 
        return 'A'


print(get_grade(70, 70, 100))