# Program menentukan apakah suatu tahun adalah tahun kabisat

# masukan tahun
year = int(input("Masukkan tahun: "))

# Menentukan apakah tahun tersebut kabisat atau bukan

if (year % 400 == 0):
    print(f"{year} adalah tahun kabisat.")
elif (year % 4 == 0 and year % 100 != 0):
    print(f"{year} adalah tahun kabisat.")
else:
    print(f"{year} bukan tahun kabisat.")