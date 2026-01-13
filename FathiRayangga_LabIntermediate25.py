secret_word = "Bumame"
user_input = input("Masukkan satu huruf: ")
if len(user_input) != 1:
    print("Input tidak valid. Harus satu huruf saja.")
elif not user_input.isalpha():
    print("Input tidak valid. Harus berupa huruf.")
else:
    if user_input.lower() in secret_word.lower():
        print("Huruf ADA di dalam secret word.")
    else:
        print("Huruf TIDAK ADA di dalam secret word.")