import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/07_Visualization/Titanic_Desaster/train.csv"
titanic = pd.read_csv(url, sep=",")

titanic.set_index('PassengerId', inplace=True)

proportions = titanic['Sex'].value_counts()
plt.pie(proportions, labels=proportions.index.values, autopct='%1.1f%%')
plt.title('Male/Female Proportion')
plt.show()

colors = {'male':'blue', 'female':'red'}
plt.scatter(titanic['Age'], titanic['Fare'], alpha=0.5, c=titanic['Sex'].map(colors))
plt.xlabel('Age')
plt.ylabel('Fare')
plt.title('Age vs Fare by Gender')
plt.show()

survived = titanic['Survived'].value_counts()[1]
print(f'{survived} people survived.')

plt.hist(titanic['Fare'], bins=50)
plt.xlabel('Fare')
plt.ylabel('Frequency')
plt.title('Fare Paid Histogram')
plt.show()

average_age = titanic['Age'].mean()
print(f'The average age of the passengers on board was {average_age:.1f} years old.')
