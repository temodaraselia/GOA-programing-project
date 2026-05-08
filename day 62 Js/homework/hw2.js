// 2) შექმენით პროდუქტების მარაგის ობიექტი warehouse. გადააწოდეთ სხვადასხვა property-ები, როგორიცაა: name (საცავის სახელი), category 
// (საჭმელი, ავეჯი, ა.შ.), კომპანია (რაც გინდათ ის დაწერეთ), status (active, low-stock, out-of-stock), stock (რაოდენობა, მაგ. 20), 
// reserved (ვიღაცისთვის ან სამომავლოდ შენახული პროდუქცები, რაც უნდა უდრიდეს ნულს)

// 2.1 შექმენით ფუნქცია updateStatus(), რომელიც არ მიიღებს არანაირ არგუმენტს. თუ stock ნაკლებია ნულზე ან ნულის ტოლია, სტატუსი უნდა გახდეს 
// out-of-stock; თუ stock ნაკლებია ხუთზე, სტატუსი უნდა იყოს low-stock. სხვა შემთხვევაში კი უნდა იყოს active
// 2.2 დაამატეთ შემდეგი ფუნქციები: restock(amount), სადაც amount უდრის პროდუქტების რაოდენობას, რომელიც მარაგს (stock) უნდა დაემატოს. 
// ამის შესრულების შემდეგ გაუშვით მანამდე შექმნილი updateStatus() ფუნქცია.
// 2.3 შექმენით შემდეგი ფუნქცია: reserve(amount), რომელიც მიიღებს amount არგუმენტს, რაც პროდუქტების რაოდენობაა. თუ ეს რაოდენობა stock-ზე 
// მეტია, მაშინ უნდა გამოიტანოს false. სხვა შემთხვევაში კი reserved + amount
// 2.4 დაამატეთ შემდეგი ფუნქცია: available(), რომელიც იქნება უარგუმენტო. უნდა გამოიტანოს ხელმისაწვდომი პროდუქტების რაოდენობა, ანუ ხელმისაწვდომს - რეზერვი (stock - reserve)
// 2.5 საბოლოოდ კი დაამატეთ toString() ფუნქცია, რომელიც გამოიტანს შემდეგ წინადადებას: "სახელი: {name}, ხელმისაწვდომი: {stock - reserved}, სტატუსი:  {status}"


let warehouse = {
    name: "A",
    category: "food",
    company: "walmart",
    status: "",
    stock: 10,
    amount: 5,
    reserved: 0,

    updatestatus: function () {
        if (this.stock <= 0) {
            this.status = "out-of-stock";
        } else if (this.stock < 5) {
            this.status = "low-stock";
        } else {
            this.status = "active"; 
        }
    },

    restock: function (amount) {
        this.stock += amount;
        this.updatestatus(); 
    },

    reserve: function (amount) {
        if (amount > this.stock) {
            return false;
        } else {
            return this.reserved + amount;
        }
    },

    available: function (){
        return this.stock - this.reserved

    },

    toString: function (){
        return `${this.company} ხელმისაწვდომია: ${warehouse.available()}, სტატუსი: ${this.status} `

    }
};


warehouse.updatestatus(); 
console.log("status", warehouse.status); 

warehouse.restock(warehouse.amount); 
console.log("last_stock:", warehouse.stock);
console.log("last_status:", warehouse.status);
console.log("reserve:", warehouse.reserve(6));
console.log("available:",warehouse.available())
console.log(warehouse.toString())