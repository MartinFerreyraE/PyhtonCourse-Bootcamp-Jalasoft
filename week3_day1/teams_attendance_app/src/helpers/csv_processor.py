import csv
import  os
import codecs
from datetime import datetime

path = '\\home\\teams_attendance_app\\attendace_reports\\09162022\\meetingAttendanceReport(General).csv'

def csv_filesreader():
        f = open(path, "r")
        for i, line in enumerate(f):
            if i == 1:
                participants = line
                print(participants)
            elif i == 2:
                meeting = line
                print(meeting)
            elif i == 3:
                start_time = line
                print(start_time)
            elif i == 4:
                end_time = line
                print(end_time)
            elif i > 4:
                break
        return participants, meeting, start_time, end_time
    
def main():
    csv_filesreader()

main()
