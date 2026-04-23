// 4) აიღეთ რაიმე მასივი და გამოიტანეთ უდიდესი რიცხვი (რამე ფუნქცია არ გამოიყენოთ)

let nums = [1,2,3,4,5,6,7,8,9,10];
let max = nums[0];
for ( i of nums ){
    if ( max < i ){
        max = i
    }
}

console.log(max)

