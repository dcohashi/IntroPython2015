#!/usr/bin/env python

import csv
import os.path
from datetime import date


def add_equipment():
    '''
    Create a new record and add it to the file
    Args:
        None
    Return:
        None
    '''
    record = dict()
    record['FTID'] = input("FTID[]: ")
    record['Nomen'] = input("Nomenclature[]: ")
    record['Asset Tag'] = input("Asset Tag[]: ")
    record['Location'] = input("Location[]: ")
    fieldnames = ['FTID', 'Nomen', 'Asset Tag', 'Location', 
                      'User', 'Date Checked Out', 'Expected Return']
    if not os.path.isfile("inventory.csv"):
        f = open("inventory.csv", "w") 
        writer = csv.DictWriter(f, fieldnames = fieldnames)
        writer.writeheader()
    else:
        f = open("inventory.csv", "a") 
        writer = csv.DictWriter(f, fieldnames = fieldnames)
    writer.writerow(record)
    f.close()
    return()

def list_equipment():
    '''
    Read the file and display contents 
    Args:
        None
    Return:
        data - all the equipment in a dictionary reader object
    '''
    with open("inventory.csv") as f:
        reader = csv.DictReader(f)
        print("   \tFTID\tAsset Tag\tNomen")
        for index, row in enumerate(reader):
            print("{} - {}\t{}\t\t{}\t".format(index+1, row['FTID'],
                    row['Asset Tag'], row['Nomen']))
    return(reader)

def checkout_equipment():
    '''
    Checkout equipement by selecting a record and adding more metadata to it
    
    Args:
        None
    Return:
        None
    '''
    # List the all the equipment, already checked out or not
    all_equipment = list_equipment()
    
    # Request user to select equipment
    num = input("enter line number of equipment to check out: ")

    # Prompt for additional metadata
    # Use today's date for checkout date
    record = all_equipment[num-1]
    record['Date Checked Out'] = str(date.today())
    record[input("name: ")]

    # update file
    with open("inventory.csv", "w") as f:
        writer = csv.DictWriter(f, fieldnames = fieldnames)
        writer.writeheader()
        for index, row in enumerate(reader):
            if index == num-1:
                writer.writerow(record)
            else:
                writer.writerow(row)

def return_equipment():
    '''
    Remove the metadata to check in the equipment
    Args:
        None
    Return:
        None
    '''
    # List all the checked out equipment
    all_equipment = list_equipment()

    # Request user to select equipment
    num = input("enter line number of equipment to return: ")

    # Remove the meta data for that record

def send_email():
    return()

if __name__  == '__main__':
# open data file and read in contents

    ans = ''
    while ans != 'q':
        ans = input("s-send email\n" + 
                    "c-checkout equipment\n" +
                    "a-add equipment\n" +
                    "r-return equipment\n" +
                    "d-delete equipment\n" +
                    "l-list equipment\n" +
                    "q-quit\n[q]:")
        if ans == 'a':
            print("\nAdd Equipment to Inventory")
            add_equipment()
        elif ans == 'c':
            print("\nCheckout Equipment")
            checkout_equipment()
        elif ans == 'r':
            print("\nReturn Equipment")
            return_equipment()
        elif ans == 'd':
            print("\nDelete Equipment from Inventory")
        elif ans == 'l':
            print("\nList All Equipment")
            list_equipment()
        elif ans == 's':
            print("\nSending email...")
            send_email()
        else:
            ans = 'q'
            print("Exiting")

