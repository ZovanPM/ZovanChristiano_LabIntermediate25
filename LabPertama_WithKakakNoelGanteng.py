secret_word = "Phoenix"

letter = input("Masukkan satu huruf: ")

if len(letter) !=1 or not letter.isalpha():
	print ("Input tidak valid. Masukkan satu huruf saja. ")

if letter.lower() in secret_word.lower():
	print("Huruf ada di dalam secret word")
else: 
	print("Huruf tidak ada di dalam secret word")
