# Interacting with Databases
==============================================================================================================================
The pandas.io.sql module provides a unified interface independent of the DB, called sqlalchemy. This interface simplifies the 
connection mode, since regardless of the DB, the commands will always be the same. To make a connection you use the 
create_ engine() function. With this feature you can configure all the properties necessary to use the driver, as a user, 
password, port, and database instance.

Oracle SQL :: 

from sqlalchemy import create_engine
import pandas as pd

oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{IP}:{port}/{SID}'

engine = create_engine(
    oracle_connection_string.format(
        username='user',
        password='password',
        hostname='IP',
        port='1981',
        database='SID',
    )
)

data = pd.read_sql("SELECT * FROM SNoah", engine)
