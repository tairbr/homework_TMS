import datetime
from time import sleep, strftime, localtime


class Pomodoro:

    def __init__(self, name, last_name, task_name, number_of_cycles=4):
        self.name = name
        self.last_name = last_name
        self.task_name = task_name
        self.number_of_cycles = number_of_cycles
        self.count = 1

    def run_pomodoro(self, x=25, y=5):
        with open('log_homework_14_2.txt', 'a') as my_file:
            my_file.writelines(f'{strftime("%x - %X", localtime())} - Program launch - {self.name} {self.last_name}\n')
        while True:
            if self.number_of_cycles > 1:
                self.time_to_focus(x)
                self.break_length(y)
                self.number_of_cycles -= 1
                self.count += 1
            elif self.number_of_cycles == 1:
                self.time_to_focus(x)
                self.number_of_cycles -= 1
                self.count += 1
            else:
                break

    def time_to_focus(self, minutes=25):
        with open('log_homework_14_2.txt', 'a') as my_file:
            my_file.writelines(
                f'           {strftime("%X", localtime())} - Working time - {minutes}min - task name:{self.task_name}\n')
        self.time = datetime.datetime(1, 1, 1, hour=0, minute=minutes, second=0, microsecond=0, tzinfo=None)
        while self.time.minute * 60 + self.time.second > 0:
            print(f'Cycle №{self.count} - time to work - {self.time.strftime("%M:%S")}')
            self.time -= datetime.timedelta(seconds=1)
            sleep(1)

    def break_length(self, minutes=5):
        with open('log_homework_14_2.txt', 'a') as my_file:
            my_file.writelines(
                f'           {strftime("%X", localtime())} - Break length - {minutes}min\n')
        self.time = datetime.datetime(1, 1, 1, hour=0, minute=minutes, second=0, microsecond=0, tzinfo=None)
        while self.time.minute * 60 + self.time.second > 0:
            print(f'relaxation - {self.time.strftime("%M:%S")}')
            self.time -= datetime.timedelta(seconds=1)
            sleep(1)


test = Pomodoro('Dima', 'Radchenko', 'Pomodoro', 2)
test.run_pomodoro(1, 1)
