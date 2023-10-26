counter = 0
avcount = 0
oldcounter = 0
youngcounter = 0
maxage = 0
minage = 999
agetot = 0

choicemaxage = 0
choiceminage = 999
choiceyoung = ''
choiceold = ''

old = ''
oldyear = ''
young = ''
youngyear = ''
yearimput = int(input('what is the year of interest '))

with open("life-expectancy.csv") as data:
    for line in data:
        if counter == 0:
            print('line 1 skipped')
        else:
            p = line.split(",")
            country = p[0]
            short = p[1]
            year = int(p[2])
            age = float(p[3])

            if age > maxage:
                maxage = age
                old = country
                oldyear = year

            if age < minage:
                minage = age
                young = country
                youngyear = year

            if yearimput == year:
                agetot = agetot + age
                avcount = avcount + 1
                if age > choicemaxage:
                    choicemaxage = age
                    choiceold = country

                if age < choiceminage:
                    choiceminage = age
                    choiceyoung = country
        
        counter = counter + 1
    counter = 0

    with open("life-expectancy.csv") as data2:
        for line in data2:
            if counter == 0:
                print('line 1 skipped')
            else:
                p = line.split(",")
                country = p[0]
                short = p[1]
                year = int(p[2])
                age = float(p[3])

                if country == choiceold:
                    if oldcounter == 0:
                        age1 = age
                        year1 = year
                        oldcounter = oldcounter + 1

                if country == choiceyoung:
                    if youngcounter == 0:
                        age2 = age
                        year2 = year
                        youngcounter = youngcounter + 1
            counter = counter + 1

    if choicemaxage > age1:
        change = 'more than'
    elif choicemaxage < age1:
        change = 'less than'
    elif choicemaxage == age1:
        change = 'the same as'

    if choiceminage > age2:
        change2 = 'more than'
    elif choiceminage < age2:
        change2 = 'less than'
    elif choiceminage == age2:
        change2 ='the same as'

    ageaverage = agetot / avcount

    print(counter)
    print(oldcounter)
    print(youngcounter)
    print('------------------------------------------------------------------------------------------------- \n')
    print(f"the highest average age of death is {maxage} at {old} on {oldyear}")
    print(f"the lowest average age of death is {minage} at {young} on {youngyear}\n")

    print(f'for the year {yearimput}:\n The max life expect was in {choiceold} at {choicemaxage}\n the min life expect was in {choiceyoung} at {choiceminage}')
    print(f' the average was {round(ageaverage, 2)} \n')
    print(f"{choiceold}'s life expectancy was {round(float(choicemaxage) - float(age1), 3)} {change} the first entry in {year1} at {age1}")
    print(f"{choiceyoung}'s life expectancy was {round(float(choiceminage) - float(age2), 3)} {change2} the first entry in {year2} at {age2}")
    print('\n--------------------------------------------------------------------------------------------------')
    