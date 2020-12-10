from dotenv import load_dotenv
load_dotenv()

import os
db_name = os.environ.get("DBN")
token_id = os.environ.get("TKN")
usn = os.environ.get("USN")
psw = os.environ.get("PSW")
hst = os.environ.get("HST")