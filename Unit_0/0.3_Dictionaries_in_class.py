##Slide 2
# people = {'Jon': 'Lawyer', 'Susan': 'Programmer', 'Robert': 'Bank Manager', 'Tanya': 'Engineer'}
# print(people[0]) # Can't access dictionary values by index
from gc import get_referents

# people['Bob'] = 'Builder'
# print(people)
#
# people['Jon'] = 'Teacher'
# print(people)

##SLide 3
# pass #This will give an error because dictionaries are not ordered (can't access by index)


# people = {'Jon': 'Lawyer', 'Susan': 'Programmer', 'Robert': 'Bank Manager', 'Tanya': 'Engineer', 'Jon':'Teacher'}
# print(people)

##Slide 4
# fords = {'Ford': 'Mustang', 'Ford': 'Fusion', 'Ford': 'F150', }
# print(fords)
#
# fords = {'Ford':['Mustang', 'Fusion'], 'Chevy':['Silvarado', 'Camaro']}
# print(fords)

##Slide 5
import faker

fake_id = faker.Faker() #Genearte a fake_id
profile = dict(fake_id.profile()) #Get a profile information from the fake id data set
print(profile)
"""
Example profile
{'job': 'Hydrographic surveyor', 'company': 'Murphy-Perez', 'ssn': '220-15-5415', 'residence': 'PSC 6499, Box 2373\nAPO AE 66777', 'current_location': (Decimal('-80.038062'), Decimal('51.104383')), 'blood_group': 'A-', 'website': ['https://perkins.org/', 'http://www.hays.biz/'], 'username': 'mary94', 'name': 'Jennifer Davenport', 'sex': 'F', 'address': '05755 Walsh Mission Suite 675\nSinghberg, OR 40960', 'mail': 'austinerin@hotmail.com', 'birthdate': datetime.date(1969, 10, 9)}
"""

##Slide 6
# print(profile['name']) ##Access the value corresponding to a key
# print(profile['Name']) #Gives an error because age is not a key in the dictionary

# print(profile.get('Name')) # Returns None because 'Name' is not a valid key
# print(profile.get('name'))


##Slide 7
# profile_keys = profile.keys() # Get all the keys
# print(profile_keys)
# print(type(profile_keys))
# print(profile_keys[0]) # Can't access specific key by its index (TypeError)
# profile_keys = list(profile_keys) # convert all the keys to a list
# print(profile_keys)
# print(profile_keys[0])

# profile_values = profile.values()
# print(profile_values)
#
# profile_items = profile.items()
# print(profile_items)
# profile_items = list(profile_items)
# print(profile_items)
# print(profile_items[0])

##Slide 8
#Loop all the keys
# for key in profile.keys():
#     print(key)


#Loop all the values
# for value in profile.values():
#     print(value)




#Loop all the keys/value pairs and display as a tuple
# for item in profile.items():
#     print(item)
#
# for key, value in profile.items():
#     print((key, value))



##Slide 9
#Add entries to a dictionary
# print(profile.get('nickname'))
# profile['nickname'] = "Champ"
# print(profile)


##Remove an entry by specifying a key
# profile.pop('username')
# print(profile)



##Slide 10 - Your turn
# me = {}
# me['name'] = 'my_name'


##Slide 11
#Given a list of classes and a list of grades create a dictionary that links the data together
courses = ['Trigonometry', 'Physics', 'Programming', 'English 2']
grades = [85, 94, 98, 80]

gradebook = {}

## Loop through the index of each course and associate the course as the key at that index to the grade as the value at the same index to the gradebook
for i in range(len(courses)):
    gradebook[courses[i]] = grades[i]
print(gradebook)

for course in courses:
    gradebook[course] = grades

## Look at both the index AND the Element from a list
for i, course in enumerate(courses):
    gradebook[course] = grades[i]



#Find the average grade of all the classes
print(gradebook)
average_grade = sum(gradebook.values())/len(gradebook.values())
print(average_grade)



##Slide 12
my_string = 'Hello, how are you'



##Slide 13 - Practice 1
"""Your task:Create a new dictionary that removes ‘ssn’, ‘blood_group’, and ‘birthdate’ from the previous dictionary and moves 
it into the new dictionary. Write the new dictionary into a variable called ‘private_data’
"""
profile = {'job': 'Clinical embryologist', 'company': 'Garcia and Sons', 'ssn': '101-48-3433', 'residence': '115 White Field Suite 854\nPort Josephmouth, NC 77328', 'current_location': (-18.7254755, -86.461244), 'blood_group': 'A-', 'website': ['https://wade-williams.com/', 'http://flores.com/'], 'username': 'arroyosusan', 'name': 'Donna Gonzalez', 'sex': 'F', 'address': '8086 Warner Inlet Suite 223 New Jack, WI 37965', 'mail': 'milesjessica@yahoo.com', 'birthdate': (1922, 1, 30)}
print(profile)

private_data = {}
ssn = profile.pop('ssn')
private_data['ssn'] = ssn
print(profile)
print(private_data)


##Slide 14 - Practice 2
'''Your Task: Create a new dictionary that contains only the dictionary entries that are greater then 50.  
Start with the code below that generates a random numbers between 1 and 100 for every letter of the alphabet.
Then write a script that creates a new dictionary with key-value that have the value data greater then 50.'''

# from random import randint
# numbers = {}
# for i in range(ord('a'), ord('a')+26):
#     numbers[chr(i)] = randint(1,100)
#
# print(numbers)