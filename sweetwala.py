# Custom Errors
class FileEmpty(Exception):
    pass

class NumberOfTestCasesMisMatchWithData(Exception):
    pass

class FirstLineOfATestSetIsIncorrect(Exception):
    pass

class NoOfSweetsToBeSelectedIsGreaterThanOrEqualToTheTotalNoOfSweets(Exception):
    pass

class PriceOfTheSweetsProvidedDoesNotMatchWithTheActualCount(Exception):
    pass

class DeliveryCostOfTheSweetsProvidedDoesNotMatchWithTheActualCount(Exception):
    pass

validInput = True # Flag that will stop the execution of the program, if any validation fails

try:
    inputFile = open('inputPS9.txt', 'r') # Opening the input file in the read mode

except FileNotFoundError:
    validInput = False
    print('Input File not found. Please ensure that the input file is present.')

except OSError:
    validInput = False
    print('An OS error occured while trying to open the input file. Please retry.')

except Exception as err:
    validInput = False
    print('Some unexpected error occured while trying to open the input file: ', repr(err))

if validInput:
    try: 
        inputFileContents = inputFile.readlines() # Reading the contents of the file
        if not inputFileContents: # When the file is empty
                raise FileEmpty

        if validInput:
            print(inputFileContents)
            noOfTestCases = inputFileContents[0]
            print('No of Test Cases: ', noOfTestCases)
            inputFileContents.remove(noOfTestCases)
            print('Elements in the list after removing the test case count', inputFileContents)
            testCasesData = []
            tempList = []
            # Validation for the no.of test cases
            i = 0
            while i < len(inputFileContents):
                if inputFileContents[i] != '\n':
                    tempList.append(inputFileContents[i])
                else: 
                    testCasesData.append(tempList)
                    tempList = []
                i = i + 1
                if (i >= len(inputFileContents)):
                    testCasesData.append(tempList)
            
            try:
                if len(testCasesData) != int(noOfTestCases):
                    raise NumberOfTestCasesMisMatchWithData
                
                print('testCasesData: ', testCasesData)

                # validate whether the value of the selected no. of sweets is less than the total no. of sweets provided
                # validate whether the total no. of sweets and the count of the price and delivery charge match
                i = 0
                while i < len(testCasesData):
                    test_set = testCasesData[i]
                    line_one = test_set[0]
                    total_count_and_wanted_count = line_one.split()
                    total_no_of_sweets = int(total_count_and_wanted_count[0])
                    no_of_sweets_to_be_selected = int(total_count_and_wanted_count[1])
                    price_of_the_sweets = test_set[1].split()
                    delivery_cost_of_the_sweets = test_set[2].split()

                    if len(total_count_and_wanted_count) != 2:
                        raise FirstLineOfATestSetIsIncorrect
                        
                    if no_of_sweets_to_be_selected >= total_no_of_sweets:
                        raise NoOfSweetsToBeSelectedIsGreaterThanOrEqualToTheTotalNoOfSweets
                    
                    if len(price_of_the_sweets) != total_no_of_sweets:
                        raise PriceOfTheSweetsProvidedDoesNotMatchWithTheActualCount
                    
                    if len(delivery_cost_of_the_sweets) != total_no_of_sweets:
                        raise DeliveryCostOfTheSweetsProvidedDoesNotMatchWithTheActualCount
                            
                    i = i + 1
            
            except NumberOfTestCasesMisMatchWithData:
                validInput = False
                print('Number of test cases specified in the first line is not matching with the data given. Please check the input file and give valid data')
            
            except FirstLineOfATestSetIsIncorrect:
                validInput = False
                print('The First Line of a test set is incorrect. It should contain only two values. Please correct and retry')

            except NoOfSweetsToBeSelectedIsGreaterThanOrEqualToTheTotalNoOfSweets:
                validInput = False
                print('The No. of sweets to be selected is greater than or equal to the total no.of sweets in one or more of the test sets. Please correct them and retry')
            
            except PriceOfTheSweetsProvidedDoesNotMatchWithTheActualCount:
                validInput = False
                print('The No. of values provided for the price of the sweets does not match with the total no. of sweets')
            
            except DeliveryCostOfTheSweetsProvidedDoesNotMatchWithTheActualCount:
                validInput = False
                print('The No. of values provided for the delivery cost of the sweets doesnot match with the total no. of sweets')
        
    except FileEmpty as err:
        validInput = False
        print('Input file is empty. Please check the input file and retry.', repr(err))
    except Exception as err:
        validInput = False
        print('Some unexpected error occured while trying to read the contents of the file. Please retry', repr(err))

else:
    print('Execution Terminated due to invalid input file')

