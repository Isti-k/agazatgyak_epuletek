

def feladat():
    Jatekos_neve=input("Kérlek, add meg a játékos nevét!")
    Szerepkor=input("Kérlek, add meg a szerepkört!")
    
    if "varázsló" in Szerepkor: 
        print(f"Üdvözlunk{Jatekos_neve},2 életed van")
    elif "harcos" in Szerepkor:
        print(f"Üdvözlünk{Jatekos_neve},10 élete van")
    else:
         print(f"üdvözlünk {Jatekos_neve} 8 élete van")






