import random

welcome_mesage = "Halo selamat datang di GuessME"
gusy_location = random.randint(1,5)

print("####################################")
print("############# GuessME ##############")
print("####################################")

gusy = """
   n n
  ('-')
  (   )╮    <--- ini gusy
 /(   )\\
  ^^ ^^
"""
print(gusy)

print("≽^•⩊•^≼ : Halo aku Gusy, apa kamu siap bermain? ")

print("------------------------------------") # pemasukan input
jawaban = input("{YA | TIDAK} --> ")

# masuk ke pengkondisian

if jawaban == "YA": # jika YA -- maka
  print("------------------------------------")
  print("≽^•⩊•^≼ : Nama mu siapa? ")
  nama = input("Namaku adalah... ")
  print(f" ≽^•⩊•^≼ : halo {nama}, selamat datang, kamu sudah tau aku bernama Gusy, ini adalah game tebak tebakan sederhana")
  print("≽^•⩊•^≼ : pilih tingkah kesusahan sebelum bermain! ")

  print("------------------------------------")
  difficulty = input("{EASY | MEDIUM | HARD} --> ")
  print("------------------------------------")

  # masuk ke percabangan lagi

  if difficulty == "EASY":
    print("≽^•⩊•^≼ : kamu memilih EASY, ayo bermain!!!!")
    print("------------------------------------")
    print("≽^•⩊•^≼ : sekarang perhatikan lubang di bawah ini!!")
    print('''

    |_| |_| |_| |_| |_|
     1   2   3   4   5

    di lubang manakah aku berada???

    ''')
    tebakan = input("|1|2|3|4|5| --> ")

    if tebakan == gusy_location:
      print(f"selamat {nama} kamu berhasil!!!!!")
      respon = input("kembali ke menu awal? {YA | TIDAK}  ")
    else:
      print(f"ayo {nama} coba lagi!!!")
      respon = input("kembali ke menu awal? {YA | TIDAK)}  ")

######

  elif difficulty == "MEDIUM":
    print("≽^•⩊•^≼ : kamu memilih MEDIUM, ayo bermain!!!!")
    print("------------------------------------")
    print("≽^•⩊•^≼ : sekarang perhatikan lubang di bawah ini!!")
    print('''

    |_| |_| |_| |_| |_|
     1   2   3   4   5

    di lubang manakah aku berada???

    ''')
    tebakan = input("|1|2|3|4|5| --> ")

    if tebakan == gusy_location:
      print(f"selamat {nama} kamu berhasil!!!!!")
      respon = input("kembali ke menu awal? {YA | TIDAK}  ")
    else:
      print(f"ayo {nama} coba lagi!!!")
      respon = input("kembali ke menu awal? {YA | TIDAK}  ")


######

  elif difficulty == "HARD":
    print("≽^•⩊•^≼ : kamu memilih HARD, wah kamu sigma bangeutt, ayo bermain!!!!")
    print("≽^•⩊•^≼ : sekarang perhatikan lubang di bawah ini!!")
    print('''

    |_| |_| |_| |_| |_|
     1   2   3   4   5

    di lubang manakah aku berada???

    ''')
    tebakan = input("|1|2|3|4|5| --> ")

    if tebakan == gusy_location:
      print(f"selamat {nama} kamu berhasil!!!!!")
      respon = input("kembali ke menu awal? {YA | TIDAK}  ")
    else:
      print(f"ayo {nama} coba lagi!!!")
      respon = input("kembali ke menu awal? {YA | TIDAK}  ")



#####

else:
  print("------------------------------------")
  print("Yaaa sayang sekali :()")
  print("------------------------------------")
