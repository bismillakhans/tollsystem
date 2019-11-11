# Main.py

import cv2
import numpy as np
import os

from tollsettings.detection import DetectChars
from tollsettings.detection import DetectPlates


import pytesseract

#pytesseract.pytesseract.tesseract_cmd = r"C:\\Users\\user\\AppData\\Local\\Tesseract-OCR\\tesseract.exe"




###################################################################################################
def detectPlate(image):
    blnKNNTrainingSuccessful = DetectChars.loadKNNDataAndTrainKNN()         # attempt KNN training
    config = ('-l eng --oem 1 --psm 3')
    if blnKNNTrainingSuccessful == False:                               # if KNN training was not successful
        print("\nerror: KNN traning was not successful\n")  # show error message
        return                                                          # and exit program
    # end if

    imgOriginalScene  = cv2.imread(image)               # open image

    if imgOriginalScene is None:                            # if image was not read successfully
        print("\nerror: image not read from file \n\n")  # print error message to std out                                # pause so user can see error message
        return                                              # and exit program
    # end if

    listOfPossiblePlates = DetectPlates.detectPlatesInScene(imgOriginalScene)           # detect plates

    # listOfPossiblePlates = DetectChars.detectCharsInPlates(listOfPossiblePlates)        # detect chars in plates

    # cv2.imshow("imgOriginalScene", imgOriginalScene)            # show scene image

    if len(listOfPossiblePlates) == 0:                          # if no plates were found
        print("\nno license plates were detected\n")  # inform user no plates were found
    else:                                                       # else
                # if we get in here list of possible plates has at leat one plate

                # sort the list of possible plates in DESCENDING order (most number of chars to least number of chars)
        listOfPossiblePlates.sort(key = lambda possiblePlate: len(pytesseract.image_to_string(possiblePlate.imgPlate,config=config)), reverse = True)

                # suppose the plate with the most recognized chars (the first plate in sorted by string length descending order) is the actual plate
        licPlate = listOfPossiblePlates[0]
        # for i in listOfPossiblePlates:
        #     cv2.imshow("imgThresh", i.imgPlate)
        #     cv2.waitKey(0)
        #     cv2.destroyAllWindows()
        # if len(licPlate.strChars) == 0:                     # if no chars were found in the plate
        #     print("\nno characters were detected\n\n")  # show message
        #     return                                          # and exit program
        # end if
    text = pytesseract.image_to_string(licPlate.imgPlate, config=config)
    out=''.join(e for e in text if e.isalnum())
    print("license plate read from image =",out)

    return out



















