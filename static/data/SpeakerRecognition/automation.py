import os 
import shutil

train_dirs = "static/data/SpeakerRecognition/train/"
test_dirs = "static/data/SpeakerRecognition/test/"

def make_test_dir():
    for dir in os.listdir(train_dirs):
        print(dir)
        os.mkdir(test_dirs+dir)

# # define the path to the file and the source and destination directories
# file_path = "path/to/file"
# src_dir = "path/to/source/directory"
# dest_dir = "path/to/destination/directory"

# # check if the file exists in the source directory
# if os.path.exists(os.path.join(src_dir, file_path)):
#     # use shutil.move to cut the file and paste it into the destination directory
#     shutil.move(os.path.join(src_dir, file_path), os.path.join(dest_dir, file_path))
#     print("File successfully cut and pasted to destination directory.")
# else:
#     print("File does not exist in source directory.")
