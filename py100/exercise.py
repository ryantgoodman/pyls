# some code will go here

# Loop on Command
while True:
  print("Should I stop looping?")
  answer = input().lower().strip()
  if answer == "yes":
    break
  else:
    print("Answer yes to stop looping")