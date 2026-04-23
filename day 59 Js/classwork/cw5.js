// 5) აიღეთ რაიმე მასივი და გამოიტანეთ უმცირესი რიცხვი (რამე ფუნქცია არ გამოიყენოთ)

let nums = [1,2,3,4,5,6,7,8,9,10];
let min = nums[0];
for ( i of nums ){
    if ( min > i ){
        min= i
    }
}

console.log(min)
