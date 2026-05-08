// 1) შექმენით პიროვნების ობიექტები და გაადაწოდეთ მას სახელი, გვარი, ასაკი და დაბადების თარიღი. შემდგომ დაამატეთ ორი ფუნქცია: aging: ასაკს + 1 და მეორე toString: 
// გამოიტანოს წინადადება: "{სახელი} {გვარი} დაიბადა {დაბადების თარიღი} და არის {ასაკი} წლის"

let person = {
    name: "temo",
    lastname: "daraselia",
    age: 15,
    birthdate: "23.07.2010",
    aging: function (){
        this.age + 1
    },
    toString: function (){
        console.log(`${this.name} ${this.lastname} დაიბადა ${this.birthdate} და არის  ${age} წლის`)

    }   

}

console.log(person.aging)
console.log(person.toString)