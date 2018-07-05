from random import choice, shuffle
students = [
    'Cole Anderson', 'Timothy Bowling', 'Desma Hervey', 'Ginger Keys',
    'Matt Lipsey', 'Myeisha Madkins', 'Henry Moore', 'John Morgan',
    'Irma Patton', 'Danny Peterson', 'Jakylan Standifer', 'Justice Taylor',
    'Ray Turner', 'Cody van', 'Andrew Wheeler', 'Logan Harrell'
]


def wed_fri_odd_jobs(lis, day):
    lis.append('{} Classroom Floor Sweep'.format(day))
    lis.append('{} Hallway Floor Sweep'.format(day))


jobs = []
for i in 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday':
    jobs.append('{} lunch set-up and clean'.format(i))
    if i == 'Friday':
        wed_fri_odd_jobs(jobs, i)
        jobs.append('{} Kitchen Clean'.format(i))
        jobs.append('{} Stairways Sweep'.format(i))
        for num in range(1, 3):
            jobs.append('{} Bathroom Clean {}'.format(i, num))
    if i == 'Wednesday':
        wed_fri_odd_jobs(jobs, i)
for i in 'Kitchen', 'Classroom':
    jobs.append('Daily {} + Trash Checks'.format(i))
jobs.append('Daily Inspections and Friday Wipe Down')


def dictionary_creation(jobs, students):
    shuffle(students)
    dictionary = dict(zip(jobs, students))
    return dictionary


def main():
    dictionary = dictionary_creation(jobs, students)
    for key, value in dictionary.items():
        print('{}: {}'.format(key, value))


main()