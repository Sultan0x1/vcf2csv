import os
import vobject 
import argparse 
import unicodecsv as csv

parser = argparse.ArgumentParser(description='Convert vCard file to CSV file')
parser.add_argument("input", help="the vCard file name")
parser.add_argument("output", help="the CSV file name")

args = parser.parse_args()

input_file = args.input
output_file = args.output

csv_file = open(output_file, 'wb') 
writer = csv.writer(csv_file, encoding='utf-8-sig')

writer.writerow(['First Name', 'Work Tel', 'Mobile Tel', 'CUSTOM EMAIL', 'HOME EMAIL'])
 
fields = ["fn", "tel", "email"] 

with open(input_file, 'r', encoding='utf-8-sig') as f:
    data = f.read()
    vcards = vobject.readComponents(data)
    for vcard in vcards:
        row = []
        for field in fields:
            try:
                row.append(vcard.contents[field][0].value)
                if field == 'email' or field == 'tel':
                    try:
                        row.append(vcard.contents[field][1].value)
                    except:
                        row.append('')
                        continue
            except:
                row += ['', '']
        writer.writerow(row)

csv_file.close()
