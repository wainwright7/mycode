#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   For - Looping across a file opened with 'with'
         while also being gentle on memory consumption.
         Sort domains ending in .org and .com into files
         org-domain.txt and com-domain.txt."""

# open file in read mode
#with open("dracula.txt", "r") as foo:   
# for x in foo:
 #       print(x, end="")

#Loop over everyline

with open("dracula.txt", "r") as foo:
    count=0
    for y in foo:
     if "vampire" in y.lower():
         count += 1
         print(y)
    for z in foo:
        z = foo.rstrip('\n')

        if "vampire" in z.lower():
            with open ("vampiretimes.txt", "a") as vampy:
                vampy.write(z + "\n")

print(count)


   # print(count)
    

           


