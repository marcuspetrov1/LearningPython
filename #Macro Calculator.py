#Macro Calculator
#import pandas as geopandas

def welcomePrompt():
    print('\n\nHello! This is an online beginner project made by Marcus that \ncalculates your caloric intake based on your needs, all catered to you! \nTo begin, we need some information from you to start:\n\n')

def setName():
   name = input('What is your name? ')
   return name

def setGender():
    userGender = int(input('\nWhat is your gender? (1)Male or (2)Female '))
    return userGender
    
def setAge():
    userAge = float(input('\nWhat is your age? '))
    return userAge

def setHeight():
    userHeight = float(input('\nWhat is your height (in inches)? '))
    return userHeight * 2.54

def setWeight():
    userWeight = float(input('\nWhat is your weight (in pounds)? '))
    return userWeight * 0.4535924

def setActivity():
    userActivity = int(input('\nHow would you rank your activity level?:(exercise is ) \n1. Very little to no exercise \n2. Light exercise (1-4 days/week) \n3. Moderate exercise (5-7 days/week) \n4. Heavy exercise (Every day/Twice a day)\n5. Very heavy (marathon, triatholon, physically demanding)\n'))
    return userActivity

def setBMR(weight, height, age, gender):
    if (gender == 1):
        BMR = 66  + (13.7 * weight) + (5*height) - (6.8*age)
    if (gender == 2):
        BMR = 655 + (9.6*weight) + (1.8*height) - (4.7*age) 
    return BMR
    # maintCal = float((88.362+(13.397 * weight)) + (4.799 * height)) - (5.677 * age)
    # print(f'\n{name}, your maintence calories is {maintCal}')
    # return maintCal

def setTDEE(BMR, activity):
    match activity:
        case 1:
            TDEE = BMR * 1.2
            return TDEE
        case 2:
            TDEE = BMR * 1.375
            return TDEE
        case 3:
            TDEE = BMR * 1.55
            return TDEE
        case 4:
            TDEE = BMR * 1.725
            return TDEE
        case 5:
            TDEE = BMR * 1.9
            return TDEE
        case _:
            print("Please enter a valid number.")

def getGoals(maintanenceCalories):
    goalChoice = input("\n\nIs your weight goal to: \n(1)cut weight \n(2)maintain weight \n(3)increase weight? ") 
    match goalChoice:
        case 1:
            toCut(maintanenceCalories)
        case 2:
            toMaintain(maintanenceCalories)
        case 3:
            toBulk(maintanenceCalories)
        case _:
            print("Im sorry, you entered an invalid input")
            getGoals()

def toCut(maintanenceCalories):
    pass

def toMaintain(maintanenceCalories):
    pass

def toBulk(maintanenceCalories):
    pass

#def toCut(usersWeight):
#    print(f'To cut, we need to be in a caloric deficit where you eat under your maintanence calories. You are currently at {usersWeight} lbs  ')

def getInfo():
    global userName, userGender, userAge, userHeight, userWeight, userActivity
    
    userName = setName()

    userGender = setGender()
    
    userAge = setAge()

    userHeight = setHeight()
   
    userWeight = setWeight()

    userActivity = setActivity()

    return userName, userAge, userHeight, userWeight, userActivity, userGender

def calcTDEE(gender, age, height, weight, activity):
    BMR = setBMR(weight, height, age, gender)
    TDEE = setTDEE(BMR, activity)
    return TDEE

def printTDEE(name, tdee):
    print(f'Okay {name}, your estimated total calories your body uses per day based on your lifestyle is {tdee} calories.')

def main():
    #Prints a speech that introduces program and what it has to offer
    welcomePrompt()
    #Takes user input of Name, age, height, weight to produce TDEE, a metric that calculates the total calories used in a day
    getInfo()
    TDEE = calcTDEE(userGender, userAge, userHeight, userWeight, userActivity)
    printTDEE(userName, TDEE)
    getGoals(TDEE)

if __name__ == "__main__":
    main()