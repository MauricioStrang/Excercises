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




def rps(p1, p2):
    if p1 == 'scissors' and p2 == 'paper':
        return "Player 1 won!"
    elif p1 == 'paper' and p2 == 'scissors':
        return "Player 2 won!"

    elif p1 == 'rock' and p2 == 'scissors':
        return "Player 1 won!"
    elif p1 == 'scissors' and p2 == 'rock':
        return "Player 2 won!"
        
    elif p1 == 'paper' and p2 == 'rock':
        return "Player 1 won!"
    elif p1 == 'rock' and p2 == 'paper':
        return "Player 2 won!"
    
    else:
        return 'Draw!'



def rps(p1, p2):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[p1] == p2:
        return "Player 1 won!"
    if beats[p2] == p1:
        return "Player 2 won!"
    return "Draw!"



def rental_car_cost(d):
    total = 0
    if d >= 7:
        total -= 50
    elif d >= 3:
        total -= 20 
    for i in range(d):
        total += 40
    return total



def digitize(n):
    digits = list(map(int, str(n)))
    return digits



def open_or_senior(data):
    num = len(data)
    for i in range(num):
        if data[i][0] >= 55 and data[i][1] > 7:
            data[i] = "Senior"
        else:
            data[i] = "Open"
    return data





def summation(num): 
    result = 0
    for i in range(num):
        result += num - i
    return result



def printer_error(s):
    list = ['a','b','c','d','e','f','g','h','i','j','k','l','m',]
    total_s = len(s)
    error = 0
    for i in range(total_s):
        if s[i] not in list:
            error += 1
    return str(error) + "/" + str(total_s)


def printer_error_improved(s):
     return "{}/{}".format(len([x for x in s if x not in "abcdefghijklm"]), len(s))
   

def sum_mix(arr):
    total = 0
    for i in range(len(arr)):
        total += int(arr[i])
    return total



#Remember to use sum() and then map()
#So basically, map() applies a parameter to the second parameter
def sum_mix_improved(arr):
    return sum(map(int, arr))

def count_sheeps(sheep):
    count = 0
    for x in sheep:
        if x == True:
            count += 1
    return count


#Using count method
def count_sheeps_improved(sheep):
    return sheep.count(True)

#Splicing, getting from index 1 to -1
def remove_char(s):
    return s[1:-1]


def check(seq, elem):
    for x in seq:
        if x == elem:
            return True
    return False

def check_improved(seq, elem):
    return elem in seq
    

def get_volume_of_cuboid(length, width, height):
    return (width * height) * length


def hero(bullets, dragons):
    return bullets / 2 >= dragons


##FIRST 6KYU Find The Parity Outlier
def find_outlier(integers):
    even = 0
    odd = 0

    if integers[0] % 2 == 0:
        even += 1
    else:
        odd += 1
    if integers[1] % 2 == 0:
        even += 1
    else:
        odd += 1   
    if integers[2] % 2 == 0:
        even += 1
    else:
        odd += 1

    
    if even > odd:
        for x in integers:
            if x % 2 != 0:
                return x
    else:
        for x in integers:
            if x % 2 == 0:
                return x




def bouncing_ball(h, bounce, window):
    if h > 0 and bounce > 0 and bounce < 1 and window < h:
        # At the beginning, we make counter once since the mom will see it at least one time when thrown from the top
        counter = 1
        # We also adjust the resting before the while loop to count the first bounce so we know if we even enter the loop
        resting = h * bounce
        while resting > window:
            resting *= bounce
            counter +=2  # Since we are starting counting at one means that the mom has seen the ball go down, so if it enter the loop
                         # That means it will bounce over the window so the mom will see it go up and down again, hence the *= 2 to the counter
        return counter
    else:
        return -1



def is_pangram(st):
    list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    ready = st.lower()
    for x in list:
        if x not in ready:
            return False
    return True


from collections import Counter

def find_it(seq):
    counts = Counter(seq) #Makes an object with the counter of each element in the array
    for num, count in counts.items():
        if count % 2 != 0:
            return num
    


def unique_in_order(sequence):
    if not sequence:
        return []    
    result = [sequence[0]]
    for item in sequence[1:]:
        if item != result[-1]:
            result.append(item)
    return result


def first_non_repeating_letter(s):
    counts = Counter(s.lower())
    result = ''
    for count in counts.items():
        if result == '' and count[1] == 1:
            result = count[0] 
    return result


def is_square(n):    
    if n < 0:
        return False
    sqrt_n = int(math.sqrt(n))
    return sqrt_n * sqrt_n == n


def count_by(x, n):
    result = []
    for i in range(1, n + 1):
        result.append(i * x)
        x-1
    return result
    
def sum_mix(arr):
    return sum(map(int, arr))


def solution(text, ending):
    if len(text) < len(ending):
        return False
    reversed_text = ''
    reversed_ending = ''
    for ch in text:
        reversed_text = ch + reversed_text

    for ch in ending:
        reversed_ending = ch + reversed_ending

    for i in range(len(ending)):
        if reversed_text[i] != reversed_ending[i]:
            return False
    return True


def disemvowel(string_):
    vowels = "aeiouAEIOU"
    new_string_ = ""
    for char in string_:
        if char not in vowels:
            new_string_ += char
    return new_string_

def disemvowel_improved(string_):
    vowels = "aeiouAEIOU"
    return "".join(map(lambda char: "" if char in vowels else char, string_))
        # map() produces an iterable, which isn't directly usable as a string.
        # "".join(...) joins all characters together into a final string.


def filter_list(l):
        # We iterate over lst and check if each item is an integer using isinstance(item, int).
        return [item for item in l if isinstance(item, int)]


def dig_pow(n, p):
    # first we separate the numbers in an array of numbers
    str_n = str(n)
    list_n = [item for item in str_n]
    int_n = list(map(int, list_n))

    # then we power each of the number for the array and sum it together into big_num
    big_num = 0
    for num in int_n: 
        big_num += num ** p
        p+=1

    # we set the base multiplator for comparison and a result to track when we are equal or passed the big_num, aka no n * k equals to big_num
    k= 1
    result = 0
    while result < big_num:
        result = n * k
        k+=1  

    # we return k mins one because of how the while loop works
    if result == big_num:
        return k -1
    
    # no big_n == n*k? return -1
    return -1



def kata_13_december(lst): 
    new_lst = []
    for i in range(len(lst)): 
        if lst[i] % 2 !=0: 
            new_lst.append(lst[i])
    return new_lst


def get_sum(a, b):
    if a == b:
        return a  # If both numbers are the same, return one of them
    
    result = 0
    counter = min(a, b)  # Start from the smaller number
    end = max(a, b)  # End at the larger number
    
    while counter <= end:  # Include both a and b
        result += counter
        counter += 1
    
    return result


def DNA_strand(dna):
    result = ''
    for char in dna:
        if char == 'T':
            result += 'A'
        elif char == 'A':
            result+= 'T'
        elif char == 'C':
            result+= 'G'
        elif char =='G':
            result+= 'C'
    return result


def DNA_strand_improved(dna):
    pairs = {'A':'T','T':'A','C':'G','G':'C'}
    return ''.join([pairs[x] for x in dna])


# God please forgive my ignorance
def order(sentence):
    nums = '123456789'
    separated = []
    ordered = []
    word = ''
    for char in sentence:
        if char != ' ':
            word += char
        else:
            separated.append(word)
            word = ''
    separated.append(word)
    
    while len(ordered) < len(separated):
        ordered.append('')

    for word in separated:
        for char in word:
            if char in nums:
                ordered[int(char) - 1] = word 

    while "" in ordered:
        ordered.remove("")

    return ' '.join(ordered)


def friend(x):
    result = []
    for each in x:
        if len(each) == 4:
            result.append(each)
    return result





def letters_to_numbers(s):
    values = {'a': 1, 'b': 2, 'c': 3, 'd': 4,'e': 5, 'f': 6, 'g': 7, 'h': 8,'i': 9, 'j': 10, 'k': 11, 'l': 12,'m': 13, 
            'n': 14, 'o': 15, 'p': 16,'q': 17, 'r': 18, 's': 19, 't': 20,'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,'z': 26,
            'A': 2, 'B': 4, 'C': 6, 'D': 8,'E': 10, 'F': 12, 'G': 14, 'H': 16,'I': 18, 'J': 20, 'K': 22, 'L': 24,'M': 26, 'N': 28, 
             'O': 30, 'P': 32,'Q': 34, 'R': 36, 'S': 38, 'T': 40,'U': 42, 'V': 44, 'W': 46, 'X': 48, 'Y': 50,'Z': 52,
             '0': 0, '1': 1, '2': 2, '3': 3,'4': 4, '5': 5, '6': 6, '7': 7,'8': 8, '9': 9}
    result = 0
    for char in s:
        if char in values:
            result += values[char]
    return result


def is_isogram(string):
    result = ''
    for char in string:
        if char.lower() not in result:
            result += char.lower()
        else:
            return False
    return True


def hoop_count(n):
    return "Keep at it until you get it" if n < 10 else "Great, now move on to tricks"



def count_smileys(arr):
    result = 0
    for smile in arr:
        if len(smile) == 2:       
            if smile[0] in (':', ';') and smile[1] in ('D',")"):
                result += 1
        elif len(smile)  == 3:
            if smile[0] in (':', ';') and smile[1] in ('-',"~") and smile[2] in ('D',")"):
                    result +=1
    return result


def find_needle(haystack):
    if haystack.index('needle'):
        return 'found the needle at position ' + str(haystack.index('needle'))

print(find_needle(['3', '123124234', None, 'world', 'hay', 2, '3', True, False]))
