from file_handling import ReadingData, WritingData
from joining_data import JoiningData
import argparse


def make_join(room_path, student_path, output_format):
    try:
        # read files
        students = ReadingData.read_file(student_path, 'json')
        rooms = ReadingData.read_file(room_path, 'json')

        # append students to rooms_list
        student_dict = JoiningData.make_student_dict(students)
        rooms_list = JoiningData.join_students_to_rooms(rooms, student_dict)

        # write rooms_list to file
        WritingData.write_to_file('result_join', output_format, rooms_list)

    except FileNotFoundError:
        print("You entered incorrect file name/path/format")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('room_path', type=str, help='Rooms-file path')
    parser.add_argument('student_path', type=str, help='Students-file path')
    parser.add_argument('output_format', type=str, help='Output-file format')
    args = parser.parse_args()

    make_join(args.room_path, args.student_path, args.output_format)


if __name__ == "__main__":
    main()
