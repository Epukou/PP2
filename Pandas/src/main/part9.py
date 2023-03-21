import pandas as pd

url = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/09_Time_Series/Apple_Stock/appl_1980_2014.csv"
apple = pd.read_csv(url, sep=",")

print(apple.dtypes)

apple['Date'] = pd.to_datetime(apple['Date'])

apple.set_index('Date', inplace=True)

print(any(apple.index.duplicated()))

apple = apple.iloc[::-1]

last_business_day = apple.resample('BM').last()

days_diff = (apple.index.max() - apple.index.min()).days
print("Difference in days:", days_diff)

months_count = len(apple.resample('M'))

# Plot the Adj Close value
import matplotlib.pyplot as plt
plt.figure(figsize=(13.5, 9))
plt.plot(apple['Adj Close'])
plt.xlabel('Year')
plt.ylabel('Adj Close')
plt.title('Apple Stock Price')
plt.show()
