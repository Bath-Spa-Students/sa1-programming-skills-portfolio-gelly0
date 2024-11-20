# Loops
e = 2
while e < 5:
  print(e)
  e += 2

 # Infinite Loop With Break Statement 
a = 1
while a < 6:
  print(a)
  if a == 3:
    break
  a += 1   

  colors= ["red", "blue", "yellow"]
  for x in colors:
    print(colors)
  
# Using the range Function with the for Loop
for x in range(0,12):
      print (x)

for x in range(12):
     print (x)

for x in range(0,20):
      print (x, end= " ,")

for x in range (0,10,2):   
   print(x ,end= ",")

# Nested Loop
topic = ["Maths","English","Physics"]
topic.pop(2)
print(topic)