import os
import time
import datetime
import pipes
from dotenv import load_dotenv
from pathlib import Path


env_path = Path("/home/ubuntu/bro/.env")
load_dotenv(dotenv_path=env_path)

DB_HOST = os.getenv("db_hostname")
DB_USER = os.getenv("db_username")
DB_USER_PASSWORD = os.getenv("db_password")
DB_NAME = os.getenv("db_name")
BACKUP_PATH = '/home/ubuntu/environment/backups'


DATETIME = time.strftime('%Y%m%d - %H%M%S')
TODAYBACKUPPATH = BACKUP_PATH + '/' + DATETIME
todaypath = '/' + DATETIME

os.chdir(BACKUP_PATH)
try:
    # os.stat(TODAYBACKUPPATH)
    os.stat(todaypath)
except FileNotFoundError:
    print(os.getcwd())
    os.mkdir(TODAYBACKUPPATH)
    os.chdir(TODAYBACKUPPATH)
print(TODAYBACKUPPATH)
print("*************")
print(todaypath)

# print("Checking for databases names file.")
# if os.path.exists(DB_NAME):
#     file1 = open(DB_NAME)
#     multi = 1
#     print("Databases file found...")
#     print("Starting backup of all databases listed in file" + DB_NAME)
# else:
#     print ("Databases file not found...")
#     print ("Starting backup of " + DB_NAME)
#     multi = 0
    
    
# if multi:
#     in_file = open(DB_NAME,"r")
#     flength = len(in_file.readlines())
#     in_file.close()
#     p = 1
#     dbfile = open(DB_NAME, "r")
    
#     while p <= flength:
#         db = dbfile.readline()
#         db = db[:-1]
#         dumpcmd = "mysqldump -h" + DB_HOST + " -u " + DB_USER + " - p" + "" + db + " > " +  pipes.quote(TODAYBACKUPPATH) + "/" + db + ".sql"
#         os.system(dumpcmd)
#         gzipcmd = "gzip " + pipes.quote(TODAYBACKUPPATH) + "/" + db + ".sql"
#         os.system(gzipcmd)
#         p = p + 1
#     dbfile.close()
    
# else:
db = DB_NAME
#print(db)
# dumpcmd = f'mysqldump --databases {DB_NAME} -h {DB_HOST} -u {DB_USER} -p ">" {DB_NAME}.sql'
dumpcmd = f'mysqldump -h {DB_HOST} -u {DB_USER} -p {DB_NAME} --password={DB_USER_PASSWORD} > {DB_NAME}.sql'
print(dumpcmd)
os.system(dumpcmd)
gzipcmd = "gzip " + pipes.quote(TODAYBACKUPPATH) + "/" + db + ".sql"
# gzipcmd = "gzip " + pipes.quote(todaypath) + "/" + db + ".sql"
print(f"\n\t{gzipcmd}")
os.system(gzipcmd)
    
print("")
print("Backup script completed")
print("Your backups have been created in '" + TODAYBACKUPPATH + "' directory")


