# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# import mysql.connector

# path = 'C:/Users/Avinash/Desktop/Programmes/Resources/Raw'

# df = pd.read_csv(path + '/accident.csv')


# conn = mysql.connector.connect(
#     host = 'localhost',
#     user = 'Analyst',
#     password = '',
#     database = 'world_layoffs'
# )

# cursor = conn.cursor()

# # Prepare a list of tuples for the batch insert
# data = [tuple(row) for row in df.itertuples(index=False)]

# # Batch insert using executemany() for efficiency
# sql = "INSERT INTO your_table_name (column1, column2, column3) VALUES (%s, %s, %s)"
# cursor.executemany(sql, data)
# conn.commit()

# cursor.close()
# conn.close()