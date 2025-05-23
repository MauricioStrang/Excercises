
const sum_two_smallest_numbers = (numbers)=>{
    let n = numbers.length - 1
    for (let i = 0; i < n ; i++) {
        for (let j = 0; j< n; j++) {
            if (numbers[j] > numbers[j + 1]) {
                let temp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j+1] = temp
            }
        }
    }
    return numbers
}


   

const letters_to_numbers =(s)=>{
    let values = {'a': 1, 'b': 2, 'c': 3, 'd': 4,'e': 5, 'f': 6, 'g': 7, 'h': 8,'i': 9, 'j': 10, 'k': 11, 'l': 12,'m': 13, 
            'n': 14, 'o': 15, 'p': 16,'q': 17, 'r': 18, 's': 19, 't': 20,'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,'z': 26,
            'A': 2, 'B': 4, 'C': 6, 'D': 8,'E': 10, 'F': 12, 'G': 14, 'H': 16,'I': 18, 'J': 20, 'K': 22, 'L': 24,'M': 26, 'N': 28, 
             'O': 30, 'P': 32,'Q': 34, 'R': 36, 'S': 38, 'T': 40,'U': 42, 'V': 44, 'W': 46, 'X': 48, 'Y': 50,'Z': 52,
             '0': 0, '1': 1, '2': 2, '3': 3,'4': 4, '5': 5, '6': 6, '7': 7,'8': 8, '9': 9}
    let result = 0

    for (let i = 0; i < s.length; i++) {
        if (s[i] in values) {
            result += values[s[i]]
           }       
    }
    return result
}