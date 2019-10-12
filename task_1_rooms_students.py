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


class JoinRoomsAndStudents():
    """
    Append data of one list with data of another list
    """

    @staticmethod
    def make_student_dict(students_list):
        """
        Returns dictionary, made of specified list
        """
        student_dict = {}

        for i in students_list:
            student_dict.setdefault(str(i['room']), []).append(i)

        return student_dict

    @staticmethod
    def join_students_to_rooms(rooms_list, student_dict):
        """
        Returns list with appended data of dictionary
        """
        for i in rooms_list:
            i['students'] = student_dict.get(str(i['id']))

        return rooms_list
