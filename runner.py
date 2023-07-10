from students import *

# student = Student("Steve", "E45")
# print(student)

# student.talk()

# student.say_favourite_language("Python")

from teams import *

team1 = Team("TeamTesters", ["Paul", "Mike", "Dave", "Sara"], "Papa Smurf")

print(team1.players)

print(team1.has_player("Paul"))
print(team1.has_player("Papa Smurf"))

team1.play_game(True)
print(team1.points)