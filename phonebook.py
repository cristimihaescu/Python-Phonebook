# Do not modify this list
from tokenize import StringPrefix


phone_list = ["98-777-653", "98-742-644", "34-855-326", "34-25-629", "34-489-115", "72-999-563", "9-321-459",
              "72-654-121", "72-4-694", "72-255-313", "98-111-323", "98-433-14", "34-577-342", "98-323-000",
              "98-202-666", "34-5435-454", "34-515-633"]

ugly_phone_list = ["98-333-111", "12--323-566", "123-34-221", "99-948-321", "-12-123-346",
                     "894-58438-543", "85-234-222",
                     "12-333-444-", "99-888--433", "15-465-876", "98-555-22", "-3-355-333", "3--344-53", "--2--45---",
                     "11-111-222", "12#22$34$222", "98 223 555"]
valid_numbers = []
invalid_numbers = []
complete_phone_list = (phone_list + ugly_phone_list)
for number in phone_list:

    if len(number)== 10:
        valid_numbers.append(number)

    if len(number)!=10:
        invalid_numbers.append(number)

for number in ugly_phone_list:

    if len(number)== 10:
        valid_numbers.append(number)

    if len(number)!=10:
        invalid_numbers.append(number)

print("     ")
print("These are the valid phone numbers in your phonebook:" + str(valid_numbers))
print("     ")
print("and these are the invalid ones:" + str(invalid_numbers))
print("""       """)
print("These are the correct area codes:")
print("""       """)

correct_area_numbers = list()
incorrect_area_numbers = list()


for area_codes in valid_numbers:
    if area_codes[0:2] == ("98"):
        correct_area_numbers.append(area_codes[0:2])
    elif area_codes[0:2] ==("34"):
        correct_area_numbers.append(area_codes[0:2])
    elif area_codes[0:2] == ("72"):
        correct_area_numbers.append(area_codes[0:2])
print(correct_area_numbers)
print("""       """)
print("These are the wrong area codes:")
print("""       """)
for incorrect_area_codes in complete_phone_list:
    if incorrect_area_codes[0:2] != ("98") and incorrect_area_codes[0:2] != ("34") and incorrect_area_codes[0:2] != ("72"):
        incorrect_area_numbers.append(incorrect_area_codes[0:2])
print(incorrect_area_numbers)
print("""       """)
print("These are the numbers without area codes:")
print("""       """)
numbers_without_area_codes = []
for scadere in valid_numbers:
        numbers_without_area_codes.append(scadere[3:11])
print(numbers_without_area_codes)
print("""       """)
print("The unique area codes are:")
print("""   """)
unique_area_codes1 = []
for unique_area_codes in valid_numbers:
    if unique_area_codes[0:2] != ("98") and unique_area_codes[0:2] != ("34") and unique_area_codes[0:2] != ("72"):
        unique_area_codes1.append(unique_area_codes[0:2])
print(unique_area_codes1)

print("""   """)
count1 = []
count2 = []
count3 = []
for count in valid_numbers:
    if count[0:2] == ("98"):
        count1.append(count)
print("You have",(len(count1)),"numbers from area 98")
print("""   """)
for count in valid_numbers:
    if count[0:2] == ("34"):
        count2.append(count)
print("You have",(len(count2)),"numbers from area 34")
print("""   """)
for count in valid_numbers:
    if count[0:2] == ("72"):
        count3.append(count)
print("You have",(len(count3)),"numbers from area 72")




# "These are the pretty phone numbers:"
# "and these are the ugly ones:"
