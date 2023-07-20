########  How Do You Check The Presence Of A Key In A Dictionary?  ##########



d1 = {'a': 100, 'b': 200, 'c':300,'x': 20}
i = 'g' and 'a'

if i in d1:
    print("Key present,", end=" ")
    print("value is=",d1[i])
else:
    print("not present")
