import firebase_admin
from firebase_admin import credentials, auth, db

try:
    cred = credentials.Certificate("path/to/serviceAccountKey.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://la-for-me-default-rtdb.asia-southeast1.firebasedatabase.app/'
    })
    print("接続できました")
except Exception as e:
    print("接続に失敗しました: ", e)
