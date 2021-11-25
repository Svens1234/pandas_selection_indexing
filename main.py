import numpy as np
import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(4,3), ['a', 'b', 'c', 'd'], ['X', 'Y', 'Z'])
print(df)
bool_df = df>0
print(bool_df)
print(df[bool_df])
print(df[df>0])
print(df)
print(df['Y']>1)
print(type(df['Y']))
print(df)
print(df[df['Y']>1])
print(df)
print(df[df['X']<0])
res = df[df['X']<0]
print(res)
print(res['Z'])
print(df[df['X']<0]['Z'])
print(df[df['X']<0][['Z', 'X']])
bool_ser = df['X']<0
print(bool_ser)
result_df = df[bool_ser]
print(result_df)
print(result_df[['Z', 'X']])
print(df[df['X']<0][['Z', 'X']])
print(df)
print(df[(df['X']>0) & (df['Z']<0)])
print(df[(df['X']>0) | (df['Z']<0)])
print(df)
df.reset_index()
print(df)
df.reset_index(inplace=True)
print(df)
z1 = [2,3,5,6]
df['z1'] = z1
print(df)
df1 = pd.DataFrame(randn(4,3), ['a', 'b', 'c', 'd'], ['X', 'Y', 'Z'])
z2 = [2,3,5,6]
df1['z2'] = z2
print(df1)
print(df1.set_index('z2'))
print(df1)
print(df1.set_index('z2', inplace=True))
print(df1)