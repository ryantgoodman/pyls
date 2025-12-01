# some code will go here
import random

class Conditionals:
# Yes? No? Part 2
# Use a ternary expressions
  @staticmethod 
  def yes_no_part_2():
    random_number = random.randint(0, 1)
    # depends on truthiness of random_number being 1 for truthy 0 for falsy
    message = "Yes!" if random_number else "No."
    print(message)
  @staticmethod
  def yes_no_part_1():
    random_number = random.randint(0 , 1)
    message = "Yes!" if random_number else "No."
    print(message)
  @staticmethod
  def check_the_weather_part_1(weather=""):
    if weather == "sunny":
      message = "It's a beautiful day!"
    elif weather == "rainy":
      message = "Grab your umbrella."
    else:
      message = "Let's stay inside."
    return message


if __name__ == "__main__":
  print(Conditionals.check_the_weather_part_1())
  print(Conditionals.check_the_weather_part_1("sunny"))
  print(Conditionals.check_the_weather_part_1("rainy"))