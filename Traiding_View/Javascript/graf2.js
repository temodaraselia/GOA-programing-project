let balance = document.getElementById("balance").innerHTML = 2000;
let crypto = document.getElementById("crypto").innerHTML = 0;
let price = 500;




let chartjs = document.getElementById('chart1');

new Chart(chartjs, {
  type: 'line',
  data: {
    labels: ["...", "...", "...", "...", "...","..."],
    datasets: [{
      label: "Company Shares price",
      data: [50, 100, 200, 400,400,price]
    }]
  }
});

function buy(){
    if (balance >= price){
        balance -= price
        document.getElementById("balance").innerHTML = balance;
        crypto += 1
        document.getElementById("crypto").innerHTML = crypto


    }

}

function sell(){
    if (crypto > 0){
        crypto -= 1;
        document.getElementById("crypto").innerHTML = crypto
        balance += price
        document.getElementById("balance").innerHTML = balance

    }


}


function output1(){
    let output = document.getElementById("output").innerHTML = "+ Crypto"
    
}

function output2(){
    let output = document.getElementById("output").innerHTML = "+ 500$"
    
}