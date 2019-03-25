import pandas as pd

Introduction to pandas Data Structures ::
two primary data structure pandas has are "SERIES" and "DATAFRAMES". 
The series constitutes the data structure designed to accommodate a sequence of one-dimensional data, while the dataframe, a 
more complex data structure, is designed to contain cases with several dimensions.

The Series ::
The series is the object of the pandas library designed to represent one-dimensional data structures, similar to an array but 
with some additional features. Its internal structure is simple and is composed of two arrays associated with each other. The 
main array holds the data (data of any NumPy type) to which each element is associated with a label, contained within the other
array, called the index.

To create a series, you simply call the Series() constructor and pass as an argument an array containing the values to be 
included in it.

>>> s = pd.Series([12,-4,7,9])
>>> s
0    12
1    -4
2     7
3     9
dtype: int64

by default if not provided pandas will assign index starting from 0. but it is better to give index.

>>> s = pd.Series([12,-4,7,9], index=['a','b','c','d'])
>>> print(s)
a    12
b    -4
c     7
d     9
dtype: int64

>>> s.values 
array([12, -4,  7,  9])
>>> s.index
Index(['a', 'b', 'c', 'd'], dtype='object')
>>> type(s.index)
<class 'pandas.core.indexes.base.Index'>

once you done creating it, you can manipulate, update and modify a Series just like how you do it in a List.
you can see the hands on part of the pandas in the jupyter notebook.

Other operations such as operators (+, -, *, and /) and mathematical functions that are applicable to NumPy array can be 
extended to series.

#dividing all the elements using an integer
>>> s/2
a    6.0
b   -2.0
c    3.5
d    4.5
dtype: float64

#determine the log values of each element of s
>>> s
a    12
b    -4
c     7
d     9
dtype: int64
>>> 
>>> s.index
Index(['a', 'b', 'c', 'd'], dtype='object')
>>> 
>>> s['b'] = 4
>>> s
a    12
b     4
c     7
d     9
dtype: int64
>>> np.log(s)
a    2.484907
b    1.386294
c    1.945910
d    2.197225
dtype: float64


you can have same index value for multiple elements in a Series.
>>> s = pd.Series([1,2,3,4,4], index = ['a','a','a','b','c'])
>>> s
a    1
a    2
a    3
b    4
c    4
dtype: int64
>>> s['a']
a    1
a    2
a    3
dtype: int64

#getting the unique values
>>> s.unique()
array([1, 2, 3, 4])

#getting the no of occurence of each element in s
>>> s.value_counts()
4    2
3    1
2    1
1    1
dtype: int64




