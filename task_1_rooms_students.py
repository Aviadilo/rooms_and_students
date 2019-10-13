import json


class ReadingData():
    """
    Open file with specified format, save file data to variable and return the variable
    """

    @staticmethod
    def read_file(file_name, file_format):
        with open('{}.{}'.format(file_name, file_format), 'r') as f:
            text_file = json.load(f)
        return text_file


class WritingData():
    """
    Write data to file with specified format
    """

    @staticmethod
    def write_to_file(file_name, file_format, text):
        with open('{}.{}'.format(file_name, file_format), 'w') as f:
            json.dump(text, f)


class JoiningData():
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


rooms_path = input('Enter file name containing rooms data')
rooms_format = input('Enter file format containing rooms data')
students_path = input('Enter file name containing students data')
students_format = input('Enter file format containing students data')
joined_path = input("Enter new file name with joined data")
joined_format = input("Enter new file format with joined data")


# read files
students = ReadingData.read_file(students_path, students_format)
rooms = ReadingData.read_file(rooms_path, rooms_format)

# append students to rooms_list
student_dict = JoiningData.make_student_dict(students)
rooms_list = JoiningData.join_students_to_rooms(rooms, student_dict)

# write rooms_list to file
WritingData.write_to_file(joined_path, joined_format, rooms_list)
