import os

Program = True
Zahl = 1

def bye():
    print("ok process finished...\nbye!")

def startsymbol():
    os.system('color b')
    print("""
/$$   /$$ /$$$$$$$$ /$$$$$$  /$$$$$$        /$$$$$$$$ /$$$$$$        /$$$$$$$  /$$   /$$  /$$$$$$ 
| $$  | $$| $$_____/|_  $$_/ /$$__  $$      |__  $$__//$$__  $$      | $$__  $$| $$$ | $$ /$$__  $$
| $$  | $$| $$        | $$  | $$  \__/         | $$  | $$  \ $$      | $$  \ $$| $$$$| $$| $$  \__/
| $$$$$$$$| $$$$$     | $$  | $$               | $$  | $$  | $$      | $$$$$$$/| $$ $$ $$| $$ /$$$$
| $$__  $$| $$__/     | $$  | $$               | $$  | $$  | $$      | $$____/ | $$  $$$$| $$|_  $$
| $$  | $$| $$        | $$  | $$    $$         | $$  | $$  | $$      | $$      | $$\  $$$| $$  \ $$
| $$  | $$| $$$$$$$$ /$$$$$$|  $$$$$$/         | $$  |  $$$$$$/      | $$      | $$ \  $$|  $$$$$$/
|__/  |__/|________/|______/ \______/          |__/   \______/       |__/      |__/  \__/ \______/ 
                                                                                                   
                                                                                                   
                                                                                                   
  /$$$$$$   /$$$$$$  /$$   /$$ /$$    /$$ /$$$$$$$$ /$$$$$$$  /$$$$$$$$ /$$$$$$$$ /$$$$$$$         
 /$$__  $$ /$$__  $$| $$$ | $$| $$   | $$| $$_____/| $$__  $$|__  $$__/| $$_____/| $$__  $$        
| $$  \__/| $$  \ $$| $$$$| $$| $$   | $$| $$      | $$  \ $$   | $$   | $$      | $$  \ $$        
| $$      | $$  | $$| $$ $$ $$|  $$ / $$/| $$$$$   | $$$$$$$/   | $$   | $$$$$   | $$$$$$$/        
| $$      | $$  | $$| $$  $$$$ \  $$ $$/ | $$__/   | $$__  $$   | $$   | $$__/   | $$__  $$        
| $$    $$| $$  | $$| $$\  $$$  \  $$$/  | $$      | $$  \ $$   | $$   | $$      | $$  \ $$        
|  $$$$$$/|  $$$$$$/| $$ \  $$   \  $/   | $$$$$$$$| $$  | $$   | $$   | $$$$$$$$| $$  | $$        
 \______/  \______/ |__/  \__/    \_/    |________/|__/  |__/   |__/   |________/|__/  |__/  
    """)

def convert(count):
    for f in os.listdir():
        if ".HEIC" in str(f):
            f = str(f)
            print("converting...")
            filename = "Bild_" + str(count) + ".png"
            os.rename(f, filename)
            count = count + 1

def filefound(f):
    files_found = '".HEIC"-Files were found!'
    Anzahl = f.count(".HEIC")
    print(Anzahl, files_found)
    Liste = os.listdir(os.getcwd())
    convert(Zahl)

startsymbol()
def search():
    list = os.listdir(os.getcwd())
    print("Searching:", os.getcwd())
    if ".HEIC" in str(list):
        list = str(list)
        filefound(list)
    else:
        print("No .HEIC-Files found in this Directory.\nquitting...")


while Program:
    X = input("Soll das Konvertieren in .png gestartet werden?\nJA[ENTER] oder Nein[N]")
    os.system('color A')
    if X == '':
        search()
    if X == 'N':
        bye()
    if X == 'n':
        bye()
    else:
        bye()
        Program = False








