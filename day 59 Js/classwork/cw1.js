// 1) აიღეთ რიცხვების მასივი ერთიდან ათამდე, თუ რიცხვი კენტია გამოიტანე true, თუ ლუწი - false

let nums = [1,2,3,4,5,6,7,8,9,10];

for (i of nums){
    if ( i % 2 == 0){
        console.log(true)
    } else {
        console.log(false)
    }
}

