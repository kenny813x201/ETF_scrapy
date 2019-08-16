import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


class Firebase_connection():

    cred = credentials.Certificate(
        'etf-au-firebase-adminsdk-3d0yf-9a9839e0c5.json')
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    etf_ref = db.collection('etf')

    def add_doc(self, etf_dict):
        self.etf_ref.document(etf_dict['ticker']).set(etf_dict)
        print(etf_dict['ticker'], "added")

    def update_doc(self, etf_dict):

        ticker = etf_dict['ticker']
        doc_ref = self.etf_ref.document(ticker)
        doc_ref.update(etf_dict)
        print(ticker, "updated")

    def check_doc_exist(self, etf_dict):
        ticker = etf_dict['ticker']
        return self.etf_ref.document(ticker).get().exists
