class JoiningData:
    """Append data of one list with data of another list"""

    @staticmethod
    def make_student_dict(students_list):
        """Returns dictionary, made of specified list"""
        student_dict = {}

        for i in students_list:
            student_dict.setdefault(str(i['room']), []).append(i)

        return student_dict

    @staticmethod
    def join_students_to_rooms(rooms_list, student_dict):
        """Returns list with appended data of dictionary"""
        for i in rooms_list:
            i['students'] = student_dict.get(str(i['id']))

        return rooms_list
