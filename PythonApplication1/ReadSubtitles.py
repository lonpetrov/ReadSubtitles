
from tkinter import Tk
from tkinter.filedialog import askopenfile
from tkinter.messagebox import askyesno
from tkinter.messagebox import askyesnocancel
from itertools import groupby

Tk().withdraw()
filename = askopenfile(initialdir="/", title="Select Subtitle file",
					  filetypes=(("SRT files", "*.srt"),))
with open("knownwords.txt","r") as kw:
	kw2 = kw.read()
	kw3 = ''.join(symbol for symbol in kw2 if symbol.isalpha() or symbol =="\'" or symbol == "\n")
	knownwords_raw = list(kw3.lower().split("\n"))
	knownwords_1 = [line for line, _ in groupby(sorted(knownwords_raw))]
	knownwords = [line for line in knownwords_1 if line != '']
	knownwords = [line.lower() for line in knownwords]


dirty_subtitles = filename.read()
clean_subtitles = ''.join(symbol for symbol in dirty_subtitles if symbol.isalpha() or symbol.isspace() or symbol =="\'")
clean_subtitles = clean_subtitles.replace("\n","")
list_of_words = list(clean_subtitles.split(" "))
list_of_words_2 = [line for line in list_of_words if line != '']
list_of_words_2 = [line.lower() for line in list_of_words_2]
list_of_words_short = [line for line, _ in groupby(sorted(list_of_words_2))]
filtered_list_of_words = [line for line in list_of_words_short if line not in knownwords]

want_to_choose_words = askyesno("Выбрать выученные слова", "Выбрать выученные слова?")
final_list =[]
if want_to_choose_words == True:
	count1 = len(filtered_list_of_words)
	count2 = 0
	
	for line in filtered_list_of_words:
		counter = count1-count2
		res = "%s будет добавлено в список усвоенных слов \n Осталось слов: %d" % (line, counter)
		add_word = askyesno("Добавить слово", res)
		if add_word == True:
			with open("knownwords.txt","a") as word:
				word.write(line + "\n")
			knownwords.append(line)
			count2 =count2+1
		else:
			continue
	final_list = [line for line in filtered_list_of_words if line not in knownwords]
else:
	final_list = filtered_list_of_words

save_to_list = askyesno("Сохранить слова в файл", "Сохранить слова в файл?")
if save_to_list == True:
	with open("list.txt","w") as lis:
		for index in final_list:
			lis.write(index + "\n")
	



#print(filtered_list_of_words)
#print(len(filtered_list_of_words))
#print(len(list_of_words_short))