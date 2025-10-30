import turtle


for x in range(4):
    turtle.forward(100)
    turtle.right(90)
    
for x in range(8):
    turtle.forward(100)
    turtle.right(45)   

def hit_the_target():
    angle = float(input("Enter the angle (between o and 90): "))
    force = float(input("Enter the force: "))

    