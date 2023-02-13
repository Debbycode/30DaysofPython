print('=====================One=====================')


import datetime

now = datetime.datetime.now()

print("Current date and time: ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))
print("Current year: ", now.year)
print("Current month: ", now.month)
print("Current day: ", now.day)
print("Current hour: ", now.hour)
print("Current minute: ", now.minute)
print("Current timestamp: ", now.timestamp())


print('=====================Two=====================')

import datetime
current_date = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
print(current_date)


print('=====================Three=====================')

import datetime
date_string = "12/05/2019"
date_object = datetime.datetime.strptime(date_string, "%m/%d/%Y")
print("Time:", date_object)

print('=====================Four=====================')

import datetime
now = datetime.datetime.now()
new_year = datetime.datetime(now.year + 1, 1, 1)
difference = new_year - now
print("Time difference:", difference)


print('=====================Five=====================')

import datetime
now = datetime.datetime.now()
start = datetime.datetime(1970, 1, 1)
difference = now - start
print("Time difference:", difference)

print('=====================Six=====================')

print('''CALCULATING TIME DIFFERENCE - To calculate the difference between
two dates or times, such as the number of days between two dates
or the duration between two events.''')

print('''DATE AND TIME FORMATING - To format dates and times in a specific
way,such as converting a date to a string or vice versa.''')

print('''SCHEDULING- To schedule events or tasks, such as reminders,
appointments, or blog post publishing.''')





