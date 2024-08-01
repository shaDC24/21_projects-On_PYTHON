#pip install schedule

import os
import shutil
import datetime
import schedule
import time


source_dir="D:/Krishna_CurrentTerm/Artificial Intelligence"
destination_dir="D:/Krishna_CurrentTerm/python/21_pythonProject/17_pythonAutomation"
def copy_folder_to_directory(src,dst):
    today=datetime.date.today()
    dst_dir=os.path.join(dst,str(today))
     
    try:
        shutil.copytree(src,dst_dir)
        print("Folder coipied to destination directory...")
    except FileExistsError:
        print(f"Folder already exists iun the destination : {dst}...")

schedule.every().day.at("17:39").do(lambda:copy_folder_to_directory(source_dir,destination_dir))       
# copy_folder_to_directory(source_dir,destination_dir)


while True:
   schedule.run_pending()
   time.sleep(60) 