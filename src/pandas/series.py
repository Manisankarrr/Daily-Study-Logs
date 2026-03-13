import pandas as pd
#Series = A Pandas 1-Dimensional labeled array that can hold any data type
#Think of it like a single column in a spreadsheet (1-Dimensional)
print(pd.__version__)

data = [100,102,104,108]
series = pd.Series(data)

print(series)

calories = { "day1" : 1750, "Day2" : 2100, "Day3" : 1800}

seri = pd.Series(calories)

print(seri)