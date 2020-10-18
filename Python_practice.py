counties = ["Arapahoe","Denver","Jefferson"]
if counties[0] != 'Jefferson':
    print(counties[2])

temperature = int(input("What is the temperature outside ? "))
if temperature > 80:
   print("Turn on the AC.")
else:
   print("Open the Window.")

#What is the score?
score = int(input("What is your test score?"))

#Determine the grade
if score >=90:
    print('Your grade is an A.')
else:
    if score >= 80:
        print('Your grade is a B.')
    else:
        if score >=70:
            print('Your grade is a C.')
        else:
            if score>=60:
                print('Your grade is a D.')
            else:
                print('Your grade is an F.')

if "Arapahoe" in counties: 
    print("Arapahoe is in the list of counties")
else:
    print("Arapahoe is not in the list of counties")

# Condition control Loop
x = 0

while x <= 5:
    print(x)
    x = x + 1
for county in counties:
    print(counties)

#new example
for num in range(5):
    print(num)

#example 2
for i in range(len(counties)):
    print(counties[i])

#Get the Keys of a Dictionary

#example 3
counties_dict={'Arapahoe':422829,'Denver':463353,'Jefferson':432438}
#use for loop to get key name in counties_dict
for county in counties_dict.keys():
    print(county)
#use for loop to get key values in counties_dict method 1
for voters in counties_dict.values():
    print(voters)
#use for loop to get key values in counties_dict method 2
for county in counties_dict:
    print(counties_dict[county])
#use for loop to get key values in counties_dict method 3
for county in counties_dict:
    print(counties_dict.get(county))
#use for loop to get key values in pairs
for county,voters in counties_dict.items():
    print(county,voters)  

#List of dictionaries exercise
voting_data = []
voting_data.append({"county":"Arapahoe","registered_voters":422829})
voting_data.append({"county":"Denver","registered_voters":463353})
voting_data.append({"county":"Jefferson","registered_voters":432438})

#Get Each Dictionary in a List of Dictionaries method 1
for counties_dict in voting_data:
    print(counties_dict)
#Get Each Dictionary in a List of Dictionaries method 2
for i in range(len(voting_data)):
    print(voting_data[i])
#Get the Values in a List of Dictionaries
for counties_dict in voting_data:
    for value in counties_dict.values():
        print(value)
#How do we retrieve the numbers of registered voters from each dictionaries
for counties_dict in voting_data:
    print(counties_dict['registered_voters'])
#if we only want to print county name
for counties_dict in voting_data:
    print(counties_dict['county'])

counties_dict = {"Arapahoe": 369237, "Denver": 413229, "Jefferson": 390222}
#printing format
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered_voters.")
#Use f-string
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registerd voters.")

    
