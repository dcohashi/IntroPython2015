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
        ret_str = "   - {:<12}\t{:<12}\t{:<20}\t{:<20}\t{:<20}\n".format(
                "FTID", "Asset Tag", "Nomen", "User", "Date Checked Out")
        for index, row in enumerate(self.contents):
            ret_str = "\n".join((ret_str,
                                 "{} - {:<12}\t{:<12}\t{:<20}\t{:<20}\t{:<20}".
                                 format(index+1, row['FTID'], row['Asset Tag'],
                                        row['Nomen'], row['Name'],
                                        row['Date Checked Out'])))
        return(ret_str)

    def select_a_row(self):
        '''
        List all the equipment and request a row number
        '''
        # List the all the equipment
        print(self.list_equipment())

        # Request user to select equipment
        rownum = int(input("select a line number: "))-1
        return(rownum)

    def checkout_equipment(self):
        '''
        Checkout equipment by selecting a record
        and adding more metadata to it
        '''
        rownum = self.select_a_row()

        # Prompt for additional metadata
        # Use today's date for checkout date
        try:
            self.contents[rownum]['Date Checked Out'] = str(date.today())
            self.contents[rownum]['Name'] = input("name: ")
        except IndexError:
            print("Invalid row")
        else:
            self.write()

    def return_equipment(self):
        '''
        Remove the metadata to check in the equipment
        '''
        # Request user to select equipment
        rownum = self.select_a_row()

        # Remove the meta data for that record
        try:
            self.contents[rownum]['Date Checked Out'] = None
            self.contents[rownum]['Name'] = None
        except IndexError:
            print("Invalid row")
        else:
            self.write()

    def del_equipment(self):
        '''
        Delete a piece of inventory
        '''
        rownum = self.select_a_row()
        # update file
        try:
            del self.contents[rownum]
        except IndexError:
            print("Invalid selection")
        else:
            self.write()

    def send_email(self):
        '''
        send email to admin
        '''
        message = "".join(("To: Cheryl.Ohashi@gmail.com",
                           "From: cheryl.ohashi@gmail.com",
                           "Subject: FTInventory",
                           "Flight Test Inventory\n",
                           self.list_equipment()))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("cheryl.ohashi@gmail.com", "passwd")
        server.sendmail("cheryl.ohashi@gmail.com",
                        "cheryl.ohashi@gmail.com", message)
        server.quit()

if __name__ == '__main__':
    # open data file and read in contents
    ft = FTInventory("inventory.csv")

    ans = ''
    while ans != 'q':
        ans = input("c-checkout equipment\n" +
                    "a-add equipment\n" +
                    "r-return equipment\n" +
                    "d-delete equipment\n" +
                    "l-list equipment\n" +
                    "s-send email\n" +
                    "q-quit\t\t[q]:")
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
            print(ft.list_equipment())
        elif ans == 's':
            print("\nSending email...")
            ft.send_email()
        else:
            ans = 'q'
            print("Exiting")
