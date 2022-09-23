import csv
import  os
import codecs
from datetime import datetime

path = '../attendace_reports/09162022/meetingAttendanceReport(General).csv'

def csv_filesreader():
       
    csv_dic = []
    results= []
    with open(path, 'rt', encoding='utf-16') as csvfile:
        csvReader = csv.reader(csvfile, delimiter='\t', quotechar='|')
        for row in csvReader:
            if row:
                csv_dic.append(row)
            else:
                break
    print(row)
    return results

def main():
    csv_filesreader()

main()