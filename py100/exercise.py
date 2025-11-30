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

if __name__ == "__main__":
  Conditionals.yes_no_part_2()