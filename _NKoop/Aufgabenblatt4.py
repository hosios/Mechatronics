# Benutzereingabe:
# name = input("Gib deinen Namen ein: ")
# 
# Loops:
# liste =[1, 2, 3, 4, 5]
# for element in liste:
#    print(element)
#------------------------------------------------------------------------notizen
# 
# 1 Wenn bei der Division (Teilen) der 3. Aufgabe, die eingelesene Zahl im Nenner steht (eingelesene_Zahl = input().... div = Zahl2 / eingelesene_Zahl), in welchem Fall schlaegt die Division dann fehl?
# Wenn durch 0 geteilt wird, entsteht ein Fehler.
# Wie kann durch eine Bedingung, dieser Fall verhindert werden? Schreibe dieses Programm.
zahl1 = int(input("Gib eine Zahl ein: \n"))
print("\n")
zahl2 = 10
print("Gib eine Zahl ein: "+ str(zahl1))

if zahl1 == 0:
    print("ERROR")
    print("Du hast eine Null eingegeben. Suche dir eine andere Zahl aus.")
else:
    print(zahl1/zahl2)
    print("Dieses ist das Ergebnis deiner Eingabe geteilt durch 10.")

# 2 Schreibe ein Programm, dass eine (beliebige) Frage ausgibt und dann eine Antwort des Benutzers abwartet.
#   Pruefe mihilfe einer Bedingung danach, ob die Frage richtig oder falsch beantwortet wurde und informiere den Benutzer mit der print-Funktion darueber.
Eingabe2 = input("Wie viel ist 1 + 1? \n")
print("\n")

if int(Eingabe2) == 2:
    print("Richtig!")
else:
    print("Falsch!")

# 3 Verbessere die Ausgabe des schnelleren Arbeiters aus der 3. Aufgabe in Aufgabenblatt2.
#   Verwende eine Bedingung, um unterschiedliche Ausgaben (print) im "Wenn" (if) und "Sonst" (else) Fall auszugeben.
# OPTION 1:
Anzahl_Steine = int(input("Gib die Steinanzahl ein: \n"))
print("\n")
t = 8

if Anzahl_Steine > 15:
    print("Arbeiter 1 ist schneller als Arbeiter 2, denn er trägt " + Anzahl_Steine/t + " Steine pro Stunde.")
else:
    print("Arbeiter 1 ist langsamer als Arbeiter 2, denn er trägt")
    print(Anzahl_Steine/t)
    print("Steine pro Stunde.")

# OPTION 2:
Stein = int(input("Wie viele Steine trägt Arbeiter 2 in 8 Stunden? \n"))
print("\n")
t = 8

if Stein > 15:
    print("Arbeiter 1 trägt mehr Steine, denn in 8 Stunden trägt er:")
    print(float(Stein/t))
else:
    print("Arbeiter 2 trägt mehr Steine, denn in 8 Stunden trägt er:")
    print(float(Stein/t))

# 3.3 Ist ein anderer Arbeiter, der 15 Steine am Tag, über eine Entfernung von 1km trägt schneller oder langsamer?
Steine2 = 15
s = 1
s_amTag = Steine2 * 2
s_pro_Tag = s * s_amTag
print("Arbeiter2 läuft " + str(s_pro_Tag) + "km am Tag")

V = 3.5
t2 = s_pro_Tag / V
print("Arbeiter2 insgesamt " + str(t2) + ("h am Tag gearbeitet"))
print("Die Aussage: Arbeiter2 ist schneller, ist: " + str(t2 < t))