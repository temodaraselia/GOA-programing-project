// 5) Hard - დაწერეთ ფუნქცია სადაც დაითვლით კენტი და ლუწი რიცხვების ჯამს ოღონდ თუ რიცხვი ლუწია კვადრატში უნდა 
// აიყვანო და კენტის დროს კუბში, ამ მასივის მიხედვით[1,2,3,4,5,6,7,8,9,10].

function even_and_odd(nums){
    let sum_even = 0;
    let sum_odd = 0;
    for ( i of nums){
        if ( i % 2 == 0){
            sum_even += i ** 2
        }else {
            sum_odd += i ** 3

        }
    }
    return `Sum even = ${sum_even} ----- Sum odd ${sum_odd}`

}

console.log(even_and_odd([1,2,3,4,5,6,7,8,9,10]))