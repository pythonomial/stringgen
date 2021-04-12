import random, sys, time
letters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()_-+={[}]|\:;'<,>.?/~`" 
while True:
  length = int(input("""
  Input length of string: """))
  print("  Your string is generating: ")
  for x in range(length):
      sys.stdout.flush()
      sys.stdout.write(random.choice(letters))
      time.sleep(0)
