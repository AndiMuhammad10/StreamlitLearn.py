import streamlit as st

st.set_page_config(page_title="Kalkulator Lengkap", page_icon="🧠")

st.title("🧮 KALKULATOR COC 1.0")
st.write("Masukkan dua angka, pilih operasi, dan lihat hasil serta caranya!")

# Input
angka1 = st.number_input("Masukkan angka pertama:", step=1.0, format="%.2f")
angka2 = st.number_input("Masukkan angka kedua:", step=1.0, format="%.2f")

# Operasi
operasi = st.selectbox("Pilih operasi:", ["Penjumlahan", "Pengurangan", "Perkalian", "Pembagian"])

# Tombol Hitung
if st.button("Hakai"):
    st.divider()
    
    if operasi == "Penjumlahan":
        hasil = angka1 + angka2
        st.success(f"Hasil: {hasil}")
        st.write("### Cara Pengerjaan:")
        st.latex(f"{angka1} + {angka2} = {hasil}")
        st.caption("Rumus: a + b = hasil")
    
    elif operasi == "Pengurangan":
        hasil = angka1 - angka2
        st.success(f"Hasil: {hasil}")
        st.write("### Cara Pengerjaan:")
        st.latex(f"{angka1} - {angka2} = {hasil}")
        st.caption("Rumus: a - b = hasil")
    
    elif operasi == "Perkalian":
        hasil = angka1 * angka2
        st.success(f"Hasil: {hasil}")
        st.write("### Cara Pengerjaan:")
        st.latex(f"{angka1} \\times {angka2} = {hasil}")
        st.caption("Rumus: a × b = hasil")
    
    elif operasi == "Pembagian":
        if angka2 != 0:
            hasil = angka1 / angka2
            st.success(f"Hasil: {hasil}")
            st.write("### Cara Pengerjaan:")
            st.latex(f"\\frac{{{angka1}}}{{{angka2}}} = {hasil}")
            st.caption("Rumus: a ÷ b = hasil")
        else:
            st.error("Tidak bisa membagi dengan nol.")
          
