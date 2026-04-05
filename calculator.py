
def plus(a,b):
    print(f"{a}+{b}={a+b}")
    return a+b

def minus(a,b):
    print(f"{a}-{b}={a-b}")
    return a-b

def multiply(a,b):
    print(f"{a}*{b}={a*b}")
    return a*b

def divide(a,b):
    print(f"{a}/{b}={round(a/b,3)}")
    return round(a/b,3)
def calculator(operator,first_number,second_number):
    if operator=="+":
        return plus(first_number,second_number)
    elif operator=="-":
        return minus(first_number,second_number)
    elif operator=="*":
        return multiply(first_number,second_number)
    elif operator=="/":
        return divide(first_number,second_number)
    else:
        return "Bad Operation"
    

def first_calculation():
 first_number=float(input("enter the First Number:"))
 print("*","\n","+","\n","-","\n","/","\n")
 operator=input("Pick an operator:")
 second_number=float(input("enter the Secod Nubmer:"))
 return calculator(operator,first_number,second_number)
result=first_calculation()

user_action=True
while user_action:
   user_action=input(f" Type 'y' to continue with {result} or type 'n' to start a new calculation or click enter to Exit the Code : ")
   if user_action=="y":
    print("*","\n","+","\n","-","\n","/","\n")
    operator=input("Pick an operator:")
    second_number=float(input("enter the Secod Nubmer:")) 
    new_result=calculator(operator,result,second_number)
    print(new_result)
    result=new_result

   elif user_action=="n":
    print("\n"*1000)
    new_result=first_calculation()
    result=new_result
    print(new_result)
   else:
      user_action=False



   





