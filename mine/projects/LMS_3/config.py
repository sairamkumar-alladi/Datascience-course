# It holds all the configuration and global variables, constants required by the software.
# LMS = {}
# LMS['admin'] = [
#     {
#         "user":"sai",
#         "password":"sai@123"
#     }
# ]
# LMS['books'] = {}
# LMS['books']['CSE'] = {}
# LMS['books']['CSE']['1stYr'] = {}
# LMS['books']['CSE']['1stYr']['1stSem'] = [] #List of books of CSE,1styr, 1stsem.
# LMS['students'] = {}
# LMS['students']['CSE'] = {}
# LMS['students']['CSE']['1stYr'] = {}
# LMS['students']['CSE']['1stYr']['1stSem'] = [] #List of students of CSE,1styr, 1stsem.
# LMS['teachers'] = {}
# LMS['teachers']['CSE'] = [] #List of teachers.

# print(LMS)

department_mapper = {
    1 : "CSE",
    2 : "EEE"
}
year_mapper = {
    1 : "1stYr",
    2 : "2ndYr"
}
sem_mapper = {
    1: "1stSem",
    2: "2ndSem"
}