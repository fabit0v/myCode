#!/usr/bin/env python3

message = "Can't figure out what to watch? "

movie = float(input("Choose a number between 1 and 50 "))

if movie >= 0:
    message = message + "How about Harry Potter?"

elif movie >=20:
    message = message + "How about Hobbit & LOR?"

elif movie >=40:
    message = message + "How about Chronicles of Narnia?"

elif movie <= 50:
    message = message + "How about Indiana Jones?"

else:
    message = message + "That number is out of bounds"
print(message)
