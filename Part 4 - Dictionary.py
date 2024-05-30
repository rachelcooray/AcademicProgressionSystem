#I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
#Any code taken from other sources is referenced within my code solution.
#UoW Student ID: w19564441
#IIT Student ID: 20220493
#Date: 13/12/2022

#PART 1

#Initialising variables, lists, tuple and dictionary
staff_or_student = ''
student_id_list = []
credits_dictionary = {}

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

    
#PART 4 

def dictionary():
    '''
    This function adds the key:value pairs of student_id:progression and credits.
    '''
    
    print('\nPart 4 - Dictionary:\n')
    for i in range (0,len(complete_list)):
        credits_dictionary[student_id_list[i]] = ','.join(complete_list[i]) #Adds the progression and credits 
    for j in credits_dictionary:
        print("{}:  {}".format(j,credits_dictionary[j])) #Prints the dictionary without curly brackets{} 



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
    elif staff_or_student == 1:
        dictionary()
    
    
def get_id():
    '''
    This function gets the student's ID.
    Format of the student ID is 'wxxxxxxx'.
    '''
    
    student_id = input("\nPlease enter the student ID in the format 'wxxxxxxx':")

    if student_id.lower()[0] != 'w' or len(student_id) != 8 or student_id[1:8].isdigit() == False:
        print('Invalid format for Student ID entered.') #Validate format of Student ID entered
        get_id()
    elif student_id in student_id_list:
        print(f'Entry for {student_id} already exists.')  #If the credits for a student is entered already it won't be appended to the list.
        get_id()
    else:
        student_id_list.append(student_id) #The student ID is appended to the list.
            

def validation_of_credits():
    '''
    This function validates the range, type and total of credits.
    Range of credits: (0, 20, 40, 60, 80, 100, 120)
    Type of credits: Integer
    Total of credits: 120
    '''
    
    global credits_pass, credits_defer, credits_fail

    get_id()
        
    while True:
        try:
            credits_pass = int(input('Please enter your credits at pass:')) #Prompt credits at pass
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
        student_id_list.pop()
        validation_of_credits()
        
    else:
        progression_outcome()

def multiple_outcomes():
    '''
    This function checks whether the user wants to quit or continue.
    '''
    
    print('\nWould you like to enter another set of data?')
    repeat = input("Enter 'y' for yes or 'q' to quit and view results:")
    
    if repeat.lower() == 'y' or repeat.lower() == 'yes':   #lower() option lowercases incase user enters uppercase characters
        validation_of_credits()
    elif repeat.lower() == 'q' or repeat.lower() == 'quit':
        dictionary()
    else: 
        print('That is an invalid option.')
        multiple_outcomes()
         
select_staff_student()












