import configparser
import os
config = configparser.RawConfigParser()
config_file_path = os.path.join(os.path.dirname(__file__), "..", "Configurations", "config.ini")
config.read(config_file_path)
print(f"Config file path: {config_file_path}")
print("Sections found in config file:", config.sections())

class ReadConfig:

    @staticmethod
    def get_application_url():
        url = config.get('common data', 'baseURL')
        return url

    @staticmethod
    def get_email():
        email = config.get('common data', 'email')
        return email

    @staticmethod
    def get_password():
        password = config.get('common data', 'password')
        return password
