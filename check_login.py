
def check(username,password):
    fhand = open("C:\\Users\\Danny\\Documents\\RealEstate\\RealEstate\\AdminLogin.txt",mode='r')
    for line in fhand:
        user_txt,pass_txt=line.split("|")
        if(user_txt!=username):
            continue
        if(password==pass_txt.strip()):
            return 1
        else:
            fhand.close()
            return 0
    else:
        fhand.close()
        return 0

