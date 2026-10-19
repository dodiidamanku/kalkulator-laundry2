import streamlit as st

st.title("Aplikasi Kasir Doctor Laundry")
st.write("Selamat datang! Silakan hitung tagihan pelanggan di bawah ini.")

# 1. Kasir memilih jenis layanan (menggantikan input teks biasa)
layanan = st.radio("Pilih Jenis Layanan:", ["Cuci Reguler", "Cuci Kilat"])

# 2. Komputer mengambil keputusan harga (Logika If/Else)
if layanan == "Cuci Reguler":
    harga_per_kg = 8000
else:
    harga_per_kg = 15000

# 3. Kasir memasukkan angka berat (menggantikan input teks biasa)
berat_pakaian = st.number_input("Masukkan berat pakaian (kg):", min_value=0)

# 4. Menghitung total
total_tagihan = harga_per_kg * berat_pakaian

# 5. Tombol untuk memunculkan struk
if st.button("Hitung Tagihan"):
    st.success("--- Struk Bukti Pembayaran ---")
    st.write("Layanan:", layanan)
    st.write("Harga per kg: Rp", harga_per_kg)
    st.write("Total Tagihan: Rp", total_tagihan)
