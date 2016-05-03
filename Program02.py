# Kirsten Richmond

# Program 02


#2.3

equation = input("\n\nPlease enter an expression of the form number+number.")
        #asking the user to input their numbers
output = equation

print(output)

sgn = equation.find("+")
i = (sgn)
if i:
    print("invalid")
else:
    firstInt = int(equation[:sgn])
    #firstInt is the first number to add
    secondInt = int(equation[sgn+1:])
    #secondInt is the second number
    theSum = firstInt + secondInt

    print("The sum is") 
    print(theSum)
   
#the program is pulling out the mathematic symbol
    
while True:
    firstInt = int(equation[:sgn]) #firstInt is the first number to add
    secondInt = int(equation[sgn+1:]) #secondInt is the second number
    theSum = firstInt + secondInt
    print("The sum is") 
    print(theSum)
    if sgn != ("+"):
        break

theSum = firstInt + secondInt
#this will add both of the numbers together
    
if (sgn):
    print("The sum is") 
    print(theSum)
if(not(equation.find("+"))):
    print("You have entered an invalid expression.")



