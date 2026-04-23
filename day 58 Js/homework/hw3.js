// 3) დაწერეთ ფუნქცია სადაც კენტ რიცხვებს აიყვანთ კვადრატში და ლუწს კუბში ხოლო თუ რიცხვი ნულის ტოლია გამოიტანეთ "Zero".


function pow1(num){
    if ( num > 0 &&  num % 2 ==0 ){
        return num ** 2
    } else if ( num > 0 && num % 2 != 0){
        return num ** 3
    } else{
        return "Zero"
    }

}

console.log(pow1(10))