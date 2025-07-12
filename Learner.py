import streamlit as st

st.set_page_config(page_title="Kalkulator Streamlit", page_icon="🧮")

st.title("🧮 Kalkulator Sederhana")
st.write("Masukkan dua angka, pilih operasi, dan lihat hasilnya.")

# Input angka
angka1 = st.number_input("Masukkan angka pertama:", step=1.0)
angka2 = st.number_input("Masukkan angka kedua:", step=1.0)

# Pilihan operasi
operasi = st.selectbox("Pilih operasi matematika:", ["Penjumlahan", "Pengurangan", "Perkalian", "Pembagian"])

# Tombol Hitung
if st.button("Hitung"):
    if operasi == "Penjumlahan":
        hasil = angka1 + angka2
        st.success(f"Hasil: {angka1} + {angka2} = {hasil}")
    elif operasi == "Pengurangan":
        hasil = angka1 - angka2
        st.success(f"Hasil: {angka1} - {angka2} = {hasil}")
    elif operasi == "Perkalian":
        hasil = angka1 * angka2
        st.success(f"Hasil: {angka1} × {angka2} = {hasil}")
    elif operasi == "Pembagian":
        if angka2 != 0:
            hasil = angka1 / angka2
            st.success(f"Hasil: {angka1} ÷ {angka2} = {hasil}")
        else:
            st.error("Error: Pembagian dengan nol tidak diperbolehkan.")
