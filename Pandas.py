import pandas as pd

Introduction to pandas Data Structures ::
two primary data structure pandas has are "SERIES" and "DATAFRAMES". 
The series constitutes the data structure designed to accommodate a sequence of one-dimensional data, while the dataframe, a 
more complex data structure, is designed to contain cases with several dimensions.

# The Series ::
=============================================================================================================================
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

#isin of pandas
>>> s1.isin([6,9])
0    False
1    False
2    False
3     True
4     True
dtype: bool
>>> s1[s1.isin([6,9])]
3    6
4    9
dtype: int64 
  
# NaN (Not a Number) values :: This specific value NaN (Not a Number) is used in pandas data structures to indicate the 
#presence of an empty field or something that’s not definable numerically. these NaN values are a problem and must be managed 
#in some way,
>>> s = pd.Series([4,5,0,-8,9])
>>> 
>>> s
0    4
1    5
2    0
3   -8
4    9
dtype: int64
>>> 
>>> np.log(s)
__main__:1: RuntimeWarning: divide by zero encountered in log
0    1.386294
1    1.609438
2        -inf
3         NaN
4    2.197225
dtype: float64
  
we can add NaN as well, whenever we want to specify a missing value. you enter np.NaN wherever you want to define a missing 
value.
>>> a = pd.Series([np.NaN, 200])
>>> a
0      NaN
1    200.0
dtype: float64
  
>>> a.isnull()
0     True
1    False
dtype: bool
  
>>> a.notnull()
0    False
1     True
dtype: bool  
  
>>> a = pd.Series(np.NaN)
>>> a
0   NaN
dtype: float64
  
#These functions are often placed inside filters to make a condition. if you want to get the values which are not null you 
#might want to use this :: 

>>> a[a.notnull()]
1    200.0
dtype: float64

# Series as Dictionaries
An alternative way to think of a series is to think of it as an object dict (dictionary). This similarity is also exploited 
during the definition of an object series.

>>> a = {'red' : 5, 'White' : 10, 'black' : 9, 'Pink' : 7}
>>> a
{'red': 5, 'White': 10, 'black': 9, 'Pink': 7}
>>> 
>>> b = pd.Series(a)
>>> b
red       5
White    10
black     9
Pink      7
dtype: int64
  
>>> m = [1,3,4]
>>> n = ['A', 'C', 'D']
>>> c = pd.Series(m, index = n)
>>> c
A    1
C    3
D    4
dtype: int64  

>>> a = {'A' : 5, 'White' : 10, 'black' : 9, 'Pink' : 7}
>>> n = ['A', 'C', 'D', 'F']
>>> c = pd.Series(a, index = n)
>>> c
A    5.0
C    NaN
D    NaN
F    NaN
dtype: float64

#Operations Between Series :: You get a new object series in which only the items with the same label are added. All other 
#labels present in one of the two series are still added to the result but have a NaN value. 

>>> a = pd.Series([5,7,9], index = ['red', 'green', 'yellow'])
>>> b = pd.Series([11,13,15], index = ['red', 'green', 'blue'])
>>> a + b
blue       NaN
green     20.0
red       16.0
yellow     NaN
dtype: float64
  
# The DataFrame
=============================================================================================================================
The Dataframe is a tabular data structure very similar to a spreadsheet. This datastructure has been defined to extend Series
to multiple dimensions. In fact, the dataframe consists of an ordered collection of columns,  each of which can contain a value
of a different type (numeric, string, Boolean, etc.). Unlike series, which have an index array containing labels associated 
with each element, the dataframe has two index arrays. The first index array, associated with the lines, has very similar 
functions to the index array in series. In fact, each label is associated with all the values in the row. The second array 
contains a series of labels, each associated with a particular column.
A dataframe may also be understood as a dict of series, where the keys are the column names and the values are the series that 
will form the columns of the dataframe. Furthermore, all elements in each series are mapped according to an array of labels, 
called the index.

The most common way to create a new dataframe is precisely to pass a dict object to the DataFrame() constructor. This dict 
object contains a key for each column that you want to define, with an array of values for each of them.
  
>>> dick = {'name' : ['Sankar', 'Puja'], 'Age': [23,24], 'color' : ['brown', 'white']}
>>> frame = pd.DataFrame(dick)
>>> frame
     name  Age  color
0  Sankar   23  brown
1    Puja   24  white  







