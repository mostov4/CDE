bikes = ["my","by",'high']

names = ["string",1,0.2,[2,3]]

print(names[3][0])

## f string

messge = f"My type is {names[0]}"
print(messge)

for bike in bikes:
    print(f"I say {bike}")

del bikes[1]
print(bikes)

print(bikes.pop()) ## By default pops last element, index can be added.
print(bikes)

print(bikes.index("by"))

## Sorted sorts without actually sorting the list
## Sort manipulates the list 

"-".join(bikes)
print(bikes)
