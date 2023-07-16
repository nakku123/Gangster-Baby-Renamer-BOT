import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "9439609")

API_HASH = os.environ.get("API_HASH", "3a64962f1face2fc285d0bb72587b139")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6344069829:AAHhElUz1o8zcNRmDF8FmvTLAAoPu1XJcuo") 

FORCE_SUB = os.environ.get("FORCE_SUB", "-1001805053423") 

DB_NAME = os.environ.get("DB_NAME","Rename")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://mithunkrishna:mithunkrishna@rename.xcxgov0.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/6abb0b1f3338755017cff.jpg https://graph.org/file/97afb9f4979168eb90c9a.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '2112711926').split()]

PORT = os.environ.get("PORT", "8080")
