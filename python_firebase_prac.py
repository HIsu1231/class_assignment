import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import pandas as pd

excel_filename = 'data.xlsx'
db_table_name = u'tongjin'

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

df = pd.read_excel(excel_filename, header=0)

for i in range(df.shape[0]):
    obj = {}

    for key in df.keys():
        value = df[key][i]
        if str(value).isnumeric():
            value = int(value)
        obj[key] = value

    db.collection(db_table_name).add(obj)