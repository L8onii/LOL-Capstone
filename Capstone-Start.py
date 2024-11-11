#Capstone Project Notes

# Creating Venv (Within Bash)
python -m venv venv

# Activate Venv
# Choose the right code based on OS
source venv/Scripts/activate #windows
source venv/bin/activate #MacOS & Linux


# Installing Jupyter & Pandas
pip install notebook
pip install pandas

# Importing in Jupyter notebook
import pandas as pd

# Importing champions to df
df = pd.read_csv("C:/Users/15024/Desktop/Capstone/data/champions.csv",)

# Importing Season data and seperates ';' so columns can be used. Without removal of ';' only 1 long column with ';' Change seasons by changing 12-XX.csv
df1 = pd.read_csv("C:/Users/15024/Desktop/Capstone/data/Season-12/12-20.csv",sep=';',)

# Dropping Columns
df1.drop(['Class', 'Tier', 'Trend'], axis=1, inplace=True)

print(df1)

# Sort By change 'Wins' to another column name
wins_df1 = df.sort_values(by='Wins', ascending=False)

print(wins_df1)

# Close Venv
deactivate