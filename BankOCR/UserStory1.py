#!/bin/python3

# Coding Dojo Problem found here: http://codingdojo.org/kata/BankOCR/#problem-description

# Function for decision tree
# Parameters: 3 lists of length 3
def digitDecision(top, middle, bottom):
    if top == [' ', ' ', ' ']:
        # number 1 or 4
        if middle == [' ', ' ', '|']:
            return(1)
        elif middle == ['|', '_', '|']:
            return(4)
        else:
            return('fail1')
    else:
        # any other number
        if middle == [' ', '_', '|']:
            # number 2 or 3
            if bottom == ['|', '_', ' ']:
                return(2)
            elif bottom == [' ', '_', '|']:
                return(3)
            else:
                return('fail2')
        elif middle == ['|', '_', '|']:
            # number 8 or 9
            if bottom == ['|', '_', '|']:
                return(8)
            elif bottom == [' ', '_', '|']:
                return(9)
            else:
                return('fail3')
        elif middle == ['|', '_', ' ']:
            # number 5 or 6
            if bottom == [' ', '_', '|']:
                return(5)
            elif bottom == ['|', '_', '|']:
                return(6)
            else:
                return('fail4')
        elif middle == [' ', ' ', '|']:
            return(7)
        elif middle == ['|', ' ', '|']:
            return(0)
        else:
            return('fail5')


# Function to evaluate checksum for User Story 2
def checksum(account):
    acc = 0
    for i in range(0,9):
        key = 8 - i
        multiplier = i + 1
        acc = acc + (multiplier * account[key])
        # print("acc: %d" % acc)
    if (acc % 11) == 0:
        return True
    else:
        return False

# Function to force numbers to be a string and join it together
def numsToAccount(account):
    new = ''
    for i in range(0,9):
        new += (str(account[i]))
    return new

filename = "digits.txt"
# Function to read in the text and handle the logic
def scan(filename):
    # Read file in line by line - store as list of lines
    lines = []
    accountNums = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line)
    # Iterate through 4-line sections
    ## Use while loop
    while len(lines) >= 4:
        ## Pop top 4 lines off front of list - label as lines1-lines4
        line1 = lines.pop(0)
        #print('line1[0]: %s, line1[1]: %s, line1[2]: %s' % (line1[0], line1[1], line1[2]))
        line2 = lines.pop(0)
        line3 = lines.pop(0)
        line4 = lines.pop(0)
        account = []
        ## Iterate through 3-character segments
        for i in range(0, 26, 3):
            ## Follow decision tree
            top = [line1[i], line1[i+1], line1[i+2]]
            middle = [line2[i], line2[i+1], line2[i+2]]
            bottom = [line3[i], line3[i+1], line3[i+2]]
            ## Keep a string and append digit to string
            account.append(digitDecision(top, middle, bottom))
        ## Store final string in array (or print them to a new file?)

        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # !!!!!!!!! make a function to turn this list into a string !!!!!!!!
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        account = numsToAccount(account)
        accountNums.append(account)



# Test
for line in lines:
    print(line)
# print("Number of lines: %d" % (numLines))
# print("Number of accounts: %d" % (numAccounts))
#for acnt in accountNums:
#    print(acnt)
# account = [3,4,5,8,8,2,8,6,5]
# print(checksum(account))
# print(numsToAccount(account))
