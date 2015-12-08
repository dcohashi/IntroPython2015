from inventory import FTInventory

def test_init():
    ft = FTInventory("test.csv")
    assert ft.filename is "test.csv"

def make_test_file():
    with open("test.csv", "w") as f:
        f.write("FTID,Nomen,Asset Tag,Location,Name,Date Checked Out\n")
        f.write("FT1234,PC,A34555,Target,None,None\n")
        f.write("FT1111,PC,A423444,TargetA,Cheryl,Oct-2-2015\n")

def test_read():
    make_test_file()
    ft = FTInventory("test.csv")
    ft.read()
    print(ft.contents[0])
    assert ft.contents[1]['Location'] == "TargetA"

def test_read_none():
    ft = FTInventory("none.csv")
    ft.read()
    assert ft.contents == []

def test_append():
    make_test_file()
    ft = FTInventory("test.csv")
    ft.append({"FTID": "FT2222", "Nomen": "printer", "Asset Tag": None,
        "Location": "TargetA","Name": None,"Checked Out Date": None})
    print(ft.contents[2])
    assert ft.contents[2]['Nomen'] == 'printer'

def test_checkout_equipment():
    make_test_file()
    ft = FTInventory("test.csv")
    ft.input = lambda _: ('NewName')
    ft.checkout_equipment()

def test_del_equipment():
    make_test_file()
    ft = FTInventory("test.csv")
    with open('test.csv') as f:
        count = sum(1 for _ in f)
    ft.input = lambda _: ('1')
    ft.del_equipment()
    with open('test.csv') as f:
        count1 = sum(1 for _ in f)
    assert count1 == count -1 

