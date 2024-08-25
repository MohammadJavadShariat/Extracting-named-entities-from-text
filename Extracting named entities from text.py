#Lists of information
List_Name_Person = {'Farhad', 'Javad', 'Reza', 'Abbas', 'Rasoul'}
List_Family_Person = {'Saeidi', 'Javadi', 'Ebrahimi', 'Mohammadi', 'Ahmadi'}
List_City = {'Ilam', 'Urmia', 'Sanandaj', 'Mazandaran', 'Mashhad', 'Qom', 'Kermanshah'}
List_Univercity = {'Kurdistan', 'Razi', 'Azad', 'Sharif', 'Tehran'}
List_Expertise = {'AI', "NLP", '', 'C++', 'python', 'Java', 'Django', 'Flask', 'MATLAB'}

#Receive email
email = input('''Suggested text\n(Hello, have a good time, I was disturbed by your ad. My name is Abbas Saeedi, a computer engineering graduate from Tehran University. I live in Mashhad. 
And I have different specializations such as: NLP, C++, Django. Thank you for reading my diary and letting me know. Thank you very much.)\n\nEnter your text:''')

#Remove points from text
e_replac = email.replace(".","")

#Verbatim text
e_split = e_replac.split()

#Creating sets to store text keywords in them
name_person = set()
Family_Person = set()
City = set()
Univercity = set()
Expertise = set()

#Saving text keywords in sets
for i in e_split :
    for j in List_Name_Person :
        if i == j :
            name_person.add(i)
    for j in List_Family_Person :
        if i == j :
            Family_Person.add(i)
    for j in List_City :
        if i == j :
            City.add(i)
    for j in List_Univercity :
        if i == j :
            Univercity.add(i)
    for j in List_Expertise :
        if i == j :
            Expertise.add(i)

#If there is no keyword in the text, the replacement text will be shown
if len(name_person) == 0 :
    name_person.add("---non-existent---")
if len(Family_Person) == 0 :
    Family_Person.add("---non-existent---")
if len(City) == 0 :
    City.add("---non-existent---")
if len(Univercity) == 0 :
    Univercity.add("---non-existent---")
if len(Expertise) == 0 :
    Expertise.add("---non-existent---")

#Print the extracted keywords for the user
print(f"\n*******Summary of the text*******\n\nName: {name_person}")
print(f"Family: {Family_Person}")
print(f"City: {City}")
print(f"University: {Univercity}")
print(f"Experience and expertise: {Expertise}")