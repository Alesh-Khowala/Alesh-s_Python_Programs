#Grades_page = {
#'alesh':"A+",
#'arnab':"A"
#}

#user_input=input("Please enter a student's name: ")

#print(Grades_page.get(user_input,"student grade not found"))

#student_name_page = {
#'alesh':{'Math':'A','Sci':'A+','Reading':'A+','Soc_Studies':'A','Writing':'A+'},

#'arnab':{'Math':'B+','Sci':'A','Reading':'A','Soc_Studies':'B+','Writing':'A+'}

#}

student_sub = {'Alesh': {'math': 'A', 'Reading': 'A+', 'sci': 'A'},
          'Arnab': {'math': 'A++', 'Reading': 'A', 'sci': 'A'}}



print(student_sub.get('Alesh').get('math'))