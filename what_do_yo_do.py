#base_camp_dict = {
#    'Glen Evans': 'co-founder',
#    'Kagan Coughlin': 'co-founder',
#    'Bethany Cooper': 'founding trustee',
#    'Sage Nichols': 'founding trustee',
#    'Carla Lewis': 'trustee',
#    'Sean Anthony': 'director',
#    'Nate Clark': 'technical director',
#    'Adam Tutor': 'Graduated 2017',
#    'Addey Welch': 'Graduated 2017',
#    'Dustin Buice': 'Graduated 2017',
#    'Eddrick Butler': 'Graduated 2017',
#    'Jacob Spence': 'Graduated 2017',
#    'James Hakim': 'Graduated 2017',
#    'James Sibert': 'Graduated 2017',
#    'Keegan Faustin': 'Graduated 2017',
#    'Martin Guzman': 'Graduated 2017',
#    'Milttreonna Owens': 'Graduated 2017',
#    'Nicole Shelton': 'Graduated 2017',
#    'Ricky Keisling': 'Graduated 2017',
#    'Alexandra Fortner': 'Graduated 2018',
#    'Edgar Guzman': 'Graduated 2018',
#    "Jo'Tavious Smith": 'Graduated 2018',
#    'Jose Vargas': 'Graduated 2018',
#    'Lizeth Buenrostro': 'Graduated 2018',
#    'Maegan Avant': 'Graduated 2018',
#    'Osvaldo Quinonez': 'Graduated 2018',
#    'Sara Hester': 'Graduated 2018',
#    'Trey Shelton': 'Graduated 2018',
#    'Valente Alvarez': 'Graduated 2018',
#    'Angel Zapata': 'Graduated 2018',
#    'Cole Anderson': 'Graduates 2019',
#    'Logan Harrell': 'Waste Technician',
#    'Timothy Bowling': 'Graduates 2019',
#    'Desma Hervey': 'Graduates 2019',
#    'Ginger Keys': 'Graduates 2019',
#    'Matt Lipsey': 'Graduates 2019',
#    'Myeisha Madkins': 'Graduates 2019',
#    'Henry Moore': 'Graduates 2019',
#    'John Morgan': 'Graduates 2019',
#    'Irma Patton': 'Graduates 2019',
#    'Danny Peterson': 'Graduates 2019',
#    'Jakylan Standifer': 'Graduates 2019',
#    'Justice Taylor': 'Graduates 2019',
#    'Ray Turner': 'Graduates 2019',
#    'Cody van der Poel': 'Graduates 2019',
#    'Andrew Wheeler': 'Graduates 2019'
#}

#base_camp_dict = {
#    'co-founder': {'Glen Evans', 'Kagan Coughlin'},
#    'Founding Trustee': {'Bethany Cooper', 'Sage Nichols'},
#    'Trustee': {'Carla Lewis'},
#    'Director': {'Sean Anthony'},
#    'Technical Director': {'Nate Clark'},
#    'Graduated 2017': {
#        'Adam Tutor', 'Addey Welch', 'Dustin Buice', 'Eddrick Butler',
#        'Jacob Spence', 'James Hakim', 'James Sibert', 'Keegan Faustin',
#        'Martin Guzman', 'Milttreonna Owens', 'Nicole Shelton',
#        'Ricky Keisling'
#    },
#    'Graduated 2018': {
#        'Alexandra Fortner', 'Edgar Guzman', "Jo'Tavious Smith"
#        'Jose Vargas', 'Lizeth Buenrostro', 'Maegan Avant', 'Osvaldo Quinonez',
#        'Sara Hester', 'Trey Shelton', 'Valente Alvarez', 'Angel Zapata'
#    },
#    'Graduates 2019': {
#        'Cole Anderson'
#        'Timothy Bowling', 'Desma Hervey', 'Ginger Keys', 'Matt Lipsey',
#        'Myeisha Madkins', 'Henry Moore', 'John Morgan', 'Irma Patton',
#        'Danny Peterson', 'Jakylan Standifer', 'Justice Taylor', 'Ray Turner',
#        'Cody van der Poel', 'Andrew Wheeler'
#    },
#    'Waste Technician': {'Logan Harrell'}
#}

from collections import defaultdict


def create_dictionary(file1):
    with open(file1, 'r') as file:
        lines = file.readlines()
    dictionary = defaultdict(set)
    for line in lines:
        name, job = line.strip().split(',')
        dictionary[job].add(name)
    return dictionary


def enter_name(dictionary):
    while True:
        name = input('Name Please? ')
        if name == 'quit':
            return None
        for job, people in dictionary.items():
            if name in people:
                return job
        print("Who dat?")


def main():
    print(create_dictionary('Names_and_jobs.txt'))
    base_camp_dict = create_dictionary('Names_and_jobs.txt')
    name = enter_name(base_camp_dict)
    if name:
        print(name)


main()