// 4) გაქვს მასივი [10, 20, 30, 40, 50]. გამოიტანე მხოლოდ პირველი და ბოლო ელემენტის ჯამი

let nums = [10, 20, 30, 40, 50];
let sum = 0;
for (i of nums){
    if (nums.indexOf(i) == 0){
        sum += i

    } else if (nums.indexOf(i) == 4)
        sum += i

}
console.log(sum)