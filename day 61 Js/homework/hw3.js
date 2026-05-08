// 4) გაქვთ მოცემული მასივი [21,7,3,3.1,2.2,10.1,7] და დაითვალეთ მათი ჯამი და დაამრგვალეთ ceil.

let nums = [21,7,3,3.1,2.2,10.1,7];
let sum = 0;
for (i of nums){
    sum += i
}

console.log(Math.ceil(sum))