import converter
linkadd=input('Give the link of html page where your table is present: \n')
address=input('Give the address of the output file with file name: \n')
number=input('Give the no of table you want on that page: \n')
choice=int(input('1.to excel  2.to json 3.to csv :'))
if choice==1:
    address=address+'.xls'
    data=converter.link(linkadd,address,number)
    data.toexcel()
elif choice==2:
    address=address+'.json'
    data=converter.link(linkadd,address,number)
    data.tojson()
elif choice==3:
    address=address+'.csv'
    data=converter.link(linkadd,address,number)
    data.tocsv()
else:
    print('wrong input')


