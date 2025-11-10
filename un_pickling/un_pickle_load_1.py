#program for Reading Emp Values from Key Board and save them as Record in File
#By using Pickling Operation
#EmpPickEx1.py
import pickle
def read_record():
    try:
        with open("D:\\Python\\FilesIO_Pickle_Module\\pickling\\emp.pick", "rb") as fp:
            record = pickle.load(fp)
            print(record, type(record))
            record = pickle.load(fp)
            print(record, type(record))
            record = pickle.load(fp)
            print(record, type(record))
            record = pickle.load(fp)
            print(record, type(record))
            # record = pickle.load(fp)
            # print(record, type(record))  #    record = pickle.load(fp) # EOFError: Ran out of input

    except FileNotFoundError:
        print("File not found")

read_record()