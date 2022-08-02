from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

contacts_list_string = []
for contact in contacts_list:
    contacts_list_string.append(','.join(contact))
      
pattern_name = r"^(\w+)\s?\,?(\w+)\s?\,?(\w*)\,{1,3}"
contacts_list_name = []
for contact in contacts_list_string:
    contacts_list_name.append(re.sub(pattern_name, r"\1,\2,\3,", contact))

pattern_number = r"(\+?\d?\s?)\(?(\d+)\)?.?(\d{3}).?(\d{2}).?(\d{2})"
contacts_list_number = []
for contact in contacts_list_name:
    contacts_list_number.append(re.sub(pattern_number, r"+7(\2)\3-\4-\5", contact))

pattern_extension = r"\(?(\доб+)\.?\s?(\d+)\)?"
contacts_list_number_extension = []
for contact in contacts_list_number:
    contacts_list_number_extension.append(re.sub(pattern_extension, r"\1.\2", contact))

contacts_list_result = []
contacts_list_number_extension.sort()
for contact in contacts_list_number_extension:
    contacts_list_result.append(contact.split(','))

result = [['lastname','firstname','surname','organization','position','phone','email']]
for contact in contacts_list_result:
        if contact[0] == result[-1][0]:
            for i in range(1,5):
                if len(contact[-i]) >= len(result[-1][-i]):
                    result[-1][-i] = contact[-i]
        else:
            result.append(contact)

pprint(result)

def whrit_file (file_name, result):
    with open(file_name, "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(result)

if __name__=='__main__':
    pass
    whrit_file("phonebook.csv", result)