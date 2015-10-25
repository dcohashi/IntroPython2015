#!/usr/bin/env python3
'''
Mailroom Program
'''

# initial list of donations
donors = [("Joe Morelli", [20, 20]),
         ("Stephanie Plum", [5, 7]),
         ("Grandma Mazur",[1,1,2]),
         ("Lula", [50]),
         ("Ranger", [2000])]

def add_donor(name, donors):
    '''Find the donor in the list or add a new entry'''
    if name == "list":
        for donor in donors:
            print(donor[0])
    else:
        for donor in donors:
            if name == donor[0]:
                break
        else:
            donors.append((name, []))
        donation = ""
        while not (donation.isnumeric()):
            donation=input("Donation amount: ")
        
        for donor in donors:
            if name == donor[0]:
                donor[1].append(int(donation))
                break
        print("Thank you {} for your generous donation of ${}!\n".format(name, donation).format(name, donation))
    return


def send_thank_you(donors):
    '''Send a thank you note to the selected donor'''
    name = input("Enter the full name: ")
    add_donor(name, donors)
    return


def create_report(donors):
    '''Create a report of all the donors'''
    for donor in donors:
        print("name: {:<25}      total donations:{:>5}      number:{:>3}      average:{:>8.2f}".format(donor[0], sum(donor[1]), len(donor[1]), sum(donor[1])/len(donor[1])))
    return

if __name__ == '__main__':
    '''main menu if in iteractive mode'''
while True:
    answer = input("Enter t-thank you, r-report, x-exit: ")
    if answer is 't':
        send_thank_you(donors)
    elif answer is 'r':
        create_report(donors)
    elif answer is 'x':
        print("Goodbye")
        break
