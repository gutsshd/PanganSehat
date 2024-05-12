import streamlit as st

base="light"
backgroundColor="#bce6ec"

def berat_badan_ideal(tinggi, jenis_kelamin):
    """Fungsi untuk menghitung berat badan ideal berdasarkan tinggi dan jenis kelamin"""
    jenis_kelamin = jenis_kelamin.lower()  # Normalisasi input jenis kelamin
    if jenis_kelamin == 'pria':
        berat_ideal = (tinggi_cm - 100) - ((tinggi_cm - 150) * 0.1)
    elif jenis_kelamin == 'wanita':
        berat_ideal = (tinggi_cm - 100) - ((tinggi_cm - 150) * 0.15)
    else:
        return "Jenis kelamin tidak valid. Masukkan 'pria' atau 'wanita'."
    return berat_ideal

def hitung_kalori(berat_badan_ideal, umur, jenis_kelamin, tinggi_cm):
    """Fungsi untuk menghitung jumlah kalori yang harus dikonsumsi setiap hari untuk mencapai berat badan ideal"""
    jenis_kelamin = jenis_kelamin.lower()  # Normalisasi input jenis kelamin
    if jenis_kelamin == 'pria':
        kalori = 88.362+(13.397 * berat_badan_ideal) + (4.799 * tinggi_cm) - (5.677 * umur)
    elif jenis_kelamin == 'wanita':
        kalori = 447.593 + (9.247 * berat_badan_ideal) + (3.098 * tinggi_cm) - (4.330 * umur)
    else:
        return "Jenis kelamin tidak valid. Masukkan 'pria' atau 'wanita'."
    return kalori

def hitung_kebutuhan_air(berat_badan):
    """Fungsi untuk menghitung kebutuhan air dalam sehari"""
    air = 35 * berat_badan
    return air

def sumber_nutrisi(nutrisi):
    sources = {
        "Protein": ["Ayam   (295kcal/100 gram)", "Daging   (143,4kcal/100 gram)", "Ikan   (167kcal/100 gram)", "Telur   (155,1kcal/100 gram)", "Tahu   (80kcal/100 gram)", "Quinoa   (374kcal/100 gram)", "Yogurt   (72kcal/100 gram)", "Salmon   (140kcal/100 gram)"],
        "Lemak": ["Alpukat   (160kcal/100 gram)", "Kacang Polong  (339kcal/100 gram)", "Keju   (402,5kcal/100 gram)", "Dark Chocolate   (581kcal/100 gram)", "Mentega   (358,5-360kcal/50 gram)"],
        "Karbohidrat": ["Nasi Merah   (110kcal/100 gram)", "Kentang   (21,08kcal/100 gram)","Umbi-umbian   (100-120kcal/100 gram)", "Roti Gandum   (250-300kcal/100 gram)", "Oats    (379kcal/100 gram)", "Sagu   (330kcal/100 gram)", "Pisang   (89kcal/100 gram)", "Berries   (30-50kcal/100 gram)", "Jagung   (86-96kcal/100 gram)"]
    }

    return sources.get(nutrisi, [])

coloredFont1 = '<b style="color:Red; font-size:55px;" >PANGAN SEHAT</b>'
st.markdown(coloredFont1, unsafe_allow_html=True)

st.subheader("Platform Interaktif Untuk Informasi Nutrisi Tubuh yang Ideal")
st.write(" Berdasarkan Input Tinggi Badan dan Usia untuk mencapai Berat Badan yang Ideal ")


tinggi_cm = st.number_input("Masukkan tinggi badan Anda (dalam cm):", min_value=0.0)
tinggi_m = tinggi_cm / 100  # Konversi tinggi ke meter
umur = st.number_input("Masukkan usia Anda:", min_value=0, max_value=150, step=1)
jenis_kelamin = st.radio("Jenis Kelamin:", ('Pria', 'Wanita'))


if st.button("Hitung Semua"):
    if tinggi_cm <= 0:  # Validasi tinggi badan
        st.error("Tinggi badan harus lebih besar dari 0.")
    else:
        st.balloons()
        berat_ideal = berat_badan_ideal(tinggi_m, jenis_kelamin)
        kalori_harian = hitung_kalori(berat_ideal, umur, jenis_kelamin, tinggi_cm)
        kebutuhan_air = hitung_kebutuhan_air(berat_ideal)

        st.write("Berat Badan Ideal Anda: **{:.2f} kg**".format(berat_ideal), unsafe_allow_html=True)
        st.write("Kalori Harian yang Harus Dikonsumsi: **{:.2f} kalori per hari**".format(kalori_harian), unsafe_allow_html=True)
        st.write("Kebutuhan Air Anda: **{:.2f} ml per hari**".format(kebutuhan_air), unsafe_allow_html=True)

with st.sidebar:
    st.title("")        
    coloredFont2 = '<b style="color:Red; font-size:35px;" >Sumber Nutrisi</b>'
    st.markdown(coloredFont2, unsafe_allow_html=True)
    #st.title("Sumber Nutrisi")
    st.subheader("Temukan Sumber-Sumber Umum untuk Protein, Lemak, dan Karbohidrat")
    
    selected_nutrient = st.selectbox("Pilih jenis nutrisi:", ["Protein", "Lemak", "Karbohidrat"])
    st.write("Berikut adalah sumber-sumber umum untuk", selected_nutrient, ":")
    sources_list = sumber_nutrisi(selected_nutrient)
    for source in sources_list:
        st.write("- ", source)


def main():
    coloredFont1 = '<b style="color:Red; font-size:55px;" >Pilihan Menu Makanan</b>'
    st.markdown(coloredFont1, unsafe_allow_html=True)


    # Daftar nilai nutrisi untuk setiap item
    nutrisi_values = {
        "Nasi Putih": {"kalori": 130, "protein": 2, "lemak": 0, "karbohidrat": 28},
        "Nasi Goreng": {"kalori": 250, "protein": 5, "lemak": 8, "karbohidrat": 40},
        "Nasi Kuning": {"kalori": 220, "protein": 4, "lemak": 5, "karbohidrat": 35},
        "Nasi Jagung": {"kalori": 180, "protein": 3, "lemak": 2, "karbohidrat": 30},
        "Ayam Goreng": {"kalori": 250, "protein": 20, "lemak": 15, "karbohidrat": 5},
        "Daging Sapi": {"kalori": 300, "protein": 25, "lemak": 18, "karbohidrat": 10},
        "Ikan Bakar": {"kalori": 200, "protein": 22, "lemak": 12, "karbohidrat": 8},
        "Tahu Goreng": {"kalori": 150, "protein": 8, "lemak": 5, "karbohidrat": 10},
        "Sayur Asem": {"kalori": 50, "protein": 2, "lemak": 1, "karbohidrat": 8},
        "Sayur Bayam": {"kalori": 30, "protein": 3, "lemak": 1, "karbohidrat": 5},
        "Sayur Lodeh": {"kalori": 100, "protein": 5, "lemak": 8, "karbohidrat": 12},
        "Burger Sayuran": {"kalori": 280, "protein": 15, "lemak": 10, "karbohidrat": 30},
        "Roti Isi Telur": {"kalori": 200, "protein": 12, "lemak": 8, "karbohidrat": 20},
        "Sop Ayam": {"kalori": 150, "protein": 10, "lemak": 5, "karbohidrat": 15},
        "Kebab Sayuran": {"kalori": 300, "protein": 15, "lemak": 12, "karbohidrat": 25},
        "Salad Buah": {"kalori": 120, "protein": 2, "lemak": 1, "karbohidrat": 30},
        "Bakso": {"kalori": 200, "protein": 15, "lemak": 10, "karbohidrat": 5},
        "Pancake Pisang": {"kalori": 180, "protein": 5, "lemak": 2, "karbohidrat": 30},
        "Capcay": {"kalori": 160, "protein": 8, "lemak": 6, "karbohidrat": 20},
        "Mie Goreng": {"kalori": 300, "protein": 10, "lemak": 15, "karbohidrat": 35},
        "Tumis Brokoli": {"kalori": 120, "protein": 5, "lemak": 3, "karbohidrat": 15},
        "Nasi Goreng Seafood": {"kalori": 350, "protein": 18, "lemak": 20, "karbohidrat": 40},
        "Sandwich Keju": {"kalori": 250, "protein": 10, "lemak": 12, "karbohidrat": 25},
        "Pizza Vegetarian": {"kalori": 400, "protein": 15, "lemak": 18, "karbohidrat": 45},
        "Bubur Ayam": {"kalori": 200, "protein": 12, "lemak": 8, "karbohidrat": 30},
        "Salad Kacang": {"kalori": 150, "protein": 6, "lemak": 5, "karbohidrat": 20},
        "Pisang Goreng": {"kalori": 100, "protein": 1, "lemak": 5, "karbohidrat": 15},
        "Lumpia Sayur": {"kalori": 120, "protein": 3, "lemak": 4, "karbohidrat": 18},
        "Sate Tahu": {"kalori": 180, "protein": 10, "lemak": 7, "karbohidrat": 12}
    }

    # Pilihan jenis nasi
    nasi_options = ["Nasi Putih", "Nasi Goreng", "Nasi Kuning", "Nasi Jagung", "Bubur Ayam","Mie Goreng","Pisang Goreng"]
    nasi_choice = st.selectbox("Pilih jenis karbohidrat:", nasi_options)

    # Pilihan lauk
    lauk_options = {
        "Ayam Goreng": nutrisi_values["Ayam Goreng"],
        "Daging Sapi": nutrisi_values["Daging Sapi"],
        "Ikan Bakar": nutrisi_values["Ikan Bakar"],
        "Tahu Goreng": nutrisi_values["Tahu Goreng"],
        "Bakso": nutrisi_values["Bakso"],
        "Sop Ayam": nutrisi_values["Sop Ayam"],
        "Bubur Ayam": nutrisi_values["Bubur Ayam"],
        "Sate Tahu": nutrisi_values["Sate Tahu"]
    }
    lauk_choice = st.selectbox("Pilih lauk:", list(lauk_options.keys()))

    # Pilihan sayuran
    with_veggies = st.checkbox("Tambahkan sayuran")

    if with_veggies:
        veggies_options = {
            "Sayur Asem": nutrisi_values["Sayur Asem"],
            "Sayur Bayam": nutrisi_values["Sayur Bayam"],
            "Sayur Lodeh": nutrisi_values["Sayur Lodeh"],
            "Capcay": nutrisi_values["Capcay"],
            "Tumis Brokoli": nutrisi_values["Tumis Brokoli"],
            "Salad Buah": nutrisi_values["Salad Buah"],
            "Salad Kacang": nutrisi_values["Salad Kacang"],
            "Lumpia Sayur": nutrisi_values["Lumpia Sayur"]
        }
        veggies_choice = st.selectbox("Pilih sayuran:", list(veggies_options.keys()))

    # Hitung total nutrisi
    total_nutrisi = {
        "kalori": nutrisi_values[nasi_choice]["kalori"] + nutrisi_values[lauk_choice]["kalori"],
        "protein": nutrisi_values[nasi_choice]["protein"] + nutrisi_values[lauk_choice]["protein"],
        "lemak": nutrisi_values[nasi_choice]["lemak"] + nutrisi_values[lauk_choice]["lemak"],
        "karbohidrat": nutrisi_values[nasi_choice]["karbohidrat"] + nutrisi_values[lauk_choice]["karbohidrat"]
    }

    if with_veggies:
        total_nutrisi["kalori"] += nutrisi_values[veggies_choice]["kalori"]
        total_nutrisi["protein"] += nutrisi_values[veggies_choice]["protein"]
        total_nutrisi["lemak"] += nutrisi_values[veggies_choice]["lemak"]
        total_nutrisi["karbohidrat"] += nutrisi_values[veggies_choice]["karbohidrat"]

    # Tampilkan pilihan menu beserta total nutrisinya
    st.write("## Pilihan Menu Makanan")
    st.write(f"**Nasi:** {nasi_choice}")
    st.write(f"**Lauk:** {lauk_choice}")
    if with_veggies:
        st.write(f"**Sayuran:** {veggies_choice}")
    st.write("## Total Nutrisi")
    st.write(f"Kalori: {total_nutrisi['kalori']} kcal")
    st.write(f"Protein: {total_nutrisi['protein']} gram")
    st.write(f"Lemak: {total_nutrisi['lemak']} gram")
    st.write(f"Karbohidrat: {total_nutrisi['karbohidrat']} gram")

if __name__ == "__main__":
    main()