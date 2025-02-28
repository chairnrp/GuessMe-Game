welcome_mesage = "Halo selamat datang di GuessME"

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
jawaban = input("{YA / TIDAK} --> ") 

# masuk ke pengkondisian

if jawaban == "YA": # jika YA -- maka
  print("------------------------------------")
  print("≽^•⩊•^≼ : Nama mu siapa? ")
  nama = input("Masukan nama: ")
  print(f" ≽^•⩊•^≼ : halo {nama}, selamat datang, kamu sudah tau aku bernama Gusy, ini adalah game tebak tebakan sederhana")
  print("≽^•⩊•^≼ : pilih tingkah kesusahan sebelum bermain! ")

  print("------------------------------------")
  difficulty = input("{EASY | MEDIUM | HARD} --> ")
  print("------------------------------------")

  # masuk ke percabangan lagi

  if difficulty == "EASY":
    print("≽^•⩊•^≼ : kamu memilih EASY, ayo bermain!!!!")

  elif difficulty == "MEDIUM":
    print("≽^•⩊•^≼ : kamu memilih MEDIUM, ayo bermain!!!!")

  elif difficulty == "HARD":
    print("≽^•⩊•^≼ : kamu memilih HARD, wah kamu sigma bangeutt, ayo bermain!!!!")

elif jawaban == "ya": # jika ya -- maka
  print("------------------------------------")
  print("≽^•⩊•^≼ : Nama mu siapa? ")
  nama = input("Masukan nama: ")
  print(f" ≽^•⩊•^≼ : halo {nama}, selamat datang, kamu sudah tau aku bernama Gusy, ini adalah game tebak tebakan sederhana")
  print("≽^•⩊•^≼ : pilih tingkah kesusahan sebelum bermain! ")

  print("------------------------------------")
  difficulty = input("{EASY | MEDIUM | HARD} ")
  print("------------------------------------")

  # masuk ke percabangan lagi

  if difficulty == "EASY":
    print("≽^•⩊•^≼ : kamu memilih EASY, ayo bermain!!!!")

  elif difficulty == "MEDIUM":
    print("≽^•⩊•^≼ : kamu memilih MEDIUM, ayo bermain!!!!")

  elif difficulty == "HARD":
    print("≽^•⩊•^≼ : kamu memilih HARD, wah kamu sigma bangeutt, ayo bermain!!!!")

elif jawaban == "Ya": # jika Ya -- maka
  print("------------------------------------")
  print("≽^•⩊•^≼ : Nama mu siapa? ")
  nama = input("Masukan nama: ")
  print(f" ≽^•⩊•^≼ : halo {nama}, selamat datang, kamu sudah tau aku bernama Gusy, ini adalah game tebak tebakan sederhana")
  print("≽^•⩊•^≼ : pilih tingkah kesusahan sebelum bermain! ")

  print("------------------------------------")
  difficulty = input("EASY | MEDIUM | HARD ")
  print("------------------------------------")

  # masuk ke percabangan lagi

  if difficulty == "EASY":
    print("≽^•⩊•^≼ : kamu memilih EASY, ayo bermain!!!!")

  elif difficulty == "MEDIUM":
    print("≽^•⩊•^≼ : kamu memilih MEDIUM, ayo bermain!!!!")

  elif difficulty == "HARD":
    print("≽^•⩊•^≼ : kamu memilih HARD, wah kamu sigma bangeutt, ayo bermain!!!!")

else:
  print("------------------------------------")
  print("Yaaa sayang sekali :()")
  print("------------------------------------")
