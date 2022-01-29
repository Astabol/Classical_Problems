def main():
    total_corners = int(input("Enter the Number of God:"))
    initial = 0
    while(1):
        #1st loop
        have = initial * 2 #flower get double after washing with water
        for j in range(1, have + 1):
            worship = j
            remaining = have - worship
            if(remaining  <= 0):
                break
            #after first loop calling function to iterate next loops
            rem = cornerLoops(worship, remaining, total_corners)
            # if(rem != None): #to see uncomment this
                # print("Remaining: ",initial,".",j,"====",rem)
            
            if(rem == 0): # return condition if remaining is zero then return
                return initial, worship, total_corners #returning initial position, worshiped Flowers, total corners or GOD
        initial += 1
            

def cornerLoops(worship, remaining, total_corenrs):
    for i in range(2, total_corenrs + 1):
        have = remaining * 2 #flower get double after washing with water
        remaining = have - worship
    if (remaining >= 0):
        return remaining
if __name__=="__main__":
    x, y, z = main()
    print("Initially you have to take:", x, "flowers and You have to worship:", y, "Flowers for", z, "corners")