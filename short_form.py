text=input('enter sentence: ')
word_list=text.split()
short_form=''
for i in word_list:
    short_form=short_form+i[0].upper()
print(short_form)
