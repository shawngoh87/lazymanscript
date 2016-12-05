import time

def init():
    hover(Pattern("1480910507966.png").targetOffset(-7,43))
    rightClick("1480910578984.png")
    click(Pattern("1480910578984.png").targetOffset(0,-170))
    time.sleep(2)
    click("1480910634159.png")
    type("192.168.10.1")
    type(Key.ENTER)

def systemPassword(id, password, newpass, bypass=False):
    time.sleep(1)
    click("1480911597347.png")
    #if exists(Pattern("1480911674806.png").targetOffset(-268,-4)) != None:
    #    click("1480911706764.png")
        
    time.sleep(3) 
    wait("1480918677729.png", 2)
    type(id)
    type(Key.TAB)
    type(password)
    click(Pattern("1480911937699.png").targetOffset(1,105))
    time.sleep(1)
    wheel(Pattern("1480913138269.png").targetOffset(59,166),WHEEL_DOWN, 2)
    time.sleep(1)
    click(Pattern("1480913344852.png").targetOffset(-202,-22))
    type(newpass)
    type(Key.TAB)
    type(newpass)
    click(Pattern("1480913452805.png").targetOffset(-291,7))
    wait("1480913475219.png", 2)
    click(Pattern("1480913475219.png").targetOffset(171,49))
    time.sleep(1)
    click(Pattern("1480913565600.png").targetOffset(146,3))
    click(Pattern("1480913581177.png").targetOffset(166,47))
    click(Pattern("1480913639789.png").targetOffset(-3,-13))
    wait("1480918359212.png",5)
    click("1480913668457.png")
    time.sleep(1)
    click(Pattern("1480913692013.png").targetOffset(-50,-54))
    type(id)
    type(Key.TAB)
    if bypass == True:
        type(password)
    else: type(newpass)
    click(Pattern("1480913753387.png").targetOffset(-15,96))
    if exists("1480913795685.png") != None:
        print("MODERATOR PASSWORD ERROR!!")
        click(Pattern("1480913838347.png").targetOffset(301,50))
        return False
    elif exists("1480918152411.png") != None:
        print("MODERATOR PASSWORD OK!!")
        click(Pattern("1480918201160.png").targetOffset(5,113))
        click(Pattern("1480918230067.png").targetOffset(174,50))
    click(Pattern("1480918752560.png").targetOffset(-4,-142))
    wait("1480918774448.png", 3)
    print("SYSTEM PASSWORD LOOP DONE!!")
    
def installerCheck():
    time.sleep(1)
    click("1480919286229.png")
    time.sleep(1)
    #try:
    #    wait("1480919309788.png", 3)
    #except:
    #    print("DOWNLOAD NOT STARTED/ TOO DAMN FAST")
    #    return False
    print("STARTED DOWNLOADING!!")
    wait("1480919405637.png", 10)
    print("FINISHED DOWNLOADING!!")
    click(Pattern("1480919524506.png").targetOffset(44,-1))
    print("DOWNLOAD CHECK COMPLETED")
    return True

def fileCheck(id, password, filename):
    time.sleep(1)
    click("1480923709757.png")
    wait("1480923765056.png", 5)
    type(id)
    type(Key.TAB)
    type(password)
    type(Key.ENTER)
    wait(Pattern("1480923789865.png").targetOffset(-125,6), 5)
    click(Pattern("1480923789865.png").targetOffset(-125,6))
    wait("1480923816523.png", 5)
    click("1480923816523.png")
    click("1480923864258.png")
    click("1480923882219.png")
    type(filename + ".txt")
    type(Key.ENTER)
    click(Pattern("1480923789865.png").targetOffset(140,6))
    click(Pattern("1480918230067.png").targetOffset(174,50))
    wait(Pattern("1480918752560.png").targetOffset(-4,-142), 5)
    click(Pattern("1480918752560.png").targetOffset(-4,-142))
    wait("1480918774448.png", 3)
    click("1480924343443.png")
    click(Pattern("1480924378510.png").targetOffset(-331,6))
    type(filename + ".txt")
    if exists("1480924620914.png") != None:
        click(Pattern("1480924620914.png").targetOffset(50,10))
    else: 
        print("FILE NOT FOUND")
        return False
    click(Pattern("1480924546842.png").targetOffset(366,81))
    try:
        wait("1480924728708.png", 10)
    except:
        print("DOWNLOAD NOT STARTED/ TOO DAMN FAST")
        return False
    print("FINISHED DOWNLOADING!!")
    click(Pattern("1480919524506.png").targetOffset(44,-1))
    print("DOWNLOAD CHECK COMPLETED")
    click("1480924841495.png")
    wait("1480918774448.png", 3)
    adminLogin(id, password)
    wait(Pattern("1480923789865.png").targetOffset(-125,6), 5)
    click(Pattern("1480923789865.png").targetOffset(-125,6))
    click("1480925684844.png")
    click(Pattern("1480925684844.png").targetOffset(228,62))
    click(Pattern("1480925721544.png").targetOffset(393,129))
    time.sleep(1)
    click(Pattern("1480913565600.png").targetOffset(146,3))
    click(Pattern("1480913581177.png").targetOffset(166,47))
    click(Pattern("1480913639789.png").targetOffset(-3,-13))
    wait("1480918359212.png",5)
    return True
    
def adminLogin(id, password):
    click("1480923709757.png")
    wait("1480923765056.png", 5)
    type(id)
    type(Key.TAB)
    type(password)
    type(Key.ENTER)
    time.sleep(1)
    
    
    
    
    
id = "admin"
password = "admin123"
newpass = "admin321"
filename = "ASDF"
init()
if exists("1480911392747.png") != None:
    click(Pattern("1480911437098.png").targetOffset(7,-1))
time.sleep(1)

# File Download/Upload Checking
fileCheck(id, password, filename)

# Installer Download Checking
for i in range(3):
    if installerCheck() == True:
        print(str(i+1) + " Done!")
    else:
        print(str(i+1) + " Error!")
    
# System Password vs Moderator Password Checking
systemPassword(id, password, newpass, bypass=False)
systemPassword(id, newpass, password, bypass=False)
systemPassword(id, password, newpass, bypass=False)
systemPassword(id, newpass, password, bypass=False)



    
