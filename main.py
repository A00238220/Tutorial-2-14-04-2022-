#importing relevant libraries
import numpy as np

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
  