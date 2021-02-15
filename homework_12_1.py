class MyTime:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @classmethod
    def myTime_input_str(cls, arg):
        x = str(arg)
        hours = int(x[0:2])
        minutes = int(x[2:4])
        seconds = int(x[4:6])
        return cls(hours, minutes, seconds)


    def __add__(self, other):  # addition (X + Y)
        return MyTime(self.hours + other.hours, self.minutes + other.minutes, self.seconds + other.seconds)

    def __mul__(self, other):  # multiplication (X * Y)
        return MyTime(self.hours * other.hours, self.minutes * other.minutes, self.seconds * other.seconds)

    def __sub__(self, other):  # subtraction (X - Y)
        return MyTime(self.hours - other.hours, self.minutes - other.minutes, self.seconds - other.seconds)

    def __eq__(self, other):  # X == Y
        return self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds

    def __ne__(self, other):  # X != Y
        return self.hours != other.hours and self.minutes != other.minutes and self.seconds != other.seconds

    def __ge__(self, other):  # X >= Y
        return self.hours >= other.hours and self.minutes >= other.minutes and self.seconds >= other.seconds

    def __le__(self, other):  # X <= Y
        return self.hours <= other.hours and self.minutes <= other.minutes and self.seconds <= other.seconds

    def __lt__(self, other):  # X < Y
        return self.hours < other.hours and self.minutes < other.minutes and self.seconds < other.seconds

    def __gt__(self, other):  # X > Y
        return self.hours > other.hours and self.minutes > other.minutes and self.seconds > other.seconds

    def __str__(self):
        if self.seconds > 60:
            self.minutes += self.seconds // 60
            self.seconds -= 60 * (self.seconds // 60)
        if self.minutes > 60:
            self.hours += self.minutes // 60
            self.minutes -= 60 * (self.minutes // 60)
        if self.hours > 24:
            self.hours = self.hours % 24
        return '{}:{}:{}'.format(self.hours, self.minutes, self.seconds)

clock_1 = MyTime()
print(clock_1)
clock_2 = MyTime.myTime_input_str(52343)
print(clock_2)
clock_3 = MyTime(12, 32, 5)
print(clock_3)
clock_4 = clock_1
print(clock_4)