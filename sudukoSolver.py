import copy
import time



def configureFromInputPuzzle(inputArray):
    sudukoArray = [[[1,2,3,4,5,6,7,8,9] for rows in range(0,9)] for columns in range(0,9)]
    for row in range(0,9):
        for column in range(0,9):
            if inputArray[row][column] != 0:
                sudukoArray[row][column] = [inputArray[row][column]]                
    return sudukoArray


def ThreeBox(sudukoArray):
    for rows in range(0,9):
        for columns in range(0,9):
            equalCount = 0
            for row in range((rows//3)*3,(rows//3)*3+3):
                for column in range((columns//3)*3,(columns//3)*3+3):
                    if sudukoArray[rows][columns] == sudukoArray[row][column]:
                        equalCount += 1
                        
            if equalCount == len(sudukoArray[rows][columns]):
                for row in range((rows//3)*3,(rows//3)*3+3):
                    for column in range((columns//3)*3,(columns//3)*3+3):
                        if sudukoArray[rows][columns] != sudukoArray[row][column]:
                            for element in sudukoArray[rows][columns]:
                                try:
                                    sudukoArray[row][column].remove(element)
                                except:
                                    pass
    return sudukoArray

def columns(sudukoArray):
    for rows in range(0,9):
        for columns in range(0,9):
            equalCount = 0
            for row in range(0,9):
                if sudukoArray[rows][columns] == sudukoArray[row][columns]:
                    equalCount += 1
                        
            if equalCount == len(sudukoArray[rows][columns]):
                for row in range(0,9):
                    if sudukoArray[rows][columns] != sudukoArray[row][columns]:
                        for element in sudukoArray[rows][columns]:
                            try:
                                sudukoArray[row][columns].remove(element)
                            except:
                                pass
    return sudukoArray

def rows(sudukoArray):
    for rows in range(0,9):
        for columns in range(0,9):
            equalCount = 0
            for column in range(0,9):
                if sudukoArray[rows][columns] == sudukoArray[rows][column]:
                    equalCount += 1
                        
            if equalCount == len(sudukoArray[rows][columns]):
                for column in range(0,9):
                    if sudukoArray[rows][columns] != sudukoArray[rows][column]:
                        for element in sudukoArray[rows][columns]:
                            try:
                                sudukoArray[rows][column].remove(element)
                            except:
                                pass
    return sudukoArray

def checkValid(sudukoArray):

    for row in range(0,9):
        rowTotals = []
        for column in range(0,9):
            if sudukoArray[row][column] == []:
                return False
            if len(sudukoArray[row][column]) == 1:
                rowTotals.append(sudukoArray[row][column][0])
        rowTotals.sort()

        
        if len(set(rowTotals)) != len(rowTotals):
            return False
    for column in range(0,9):
        columnTotals = []
        for row in range(0,9):
            if sudukoArray[row][column] == []:
                return False
            if len(sudukoArray[row][column]) == 1:
                columnTotals.append(sudukoArray[row][column][0])
        columnTotals.sort()

        if len(set(columnTotals)) != len(columnTotals):
            return False
    # Add square checker

    return True
                                    

inputArray =  [[2,9,0,0,0,0,0,7,0],
               [3,0,6,0,0,8,4,0,0],
               [8,0,0,0,4,0,0,0,2],
               [0,2,0,0,3,1,0,0,7],
               [0,0,0,0,8,0,0,0,0],
               [1,0,0,9,5,0,0,6,0],
               [7,0,0,0,9,0,0,0,1],
               [0,0,1,2,0,0,3,0,6],
               [0,3,0,0,0,0,0,5,9]]

inputArray =     [[8, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 3, 6, 0, 0, 0, 0, 0],
     [0, 7, 0, 0, 9, 0, 2, 0, 0],
     [0, 5, 0, 0, 0, 7, 0, 0, 0],
     [0, 0, 0, 0, 4, 5, 7, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 3, 0],
     [0, 0, 1, 0, 0, 0, 0, 6, 8],
     [0, 0, 8, 5, 0, 0, 0, 1, 0],
     [0, 9, 0, 0, 0, 0, 4, 0, 0]]

def IsComplete(sudukoArray):
    for row in sudukoArray:
        for element in row:
            if len(element) != 1:
                return False
    return True

                            
        

def guess(inputArray):
    prevrun = copy.deepcopy(inputArray)
    currentrun = copy.deepcopy(columns(rows(ThreeBox(inputArray))))
    while prevrun != currentrun:
##        for row in currentrun:
##            print(row)
##        print('')
##        print('')
##        print(' ------ ')
        prevrun = copy.deepcopy(currentrun)
        currentrun = copy.deepcopy(columns(rows(ThreeBox(currentrun))))
    if checkValid(currentrun) == True:
        if IsComplete(currentrun) == True:
            for row in currentrun:
                print(row)
            print('')
            print('')
            print(' ------ ')
            print('Finished')
            return True
        else:
            for row in range(0,9):
                for element in range(0,9):
                    if len(currentrun[row][element]) != 1:
                        for number in currentrun[row][element]:
                            tryArray = copy.deepcopy(currentrun)
                            tryArray[row][element] = [number]
                            result = guess(tryArray)
                            if result == True:
                                return True
                        return False  
    else:
        return False
startTime = time.time()
OriginalArray = configureFromInputPuzzle(inputArray)
guess(OriginalArray)
endTime = time.time()
print(endTime-startTime)

