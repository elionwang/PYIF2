import random
people = []
i = 0
aantalPers = int(input('Hoeveel mensen wil je uitnodigen? '))

while i < aantalPers:
  inv_person = input('Zet iemand op je uitnodingslijst: ').title()
  people.append(inv_person)
  i += 1

invite = ['zou jij naar mijn feest willen komen?', 'kom zaterdag langs bij mijn feest!', 'ik heb zaterdag een feest, zin om te hangen?']


for person in people:
  randInvite = random.choice(invite)
  print(f'Hoi {person},', randInvite)
