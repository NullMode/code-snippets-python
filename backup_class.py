#!/usr/bin/python
import datetime
import os
import zipfile

#TODO
# Zip file output needs to contain just the taget folder not the whole path to the target folder

class Backup:
    def __init__(self, backup_name, output_folder, target_folder):
        self.backup_name = backup_name
        self.output_folder = output_folder
        self.target_folder = target_folder
        self.run()

    def zip_dir(self, path, zip_handle):
        print path
        if "\\" in path:
            targetpath = path.rstrip("\\").split("\\")[-1]
            print targetpath
        elif "/" in path:
            targetpath = path.rstrip("").split("/")[-1]
            print targetpath

        for root, dirs, files in os.walk(path):
            print root
            for file_name in files:
                zip_handle.write(os.path.join(root, file_name))

    def run(self):
        date_stamp = datetime.date.today().strftime("%Y-%m-%d")
        file_name = self.output_folder + "/" + date_stamp + "-" + self.backup_name + ".zip"

        zip_handle = zipfile.ZipFile(file_name, 'w')
        self.zip_dir(self.target_folder, zip_handle)
        zip_handle.close()
