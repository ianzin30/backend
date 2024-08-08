import firebase_admin
from firebase_admin import firestore, storage, credentials, auth
import json
import os

class FirebaseClass():
    def __init__(self):
        cred = credentials.Certificate('./src/firebase/credentials.json')
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()
        # self.storage = storage.bucket()
        self.auth = auth
    
    def login_password(self, email:str, password:str):
        try:
            user_auth = self.auth.sign_in_with_email_and_password(email, password)
            
            user_ref = self.db.collection("users").document(user_auth["localId"])
            user_db = user_ref.get()
            if not user_db.exists:
                raise ValueError("User not found.")
            
            return user_db
        except Exception as e:
            raise e
    
    def get_activity(self, actID:str, name:str):
        actv = self.db.collection("activities").document(actID).get().to_dict()
        return actv
    
    def save_actv(self, actID, actvPath):
        try:
            with open (actvPath, "r") as actv:
                actv_json = json.load(actv)
            
            self.db.collection("activities").document(actID).set(actv_json)
        except Exception as e:
            raise e

firebase = FirebaseClass()

if __name__ == "__main__":

    firebase.save_actv("AC001PT_BR", "./activities/AC001PT_BR.json")
    print(firebase.get_activity("AC001PT_BR", "PAULINO"))