import pandas as pd
 # extracts students
df = pd.read_json("students.json")

registries = set()
filtered_data = []

# checks for duplicate registration
for index, row in df.iterrows():
    registry = row["students"]["registry"]
    if registry not in registries:
        registries.add(registry)
        filtered_data.append(row)

if len(df) > len(filtered_data):
    print(f"{len(df) - len(filtered_data)} matrícula(s) duplicada(s) foi(foram) removida(s). Verifique a base de dados original por duplicações.")

# load students in CSV file
filtered_df = pd.DataFrame(filtered_data)
filtered_df.to_csv("students.csv", index=False)