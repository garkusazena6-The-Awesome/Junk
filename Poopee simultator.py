import random
class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 1
        self.alive = True
    def to_study(self):
        print("Time to study!")
        self.progress += 0.20
        self.gladness -= 3
    def to_sleep(self):
        print("GO TO SLEEP")
        self.gladness +=3
    def to_chill(self):
        print("Alr you can chill for now")
        self.gladness +=5
        self.progress -= 0.2
    def is_alive(self):
        if self.progress <= -0.5:
            print("He cant take anymore , he..hangs himself.")
            self.alive = False
        elif  self.progress <= 0.01:
            print("He fells..depressing..")
            self.alive = False
        elif self.progress >= 5:
            print("He made it!")
            self.alive = False
    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress,2)}")
    def live(self,day):
        day = "Day" + str(day) + "For" + self.name + "Live"
        print(f"{day:=^50}")
        choose = random.randint(1,3)
        if choose == 1:
            self.to_study()
        elif choose == 2:
            self.to_sleep()
        elif choose == 3:
            self.to_chill()
        self.is_alive()
        self.end_of_day()
oleksandr = Student(name="Oleksandr")
for day in range(365):
    if oleksandr.alive == False:
        break
    oleksandr.live(day)

