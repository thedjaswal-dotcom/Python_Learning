
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

calclulation_operation={
    "+":plus,
    "-":minus,
    "*":multiply,
    "/":divide
}

user_action=True
def first_calculation():
 first_number=float(input("enter the First Number:"))
 for symbol in calclulation_operation:
    print(symbol)
# print("*","\n","+","\n","-","\n","/","\n")
 operator=input("Pick an operator:")
 second_number=float(input("enter the Secod Nubmer:"))
 new_var=calclulation_operation[operator]
 return new_var(first_number,second_number)

result=first_calculation()
while user_action:
   user_action=input(f" Type 'y' to continue with {result} or type 'n' to start a new calculation or click enter to Exit the Code : ")
   if user_action=="y":
    #print("*","\n","+","\n","-","\n","/","\n")
    for symbol in calclulation_operation:
     print(symbol)
    operator=input("Pick an operator:")
    second_number=float(input("enter the Secod Nubmer:")) 
    new_var=calclulation_operation[operator]
    new_result=new_var(result,second_number)
    print(new_result)
    result=new_result

   elif user_action=="n":
    print("\n"*1000)
    new_result=first_calculation()
    result=new_result
    print(new_result)
   else:
      user_action=False
