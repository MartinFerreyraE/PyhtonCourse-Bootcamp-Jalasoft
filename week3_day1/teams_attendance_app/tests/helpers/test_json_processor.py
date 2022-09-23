from teams_attendance_app.src.helpers.json_processor import generate_filename

def generate_another_type_of_file():
    result = generate_filename(filename="arguments", extension="csv")
    print(result)
    assert not result, 'expected new file'
