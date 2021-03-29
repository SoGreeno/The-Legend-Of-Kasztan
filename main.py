import time
import random

print("The legend of kasztan 1.0v")
time.sleep(1)
print("Napisz a aby rozpocząć grę")

nazwaBohatera = "SoGreeno" # Nazwałem samego siebie jako defaultową nazwę bohatera. ...który nic nie robi.
koniecHistorii = "nie"
wyborGry = "none"
kasztany = 0
startgry = input("> ")

if startgry == "a": # Jeśli tu dam "a" or "A" to wtedy każda odpowiedź uruchamia if'a. excuse me what.
    print("Dawno (nie aż tak dawno) temu był legendarny mistrz kasztanów )
    time.sleep(2)     # Nie wiem dlaczego tutaj zatrzymuje pythona ale może poprostu usunę time.sleep i będzie ok.
    print("który rządził wszystkimi kasztanami na świecie.")
    time.sleep(2)
    print("Ale nadszedł dzień...")
    time.sleep(1.6) #tutaj też zatrzymuje. nie wiem dlaczego
    print("Gdzie Mistrz kasztanów został zwyciężony przez armię Anty-Kasztanową...")
    time.sleep(3)
    print("Wieśniacy potrzebowali bohatera. który pokona armię Anty-Kasztanową")
    time.sleep(3)
    print("A ten bohater był:")
    nazwaBohatera = input("> ") # z jakiegoś powodu tutaj zamiast nazwy jakiej wpisałeś pokazało "" dlaczego? bo nie dodałem na zmiennej która jest na linijce 8
    print(nazwaBohatera + ". Który pokona armię i uratuję wioskę Kukankowo.")
    print("-----------------------------------------------------------")
    koniecHistorii = "tak"
else:
    print("Błąd. Zmienna nie jest równa z if'em.") # orginalniej było "coś się zjebało dowidzenia dobranoc"
    
if koniecHistorii == "tak":
    print("Jesteś w wioscę Kukankowo. Co robisz?")
    print("a - Szukaj kasztany")
    print("b - Wejdź do sklepu")
    wyborGry = input("> ")
else:
    print("Błąd. Zmienna nie jest równa z if'em.")

if wyborGry == "a": # dlaczego to niedziała? 
    koniecHistorii = "nie"
    print("Szukasz kasztany wokół siebie...")
    time.sleep(5)
    kasztany += random.randint(0, 5)
    print(("Masz teraz") + kasztany + ("Kasztanów!")) 
    
    

    time.sleep(3)