#------------------------------------------------#
#Title: Pickling and Error Handling Demo
#Description: This script demonstrates error handling using try-except statements, and pickling in Python.
#ChangeLog: (Who,When,What)
#JGeigel, 5.29.2023,Created script
#------------------------------------------------#
import sys

#Try to import the pickle module and raise an exception if pickle is not available.
try:
    import pickle           #Try to import the pickle module
    print ("Imported the pickle module!\n")
except ImportError:
    print ("ERROR: Could not import the module.")  #Raise exception if import process fails
    sys.exit()

#Pickling demo below
#---------- Data ---------------------------------------------------------------------- #
# Declare variables and constants
filename = "ToDoList.txt"       #Name of text file with original data
list_from_file = []             #List for lines that will be extracted from file.
b_filename = "AppData.dat"      #Name of binary file for pickling/unpickling

#---------- Processing  --------------------------------------------------------------- #
def save_data(filename, list_from_file):
    """ Reads data from a file into a list
    :param filename: (string) with name of file:
    :param list_from_file: (list) you want filled with file data:
    :return: (list) of rows extracted from file
    """
    with open(filename) as file:
        for row in file:
            list_from_file += [row.strip()]
    file.close()
    return list_from_file

def dump_data(b_filename, list_from_file):
    """ Dumps data from a list into a binary file
    :param b_filename: (string) with name of the binary file:
    :param list_from_file: (list) filled with file data
    """
    b_file = open(b_filename,"ab")
    pickle.dump(list_from_file,b_file)
    b_file.close()

def read_data(b_filename):
    """ Loads data from a binary file into a list
    :param b_filename: (string) with name of binary file:
    :return: (list) of items loaded from binary file
    """
    b_file = open(b_filename, "rb")
    data = pickle.load(b_file)
    b_file.close()
    return data

#---------- Presentation  ----------------------------------------------------------- #
save_data(filename, list_from_file)    #Read data from ToDoList.txt
print('Extracted data from text file!\n')

dump_data(b_filename, list_from_file)   #Pickle data from ToDoList.txt into AppData.dat
print ('Pickled the data!\n')

data = read_data(b_filename)            #Unpickle data into list
print ('Unpickled the data!\n')
print("This is the data that was pickled and unpickled: " +'\n')
print (data,type(data))                 #Print list of unpickled items
