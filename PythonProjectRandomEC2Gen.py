#Week 13 EC2 Random Name Generator Project

print ("Initialize EC2 Random Name Generator")

#Identify Department/Area
dept = input ("i.e Home/Office, Computers, Audio-Visual, Software\n")

#Valid Department/Areas

while True:
    try:
        list = ["Home/Office", "Computers" "Audio-Visual" "Software"]
        if dept not in list:
            raise Error
        break
    
    except ValueError
        print ("Access to the Rando Name Generator has been denied")
        
        print ("Acknowledged")
        
    #Generate Random EC2 Names
    while True
    try:
        instnumb = int(input("Define number of instance names")) 
        print ("Acknowledged" + str(instnub) + ("random EC2 names initialized."))
        print ("Any:")
        break
    except Error:
        print("This response is invalid. Please redefine your desired parameters")
        continue
    else:
        break
    
    #Generate characters synonymous with department names
    import string
    import random
    n = instnumb
    N = 4
    
    for _ in range (n):
        custom_id = str(''.join([random.choice(string.ascii_letters + string.digits) for instumb in range(10)]))
        
        print ("Confirming use of EC2 Random Name Generator. Success.")
