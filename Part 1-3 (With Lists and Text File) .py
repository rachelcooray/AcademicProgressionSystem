#I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
#Any code taken from other sources is referenced within my code solution.
#UoW Student ID: w19564441
#IIT Student ID: 20220493
#Date: 13/12/2022

#PART 1

#Initialising variables, tuple and list
staff_or_student = ''

credits_pass = 0
credits_defer = 0
credits_fail = 0

credits_range = (0, 20, 40, 60, 80, 100, 120) #Tuple includes the values that the credits can take

progress_count = 0
trailer_count = 0
retriever_count = 0
exclude_count = 0

complete_list = []

def select_staff_student():
    '''
    This function identifies whether the user is a Staff Member or Student.
    Staff Member is identified by '0'.
    Student is identified by '1'.
    '''
    
    global staff_or_student
    
    try:
        staff_or_student = int(input("Please enter '0' if you are a Staff Member and '1' if you are a Student:"))
    except ValueError:
        print('Integer required.')
        
    while staff_or_student == 0 or staff_or_student == 1:
        validation_of_credits()
        break
    else:
        print('That is invalid. Please try again.\n')
        select_staff_student()


def progression_outcome():
    '''
    This function prints the progression of a given student from the entered input credits and appends them to the complete list.
    '''
    
    global credits_pass, credits_defer, credits_fail
    global progress_count, trailer_count, retriever_count, exclude_count
    global staff_or_student
    
    if credits_pass == 120:
        progress_count += 1
        complete_list.append(['Progress                  -  ' + str(credits_pass), str(credits_defer), str(credits_fail)]) #Appends the progression and credits to the complete list
        print('Progress')
    elif credits_pass == 100:
        trailer_count += 1
        complete_list.append(['Progress (module trailer) -  '+ str(credits_pass), str(credits_defer), str(credits_fail)])
        print('Progress (module trailer)')
    elif credits_fail >= 80:
        exclude_count += 1
        complete_list.append(['Exclude                   -  '+ str(credits_pass), str(credits_defer), str(credits_fail)])
        print('Exclude')
    else:
        retriever_count += 1
        complete_list.append(['Module retriever          -  '+ str(credits_pass), str(credits_defer), str(credits_fail)])
        print('Module retriever')
    

    if staff_or_student == 0:
        multiple_outcomes()            


def validation_of_credits():
    '''
    This function validates the range, type and total of credits.
    Range of credits: (0, 20, 40, 60, 80, 100, 120)
    Type of credits: Integer
    Total of credits: 120
    '''
    
    global credits_pass, credits_defer, credits_fail
    
    while True:
        try:
            credits_pass = int(input('\nPlease enter your credits at pass:')) #Prompt credits at pass
            if credits_pass not in credits_range:   #Entered credits are out of range
                print('Out of range')
            elif credits_pass in credits_range:
                break
        except ValueError:  #Wrong data type entered
            print('Integer required')

    while True:
        try:
            credits_defer = int(input('Please enter your credits at defer:')) #Prompt credits at defer
            if credits_defer not in credits_range:  #Entered credits are out of range
                print('Out of range')
            elif credits_defer in credits_range:
                break
        except ValueError:  #Wrong data type entered
            print('Integer required')

    while True:
        try:
            credits_fail = int(input('Please enter your credits at fail:')) #Prompt credits at fail
            if credits_fail not in credits_range:   #Entered credits are out of range
                print('Out of range')
            elif credits_fail in credits_range:
                break
        except ValueError:  #Wrong data type entered
            print('Integer required')

    total_credits = credits_pass + credits_defer + credits_fail
    if total_credits != 120:    #Total of credits is incorrect
        print('Total Incorrect')
        validation_of_credits()
        
    else:
        progression_outcome()
    

def histogram():
    '''
    This function prints the histogram of progression outcomes with the total number of outcomes.
    '''
    
    print('-' * 65)
    print('Histogram\n')
    print(f'Progress {progress_count}  : {"*" * progress_count}')
    print(f'Trailer {trailer_count}   : {"*" * trailer_count}')
    print(f'Retriever {retriever_count} : {"*" * retriever_count}')
    print(f'Exclude {exclude_count}   : {"*" * exclude_count}')
    print('\n')
    print(f'{progress_count + trailer_count + retriever_count + exclude_count} outcomes in total.') #Total number of outcomes 
    print('-' * 65)
    

def multiple_outcomes():
    '''
    This function checks whether the user wants to quit or continue.
    '''
    
    print('\nWould you like to enter another set of data?')
    repeat = input("Enter 'y' for yes or 'q' to quit and view results:")
    
    if repeat.lower() == 'y' or repeat.lower() == 'yes':   #lower() option lowercases incase user enters uppercase characters
        validation_of_credits()
    elif repeat.lower() == 'q' or repeat.lower() == 'quit':
        histogram()
    else: 
        print('That is an invalid option.')
        multiple_outcomes()
         
select_staff_student()


#PART 2

def credits_lists():
    '''
    This function prints all the progressions stored in the complete_list.
    '''
    
    print('\nPart 2 - List: \n')
    for i in range (0,len(complete_list)):  # This for loop iterates through every item stored in complete_list
        print(','.join(complete_list[i]))   #Prints the list without square brackets[]

if len(complete_list) > 0:  
    credits_lists()        

            
#PART 3

def credits_text_file():
    '''
    This function creates a text file to write(store) all the progressions stored in the complete_list, reads it and prints it.
    '''
    
    print('\nPart 3 - Text File:\n')
    file_outcomes = open('Text File.txt', 'w')   #Opening a text file to write
    for i in range (0,len(complete_list)): #Iterate through the for loop to write each progression outcome in the text file
        file_outcomes.write(','.join(complete_list[i]))
        file_outcomes.write('\n')


    print('Text File Extension:\n')

    file_outcomes = open('Text File.txt', 'r')  #Opening a text file to read the data written to it
    text_files = file_outcomes.read()
    print(text_files)
    file_outcomes.close()   #Close text file
    
credits_text_file()


    




