def catAndMouse(x,y,z):
    #check if the absolute difference between x and z is less than the absolute difference between y and z
    catA = abs(x-z)
    # if the condition is true, return "Catb"
    catB = abs(y-z)
    # check the if statement for the opposite condition
    if catA < catB:
        return "Cat A"
    # if the condition is true, return "Cat A"
    elif catA > catB:
        return "Cat B"
    # if the two conditions are equal, return "Mouse C"
    else:
        return "Mouse C"
        
if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        xyz = input().split()
        x = int(xyz[0])
        y = int(xyz[1])
        z = int(xyz[2])
        print(catAndMouse(x,y,z))
        