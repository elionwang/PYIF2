import time 
import os

print('Hoeveel verdien je bruto per maand?')
inkomen = float(input('Ik verdien per maand bruto: '))
dertiendeMaand = input('Heb je een dertiende maand? (j/n): ')
print('\x1b[3;37;40mBerekenen...\033[0m')


def jaarloonFormule(maandloon):
  global jaarloon
  if dertiendeMaand == 'j':
    jaarloon = round(maandloon * 13, 2)
  elif dertiendeMaand == 'n':
    jaarloon = round(maandloon * 12, 2)
  return f'Jaarloon (Bruto): €{jaarloon:.2f}'

def belastingBox1(var1):
  global nettoJaar
  if var1 < 73031:
    belasting = round(0.3693 * var1, 2)
    nettoJaar = jaarloon - belasting
    return f'Schijf 1 (< €73031): €{belasting:.2f}\nTotale Belasting: €{belasting:.2f}'
  elif var1 >= 73031:
    belastingS1 = round(0.3693 * 73031, 2)
    belastingS2 = round(0.4950 * (var1 - 73031), 2)
    belasting = belastingS1 + belastingS2
    nettoJaar = jaarloon - belasting
    return f'Schijf 1 (< €73031): €{belastingS1:.2f}\nSchijf 2 (>= €73031): €{belastingS2:.2f}\nTotale Belasting: €{belasting:.2f}'

def nettoMaandFormule(var1):
  if dertiendeMaand == 'j':
    nettoMaand = round(var1 / 13, 2)
  elif dertiendeMaand == 'n':
    nettoMaand = round(var1 / 12, 2)
  return f'Maandloon (netto): €{nettoMaand:.2f}'

time.sleep(3)
os.system('clear')
print('-------------------------------------')  
print('\x1b[1;34;40mBELASTING BEREKENAAR\033[0m')
print('-------------------------------------')
print('\x1b[1;36;40mBRUTO\033[0m')
print(f'Maandloon (Bruto): €{inkomen:.2f}')
print(jaarloonFormule(inkomen))
print('-------------------------------------')
print('\x1b[1;31;40mBELASTING\033[0m')
print(belastingBox1(jaarloon))
print('-------------------------------------')
print('\x1b[1;32;40mNETTO\033[0m')
print(nettoMaandFormule(nettoJaar))
print(f'Jaarloon (netto): €{nettoJaar:.2f}')