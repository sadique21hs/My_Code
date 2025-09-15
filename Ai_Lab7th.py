import pandas as pd
from sklearn.preprocessing import MinMaxScaler
data = {
     'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan'],
    'Salary': [55000.0, 62000.5, 75000.0, 80000.0, 47000.0],
    'ID': [101, 102, 103, 104, 105],
    'Age': [25, 30, 35, 28, 22],
    'Experience' :[2, 5, 10, 4, 1],
    'City': ['New York', 'Los Angeles', 'Chicago','New York', 'Chicago']
}

df = pd.DataFrame(data)
print(df)

print(df.dtypes)

scaler = MinMaxScaler()
df['Salary'] = scaler.fit_transform(df[['Salary']])

print(df)
