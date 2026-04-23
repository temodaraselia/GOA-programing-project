// 4) დაწერეთ ფუნქცია სადაც გექნებათ პროდუქტის ფასი და პროდუქტის აქცია და გამოთვალეთ 
// მისი საბოლოო ფასი ფორმულით. price - (price * discount) / 100


function shop(price,discount){
    return price - (price * discount) / 100


}

console.log(shop(100,10))