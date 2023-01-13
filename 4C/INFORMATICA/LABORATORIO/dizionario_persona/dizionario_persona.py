#4C Bracco Mattia - Dizionario persona

persona = dict()
persona['nome'] = 'Mattia'
persona['cognome'] = 'Bracco'
persona['classe'] = '4C'
print(persona)

persona['nascita'] = 2005
print(persona)

print("Nascita in persona - (prima il pop)")
print('nascita' in persona)

persona.pop('nascita')

print("Nascita in persona - (dopo il pop)")
print('nascita' in persona)
