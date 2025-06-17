import pandas as pd

data = [1,2,3,4,5]

s = pd.Series(data)

print(s)

# Now we are creating custom labels(indexes)

data1 = [10,20,30,40,50]
labels = ['A','B','C','D', 'E']
s1 = pd.Series(data1, index=labels)

print(s1)

print(s1['B'])

#Creating a Series with our own fruits and their prices

fruits = ["Apple", "Orange", "Banana", "Watermelon"]

prices = [250, 50, 60, 120]

result = pd.Series(prices, index=fruits)

print(f"The prices of the fruits are \n{result}")

print(result[["Apple", "Orange"]])
print(f"The price of the third fruit is {result["Banana"]}")
print(f"The sum of the 5 fruits is {result.sum(axis=0)}")
print(f"the average price is {result.sum(axis=0)/result.count()}")
print(result[:3])
print(result[-2:])
print("Pineapple" in result)
print(f"The fruits taht cost more than 50 is \n{result[result > 50]}")
result["Banana"] += 10
print(result)

print(result[result > 100])