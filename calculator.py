import logging
logging.basicConfig(level=logging.INFO)# set up a basic configuration to show the message in console


operation = int(input(''' Please select a number between 1 and 4
                  1 - divide
                  2 - multiply
                  3 - add
                  4 - substract
                  : '''))
                  
if (operation == 2 or operation == 3 ):   # 3 values can be used for addition and multiplication function, 2 values can be used for division and substraction function  
 a =  float(input('''Please type a first number 
          -> ''')) # convert into the float
 b = float(input('''Please type a second number
          -> ''')) # convert into the float
 d = float(input('''Please type a third number
          -> ''')) # convert into the float        
      
elif (operation == 1 or operation == 4 ):   
 a =  float(input('''Please type a first number 
          -> ''')) # convert into the float
 b = float(input('''Please type a second number
          -> ''')) # convert into the float
          
else:
     print("incorrect operation selected by user - Invalid input")  
          
def divide(num1, num2):    
    return num1 / num2  # function to divide 2 numbers
         
def multiply(num1, num2, num3): 
    return num1 * num2 * num3   # function to multiply 3 numbers

def add(num1, num2, num3):  
    return num1 + num2 + num3 #function to add 3 numbers

def substract(num1, num2):
    return num1 - num2 # function to substract 2 numbers

if operation == 1:
    #print(a, "/", b, "=", divide(a, b))# replace "print" by "logging"
    logging.info("The division of {a} with {b} is {c}".format(a=a, b=b, c=divide(a,b)))
    
elif operation == 2:
   # print(a, "*", b, "=", multiply(a, b, d3)
   logging.info("The multiplication of {a} with {b} and {d} is {c}".format(a=a, b=b, d=d, c= multiply(a,b,d)))

  
elif operation == 3:
    #print(a, "+", b, "=", add(a, b, d))
    logging.info("The addition of {a} with {b} and {d} is {c}".format(a=a, b=b, d=d, c= add(a,b,d)))
    
  
elif operation == 4:
    #print(a, "-", b, "=", substract(a, b))
    logging.info("The substraction of {a} with {b} is {c}".format(a=a, b=b, c=substract(a,b)))
    
else:
    print("incorrect operation selected by user - Invalid input")  
    
  
  
          