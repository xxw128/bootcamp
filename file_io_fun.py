import os

if os.path.isfile('gimme_phi.txt'):
    print('Sorry, file exists.')
else:
    with open('gimme_phi.txt', 'w') as f:
        f.write('the golden ratio is ')
        f.write('{phi:.8f}'.format(phi = 1.61803398875))
