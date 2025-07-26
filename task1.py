def  get_ticket_price(age, seat_type,is_student):
    if seat_type=="yes":
        x=150
        print("Seat Type:Premium")
    else:
        x=0
        print("Seat Type:Normal")

    if age<=12:
        x=x+100
    elif age>12 and age <=60:
        x=x+200
    else:
        x=x+150
    
    print("Base Ticket Price:",x)
    total=apply_discount (x, is_student)
    return total

def apply_discount(x,is_student):
    if is_student=="yes":
        price=x-(x*0.1)
        print("Final Price after Student Discount:", price)
    else:
        price=x
    return price
        
    
age=float(input("Enter age:"))
seat_type=input("Is premium? yes or no:")
is_student=input("Are you a student? type: yes or no:")
total=get_ticket_price(age,seat_type,is_student)
print("Final price:",total)