import json


class OpenFile():
    """
    Open file with specified format, save file data to variable and return the variable
    """

    @staticmethod
    def read_file(file_name, file_format):
        with open('{}.{}'.format(file_name, file_format), 'r') as f:
            text_file = json.load(f)
        return text_file


class WriteFile():
    """
    Write data to file with specified format
    """

    @staticmethod
    def write_to_file(file_name, file_format, text):
        with open('{}.{}'.format(file_name, file_format), 'w') as f:
            json.dump(text, f)
