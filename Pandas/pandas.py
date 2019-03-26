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

If the dict object from which you want to create a dataframe contains more data than you are interested in, you can make a 
selection.

>>> frame1 = pd.DataFrame(dick, columns = ['name'])
>>> frame1
     name
0  Sankar
1    Puja


# we can assign our own index as well other than the sequence integer number strating from 0
>>> frame1 = pd.DataFrame(dick, index = ['first', 'second'])
>>> frame1
          name  Age  color
first   Sankar   23  brown
second    Puja   24  white

#other ways to define a DataFrame
>>> frame3 = pd.DataFrame(np.arange(16).reshape((4,4)), index=['red','blue','yellow','white'], columns=['ball','pen','pencil','paper'])
>>> frame3
        ball  pen  pencil  paper
red        0    1       2      3
blue       4    5       6      7
yellow     8    9      10     11
white     12   13      14     15

# Selecting Elements
>>> frame.columns
Index(['name', 'Age', 'color'], dtype='object')

>>> frame.index
RangeIndex(start=0, stop=2, step=1)

>>> frame.values
array([['Sankar', 23, 'brown'],
       ['Puja', 24, 'white']], dtype=object)

#selecting a particular a column : return a Series as output
>>> frame['name']
0    Sankar
1      Puja
Name: name, dtype: object

>>> frame['Age']
0    23
1    24
Name: Age, dtype: int64

#selecting multiple columns
    
>>> frame[['name', 'Age']]
     name  Age
0  Sankar   23
1    Puja   24    

#selecting a particular row     
>>> frame.loc[1]
name      Puja
Age         24
color    white
Name: 1, dtype: object
    
>>> frame.loc[0]
name     Sankar
Age          23
color     brown
Name: 0, dtype: object    

#selecting multiple rows

>>> frame.loc[[0, 1]]
     name  Age  color
0  Sankar   23  brown
1    Puja   24  white   

>>> frame['name'][1]
'Puja'

# Assigning Values ::
>>> frame.name[0] = 'Sambhu'
__main__:1: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame

>>> frame
     name  Age  color
0  Sambhu   23  brown
1    Puja   24  white


we can put label on the index and column names as well ::
>>> frame
     name  Age  color
0  Sambhu   23  brown
1    Puja   24  white

>>> frame.index.name = 'idd'

>>> frame
       name  Age  color
idd                    
0    Sambhu   23  brown
1      Puja   24  white

>>> frame.columns.name = 'PwC'

>>> frame
PwC    name  Age  color
idd                    
0    Sambhu   23  brown
1      Puja   24  white

>>> frame.columns.name = 'PwC sucks'

>>> frame
PwC sucks    name  Age  color
idd                          
0          Sambhu   23  brown
1            Puja   24  white    


#One of the best features of the data structures of pandas is their high flexibility. In fact, you can always intervene at any 
#level to change the internal data structure.

#adding a new column 
>>> frame['Company'] = ['PwC', 'Infosys']
>>> frame
PwC sucks    name  Age  color  Company
idd                                   
0          Sambhu   23  brown      PwC
1            Puja   24  white  Infosys

# adding a new column using a Series

ser = pd.Series['Janai', 'BBSR']

>>> ser = pd.Series(['Janai', 'BBSR'])
>>> ser
0    Janai
1     BBSR
dtype: object

>>> frame['Address'] = ser
>>> frame
PwC sucks    name  Age  color  Company Address
idd                                           
0          Sambhu   23  brown      PwC   Janai
1            Puja   24  white  Infosys    BBSR

# changing a single value
>>> frame['Address'][0] = 'Kolkata' 

>>> frame
PwC sucks    name  Age  color  Company  Address
idd                                            
0          Sambhu   23  brown      PwC  Kolkata
1            Puja   24  white  Infosys     BBSR

# Deleting a Column
>>> del frame['color']
>>> frame
PwC sucks    name  Age  Company  Address
idd                                     
0          Sambhu   23      PwC  Kolkata
1            Puja   24  Infosys     BBSR

#putting restriction (The below example will put restriction on all the columns having data type as numeric)
>>> frame['salary'] = pd.Series([1000,999])

>>> frame
PwC sucks    name  Age  Company  Address  salary
idd                                             
0          Sambhu   23      PwC  Kolkata    1000
1            Puja   24  Infosys     BBSR     999

>>> frame[frame > 999]
PwC sucks    name  Age  Company  Address  salary
idd                                             
0          Sambhu  NaN      PwC  Kolkata  1000.0
1            Puja  NaN  Infosys     BBSR     NaN

# Transposition of a Dataframe : just s
>>> frame.T
idd              0        1
PwC sucks                  
name        Sambhu     Puja
Age             23       24
Company        PwC  Infosys
Address    Kolkata     BBSR
salary        1000      999


# conditional element search and fetching the elements based on a condition

>>> frame.isin(['PwC', 23, 999])
PwC sucks   name    Age  Company  Address  salary
idd                                              
0          False   True     True    False   False
1          False  False    False    False    True

>>> frame[frame.isin(['PwC', 23, 999])]
PwC sucks name   Age Company Address  salary
idd                                         
0          NaN  23.0     PwC     NaN     NaN
1          NaN   NaN     NaN     NaN   999.0

# DataFrame from Nested dict :: This data structure, when it is passed directly as an argument to the DataFrame() constructor, 
# will be interpreted by pandas to treat external keys as column names and internal keys as labels for the indexes. It might 
# happen 


>>> nestdict = {'red': { 2012: 22, 2013: 33 },'white': { 2011: 13, 2012: 22, 2013: 16},'blue': {2011: 17, 2012: 27, 2013: 18}}

>>> frame4 = pd.DataFrame(nestdict)
>>> frame4
       red  white  blue
2011   NaN     13    17
2012  22.0     22    27
2013  33.0     16    18



# The index object :: 
the majority of excellent characteristics that the Series and DataFrame has, are due to the presence of an Index object that’s 
integrated in these data structures. Unlike all the other elements in the pandas data structures (series and dataframe), the 
Index objects are immutable. Once declared, they cannot be changed. This ensures their secure sharing between the various data 
structures.

#Different methods on index :: 
>>> ser = pd.Series([5,0,3,8,4], index=['red','blue','yellow','white','green'])

>>> ser.idxmin()
'blue'

>>> ser.idxmax()
'white'

# if you have multiple values for a particular index label, when you will fetch output based on that label, all the rows will
# be shown as output, this is true for both Series and DataFrame.

using different index methods you can find out whether your index labels are having duplicates or not :: 

>>> ser2 = pd.Series(range(5))
>>> ser2
0    0
1    1
2    2
3    3
4    4
dtype: int64
  
>>> ser2.index.is_unique
True

>>> frame3.index.is_unique
True

# Other Functionalities on Indexes
1) Reindexing :: we can change the existing indexing and reallign all the data. During reindexing, it is possible to change 
    the order of the sequence of indexes, delete some of them, or add new ones. In the case of a new label, pandas adds NaN 
    as the corresponding value.
    
>>> ser10 = pd.Series([1,2,3,4,5], index = [0,3,4,6,9])

>>> ser10
0    1
3    2
4    3
6    4
9    5
dtype: int64

>>> ser11 = ser10.reindex([1,2,3,4,5])

>>> ser11
1    NaN
2    NaN
3    2.0
4    3.0
5    NaN
dtype: float64

you can see the NaN values because those indexes were not present before.

you can use methods like 'bfill' and 'ffill' to replace those NaN's.

>>> ser12 = ser10.reindex([1,2,3,4,5], method = 'ffill')
>>> ser12
1    1
2    1
3    2
4    3
5    3
dtype: int64
  
>>> ser13 = ser10.reindex([1,2,3,4,5], method = 'bfill')
>>> ser13
1    2
2    2
3    2
4    3
5    4
dtype: int64
# i need to explore more on bfill and ffill 
>>> ser14 = pd.Series([1,3,5,7,9], index = [1,3,4,6,7])
>>> 
>>> ser14.reindex(range(5))
0    NaN
1    1.0
2    NaN
3    3.0
4    5.0
dtype: float64
>>> 
>>> ser14.reindex(range(5), method = 'ffill')
0    NaN
1    1.0
2    1.0
3    3.0
4    5.0
dtype: float64
>>> 
>>> ser14.reindex(range(5), method = 'bfill')
0    1
1    1
2    3
3    3
4    5
dtype: int64
  
we can do these operations on DataFrame as well.
>>> frame.reindex(range(5), method='ffill',columns=['colors','price','new','object'])
  
2) Dropping :: Deleting a row or a column becomes simple, due to the labels used to indicate the indexes and column names.
    
>>> ser = pd.Series(np.arange(4.), index=['red','blue','yellow','white'])
>>> ser
red       0.0
blue      1.0
yellow    2.0
white     3.0
dtype: float64
  
>>> ser.drop('yellow')
red      0.0
blue     1.0
white    3.0
dtype: float64
  
>>> ser.drop(['blue','white'])
red       0.0
yellow    2.0
dtype: float64  
  
DataFrame element can be deleted out as well :: 
>>> frame = pd.DataFrame(np.arange(16).reshape((4,4)),index=['red','blue','yellow','white'],columns=['ball','pen','pencil','paper'])
>>> 
>>> frame
        ball  pen  pencil  paper
red        0    1       2      3
blue       4    5       6      7
yellow     8    9      10     11
white     12   13      14     15
>>> 
>>> 
>>> frame.drop(['blue','yellow'])
       ball  pen  pencil  paper
red       0    1       2      3
white    12   13      14     15

#To delete columns, you always need to specify the indexes of the columns, but you must specify the axis from which to delete 
#the elements, and this can be done using the axis option. So to refer to the column names, you should specify axis = 1.

>>> frame.drop(['pen','pencil'], axis = 1)
        ball  paper
red        0      3
blue       4      7
yellow     8     11
white     12     15


# 3) Arithmetic and Data Alignment ::
pandas can align indexes coming from two different data structures. This is especially true when you are performing an 
arithmetic operation on them.

>>> s1 = pd.Series([3,2,5,1],['white','yellow','green','blue'])
>>> s2 = pd.Series([1,4,7,2,1],['white','yellow','black','blue','brown'])

>>> s1 + s2
black    NaN
blue     3.0
brown    NaN
green    NaN
white    4.0
yellow   6.0
dtype: float64
  
for Dataframe it considers the indexes and additionally it considers the column names as well.

>>> frame1 = pd.DataFrame(np.arange(16).reshape((4,4)),
...                   index=['red','blue','yellow','white'],
...                   columns=['ball','pen','pencil','paper'])
>>> frame2 = pd.DataFrame(np.arange(12).reshape((4,3)),
...                   index=['blue','green','white','yellow'],
...                   columns=['mug','pen','ball'])
>>> frame1
        ball  pen  pencil  paper
red        0    1       2      3
blue       4    5       6      7
yellow     8    9      10     11
white     12   13      14     15
>>> frame2
        mug  pen  ball
blue      0    1     2
green     3    4     5
white     6    7     8
yellow    9   10    11

>>> frame1 + frame2
        ball  mug  paper   pen  pencil
blue     6.0  NaN    NaN   6.0     NaN
green    NaN  NaN    NaN   NaN     NaN
red      NaN  NaN    NaN   NaN     NaN
white   20.0  NaN    NaN  20.0     NaN
yellow  19.0  NaN    NaN  19.0     NaN


