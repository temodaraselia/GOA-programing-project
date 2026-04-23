// 2) დაწერეთ ფუნქცია სადაც გაიგებთ უმცირეს რიცხვს ამ მასივიდან [2,10,-20,100,90,50,40].

function FindMin(nums){
    let min = nums[0]
    for (i of nums){
        if (i < min){
            min = i
        }
    }
    return min

}

console.log(FindMin([2,10,-20,100,90,50,40]))