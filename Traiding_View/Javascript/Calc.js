function calc1(){
    let money = document.getElementById("money").value;
    let percent = document.getElementById("percent").value;
    let years = document.getElementById("years").value;
    let total = money * (1 + percent/100 * years)
    document.getElementById("first").innerHTML = money;
    document.getElementById("result").innerHTML = total;
    document.getElementById("profit").innerHTML = "+" + total - money;

}