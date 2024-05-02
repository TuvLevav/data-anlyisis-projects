import pandas as pd

# Create a DataFrame
df = pd.DataFrame({'Column1': ['Value1', 'Value2', 'Value3'],
                   'Column2': ['Value4', 'Value5', 'Value6'],
                   'Column3': ['Value7', 'Value8', 'Value9']})

# New row data
new_row = pd.Series(['New Value 1', 'New Value 2', 'New Value 3'], index=df.columns)

# Append the new row to the DataFrame
df = df.append(new_row, ignore_index=True)

print(df)
