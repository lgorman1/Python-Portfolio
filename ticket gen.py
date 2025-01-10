#Luisa Gorman
#12/12/24

#Initialize
import turtle
t = turtle.Turtle()

#Functions

#Draws an admission ticket with a label and customer information inside. This function uses a turtle to draw a ticket with the name of the customer and the price paid for the ticket.
#(string: name) represents the customers name that appears inside the ticket
#(integer: price) represents the price the customer paid that appears inside the ticket
#(string: dayofweek) represents the day of the week that the ticket was purchased
#(integer: y_location) y_location represents the vertical loction of the ticket
def draw_ticket(name, price, dayofweek, y_location):
    t.goto(-50, y_location)
    t.write("Ticket", font=("Arial", 15), align="right")
    t.pendown()
    for i in range(2):
        t.forward(500)
        t.left(90)
        t.forward(250)
        t.left(90)
    t.penup()
    t.goto(50, y_location +215)
    t.write("Admit One", font=("Arial", 15), align="right")
    t.goto(440, y_location +215)
    t.write(dayofweek, font=("Arial", 15), align="right")
    t.goto(225, y_location +135)
    t.write(name, font=("Arial", 15), align="right")
    t.goto(225, y_location +15)
    t.write(price, font=("Arial", 15), align="right")

def ticket_generator():
    #1. Introduce the customer to your app
    print("Welcome to the six flags generator app!")

    #2. Collect the pertinent information
    #Name
    name = input("Enter name:")
    #Age
    age = int(input("Enter age:")) #interger(Good!,
    #Day of the week
    day = input("Enter day of the week:")
    #Coupon code
    coupon = input("Enter a coupon code:")

    #3.Algorithm for setting the price
    if age <= 3:
        price = 0 #baby price
    elif age >= 4 and age <= 17 and day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday":
        price = 50 #kid/student price
    elif age >= 4 and age <= 17 and day == "saturday":
        price = 100
    elif age >= 4 and age <= 17 and day == "friday" and coupon == "FREEFRIDAY":
        price = 0
    elif age >= 4 and age <= 17 and day == "sunday" and coupon == "SUNDAY10":
        price = 90
    elif age >= 18:
        price = 100
    #4. Print the ticket
    draw_ticket(name,price,day,0)

#Main
ticket_generator()
