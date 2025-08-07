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

print('Now let us test for basic radical')
print('Add sodium hydroxide to the salt solution and heat')
t6 = input('Are you getting a smell of ammonia? (y/n) : ')
if t6.lower()=='y':
    print('It maybe a salt of ammonia')
    #proceed with the confirmatory test
else:
    print('Add dil. hydrochloric acid to the salt solution')

t7 = input('Are you getting a white precipitate')
if t7.lower()=='y':
    print('It maybe a salt of lead')
    #proceed with the confirmatory test
else:
    print('Add hydrogen disulphide to the salt solution')

t8 = input('Are you getting a black precipitate? (y/n) : ')
if t8.lower()=='y':
    print('It maybe a salt of copper')
    #proceed with the confirmatory test
else:
    print('Add ammonium chloride followed by ammonium hydroxide to the salt solution')

t9 = input('Are you getting a reddish brown precipitate? (y/n) : ')
if t9.lower()=='y':
    print('It maybe a salt of iron')
    #proceed with the confirmatory test
else:
    print('Add hydrogen disulphide to the salt solution')

t10 = input('Are you getting a white precipitate? (y/n) : ')
if t10.lower()=='y':
    print('It maybe a salt of zinc')
    #proceed with the confirmatory test
else:
    print('Salt is out of syllabus')