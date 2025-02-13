
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


console.log(sum_two_smallest_numbers([500, 5, 3, 8, 1, 2, 7]));

   