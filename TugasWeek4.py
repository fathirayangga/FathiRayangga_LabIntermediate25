kata_list = ["prasmul", "eka", "csl", "bumame"]
menang = 0
kalah = 0
skor = 0
print("GAME HANGMAN")
index = 0
while index < len(kata_list):
    kata = kata_list[index]
    index += 1
    huruf_tertebak = []
    kesempatan = 6
    print("\nKata baru dimulai")
    while kesempatan > 0:
        tampilan = ""
        for huruf in kata:
            if huruf in huruf_tertebak:
                tampilan += huruf + " "
            else:
                tampilan += "_ "
        print("\nKata:", tampilan)
        print("Kesempatan:", kesempatan)
        tebakan = input("Tebak huruf: ").lower()
        if tebakan not in huruf_tertebak:
            huruf_tertebak.append(tebakan)
        kesempatan -= 1
        selesai = True
        for huruf in kata:
            if huruf not in huruf_tertebak:
                selesai = False
        if selesai:
            print("\nKamu MENANG!")
            print("Kata:", kata)
            menang += 1
            skor += 10
            break
    if kesempatan == 0:
        print("\nKamu KALAH!")
        print("Kata yang benar:", kata)
        kalah += 1
        skor -= 5
    print("\nSkor sementara")
    print("Menang:", menang)
    print("Kalah:", kalah)
    print("Skor:", skor)
    if index == len(kata_list):
        break
    ulang = input("\nMain lagi? (mau/tidak): ").lower()
    if ulang != "mau":
        break
print("\nGAME SELESAI")
print("Skor akhir:", skor)
print("Total menang:", menang)
print("Total kalah:", kalah)