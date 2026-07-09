tuples = ("chocolate", "mango", "noi")
print(tuples)print(tuples[2])
if "mango" in tuples:
    print("yes")
if "man" not in tuples:
    print("no")print(len(tuples))tuples.remove("noi")
tuples[2] = "banana"
print(tuples)