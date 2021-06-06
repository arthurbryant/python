from datetime import timedelta, date

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        if(n % 7) == 0:
            yield start_date + timedelta(n)

i = 0
message = "Sorr for the last message. Please ignore it. This is Google Home. The Google Home Clean Schedule is as following:\n\n"
users = ['Michael', 'Arthur', 'Allan', 'Arthur']
start_date = date(2017, 12, 4)
end_date = date(2018, 3, 31)
for single_date in daterange(start_date, end_date):
    message += single_date.strftime("%Y-%m-%d(Monday)  ") + users[i] + "\n"
    i += 1
    if(i == len(users)):
        i = 0

print(message)
