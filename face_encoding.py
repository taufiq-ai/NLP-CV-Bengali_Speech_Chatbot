from face_recognition import load_image_file, face_encodings
from os import listdir
from pandas import DataFrame, read_csv


"""
1. Create a csv from where img paths can be fetched to encode
2. Save endoded img in csv or sqlite database, initially we can use csv file
3. Pass the endoded image to compare 

"""


# Create csv file with contains train image's path and label
def create_img_csv(users_img_path:str, user_img_csv_path: str):
    """
    :@ params
    users_img_path: path to the directory which contains images of users, here the "static/image/users/" path contains images of users and the image name has been written with user nama
    user_img_csv_path: the path where the created csv file will be saved.
    """
    
    img_files = [] # path
    img_names = [] # user name or label

    for img_file in listdir(users_img_path):
        img_files.append(users_img_path+img_file)
        name = img_file.split('.')[0] #split the image file in dot(.); As the file name has been written as username.extention, it will get user's name
        img_names.append(name)
    # print(img_files)
    # print(img_names)

    # Create pandas daraframe
    df = DataFrame(
        
        {
            'img_path' : img_files,
            'img_label': img_names
        }
    )
    # print(df)
    df.to_csv(user_img_csv_path, index=False) #save dataframe to csv file




# encode images and save to csv

def img_encode(user_img_csv_path: str, user_encoded_img_csv_path: str):
    """
    :@ params
    user_img_csv_path: the path where the created csv file will be saved.
    user_encoded_img_csv_path: path where the csv file of encoded image will be saved
    """
    df = read_csv(user_img_csv_path)
    known_face_encodings = []
    known_face_names = []
    for i in range(len(df)):
        user_image_path = df['img_path'][i]
        user_name = df['img_label'][i]
        known_face_names.append(user_name)
        # print(f"User: {user_name}, Img Path: {user_image_path}")

        # Load a sample picture and learn how to recognize it.
        img_loading = load_image_file(user_image_path)
        # print(img_loading)

        img_encoding = face_encodings(img_loading)[0]
        # print(face_encodings(img_loading))

        known_face_encodings.append(img_encoding)
    #     print(img_encoding)
    #     print()
    # print(known_face_names)
    # print(known_face_encodings)

    # Create pandas daraframe
    df = DataFrame(   
        {
            'user': known_face_names,
            'encoded_img' : known_face_encodings
        }
    )
    # print(df)
    df.to_csv(user_encoded_img_csv_path, index=False) #save dataframe to csv file

    return known_face_encodings, known_face_names


# users_img_path = "static/image/users/"
# user_img_csv_path = "database/user_image.csv"
# user_encoded_img_csv_path = "database/encoded_img.csv"

# known_face_encodings, known_face_names = img_encode(user_img_csv_path, user_encoded_img_csv_path)


# fetch dataset of encoded image to get encoded img and user name
# user_encoded_img_csv_path = "database/encoded_img.csv"
# df = read_csv(user_encoded_img_csv_path, index_col= False)
# known_face_encodings, known_face_names = list(df['encoded_img']), list(df['user'])
# print(known_face_names)

# print(known_face_encodings[0])

# img_encode(user_img_csv_path, user_encoded_img_csv_path)

# df = read_csv(user_img_csv_path)
# known_face_encodings = []
# known_face_names = []
# for i in range(len(df)):
#     user_image_path = df['img_path'][i]
#     user_name = df['img_label'][i]
#     known_face_names.append(user_name)
#     print(f"User: {user_name}, Img Path: {user_image_path}")

#     # Load a sample picture and learn how to recognize it.
#     img_loading = load_image_file(user_image_path)
#     img_encoding = face_encodings(img_loading)[0]
#     known_face_encodings.append(img_encoding)
#     print(img_encoding)
#     print()

# # fetch dataset of encoded image to get encoded img and user name
# user_encoded_img_csv_path = "database/encoded_img.csv"
# df = read_csv(user_encoded_img_csv_path, index_col= False)
# known_face_encodings, known_face_names = list(df['encoded_img']), list(df['user'])
# # print(known_face_encodings)


# for i in known_face_encodings:
#     print(i)