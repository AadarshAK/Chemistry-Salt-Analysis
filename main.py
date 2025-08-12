'''
Data sourced from Sathvik Badhya XII B
Conceptualised and engineered by Aadarsh A.K, XII B (Opposition Minister)
'''

ar = ''
br = ''

#Acid radical functions
def sulphate():
    print('Now add barium chloride to the salt solution')
    t5 = input('Are you getting any white precipitate? (y/n) : ')
    if t5.lower()=='y':
        print('It maybe a sulphate salt')
        #Proceed with confirmatory test
        print('Add acetic acid and lead acetate')
        c5 = input('Are you getting a white precipitate? (y/n) : ')
        if c5.lower()=='y':
            print('Sulphate is confirmed')
            ar = 'Sulphate'
        else:
            print('Salt is out of syllabus')
    else:
        print('Salt is out of syllabus')

def nitrate():
    t4 = input('Are you getting any brown fumes? (y/n) : ')
    if t4.lower()=='y':
        print('It maybe a nitrate salt')
        #proceed with confirmatory test
        print('Add ferrous sulphate and conc. sulphuric acid to the salt solution')
        c4 = input('Does it form a brown ring? (y/n) : ')
        if c4.lower()=='y':
            print('Nitrate is confirmed')
            ar = 'Nitrate'
        else:
            sulphate()
    else:
        sulphate()

def acetate():
    t3 = input('Are you getting the smell of vinegar? (y/n) : ')
    if t3.lower()=='y':
        print('It maybe an acetate salt')
        #proceed with confirmatory test
        print('Add ferric chloride to the salt solution')
        c3 = input('Does the solution turn blood red? (y/n) : ')
        if c3.lower()=='y':
            print('Acetate is confirmed')
            ar = 'Acetate'
        else:
            nitrate()
    else:
        nitrate()

def chloride():
    print('Add nitric acid to the solution and boil, after cooling add silver nitrate')
    t2 = input('Are you getting any white fumes? (y/n) : ')
    if t2.lower()=='y':
        print('It maybe a chloride salt')
        #proceed with confirmatory test
        print('Add nitric acid to the solution and boil, after cooling add silver nitrate')
        c2 = input('Are you getting a white precipitate? (y/n) : ')
        if c2.lower()=='y':
            print('Chloride is confirmed')
            ar = 'Chloride'
        else:
            acetate()
    else:
        acetate()

def carbonate():
    t1 = input('Did you observe effervesence? (y/n) : ')
    if t1.lower()=='y':
        print('It maybe a carbonate salt')
        #proceed with confirmatory test for co3
        print('Heat the salt solution and pass the gas through lime water')
        c1 = input('Is the solution turning milky? (y/n) : ')
        if c1.lower()=='y':
            print('Carbonate is confirmed')
            ar = 'Carbonate'
        else:
            chloride()
    else:
        chloride()


#Basic radical functions
def magnesium():
    t15 = input('Are you getting a white precipitate? (y/n) : ')
    if t15.lower()=='y':
        print('Maybe magnesium')
        print('To the original solution, add ammonium chloride, ammonium hydroxide, ammonium carbonate and magnesson reagent')
        t16 = input('Did it turn sky blue? (y/n) : ')
        if t16.lower()=='y':
            print('Magnesium is confirmed')
            br = 'Magnesium'
        else:
            print('You have reached dead end')
    else:
        print('Salt is out of syllabus')

def calcium():
    print('To the third part, add ammonium oxalate')
    t13 = input('Áre you getting a white precipitate? (y/n) : ')
    if t13.lower()=='y':
        print('Çalcium confirmed')
        br = 'Calcium'
    else:
        print('You have reached dead end')

def strontium():
    print('To the second part, add ammonium sulphate')
    t12 = input('Áre you getting a white precipitate? (y/n) : ')
    if t12.lower()=='y':
        print('Strontium confirmed')
        br = 'Strontium'
    else:
        calcium()

def barium():
    print('Two one part of the above solution add Potassium Chromate')
    t11 = input('Are you getting a yellow precipitate? (y/n) : ')
    if t11.lower()=='y':
        print('Barium confirmed')
        br = 'Barium'
    else:
        strontium()
    
def zinc():
    print('Add hydrogen disulphide to the salt solution')
    t10 = input('Are you getting a white precipitate? (y/n) : ')
    if t10.lower()=='y':
        print('It maybe a salt of zinc')
        #proceed with the confirmatory test
        print('Add sodium hydroxide to the original solution')
        print('Add potassium ferrocyanide')
        c10 = input('Are you getting a white precipitate? (y/n) : ')
        if c10.lower()=='y':
            print('Zinc is confirmed')
            br = 'Zinc'
        else:
            print('Sr, Ca, Ba salt')
            t14 = input('Are you getting a white precipitate? (y/n) : ')
            if t14.lower()=='y':
                print('Dissolve the precipitate in acetic acid and then divide it into 3 parts')
                barium()
            else:
                print('Add disodium hydrogen phosphate solution to the above solution')
                magnesium()
    else:
        print('Ádd ammonium carbonate solution')
        t14 = input('Áre you getting a white precipitate? (y/n) : ')
        if t14.lower()=='y':
            print('Dissolve the precipitate in acetic acid and then divide it into 3 parts')
            barium()
        else:
            print('Ádd disodium hydrogen phosphate solution to the above solution')
            #Magnesium function
            magnesium()


def iron():
    print('Add ammonium chloride followed by ammonium hydroxide to the salt solution')
    t9 = input('Are you getting a reddish brown precipitate? (y/n) : ')
    if t9.lower()=='y':
        print('It maybe a salt of iron')
        #proceed with the confirmatory test
        print('Dissolve the precipitate in dil. hydrochloric acid')
        print('Add potassium sulphocyanide')
        c9a = input('Did it turn blood red? (y/n) : ')
        print('Add potassium ferrocyanide')
        c9b = input('Did it turn prussian blue? (y/n) : ')
        if c9a.lower()=='y' and c9b.lower()=='y':
            print('Iron is confirmed')
            br = 'Iron'
        else:
            zinc()
    else:
        zinc()

def copper():
    print('Add hydrogen disulphide to the salt solution')
    t8 = input('Are you getting a black precipitate? (y/n) : ')
    if t8.lower()=='y':
        print('It maybe a salt of copper')
        #proceed with the confirmatory test
        print('Add potassium ferrocyanide to it')
        c8 = input('Did you get a chocolate brown precipitate? (y/n) : ')
        if c8.lower()=='y':
            print('Copper is confirmed')
            br = 'Copper'
        else:
            iron()
    else:
        iron()

def lead():
    print('Add dil. hydrochloric acid to the salt solution')
    t7 = input('Are you getting a white precipitate? (y/n) : ')
    if t7.lower()=='y':
        print('It maybe a salt of lead')
        #proceed with the confirmatory test
        print('Make two parts of the above solution and add potassium iodide to one part and potassium chromate to the other')
        c7 = input('Did both the parts turn yellow? (y/n) : ')
        if c7.lower()=='y':
            print('Lead is confirmed')
            br = 'Lead'
        else:
            copper()
    else:
        copper()

def ammonia():
    t6 = input('Are you getting a smell of ammonia? (y/n) : ')
    if t6.lower()=='y':
        print('It maybe a salt of ammonia')
        #proceed with the confirmatory test
        print('Put a cotton containing nesslers reagent and place it on the mouth of the test tube')
        c6 = input('Did the cotton turn brown? (y/n) : ')
        if c6.lower()=='y':
            print('Ammonia is confirmed')
            br = 'Ammonia'
        else:
            lead()
    else:
        lead()

print('Test for Acid Radical')
print('First add dil. sulphuric acid to the salt solution')
carbonate()

print('\nNow let us test for basic radical')
print('Add sodium hydroxide to the salt solution and heat')
ammonia()

print(f'The acid radical is {ar} and the basic radical is {br}')
