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


# load files from .json
students = OpenFile.read_file('students', 'json')
rooms = OpenFile.read_file('rooms', 'json')

# append students to rooms_list
student_dict = JoinRoomsAndStudents.make_student_dict(students)
rooms_list = JoinRoomsAndStudents.join_students_to_rooms(rooms, student_dict)

# write rooms_list to file .xml
WriteFile.write_to_file('full_rooms', 'xml', rooms_list)

# or write rooms_list to file .json
WriteFile.write_to_file('full_rooms', 'json', rooms_list)
