
#Boolean

friends = [ "Rolf", "Bob"]
abroad = [ "Rolf", "Bob"]

print(friends == abroad)
print(friends is abroad)
print(friends is friends)

#IF statements

day_of_week = input("What day of the week is it today?").lower()
if day_of_week == "monday":
    print("Have a great start to your week!")
elif day_of_week == "tuesday":
    print("it's tuesday")
else:
    print("full speed ahead!")

#IN keyword

friends = ["Rolf", "Bob", "Jen"]
print("Jen" in friends) # equals TRUE

movies_watched = {"The Matrix", "Green book", "Her"}
user_movie = input("Enter something you watched recently: ")
print(user_movie in movies_watched) 

#IF statements with IN keyword

if user_movie in movies_watched:
    print(f"I've watched {user_movie} too!")
else:
    print("I haven't watched that yet")