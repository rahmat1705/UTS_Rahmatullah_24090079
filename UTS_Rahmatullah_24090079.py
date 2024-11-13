# Program Kalkulator Kesehatan BMI

def hitung_bmi(berat, tinggi):
    """Fungsi menghitung BMI"""
    return berat / (tinggi ** 2)

def rekomendasi_bmi(bmi):
    """Fungsi buat memberikan rekomendasi berdasarkan nilai BMI"""
    if bmi < 18.5:
        return " termasuk dalam kategori Underweight (Kurang Berat Badan)."
    elif 18.5 <= bmi < 24.9:
        return " termasuk dalam kategori Normal weight (Berat Badan Normal)."
    elif 25 <= bmi < 29.9:
        return " termasuk dalam kategori Overweight (Kelebihan Berat Badan)."
    else:
        return " termasuk dalam kategori Obesity (Terlalu Gemuk)."

def main():
    print("Selamat datang kawannn di Kalkulator BMI!")
    
    # input dari pengguna
    try:
        berat = float(input("Masukkan berat badan Anda (dalam kg): "))
        tinggi = float(input("Masukkan tinggi badan Anda (dalam meter): "))
        
        # Menghitung BMI
        bmi = hitung_bmi(berat, tinggi)
        
        # Menampilkan hasil
        print(f"\nBMI Anda adalah: {bmi:.2f}")
        print(rekomendasi_bmi(bmi))
        
    except ValueError:
        print("Input tidak valid. Pastikan Anda memasukkan angka yang benar.")

if __name__ == "__main__":
    main()