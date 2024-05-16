import pandas as pd

# Load Table 1 
table1 = pd.read_csv('Table_Input.csv')

# Create HTML for Table 1
table1_html = table1.to_html(index=False, classes='table')

# Data for Table 2
A5 = pd.to_numeric(table1.loc[table1['Index #'] == 'A5', 'Value']).values[0]
A20 = pd.to_numeric(table1.loc[table1['Index #'] == 'A20', 'Value']).values[0]
A15 = pd.to_numeric(table1.loc[table1['Index #'] == 'A15', 'Value']).values[0]
A7 = pd.to_numeric(table1.loc[table1['Index #'] == 'A7', 'Value']).values[0]
A13 = pd.to_numeric(table1.loc[table1['Index #'] == 'A13', 'Value']).values[0]
A12 = pd.to_numeric(table1.loc[table1['Index #'] == 'A12', 'Value']).values[0]

# Calculate values for Table 2
alpha_value = A5 + A20
beta_value = A15 / A7
charlie_value = A13 * A12

# Create Table 2 as a DataFrame
table2 = pd.DataFrame({
    'Category': ['Alpha', 'Beta', 'Charlie'],
    'Value': [alpha_value, beta_value, charlie_value]
})

# Create HTML for Table 2
table2_html = table2.to_html(index=False, classes='table')

# Generate HTML Stuff
html_content = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Table Display</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 0;
            background-color: #f4f4f4;
        }}
        h2 {{
            color: #333;
        }}
        .table {{
            width: 100%;
            max-width: 800px;
            margin: 25px auto;
            border-collapse: collapse;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            background-color: #fff;
        }}
        th, td {{
            padding: 12px 15px;
            border: 1px solid #ddd;
            text-align: left;
        }}
        th {{
            background-color: #f4f4f4;
        }}
        tr:nth-child(even) {{
            background-color: #f9f9f9;
        }}
        tr:hover {{
            background-color: #f1f1f1;
        }}
    </style>
</head>
<body>
    <h2>Table 1</h2>
    {table1_html}
    <h2>Table 2</h2>
    {table2_html}
</body>
</html>
'''


with open('output.html', 'w') as f:
    f.write(html_content)

print("Job Complete.")
