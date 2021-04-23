import csv
def readFileIntoList():
    # abbrevation = []
    # meaning = []

    name = 'myfile.txt'
    accessMode = 'r'

    with open(name, accessMode) as file:
        content = csv.reader(file, delimiter=':')
        myContent = list(content)
        return myContent

def checkFile():
    pass

def colectUserText():
    print('enter text below')
    text = input('-->')
    userText = text.split(' ')
    # print(userText)
    # for steps in userText:
    #     each = steps
    #     print(each)
    return userText

def compare():
    abbrevation = []
    meaning = []
    myContent = readFileIntoList()
    for myContent in myContent:
        abbr = myContent[0]
        mean = myContent[1]
        abbrevation.append(abbr)
        meaning.append(mean)
    # print(abbrevation)
    # print(meaning)

    userText = colectUserText()
    # print(userText)
    for steps in userText:
        textpos = userText.index(steps)
        #print(textpos)
        steps = steps.upper()

    if (steps in abbrevation):
        newUserText = userText
        possition = abbrevation.index(steps)
        newUserText[textpos] = meaning[possition]
        return newUserText

    elif steps not in abbrevation:
        return userText




def result():
    a = compare()
    b = ' '
    print(b.join(a))






result()
