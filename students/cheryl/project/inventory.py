#!/usr/bin/env python

import csv
import os.path
from datetime import date


def add_equipment(filename, fields):
    '''
    Create a new record and add it to the file
    Args:
        fn - filename of inventory file
        fieldnames - list of top row of csv file
    Return:
        None
    '''
    f = open(filename, "a")
    writer = csv.DictWriter(f, fieldnames = fieldnames)

    record = dict()
    record['FTID'] = input("FTID[]: ")
    record['Nomen'] = input("Nomenclature[]: ")
    record['Asset Tag'] = input("Asset Tag[]: ")
    record['Location'] = input("Location[]: ")
    writer.writerow(record)
    f.close()
    return()

def list_equipment(fn, fields):
    '''
    Read the file and display contents
    Args:
        fn - filename of the inventory file
    Return:
        data - all the equipment in a dictionary reader object
    '''
    f = open(fn, "r")
    reader = csv.DictReader(f, fieldnames=fields)
    print("   \tFTID\tAsset Tag\t\tNomen\tUser\tDate Checked Out")
    for index, row in enumerate(reader):
        print("{} - \t{}\t\t{}\t\t{}\t\t{}\t\t{}".format(index+1, row['FTID'],
               row['Asset Tag'], row['Nomen'],
               row['User'], row['Date Checked Out']))
    print("\n")
    f.close()
    return()

def checkout_equipment(fn, fields):
    '''
    Checkout equipement by selecting a record and adding more metadata to it

    Args:
        fieldnames - list of top row of csv file
    Return:
        None
    '''
    # List the all the equipment, already checked out or not
    all_equipment = list_equipment(fn, fields)

    # Request user to select equipment
    rownum = int(input("enter line number of equipment to check out: "))-1

    # Prompt for additional metadata
    # Use today's date for checkout date

    # update file
    with open(fn, "r") as f:
        reader = csv.DictReader(f, fieldnames = fields)
        contents = [row for row in reader]

    contents[rownum]['Date Checked Out'] = str(date.today())
    contents[rownum]['User'] = input("name: ")

    with open(fn, "w") as f:
        writer = csv.DictWriter(f, fieldnames = fields)
        for row in contents:
            writer.writerow(row)
    
def return_equipment(fn, fields):
    '''
    Remove the metadata to check in the equipment
    Args:
        None
    Return:
        None
    '''
    # List the all the equipment, already checked out or not
    all_equipment = list_equipment(fn, fields)

    # Request user to select equipment
    rownum = int(input("enter line number of equipment to return: "))-1

    # update file
    with open(fn, "r") as f:
        reader = csv.DictReader(f, fieldnames = fields)
        contents = [row for row in reader]

    # Remove the meta data for that record
    contents[rownum]['Date Checked Out'] = None
    contents[rownum]['User'] = None
 
    with open(fn, "w") as f:
        writer = csv.DictWriter(f, fieldnames = fields)
        for row in contents:
            writer.writerow(row)
    return() 

def del_equipment(fn, fields):
    '''
    Delete a piece of inventory 
    Args:
        None
    Return:
        None
    '''
    # List the all the equipment, already checked out or not
    all_equipment = list_equipment(fn, fields)

    # Request user to select equipment
    rownum = int(input("enter line number of equipment to delete: "))-1

    # update file
    with open(fn, "r") as f:
        reader = csv.DictReader(f, fieldnames = fields)
        contents = [row for index,row in enumerate(reader) if rownum != index]

 
    with open(fn, "w") as f:
        writer = csv.DictWriter(f, fieldnames = fields)
        for row in contents:
            writer.writerow(row)
    return() 
def send_email():
    return()

if __name__  == '__main__':
# open data file and read in contents
    fieldnames = ['FTID', 'Nomen', 'Asset Tag', 'Location',
                      'User', 'Date Checked Out', 'Expected Return']
    filename = 'inventory.csv'


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
            add_equipment(filename, fieldnames)
        elif ans == 'c':
            print("\nCheckout Equipment")
            checkout_equipment(filename, fieldnames)
        elif ans == 'r':
            print("\nReturn Equipment")
            return_equipment(filename, fieldnames)
        elif ans == 'd':
            print("\nDelete Equipment from Inventory")
            del_equipment(filename, fieldnames)
        elif ans == 'l':
            print("\nList All Equipment")
            list_equipment(filename, fieldnames)
        elif ans == 's':
            print("\nSending email...")
            send_email()
        else:
            ans = 'q'
            print("Exiting")

