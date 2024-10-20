# import pandas as pd
# from sqlalchemy import create_engine, Table, Column, MetaData, Integer, String, Float, Date


# # Create a database connection string
# DATABASE_TYPE = 'mysql'
# DB_DRIVER = 'pymysql'
# USERNAME = 'Analyst'
# PASSWORD = '123456789asdf'
# HOST = 'localhost'
# PORT = '3306'
# DATABASE = 'world_layoffs'

# # Connection URL for SQLAlchemy
# connection_string = f"{DATABASE_TYPE}+{DB_DRIVER}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

# # Create the SQLAlchemy engine
# engine = create_engine(connection_string)

# # Test the connection
# try:
#     # Establish a connection to the database
#     with engine.connect() as connection:
#         print("Connection to the database was successful!")
# except Exception as e:
#     print(f"An error occurred while connecting to the database: {e}")

# # Load your data into a DataFrame
# df = pd.read_csv('C:/Users/Avinash/Desktop/Programmes/Resources/Raw/layoffs.csv')

# # Create the SQLAlchemy engine as before
# engine = create_engine(connection_string)

# # Create the table schema using SQLAlchemy if it doesn't exist
# metadata = MetaData()

# # Define the table
# layoffs_table = Table('layoffs', metadata,
#                       autoload_with=engine,
#                       autoload=True,
#                       schema='world_layoffs')

# with engine.connect() as connection:
#     for record in df.itertuples():
#         stmt = insert(layoffs_table)