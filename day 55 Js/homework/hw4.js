// დაწერეთ კოდი, რომელიც აიღებს მასივს [2,4,6,8], თუ რიცხვი იყოფა 4-ზე, გამოიტანოს true, სხვა შემთხვევაში false

let nums = [2,4,6,8];

for (let i = 0; i < nums.length; i++){
    if ( nums[i] % 2 === 0){
        console.log(true)
    } else {
        console.log(false)
    }

}