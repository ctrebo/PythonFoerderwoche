"""
Schreibe ein Programm, welches folgender Logik folgt:

Wenn der Wert kleiner als 3 ist, soll der Text "Der Wert ist kleiner als 3" ausgegeben werden.
Wenn der Wert genau 3 ist, soll der Text "Der Wert ist genau 3" ausgegeben werden.
Wenn der Wert größer als 3 ist, soll der Text "Der Wert ist größer als 3" ausgegeben werden.

"""
wert = 3

if wert<3:
    print("Der Wert ist kleiner als 3")
elif wert == 3:
    print("Der Wert ist genau 3")
else:
    print("Der Wert ist größer als 3")

