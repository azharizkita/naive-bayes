import csv

datatest = []
datatrain = []

with open('TestsetTugas1ML.csv') as target:
    tempData = csv.reader(target, delimiter='\n')
    for row in tempData:
        tempText = ''.join(row)
        tempArray = tempText.split(',')
        datatest.append(tempArray)
    datatest.pop(0)


with open('TrainsetTugas1ML.csv') as target:
    tempData = csv.reader(target, delimiter='\n')
    for row in tempData:
        tempText = ''.join(row)
        tempArray = tempText.split(',')
        datatrain.append(tempArray)
    datatrain.pop(0)

def probabilityCounter(x, income):
    counter = 0
    for row in datatrain:
        if x in row:
            if income in row:
                counter += 1
    return counter

def count():
    more = 0
    less = 0
    for row in datatrain:
        if '>50K' in row:
            more += 1
        else:
            less += 1
    return {'moreProbability': more / len(datatrain), 'lessProbability': less / len(datatrain), 'moreTotal': more, 'lessTotal': less}

def outputData(data):
    with open('TebakanTugas1ML.csv', mode='w', newline='') as target:
        fieldnames = ['guess']
        writer = csv.DictWriter(target, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow({'guess': row})

if __name__ == "__main__":
    checked = []
    moreList = {}
    lessList = {}
    values = count()
    guess = []

    for row in datatest:
        for i in range(1, len(row)):
            if row[i] in checked:
                pass
            else:
                moreThan = probabilityCounter(row[i], '>50K')
                moreList[row[i]] = moreThan / values['moreTotal']
                lessThan = probabilityCounter(row[i], '<=50K')
                lessList[row[i]] = lessThan / values['lessTotal']
                checked.append(row[i])

    for rows in datatest:
        moreProbability = 1
        lessProbability = 1
        rows.pop(0)
        for row in rows:
            moreProbability = moreProbability * moreList[row]
            lessProbability = lessProbability * lessList[row]
        if ((moreProbability * values['moreProbability']) > (lessProbability * values['lessProbability'])):
            guess.append('>50K')
        else:
            guess.append('<=50K')

    outputData(guess)