import time # import de 'time' library, voor time.sleep()
import os # import os (operating system), voor os.system('clear')

print('Hoeveel verdien je bruto per maand?') # print vraag naar console over hoeveel de gebruiker verdient per maand (bruto)
inkomen = float(input('Ik verdien per maand bruto: €')) # geef een regel voor de gebruiker om een antwoord in te vullen, maak hier een float van, en sla op in de variabele 'inkomen'

dertiendeMaand = input('Heb je een dertiende maand? (j/n): ') # vraag of de gebruiker een dertiende maand bonus krijgt, sla antwoord op in de variabele 'dertiendeMaand'


print('\x1b[3;37;40mBerekenen...\033[0m') # laat gebruiker weten dat de computer bezig is met berekenen, gebruik ANSI escape code voor schuingedrukte tekst


def jaarloonFormule(maandloon): # maak een functie 'jaarloonFormule()', met als parameter 'maandloon'
  global jaarloon # zorg ervoor dat de variabele 'jaarloon' globaal te gebruiken is (in de gehele code)
  if dertiendeMaand == 'j': # check of 'dertiendeMaand' gelijk staat aan 'j', voer code uit als dit klopt
    jaarloon = maandloon * 13 # als de gebruiker een dertiende maand bonus krijgt, maandloon vermenigvuldigen met 13 en opslaan in variabele 'jaarloon'
  elif dertiendeMaand == 'n': # check of 'dertiendeMaand' gelijk staat aan 'n', voer code uit als dit klopt
    jaarloon = maandloon * 12 # als de gebruiker geen dertiende maand bonus krijgt, maandloon vermenigvuldigen met 12 en opslaan in variabele 'jaarloon'
  return f'Jaarloon (Bruto): €{jaarloon:.2f}' # return een f-string met het bruto jaarloon, afgerond op 2 decimalen

def belastingBox1(brutoJaar): # maak een functie 'belastingBox1' met als parameter 'brutoJaar'
  global nettoJaar # zorg ervoor dat de variabele 'nettoJaar' globaal te gebruiken is (in de gehele code)
  if brutoJaar < 73031: # check of de waarde van 'brutoJaar' kleiner is dan 73031, voer code uit als dit klopt
    belasting = 0.3693 * brutoJaar # vermenigvuldig de waarde van 'brutoJaar' met 0.3693, om zo 36.93% te krijgen van het bruto jaarloon
    nettoJaar = jaarloon - belasting # bereken het netto jaarloon door de waarde van 'belasting' van 'brutoJaar' af te halen
    return f'Schijf 1 (< €73031): €{belasting:.2f}\nTotale Belasting: €{belasting:.2f}' # return een f-string met het netto jaarloon, afgerond op 2 decimalen
  elif brutoJaar >= 73031: # check of de waarde van 'brutoJaar' groter of gelijk is aan 73031 en voer code uit als dit klopt
    belastingS1 = 0.3693 * 73031 # vermenigvuldig de waarde van 'brutoJaar' met 0.3693, om zo 36.93% te krijgen van het bruto jaarloon (voor de eerste €73031) en sla de waarde op in variabele 'belastingS1'
    belastingS2 = 0.4950 * (brutoJaar - 73031) # vermenigvuldig de waarde van 'brutoJaar' met 0.4950, om zo 49.5% te krijgen van het bruto jaarloon (voor alles na €73031) en sla de waarde op in variabele 'belastingS2'
    belasting = belastingS1 + belastingS2 # tel de waarden van 'belastingS1' en 'belastingS2' bij elkaar op en sla de waarde op in variabele 'belasting'
    nettoJaar = jaarloon - belasting # bereken het netto jaarloon door de waarde van 'belasting' van 'brutoJaar' af te halen
    return f'Schijf 1 (< €73031): €{belastingS1:.2f}\nSchijf 2 (>= €73031): €{belastingS2:.2f}\nTotale Belasting: €{belasting:.2f}' # return een f-string met de belasting uit schijf 1 en schijf 2, afgerond op 2 decimalen

def nettoMaandFormule(nettoLoon): # maak een functie 'nettoMaandFormule' met als parameter 'nettoLoon'
  if dertiendeMaand == 'j': # check of de waarde van 'dertiendeMaand' gelijk staat aan 'j', voer code uit als dit klopt
    nettoMaand = nettoLoon / 13 # deel nettoLoon door 13, sla de waarde op in variabele 'nettoMaand'
  elif dertiendeMaand == 'n': # check of de waarde van 'dertiendeMaand' gelijk staat aan 'n', voer code uit als dit klopt
    nettoMaand = nettoLoon / 12 # deel nettoLoon door 12, sla de waarde op in variabele 'nettoMaand'
  return f'Maandloon (netto): €{nettoMaand:.2f}' # return een f-string met het netto maandloon, afgerond op 2 decimalen

time.sleep(3) # gebruik sleep functie uit de 'time' library om de computer 3 seconden te laten wachten voor de rest van de code uitgevoerd wordt
os.system('clear') # gebruik os.system('clear') om de console leeg te maken, zodat het overzichtelijker is
print('-------------------------------------') # print een lijn met streepjes voor overzichtelijkheid
print('\x1b[1;34;40mBELASTING BEREKENAAR\033[0m') # print dikgedrukte blauwe tekst naar de console (ANSI escape code)
print('-------------------------------------') # print een lijn met streepjes voor overzichtelijkheid
print('\x1b[1;36;40mBRUTO\033[0m') # print dikgedrukte turquoise tekst naar de console (ANSI escape code) 
print(f'Maandloon (Bruto): €{inkomen:.2f}') # print het bruto maandloon naar de console, afgerond op 2 decimalen
print(jaarloonFormule(inkomen)) # print het resultaat van de functie jaarloonFormule, met als gegeven parameter de variabele 'inkomen'
print('-------------------------------------') # print een lijn met streepjes voor overzichtelijkheid
print('\x1b[1;31;40mBELASTING\033[0m') # print dikgedrukte rode tekst naar de console (ANSI escape code)
print(belastingBox1(jaarloon)) # print het resultaat van de functie belastingBox1, met als gegeven parameter de variabele 'jaarloon'
print('-------------------------------------') # print een lijn met streepjes voor overzichtelijkheid
print('\x1b[1;32;40mNETTO\033[0m') # print dikgedrukte groene tekst naar de console (ANSI escape code)
print(nettoMaandFormule(nettoJaar)) # print het resultaat van de functie nettoMaandFormule, met als gegeven parameter de variabele 'nettoJaar'
print(f'Jaarloon (netto): €{nettoJaar:.2f}') # print het netto jaarloon naar de console, afgerond op 2 decimalen