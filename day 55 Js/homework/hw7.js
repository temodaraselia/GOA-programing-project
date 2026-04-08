// დაწერეთ კოდი, რომელიც აიღებს მასივს [2,5,8,11], თუ რიცხვი ნაკლებია 6-ზე, გამოიტანოს "low", სხვა შემთხვევაში "high"

let nums = [2,5,8,11];

for (let i = 0; i < nums.length; i++){
    if (nums[i] < 6){
        console.log("low")
    } else {
        console.log("high")
    }
    
}