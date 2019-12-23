import pandas as pd
# import numpy as np
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','fare']]
print(df.head())
print('\n')
print(type(df))
print('\n')
addition = df + 10
print(addition.head())
print('\n')
print(type(addition))