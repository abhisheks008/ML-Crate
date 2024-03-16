# importing libraries
import cv2 as cv
import os
import numpy as np
import cv2.aruco as aruco
# import matplotlib.pyplot as plt

# Creating list of all dictionary to make sure all the markers get detected
dic_list = [
    aruco.DICT_4X4_50,
    aruco.DICT_4X4_100,
    aruco.DICT_4X4_250,
    aruco.DICT_4X4_1000,
    aruco.DICT_4X4_100,
    aruco.DICT_4X4_250,
    aruco.DICT_4X4_1000,
    aruco.DICT_4X4_100,
    aruco.DICT_4X4_250,
    aruco.DICT_4X4_1000,
    aruco.DICT_4X4_100,
    aruco.DICT_4X4_250,
    aruco.DICT_4X4_1000,
    aruco.DICT_4X4_100,
    aruco.DICT_4X4_250,
    aruco.DICT_4X4_1000,
    aruco.DICT_5X5_50,
    aruco.DICT_5X5_100,
    aruco.DICT_5X5_250,
    aruco.DICT_5X5_1000,
    aruco.DICT_6X6_50,
    aruco.DICT_6X6_100,
    aruco.DICT_6X6_250,
    aruco.DICT_6X6_1000,
    aruco.DICT_7X7_50,
    aruco.DICT_7X7_100,
    aruco.DICT_7X7_250,
    aruco.DICT_7X7_1000,
    aruco.DICT_ARUCO_ORIGINAL,
    aruco.DICT_APRILTAG_16h5,
    aruco.DICT_APRILTAG_25h9,
    aruco.DICT_APRILTAG_36h10,
    aruco.DICT_APRILTAG_36h11,
]


# Path to the folder 
folder_path = "Dataset"

# Initializing aruco dictionary
aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_250)

# Initializing detector parameters
parameters = aruco.DetectorParameters_create()


# Accessing each image 
for image_item in os.listdir(path= folder_path):


    img_path = os.path.join(folder_path, image_item)
    img = cv.imread(str(img_path))

    img = cv.resize(img, (250, 250), interpolation=cv.INTER_AREA)
    
    #Creating copy of the image
    img_copy = img

    cv.waitKey(0)

    # Got the image now converting it to grayscale
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    aruco_ids = set()

    for dic in dic_list:
        aruco_dict = aruco.Dictionary_get(dic)
        corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
        
        if ids is not None:
            aruco.drawDetectedMarkers(img, corners, ids)

            # Adding ids to the set
            ids = np.ravel(ids)
            for id in ids:
                aruco_ids.add(id)

    # print(f"""
    # corners = {corners}
    # ids = {ids}
    # rejected = {rejectedImgPoints} 
    # """)

    if not aruco_ids:
        print("Not able to detect.")
    else: 
        print(f"Detected Ids: {aruco_ids}")

    # Displaying the marked image
    cv.imshow("Original Image", img_copy)
    cv.imshow('ArUco Marked Image', img)
    # cv.waitKey(0) 
    # Break the loop when 'q' key is pressed
    if cv.waitKey(0) & 0xFF == ord('q'):
        break