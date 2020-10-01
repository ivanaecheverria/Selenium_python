# ADVANCE SET OPERATIONS
# difference()

friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

local_friends = friends.difference(abroad)
print(f"The local friends are {local_friends}.")

# union()

local = {"Rolf"}
total_friends = local.union(abroad)
print(f"The total friends are {total_friends}.")

#intersection

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = { "Bob", "Jen", "Adam", "Anne"}

both = art.intersection(science)
print(f"Intersection between Art and Science is {both}.")




