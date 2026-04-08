// დაწერეთ კოდი, რომელიც აიღებს მასივს [1,3,5,7], და დაითვალოს რამდენი კენტი რიცხვია

let nums = [1,3,5,7];
let even = 0;
let odd = 0;

for (let i = 0; i < nums.length; i++){
    if (nums[i] % 2 == 0){
        even += 1
    } else {
        odd += 1
    }
}

console.log(`even --- ${even}      odd --- ${odd}`)