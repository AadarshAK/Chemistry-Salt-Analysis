class Dil_H2SO4():
    effervesence = False

class Conc_H2SO4():
    white_fumes = False
    smell = None
    brown_fumes = False

class BaCl():
    white_precipitate = False

print('Test for Acid Radical')
print('First add dil. sulphuric acid to the salt solution')
t1 = input('Did you observe effervesence? (y/n) : ')
if t1.lower()=='y':
    print('It maybe a carbonate salt')
    #proceed with confirmatory test for co3
else:
    print('Now add conc. sulphuric acid to the salt solution')
t2 = input('Are you getting any white fumes? (y/n) : ')
if t2.lower()=='y':
    print('It maybe a chloride salt')
    #proceed with confirmatory test
else:
    t3 = input('Are you getting the smell of vinegar? (y/n) : ')
    if t3.lower()=='y':
        print('It maybe an acetate salt')
        #proceed with confirmatory test
    else:
        t4 = input('Are you getting any brown fumes? (y/n) : ')
        if t4.lower()=='y':
            print('It maybe a nitrate salt')
            #proceed with confirmatory test
        else:
            print('Now add barium chloride to the salt solution')

t5 = input('Are you getting any white precipitate? (y/n) : ')
if t5.lower()=='y':
    print('It maybe a sulphate salt')
    #Proceed with confirmatory test
else:
    print('Salt is out of syllabus')
