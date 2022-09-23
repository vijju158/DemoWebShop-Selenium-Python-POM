import configparser

#config=configparser.ConfigParser()
#config.read("..\\Configurations\\config.ini")


path_config_file = "./Configurations/config.ini"
config=configparser.RawConfigParser()
##config = configparser.ConfigParser()
config.read(path_config_file)

"""
config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")"""

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return url

    @staticmethod
    def getUseremail():
        username=config.get('common info','useremail')
        return username

    @staticmethod
    def getPassword():
        password=config.get('common info','password')
        return password

