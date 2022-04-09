import pandas
import json

sheet: pandas.DataFrame = pandas.read_excel("Abiball Bestellungen.ods", sheet_name="Bestellungen", engine="odf")

dict = {}

for index, row in sheet.iterrows():
    ticket = {
        "name": row["Vorname"] + " " + row["Nachname"],
        "age": str(row["Alter zum Zeitpunkt des Abiballs "]),
        "food": str(row["Essenspräferenz und Unverträglichkeiten"]),
        "student_name": row["Vorname.1"] + " " + row["Nachname.1"],
    }

    dict[str(row["Bestell-ID"])] = ticket

# Open file and write to it
with open("data.json", "w") as f:
    f.write(str(json.dumps(dict)))