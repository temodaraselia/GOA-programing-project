// 3) გამოიყენე do... while loop, მასივი: [2, 4, 6, 8]. შეკრიბე ყველა რიცხვი და გამოიტანე მათი ჯამი

let nums = [2, 4, 6, 8]
let sum = 0;
let i = 0;
do {
    sum += nums[i]
    i++
} while (i != nums.length)
console.log(sum)




