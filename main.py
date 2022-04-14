#importing relevant libraries
import numpy as np
import random
import time


###########
#Question 1
###############
#making a dictionary
stock_prices = {
  "dangote" : [24.2, 14.3, 47.8, 45.7, 10.2, 4.13, 17.9, 19.5, 25.7, 33.5],
  "apple" : [2.2, 14.3, 7.8, 55.7, 10.2, 4.13, 17.9, 19.5, 5.7, 33.5],
  "microsoft" : [24.2, 114.3, 47.8, 45.7, 110.2, 4.13, 132.9, 19.5, 215.7, 33.5]  
}

#setting for loop
for price in stock_prices:
  min_price = np.min(stock_prices[price])
  max_price = np.max(stock_prices[price])
  average_price = np.mean(stock_prices[price])

  print(f"The minimum stock for {price.title()} is {min_price}\nThe maximum stock for {price.title()} is {max_price}\nThe average stock for {price.title()} is {average_price}")
  print()

print()
###########
#Question 2
###############

popularity_score = 0
  
for x in range(5): 
  gains = random.randint(1, 20)
  popularity_score += gains
  
  print(f"Ada gives a great speech and gains {gains}% popularity! Total popularity is now {popularity_score}%!")

#setting conditional statement
if popularity_score >= 51:  
  print("Score high enough, Ada wins the election")
else:
  print("Score too low, Ada loses the election")


popularity_score = popularity_score + gains

choice_list = ['a', 'b', 'c', 'd']

print()
###########
#Question 3
###############
input1 = input("please enter your name: ")
time.sleep(1)

print(f"welcome {input1.title()}!")
time.sleep(1)

print()
print("Pizza Menu Price:\n\n[1] Small $6.99\n[2] Medium $8.99\n[3] Large $10.99")

print()
input2 = input("please enter selection: ")
time.sleep(1)

print()
input3 = input("please number of pizza: ")
time.sleep(1)

print()
#setting condition
if input2 == '1':
  tax = 0.13 * (6.99 * int(input3))
  total = tax + (6.99 * int(input3))
  print(f"customer name : {input1.title()}\norder: small-size pizza @ $6.99\ntax: {tax}\ntotal: {total}")

elif input2 == '2':
  tax = 0.13 * (8.99 * int(input3))
  total = tax + (8.99 * int(input3))
  print(f"customer name : {input1.title()}\norder: medium-size pizza @ $8.99\ntax: {tax}\ntotal: {total}")

elif input2 == '3':
  tax = 0.13 * (10.99 * int(input3))
  total = tax + (10.99 * int(input3))
  print(f"customer name : {input1.title()}\norder: large-size pizza @ $10.99\ntax: {tax}\ntotal: {total}")

print()
###########
#Question 4
###############
#Question 3
#creating a while loop with an input function for age
count = 0

while True:
  t_cost = 0
  count += 1
  print("\n\nWelcome to Sharon's Restaurant")
  name = input('Please enter member ' + str(count) + ' name: ')
  print(f"\nHello, {name.title()}!")
  age = int(input('Please enter member ' + str(count) + ' age to see dinner cost: '))
  time.sleep(2)

#creating conditional statements and summary of dinner with updated cost
  if age < 5:
    t_cost += 0
  elif age < 10:
    t_cost += 5
  elif age < 18:
    t_cost += 10
  elif age > 65:
    t_cost += 15
  else:
    t_cost += 15

  t_cost += t_cost * 0.08
  avg_cost = t_cost/count
  cum_cost = t_cost * count
  
  print(f"\nSummary:\nYour number of dinner plate is {count}\nYour cost of dinner is ${t_cost}\nYour average dinner cost is ${avg_cost}\nThe cumulative dinner cost is ${cum_cost}")

  member2 = input("\nplease enter 'exit' to end program or press enter to add dinner plate: ")
  if member2 == 'exit':
    break
  else:
    continue
  time.sleep(2)