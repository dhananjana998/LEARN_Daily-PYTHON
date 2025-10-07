import pandas as pd

# Use raw string (r) or double backslashes for Windows file path
dataFrame = pd.read_csv(r"C:\Users\User\Desktop\python_practice\sample\Book1.csv")

# Display the DataFrame
print(dataFrame)