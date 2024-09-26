#to get marks from user ,biggest of two numbers ,avg
a=int(input("enter a value"))
b=int(input("enter b value"))
c=int(input("enter c value"))
if (a>b and a>c):
 if(b>c):
   print("a and b is bigger")
   print("the avg of both is",(a+b)/2)
 else:
   print("a and c is bigger")
   print("the avg of both is",(a+c)/2)
elif (b>a and b>c):
  if(a>c):
   print("b and a is bigger")
   print("the avg of both is",(b+a)/2)
  else:
   print("b and c is bigger")
   print("the avg of both is",(b+c)/2)
else:
  if(a>b):
   print("a and c is bigger")
   print("the avg of both is",(a+c)/2)
  else:
   print("b and c is bigger")
   print("the avg of both is",(b+c)/2)
