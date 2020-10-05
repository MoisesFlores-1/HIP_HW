sales_tax = .95
#sales tax is defined here and can be changed 
price = int(input ("Enter Price: ") )
result = 0
#The user inputs the price of the item here. 
while (price > 0) :
  #As long as the price is greater than 0,
  # then the program will loop until 0 is the input from the user
  price = float(input("Enter Price :"))
  #the price is converted to float from string
  total = price % 10
result = result + total 
price = price //10 
Final_Tax = float(price*sales_tax)
 #Here is where the final total plus the tax is calculated. 
 #However I believe this may be useless if the function below does the same thing?
def calculateCountyTax(price):
    return price:float * sales_tax:float 
    #Once again this is where tax is calculated with the cost of items
input("Is Sales Tax Applicable? Y/N :" )
#User is asked if sales tax is applicable. 
#I am having trouble with the "if" statements because when the user inputs "N" the program does not run the section for a taxless price.
if True:
  #if true is meant to represent if tax IS applicable
  print(" Your Final TAX Total is:", Final_Tax:float + price:float )
  #The taxed total is described here
  float(input("Enter Amount Paid :"))
print("Change today is: ", input - Final_Tax:float + price:float )
#Here is where the change of the customer's money is displayed
if not True: 
  #if not true would represent if tax is NOT applicable
    print ("Your NON TAX Total is:", price:float )
    #The total cost without tax is presented
input("Enter Amount Paid :")
print("Change today is: ", input-price:float)