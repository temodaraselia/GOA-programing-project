// 6) გაქვს მასივი, სადაც წერია როგორც დადებითი, ისე უარყოფითი რიცხვები. დაითვალე, რამდენი უარყოფითი რიცხვია მასივში.

let nums = [1,2,3,4,5,-1,-2,-3,-4,-5,-6,-7];
let possitive = 0;
let negative = 0;
for (i of nums){
    if ( i > 0){
        possitive += 1
    } else {
        negative += 1

    }

}
console.log(`დადებითის რაოდენობა = ${possitive}   უარყოფითის რაოდენობა = ${negative}`)