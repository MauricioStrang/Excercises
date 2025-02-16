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


def repeat_str(repeat, string):
    return string * repeat



def zero_fuel(distance_to_pump, mpg, fuel_left):    
    if mpg * fuel_left >= distance_to_pump:
        return True
    else:
        return False


def area_or_perimeter(l , w):
    if l == w:
        return l * w
    else:
        return l * 2 + w * 2



def add_binary(a,b):
    c = a + b

    return bin(c)[2:]




def make_negative( number ):
    if number < 0:
        return number
    else:
        return -number



def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())



def sum_two_smallest_numbers(numbers):

    n = len(numbers) - 1

    for i in range(n):
        for j in range(n):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    return numbers




def smash(words):   
    n = len(words)
    complete = ''
    for i in range(n):
        print(i, n)
        complete += words[i]
        if i != n -1:
            complete += ' '
    return complete


def smashImproved(words):
    return " ".join(words)


def sum_array(a):
    result = 0
    for x in a:
        result += x
    return result



def sum_arrayImproved(a):
  return sum(a)





def is_square(n):    
    root = math.isqrt(n)
    if root * root == n: return True
    else: return False


def is_squareImproved(n): 
    return n >= 0 and (n**0.5) % 1 == 0 



def greet(name):
    return f"Hello, {name}, how are you doing today?"



def points(games):
    score = 0
    for i in range(len(games)):
        if games[i][0] > games[i][2]:
            score += 3
        elif games[i][0] == games[i][2]:
            score += 1
    return score



print(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']))





# def digitize(n):
#     string = str(n.reverse())
#     arrayed = []
#     for x in string:
#         arrayed.append(x)
#     return arrayed


# print(digitize(869))

