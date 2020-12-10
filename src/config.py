import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname('src/.env'), '.env')
load_dotenv(dotenv_path)

DBS = os.environ.get("DB_NAME")
USN = os.environ.get("USER_NAME")
PSW = os.environ.get("PASSWORD")
HST = os.environ.get("HOST")
PRT = os.environ.get("PORT")
TKN = os.environ.get("TOKEN")
print(DBS)
print(USN)
print(PSW)
print(HST)
print(PRT)
print(TKN)