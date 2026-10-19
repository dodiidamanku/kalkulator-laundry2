import streamlit as st

st.title("Aplikasi Kasir Doctor Laundry")
st.write("Selamat datang! Silakan hitung tagihan pelanggan.")

layanan = st.radio("Pilih Jenis Layanan:", ["Cuci Reguler", "Cuci Kilat"])

if layanan == "Cuci Reguler":
    harga_per_kg = 8000
else:
    harga_per_kg = 15000

berat_pakaian = st.number_input("Masukkan berat pakaian (kg):", min_value=0)
total_tagihan = harga_per_kg * berat_pakaian

if st.button("Hitung Tagihan"):
    st.success("--- Struk Bukti Pembayaran ---")
    st.write("Layanan:", layanan)
    st.write("Harga per kg: Rp", harga_per_kg)
    st.write("Total Tagihan: Rp", total_tagihan)
  
