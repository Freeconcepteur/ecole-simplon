from components.mymodule import addition
import numpy as np
import pandas as pd

print(addition(2, 3))


# Créer un array
array = np.array([1, 2, 3, 4, 5])

# Afficher l'array
print(array)



df = pd.read_csv('data/titanic_in.csv')
columns_to_drop = ['Ticket', 'Fare', 'Cabin']
df_clean = df.drop(columns=columns_to_drop)

df_clean.to_csv('data/titanic_clean.csv', index=False)


print(df_clean.head())