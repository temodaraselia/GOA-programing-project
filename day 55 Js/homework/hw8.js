// დაწერეთ კოდი, რომელიც აიღებს მასივს [4,9,16,25], თითოეული რიცხვიდან გამოიტანოს მისი კვადრატული ფესვი

let nums = [4,9,16,25];
let result;

for (let i = 0; i < nums.length; i++){
    console.log(`${nums[i]} = ${result = Math.sqrt(nums[i])}`)

}