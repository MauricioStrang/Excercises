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


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def check_for_factor(base, factor):
    return base % factor == 0


def minimum(arr):
    result = arr[0]
    for i in arr:
        if i < result:
            result = i
    return result

def maximum(arr):
    result = arr[0]
    for i in arr:
        if i > result:
            result = i
    return result


def sum_two_smallest_numbers_long(numbers):
    num_1 = float('inf')
    num_2 = float('inf')
    
    for n in numbers:
        if n < num_1:
            num_2 = num_1
            num_1 = n
        elif n < num_2:
            num_2 = n
    return num_1 + num_2

def sum_two_smallest_numbers(numbers):
    sorted_nums = sorted(numbers)
    return sorted_nums[0] + sorted_nums[1]


print(sum_two_smallest_numbers([76231194, 71562063, 58861905, 87280028, 35089290, 96717064, 75095987, 41509088, 89097889, 69799171, 70417078, 86512544, 98670217, 61573787, 31697905, 11799344, 51669002, 49209858, 81546719, 13067798, 26453366, 96317800, 33939340, 51661217, 6718037, 50253532, 53567717, 75577337, 55230491, 72383733, 30781195, 22459931, 51634543, 2665832, 68626345, 63826625, 13235149, 25716236, 19565508, 52416086, 3386970, 92950516, 21279221, 77369798, 24244551, 63546820, 41035047, 80888893, 56614639, 87441678, 56029346, 37140507, 39581996, 83237430, 56699191, 38206881, 11328683, 46822742, 30346466, 90359054, 92404754, 75560931, 62407267, 27238580, 77795435, 41135141, 86109908, 63171954, 67761118, 71317762, 97604497, 42281157, 3302092, 46721580, 656472, 38383317, 48735893, 95534898, 17472184, 85468680, 51465819, 70070467, 35848437, 46045306, 78724427, 50913863, 28933897, 99419038, 19459297, 12664867, 38052573, 23027652, 26720542, 37269495, 14378677, 51164802, 40530706, 76805156, 26144114, 79969747, 28391916, 67973187, 59318679, 64503202, 22822813, 77997478, 16264296, 96543513, 30884249, 46858271, 54768500, 95850996, 76930293, 79318332, 3725634, 35309658, 50018784, 71537689, 23857156, 33804660, 40725183, 67986401, 61476586, 36767951, 1926512, 5089439, 34775543, 15065551, 72101630, 18222955, 28617850, 71741735, 89374869, 78256092, 36268511, 97090617, 34089779, 10563108, 62565176, 51079646, 11914512, 34685836, 98601705, 39393027, 11722138, 60637410, 86554873, 43378518, 50418752, 13755998, 6743832, 75643058, 72743597, 87023847, 46398081, 31209134, 570281, 49232632, 75972968, 34082235, 21992545, 67815424, 18412442, 58604210, 45224356, 39744543, 16467951, 11947727, 91380952, 85892524, 30134392, 81327027, 51521418, 79932325, 68543815, 26004823, 31268369, 85918437, 2694219, 95004720, 24702519, 65373965, 78168486, 25384198, 21249353, 10352507, 90516676, 37781017, 95390487, 85868293, 92562120, 40156989, 38930456, 73470545, 32718810, 15760454, 14833168, 36311896, 28261047, 53590722, 29918805, 25862604, 45422060, 98801711, 86980684, 29420485, 10192355, 94334912, 80126134, 62807382, 36720200, 47630573, 2251608, 32522202, 88827675, 27962494, 90271916, 82795962, 15310228, 48394514, 34652893, 27913620, 62822652, 10222558, 11460572, 60826549, 98882487, 32438690, 29790747, 70264268, 51660189, 70023145, 2987938, 27852268, 12834771, 16185697, 64027414, 2549042, 29514042, 60247215, 75272590, 639771, 41762795, 74390101, 48008856, 52272043, 43771230, 17253568, 23849540, 35704161, 65439197, 75816943, 32921051, 42898782, 7145195, 89174465, 1207069, 75313125, 6742204, 32537374, 25881073, 65374034, 72548265, 86817056, 44565468, 20374038, 72861361, 60875310, 72410797, 36236868, 71048572, 98017729, 16429972, 49376496, 93339977, 37388049, 28768861, 11023867, 4557636, 94255969, 73497260, 92946383, 86187614, 17573912, 1130189, 81801501, 53049246, 60039256, 71303441, 52225020, 58700015, 14398754, 28257707, 61548351, 28088387, 84804395, 16397271, 61883103, 38558874, 25885082, 21686980, 17068895, 37783068, 56469359, 53960822, 84509532, 35576971, 25100747, 52440780, 48683795, 67428807, 91193134, 33413160, 78472515, 2057937, 35951172, 6549729, 50476433, 41084060, 41945909, 9844131, 63657039, 80145780, 35744875, 8657298, 78833153, 66039398, 30886098, 7233267, 4350854, 10113362, 46646587, 54965208, 74156188, 8944695, 81185420, 90456459, 95482273, 14505756, 610716, 21558383, 48447678, 16052441, 68574158, 58575804, 33241783, 80304873, 27140357, 39441631, 59434519, 69040094, 93348855, 66640701, 86342064, 31982969, 48209040, 79226318, 57714927, 92308773, 99517490, 22139973, 56911051, 6298287, 349569, 75465215, 36717029, 83403609, 18227126, 94476142, 81723655, 88624780, 94722599, 41126717, 18963872, 97861709, 15386298, 85466246, 51600370, 60172702, 11828519, 76444933, 5835564, 66543675, 4618078, 1264538, 91677703, 95404286, 54248921, 93907920, 94285097, 51344642, 97011859, 4990245, 81277527, 45182969, 52423780, 60973986, 87169075, 24853806, 13691438, 20120595, 40481202, 22611800, 83776539, 23814375, 89195659, 24626708, 14190894, 53012067, 47109646, 94017314, 62792559, 95369827, 33275840, 41585573, 58797181, 47179108, 39463038, 40288265, 71875052, 68831573, 54352737, 99624897, 64847341, 80795891, 58621978, 29286288, 25946504, 77175350, 29419949, 47955069, 95452253, 10490619, 10957226, 3326844, 86032114, 40405437, 7338041, 76157548, 33094684, 16785027, 66638083, 53316329, 48255659, 60120669, 20592449, 59214404, 67286741, 26338800, 84672529, 63255475, 91548027, 17917905, 7961124, 50063544, 10013622, 8574599, 62676771, 26932824, 29858829, 83984313, 75739860, 44315405, 22400195, 39834258, 39391853, 89669037, 12796974, 60587361, 50023525, 67262598, 97021411, 38150928, 77084226, 75395092, 97744548, 892535, 68982811, 67794324, 59056722, 58974651, 7807775, 6290599, 74186339, 12251617, 46764676, 82141277, 60108533, 81711982, 68305617, 2868810, 85684072, 40704275, 95617254, 74322825, 21135148, 97913605, 33106046, 1751141, 30361511, 35970864, 71565477, 79839698, 83847602, 83104103, 99460917, 53588701, 83533369, 56834033, 22288499, 35584030, 24654752, 87966365, 74655386, 84279408, 38623237, 31160558, 40694515, 70275015, 66878266, 88611366, 6061009, 70937870, 95917894, 45099882, 33812425, 80072614, 48413522, 99725500, 68013643, 40993960, 13642906, 5029464, 37718518, 904742, 8532130, 87665172, 690698, 41037571, 41634712, 27559863, 48040885, 65779048, 86410854, 48016235, 55777365, 82005597, 96592587, 67424734, 71017036, 38357734, 54830529, 9195159, 90928701, 74812644, 10413499, 94644882, 6504701, 99772452, 67497318, 74952907, 87652897, 9712579, 50882463, 79244455, 81489504, 28857328, 38424726, 63742694, 15956392, 54395692, 92278186, 18530028, 98245988, 71152624, 8859256, 64194787, 52822181, 26292591, 97752964, 21756618, 49053500, 75242440, 22756790, 74980368, 77469256, 12537297, 60515778, 68409263, 80403625, 67696897, 21058369, 12906189, 39681798, 66367168, 64508400, 8643183, 16264091, 79304651, 13605936, 41895962, 75358100, 71405130, 71955601, 57249933, 22505162, 32542227, 9877845, 49533092, 91096163, 3694528, 27576939, 81352542, 71290238, 35547334, 29014914, 17143710, 10393718, 20375900, 65239908, 27369848, 822809, 96353505, 49092179, 82136978, 3080414, 8302970, 45477182, 56771121, 51937330, 19840386, 99510169, 53865943, 30115424, 82357026, 12908229, 93217744, 97315453, 27224315, 21695071, 81728146, 24524154, 28308092, 12166607, 54842977, 45242917, 52946895, 65617860, 55566450, 97572840, 14682781, 89908162, 86521404, 80042677, 73523528, 61235304, 58963034, 80289390, 47896758, 58451507, 30629746, 39753047, 36966334, 17955086, 11243102, 22429522, 78422757, 71715119, 29484872, 1906929, 70461001, 6026568, 18953647, 49455686, 22208163, 29557139, 3343526, 14690511, 96607455, 71679757, 29567411, 7673043, 63365913, 90033101, 72694116, 23262890, 38156163, 60820192, 21520176, 67162624, 39012922, 82645120, 23714188, 64204052, 48161581, 24436045, 71788494, 22273181, 13684549, 73134221, 31615736, 63086600, 76234562, 1151333, 18101988, 89513477, 5444060, 66998618, 43051999, 37105537, 86073324, 61056454, 6639285, 82644714, 46533514, 94510645, 81568725, 16899618, 90280872, 49255675, 87105655, 83983774, 92676427, 24488616, 40253342, 37990223, 4810107, 2251204, 72360694, 96356449, 17617904, 63364613, 32529668, 78227087, 16214595, 95138404, 17477791, 33877876, 60137771, 22103356, 84646261, 15778533, 45657074, 73650652, 22822799, 96223978, 32879437, 91487072, 65341745, 92802960, 4234796, 19613749, 47732952, 16124268, 21036413, 10031442, 47780122, 54403684, 53078734, 9898848, 97995386, 53901431, 37915654, 16690243, 27840649, 46920709, 67328787, 74427581, 37185106, 67100860, 29625725, 52953064, 30702697, 25228465, 19515227, 303058, 27852683, 4115347, 15154591, 41213670, 68700456, 53636140, 96703781, 13630760, 52552637, 4487175, 67751642, 60156562, 69763473, 4549459, 27188136, 89355788, 10039140, 96117925, 84232228, 46793937, 37995161, 35870438, 66549240, 66672342, 49249252, 93926604, 11810008, 80075647, 29688251, 72673652, 71437967, 27290802, 66072954, 22762865, 22556260, 20793818, 54851009, 93480507, 88201638, 81409678, 90680077, 62777109, 52047650, 68332949, 61134024, 88359702, 41342362, 66107412, 9586379, 71485255, 4551744, 15333873, 14637881, 62779105, 57982522, 52676701, 23155774, 67401575, 41569817, 62530897, 45134774, 13710530, 58083086, 38467297, 13559446, 20326923, 25002118, 6854489, 25143400, 36902192, 87971892, 4861230, 62375348, 92468074, 84882661, 7515223, 82836965, 61394093, 77654298, 31662095, 74421461, 99229592, 35120137, 34263262, 86758546, 48246303, 5915282, 84827703, 74714965, 48737814, 78708496, 46854620, 95283967, 39489683, 61254184, 4797996, 11156048, 3185913, 30974122, 49378570, 76430962, 24731185, 36186488, 46323492, 60725874, 91140352, 16809589, 55729316, 8618390, 69713521, 62666173, 64815360, 97608824, 75965117, 31402184, 92531900, 84105212, 65116866, 83677007, 48089203, 99388049, 909827, 21628898, 7053222, 40410640, 95521694, 76913506, 52240542, 94945853, 12888750, 140793, 75584784, 15936555, 95446791, 2868111, 7671881, 78233392, 64831543, 75365671, 89729809, 27994837, 9709033, 20203651, 98425995, 38033378, 90392984, 85936104, 31422173, 90599994, 28736640, 94072618, 6686557, 73299351, 39518705, 28026597, 80698961, 77899556, 46803927, 65577789, 24990853, 78518558, 28232493, 89762597, 24514739, 39982450, 36823663, 95396220, 22169202, 44693407, 10028144, 79041440, 7607286, 40562064, 97827784, 14325733, 22194760, 66533618, 16932946, 13566251, 46763162, 93473878, 98679486, 88131981, 73898260, 62288057, 51546175, 10400271, 49049141, 1309346, 40923405, 19165060, 60906110, 99277410, 87612768, 72607225, 69359811, 82973311, 81822066, 12583251, 80090970, 63505815, 26422166, 56847651, 43798019, 73051973, 44160180, 33949114, 78393988, 49715031, 68040370, 57942471, 69504554, 95345512, 47873804, 48680400, 39510081, 60924073, 25624794, 15992949, 50882031, 52775914, 68915657, 94297826, 75646060, 51434265, 12599040, 87509307, 98247656, 99984851, 73382434, 90775837, 50179341, 8658746, 38418895, 56888559, 14958381, 83495736, 17119397, 93130396, 64076550, 77259428, 29852014, 47472196, 73491046, 91944530, 11513753, 63111062, 90647608, 62857502, 10136773, 76042731, 24467841, 93623840, 60946286, 34423781, 69779571, 78073599, 93169708, 92442999, 52803885, 45511220, 6975698, 4389849, 54705539, 35039700, 68922853, 66790083, 48149538, 82427393, 48439449, 73430943, 14658454, 56842333, 59965769, 74691631, 26477988, 5403311, 90131236, 54944468, 46276398, 84853289, 81147865, 95643657, 4453584, 63577132, 19009463, 45318940, 88333192, 61418162, 59248755, 98119213, 2122067, 84987608, 52932424, 84197307, 28591832, 27036594, 20072654, 71929146, 85744384, 15618382, 86105885, 51608067, 15942805, 81152143, 23518722, 34979315, 91930314, 79142534, 15062518, 56752187, 58620609, 70260467, 45468013, 34816435, 51595693, 67816159, 88229508, 24572906, 39531079, 52615887, 77237000, 91880152, 99803697, 99833229, 6689239, 69119026, 82777851, 63862796, 64814153, 84236594, 74644046, 69073803, 5271562, 66767091, 72425742, 89952867, 39451733, 10937175, 33521746, 18748516, 12554882, 40234205, 54299088, 16726320, 27213289, 71117740, 54505667, 14314236, 28715302, 22734176, 84629969, 58682214, 92467946, 22371213, 4076958, 10525015, 4136035, 38934830, 13575364, 33165533, 72981640, 89198858, 98017263, 65060333, 48469086, 13784053, 55645300, 57023227, 68613574, 31622125, 16710433, 17086447, 27745677, 58136378, 11322146, 88315544, 18382331, 9641770, 9619238, 58028813, 95097924, 3806351, 80958917, 67500642, 91811521, 17996162, 51465485, 94027527, 69190935, 5971737, 88828134, 89709028, 83655845, 90977103, 81548074, 1954528, 25466628, 83057940, 1128226, 24260531, 23204672, 22966919, 27238740, 46973875, 95003647, 86140716, 42968419, 37986962, 45408360, 86793300]))