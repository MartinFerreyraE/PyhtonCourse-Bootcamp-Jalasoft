## app entry point

from helpers import data_processor

from helpers.data_processor import enter_dates

import json

from helpers.json_processor import write_file, generate_filename


def user_inputs(question):

    meeting = input('\nPlease enter the meeting name:')
    start_input, end_input = enter_dates()
 
    arguments = {
        'Question': question,
        'Meeting name': meeting,
        'Start date': start_input,
        'End date': end_input   
        }

    # print(arguments['Meeting name'])

    if question == '1':
        print('Question 1')
    elif question == '2':
        print('Question 2')
    else:
        exit

    # json_data = json.dumps(arguments)
    # print(json.loads(json_data)['Meeting name'])

    return arguments, question

def process_question():
    
    print('Hello, type 1 or 2 to select a question ("q" to exit')
    print('- What is the number of participants attending Python Training per date, date filter between 9/9/2022 and 9/16/2022?\n')
    print('- What is the Meeting duration of Python Training per date, date filter between between 9/9/2022 and 9/16/2022\n')
    
    question = input().lower()

    return question
       

def main():

    question = process_question()
    
    if(question == 'q'):
        exit

    arguments = user_inputs(question)

    data = json.dumps(arguments, indent = 4)
    print(data)

    filename = generate_filename(filename="JSON")

    write_file(filename, data)
    
main()