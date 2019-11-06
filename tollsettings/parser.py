from django.conf import settings

from tollsettings.detection import Main

class PlateParser(object):
    def __init__(self, file_upload):



        self.__details = {
            'name'              : None
        }
        self.__file_upload = file_upload
        self.__final =Main.detectPlate(file_upload)
        print(self.__final)


    def get_extracted_data(self):
        self.__details['name'] = self.__final
        return self.__details






