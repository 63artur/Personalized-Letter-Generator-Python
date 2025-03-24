
names = []
f = open('Input/Names/invited_names.txt', 'r')
for name in f:
    names.append(name.strip())
f.close()
with open('Input/Letters/starting_letter.txt', 'r') as l:
    letter = l.read()
for name in names:
    with open(f'Output/ReadyToSend/letter_for_{name}.txt', 'w') as output:
        letter.replace('[name]', name)