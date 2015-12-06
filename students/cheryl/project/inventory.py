#!/usr/bin/env python

import csv
import os.path
from datetime import date
import smtplib


class FTInventory:
    '''
    Flight Test Equipment Inventory class
    '''
    def __init__(self, filename):
        self.fieldnames = ['FTID', 'Nomen', 'Asset Tag', 'Location',
                           'Name', 'Date Checked Out', 'Expected Return']
        self.filename = filename

    def read(self):
        '''
        Read the file into memory
        '''
        try:
            with open(self.filename, "r") as f:
                #  reader = csv.DictReader(f, self.fieldnames)
                reader = csv.DictReader(f)
                self.contents = [row for row in reader]
        except FileNotFoundError:
            self.contents = []

    def append(self, new_record):
        '''
        Append content
        '''
        self.read()
        self.contents.append(new_record)

    def write(self):
        '''
        Write out to the file
        '''
        with open(self.filename, "w") as f:
            writer = csv.DictWriter(f, fieldnames=self.fieldnames)
            writer.writeheader()
            for row in self.contents:
                writer.writerow(row)

    def add_equipment(self):
        '''
        Create a new record and add it to the file
        '''
        record = dict.fromkeys(self.fieldnames, None)
        record['FTID'] = input("FTID[]: ")
        record['Nomen'] = input("Nomenclature[]: ")
        record['Asset Tag'] = input("Asset Tag[]: ")
        record['Location'] = input("Location[]: ")
        self.append(record)
        self.write()

    def list_equipment(self):
        '''
        Format and display contents
        '''
        self.read()
        print("   \tFTID\tAsset Tag\t\tNomen\tUser\tDate Checked Out")
        for index, row in enumerate(self.contents):
            print("{} - \t{}\t\t{}\t\t{}\t\t{}\t\t{}".
                  format(index+1, row['FTID'], row['Asset Tag'],
                         row['Nomen'], row['Name'], row['Date Checked Out']))
        print("\n")

    def checkout_equipment(self):
        '''
        Checkout equipment by selecting a record
        and adding more metadata to it
        '''
        # List the all the equipment, already checked out or not
        self.list_equipment()

        # Request user to select equipment
        rownum = int(input
                     ("enter line number of equipment to check out: ")) - 1

        # Prompt for additional metadata
        # Use today's date for checkout date
        self.contents[rownum]['Date Checked Out'] = str(date.today())
        self.contents[rownum]['Name'] = input("name: ")
        self.write()

    def return_equipment(self):
        '''
        Remove the metadata to check in the equipment
        '''
        # List the all the equipment, already checked out or not
        self.list_equipment()

        # Request user to select equipment
        rownum = int(input("enter line number of equipment to return: ")) - 1

        # Remove the meta data for that record
        self.contents[rownum]['Date Checked Out'] = None
        self.contents[rownum]['Name'] = None
        self.write()

    def del_equipment(self):
        '''
        Delete a piece of inventory
        '''
        # List the all the equipment, already checked out or not
        self.list_equipment()

        # Request user to select equipment
        rownum = int(input("enter line number of equipment to delete: "))-1

        # update file
        del self.contents[rownum]
        self.write()

    def send_email(self):
        '''
        send email to admin
        '''
        self.read()
        message = str()
        message.join("   \tFTID\tAsset Tag\t\tNomen\tUser\tDate Checked Out")
        for index, row in enumerate(self.contents):
            message.join("{} - \t{}\t\t{}\t\t{}\t\t{}\t\t{}".
                         format(index+1,
                                row['FTID'], row['Asset Tag'],
                                row['Nomen'],
                                row['Name'], row['Date Checked Out']))
        server = smtplib.SMTP('localhost')
        server.sendmail(triageuser@dst.com, admin@dst.com, message)
        server.quit()

if __name__ == '__main__':
    # open data file and read in contents
    ft = FTInventory("inventory.csv")

    ans = ''
    while ans != 'q':
        ans = input("s-send email\n" +
                    "c-checkout equipment\n" +
                    "a-add equipment\n" +
                    "r-return equipment\n" +
                    "d-delete equipment\n" +
                    "l-list equipment\n" +
                    "q-quit\t[q]:")
        if ans == 'a':
            print("\nAdd Equipment to Inventory")
            ft.add_equipment()
        elif ans == 'c':
            print("\nCheckout Equipment")
            ft.checkout_equipment()
        elif ans == 'r':
            print("\nReturn Equipment")
            ft.return_equipment()
        elif ans == 'd':
            print("\nDelete Equipment from Inventory")
            ft.del_equipment()
        elif ans == 'l':
            print("\nList All Equipment")
            ft.list_equipment()
        elif ans == 's':
            print("\nSending email...")
            ft.send_email()
        else:
            ans = 'q'
            print("Exiting")
