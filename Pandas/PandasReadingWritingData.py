We will be seeing I/O APIs (a set of function) available with pandas library. These functions are divided into 2 categories ::

Readers ::            
read_csv                            
read_excel
read_hdf
read_sql
read_json
read_html
read_stata
read_clipboard
read_pickle
read_msgpack
read_gbq

Writers ::
to_csv
to_excel
to_hdf
to_sql
to_json
to_html
to_stata
to_clipboard to_pickle
to_msgpack (experimental) to_gbq (experimental)

>>> import os
>>> os.chdir('/Users/sankar.biswas/Desktop/AI:ML docs/Notebooks/InputFiles')

>>> csvFrame = pd.read_csv('input.txt')
>>> csvFrame
   white  red  blue  green animal
0      1    5     2      3    cat
1      2    7     8      5    dog
2      3    3     6      7  horse
3      2    2     8      3   duck
4      4    4     2      1  mouse

If you want to use separator for your input file ::

>>> csvFrame = pd.read_table('input.txt', sep = ',')
>>> csvFrame
   white  red  blue  green animal
0      1    5     2      3    cat
1      2    7     8      5    dog
2      3    3     6      7  horse
3      2    2     8      3   duck
4      4    4     2      1  mouse

# generally first line of the input file is considered as the header, but if you would like to not do that, you would have to 
# specify that, so by default column names will be specified

>>> csvFrame = pd.read_csv('input.txt', header= None)
>>> csvFrame
       0    1     2      3       4
0  white  red  blue  green  animal
1      1    5     2      3     cat
2      2    7     8      5     dog
3      3    3     6      7   horse
4      2    2     8      3    duck
5      4    4     2      1   mouse

# or you can give your own headers while importing the dataset (removing the header from the input file)
>>> csvFrame = pd.read_csv('input.txt', names = ['white','red','blue','green','animal'])
>>> csvFrame
   white  red  blue  green animal
0      1    5     2      3    cat
1      2    7     8      5    dog
2      3    3     6      7  horse
3      2    2     8      3   duck
4      4    4     2      1  mouse

# Hierarchical structure in index 
input data :: 
color,status,item1,item2,item3
black,up,3,4,6
black,down,2,6,7
white,up,5,5,5
white,down,3,3,2
white,left,1,2,1
red,up,2,2,2
red,down,1,1,4


>>> csvFrame1 = pd.read_csv('input2.txt', index_col = ['color', 'status'])
>>> csvFrame1
              item1  item2  item3
color status                     
black up          3      4      6
      down        2      6      7
white up          5      5      5
      down        3      3      2
      left        1      2      1
red   up          2      2      2
      down        1      1      4
      
# Using RegExp to Parse TXT Files : many a times you would end up having an input file the separator oh which is not well 
# defined, in such cases we can define 

