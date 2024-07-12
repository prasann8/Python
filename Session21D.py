from Session21C import MongoDBHelper
from Session21A import User
from bson.objectid import ObjectId # import 
from tabulate import tabulate
def main():

    print("Welcome to MongoDB Test App")
    dbHelper = MongoDBHelper()

    """
    user = User()
    user.add_user_details()
    document = vars(user)

    dbHelper.insert(document)
    """

    # query = {"email": "ben@example.com"}
    query = {"_id": ObjectId("668b8cac2e2eded2146a7834")}
    users = dbHelper.fetch(query)
    for user in users:
        print(user)

    print(tabulate(users, tablefmt='grid'))

if __name__ == "__main__":
    main()