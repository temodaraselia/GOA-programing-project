// 1) შექმენით მანქანის ობიექტი, იყოს მოცემული სიჩქარე, 
// რაც უნდა უდრიდეს 0-ს. ასევე მიუთეთ მანქანის ბრენდი, 
// მოდელი, გამოშვების წელი და ფერი


// 2) ობიექტში ჩაამატეთ რამე ნებისმიერი ორი გასაღები, 
// რაც მანქანის აგებულობას შეეხება (property.newKey <- ეს გამოიყენეთ)


// 3) ჩაამატეთ სამი ფუნქცია: აჩქრება: სიჩქარეს + 10; შენელება: 
// სიჩქარეს - 10. თუ სიჩქარე 10ზე ნაკლებია, მაშინ სიჩქარე 
// 0ზე უნდა დავარდეს, არ უნდა იყოს უარყოფითი. მესამე კი 
// იქნება toString ფუნქცია, რომელიც გამოიტანს წინადადებას: 
// "მანქანა {ბრენდი}, {მოდელი}, გამოიშვა {წელი} წელს და 
// არის {ფერი} ფერის."
const car = {
    brand: "Audi",
    model: "A7",
    year: "2022",
    color: "Black",
    speed: 0,
    Speedup: function(){
        this.speed += 10

    },
    Speeddown: function(){
        if (this.speed < 10){
            this.speed -= 10

        }
    },
    toString1: function(){
        return `მანქანა ${this.brand}, ${this.model}, გამოიშვა ${this.year} წელს და არის ${this.color} ფერის`

    }

}

car.horse_power = 500;
car.interier_color = "Red"

console.log(car)
console.log(car.Speedup)
console.log(car.Speeddown)
console.log(car.toString1)