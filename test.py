R= int(input("What is the R value of your color? (1-255)"))
G= int(input("What is the G value of your color? (1-255)"))
B= int(input("What is the B value of your color? (1-255)"))



def rbgtohex(rgb):

    hex = "#{:02x}{:02x}{:02x}".format(R,G,B)
    return hex
    print (hex)
    
rgbtohex(rgb)
