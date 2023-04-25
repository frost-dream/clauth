using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PythonToCSharp
{
    class Program
    {
        static void Main(string[] args)
        {
            // Python code:
            // x = 10
            // y = 20
            // print(x + y)

            int x = 10;
            int y = 20;
            Console.WriteLine(x + y);

            // Python code:
            // if x > y:
            //     print("x is greater than y")
            // elif x < y:
            //     print("x is less than y")
            // else:
            //     print("x and y are equal")

            if (x > y)
            {
                Console.WriteLine("x is greater than y");
            }
            else if (x < y)
            {
                Console.WriteLine("x is less than y");
            }
            else
            {
                Console.WriteLine("x and y are equal");
            }

            // Python code:
            // def greet(name):
            //     print("Hello, " + name + "!")
            //
            // greet("John")

            void Greet(string name)
            {
                Console.WriteLine("Hello, " + name + "!");
            }

            Greet("John");

            // Python code:
            // def add(x, y):
            //     return x + y
            //
            // result = add(10, 20)
            // print(result)

            int Add(int x, int y)
            {
                return x + y;
            }

            int result = Add(10, 20);
            Console.WriteLine(result);
// Python code:
// fruits = ["apple", "banana", "cherry"]
//
// for fruit in fruits:
//     print(fruit)

string[] fruits = { "apple", "banana", "cherry" };

foreach (string fruit in fruits)
{
    Console.WriteLine(fruit);
}

// Python code:
// i = 0
// while i < 5:
//     print(i)
//     i += 1

int i = 0;

while (i < 5)
{
    Console.WriteLine(i);
    i++;
}

// Python code:
// class Car:
//     def __init__(self, make, model, year):
//         self.make = make
//         self.model = model
//         self.year = year
//
// my_car = Car("Tesla", "Model S", 2021)
// print(my_car.make)
// print(my_car.model)
// print(my_car.year)

class Car
{
    public string Make { get; set; }
    public string Model { get; set; }
    public int Year { get; set; }

    public Car(string make, string model, int year)
    {
        Make = make;
        Model = model;
        Year = year;
    }
}

Car myCar = new Car("Tesla", "Model S", 2021);
Console.WriteLine(myCar.Make);
Console.WriteLine(myCar.Model);
Console.WriteLine(myCar.Year);

// Python code:
// def square(x):
//     return x * x
//
// numbers = [1, 2, 3, 4, 5]
//
// squares = list(map(square, numbers))
//
// print(squares)

int Square(int x)
{
    return x * x;
}

int[] numbers = { 1, 2, 3, 4, 5 };

List<int> squares = numbers.Select(Square).ToList();

Console.WriteLine(string.Join(", ", squares));
// Python code:
// numbers = [1, 2, 3, 4, 5]
//
// even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
//
// print(even_numbers)

int[] numbers = { 1, 2, 3, 4, 5 };

List<int> evenNumbers = numbers.Where(x => x % 2 == 0).ToList();

Console.WriteLine(string.Join(", ", evenNumbers));

// Python code:
// numbers = [1, 2, 3, 4, 5]
//
// sum = reduce(lambda x, y: x + y, numbers)
//
// print(sum)

int[] numbers = { 1, 2, 3, 4, 5 };

int sum = numbers.Aggregate((x, y) => x + y);

Console.WriteLine(sum);

// Python code:
// def fibonacci(n):
//     if n == 0:
//         return 0
//     elif n == 1:
//         return 1
//     else:
//         return fibonacci(n-1) + fibonacci(n-2)
//
// for i in range(10):
//     print(fibonacci(i))

int Fibonacci(int n)
{
    if (n == 0)
    {
        return 0;
    }
    else if (n == 1)
    {
        return 1;
    }
    else
    {
        return Fibonacci(n - 1) + Fibonacci(n - 2);
    }
}

for (int i = 0; i < 10; i++)
{
    Console.WriteLine(Fibonacci(i));
}

// Python code:
// def calculate_sum(*args):
//     return sum(args)
//
// print(calculate_sum(1, 2, 3, 4, 5))

int CalculateSum(params int[] args)
{
    return args.Sum();
}

Console.WriteLine(CalculateSum(1, 2, 3, 4, 5));
// Python code:
// class Person:
//     def __init__(self, name, age):
//         self.name = name
//         self.age = age
//
//     def __str__(self):
//         return f"{self.name} is {self.age} years old."
//
// person = Person("John", 30)
// print(person)

class Person
{
    public string Name { get; set; }
    public int Age { get; set; }

    public Person(string name, int age)
    {
        Name = name;
        Age = age;
    }

    public override string ToString()
    {
        return $"{Name} is {Age} years old.";
    }
}

Person person = new Person("John", 30);
Console.WriteLine(person);

// Python code:
// class Rectangle:
//     def __init__(self, width, height):
//         self.width = width
//         self.height = height
//
//     def area(self):
//         return self.width * self.height
//
// rectangle = Rectangle(3, 4)
// print(rectangle.area())

class Rectangle
{
    public int Width { get; set; }
    public int Height { get; set; }

    public Rectangle(int width, int height)
    {
        Width = width;
        Height = height;
    }

    public int Area()
    {
        return Width * Height;
    }
}

Rectangle rectangle = new Rectangle(3, 4);
Console.WriteLine(rectangle.Area());

// Python code:
// class Dog:
//     def __init__(self, name):
//         self.name = name
//
//     def bark(self):
//         print(f"{self.name} is barking!")
//
// dog = Dog("Fido")
// dog.bark()

class Dog
{
    public string Name { get; set; }

    public Dog(string name)
    {
        Name = name;
    }

    public void Bark()
    {
        Console.WriteLine($"{Name} is barking!");
    }
}

Dog dog = new Dog("Fido");
dog.Bark();
// Python code:
// class Car:
//     def __init__(self, make, model):
//         self.make = make
//         self.model = model
//
//     def start(self):
//         print(f"The {self.make} {self.model} is starting.")
//
// car = Car("Toyota", "Corolla")
// car.start()

class Car
{
    public string Make { get; set; }
    public string Model { get; set; }

    public Car(string make, string model)
    {
        Make = make;
        Model = model;
    }

    public void Start()
    {
        Console.WriteLine($"The {Make} {Model} is starting.");
    }
}

Car car = new Car("Toyota", "Corolla");
car.Start();

// Python code:
// class Account:
//     def __init__(self, owner, balance):
//         self.owner = owner
//         self.balance = balance
//
//     def deposit(self, amount):
//         self.balance += amount
//         print(f"Deposit of {amount} accepted. New balance is {self.balance}.")
//
//     def withdraw(self, amount):
//         if amount > self.balance:
//             print("Funds unavailable!")
//         else:
//             self.balance -= amount
//             print(f"Withdrawal of {amount} accepted. New balance is {self.balance}.")
//
// account = Account("John", 1000)
// account.deposit(500)
// account.withdraw(2000)

class Account
{
    public string Owner { get; set; }
    public int Balance { get; set; }

    public Account(string owner, int balance)
    {
        Owner = owner;
        Balance = balance;
    }

    public void Deposit(int amount)
    {
        Balance += amount;
        Console.WriteLine($"Deposit of {amount} accepted. New balance is {Balance}.");
    }

    public void Withdraw(int amount)
    {
        if (amount > Balance)
        {
            Console.WriteLine("Funds unavailable!");
        }
        else
        {
            Balance -= amount;
            Console.WriteLine($"Withdrawal of {amount} accepted. New balance is {Balance}.");
        }
    }
}

Account account = new Account("John", 1000);
account.Deposit(500);
account.Withdraw(2000);

// Python code:
// class Student:
//     def __init__(self, name, grade):
//         self.name = name
//         self.grade = grade
//
//     def promote(self):
//         self.grade += 1
//         print(f"{self.name} has been promoted to grade {self.grade}.")
//
// student = Student("John", 10)
// student.promote()

class Student
{
    public string Name { get; set; }
    public int Grade { get; set; }

    public Student(string name, int grade)
    {
        Name = name;
        Grade = grade;
    }

    public void Promote()
    {
        Grade++;
        Console.WriteLine($"{Name} has been promoted to grade {Grade}.");
    }
}

Student student = new Student("John", 10);
student.Promote();
xff);
                    finalBytes[3] = (byte)(id & 0xff);

                    finalBytes[4] = (byte)((outLength >> 24) & 0xff);
                    finalBytes[5] = (byte)((outLength >> 16) & 0xff);
                    finalBytes[6] = (byte)((outLength >> 8) & 0xff);
                    finalBytes[7] = (byte)(outLength & 0xff);

                    Array.Copy(outbuf, 0, finalBytes, 8, outLength);

                    // Add the padding
                    for (int i = outLength + 8; i < finalBytes.Length; i++)
                    {
                        finalBytes[i] = (byte)(padLen - 1);
                    }

                    return finalBytes;
                }
            }
        }
    }
}