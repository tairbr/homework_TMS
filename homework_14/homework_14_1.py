import datetime
from time import sleep, strftime, localtime

print('Timer program ver.1.0')
name_input = input('Enter name:')
last_name_input = input('Enter your last name:')
print(f"{name_input} {last_name_input} let's set a timer ")
hour_input = int(input('Enter hour:'))
minutes_input = int(input('Enter minutes:'))
seconds_input = int(input('Enter seconds:'))


class Timer:

    def __init__(self, name, last_name, hour, minutes, seconds):
        self.name = name
        self.last_name = last_name
        self.time = datetime.datetime(1, 1, 1, hour=hour, minute=minutes, second=seconds, microsecond=0, tzinfo=None)

    def run_timer(self):
        with open('log_homework_14_1.txt', 'a') as my_file:
            my_file.writelines(f'{strftime("%x - %X", localtime())} - {self.name} {self.last_name}\n')
        while self.time.hour * 3600 + self.time.minute * 60 + self.time.second > 0:
            print(self.time.time())
            self.time -= datetime.timedelta(seconds=1)
            sleep(1)
        print('ALARM!!!!')


timer = Timer(name_input, last_name_input, hour_input, minutes_input, seconds_input)
timer.run_timer()
