#!/usr/bin/env python3
'''
Mailroom Program
'''

# initial list of donations
donors = {
    "Joe Morelli": [20, 20],
    "Stephanie Plum": [5, 7],
    "Grandma Mazur": [1, 1, 2],
    "Lula": [50],
    "Ranger": [2000]}


def print_donors(donors):
    '''print a list of all the donor names'''
    print(list(donors.keys()))


def add_donor(name, donors):
    '''Find the donor in the dict or add a new entry'''
    donation = ""
    while True:
        donation = input("Donation amount: ")
        try:
            dollar = int(donation)
        except ValueError:
            continue
        else:
            break
    try:
        donors[name].append(dollar)
    except KeyError:
        donors[name] = [dollar] 
    print("Thank you {} for your generous donation of ${}!\n".format(name, donation))
    return


def send_thank_you(donors):
    '''Send a thank you note to the selected donor'''
    name = input("Enter the full name: ")
    if name == "list":
        print_donors(donors)
        return
    add_donor(name, donors)
    return


def create_report(donors):
    '''Create a report of all the donors'''
    for donor in donors:
        print("name: {:<25}  total:${:>5}   number:{:>3}   avg:${:>8.2f}".format(donor, sum(donors[donor]), len(donors[donor]), sum(donors[donor])/len(donors[donor])))
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
