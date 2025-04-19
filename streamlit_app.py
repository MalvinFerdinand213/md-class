import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load('model.pkl')

st.title("Prediksi Pembatalan Booking Hotel")

# Input dari user
no_of_adults = st.number_input("Jumlah Dewasa", min_value=0, value=2)
no_of_children = st.number_input("Jumlah Anak", min_value=0, value=0)
no_of_weekend_nights = st.number_input("Jumlah Malam Akhir Pekan", min_value=0)
no_of_week_nights = st.number_input("Jumlah Malam Hari Kerja", min_value=0)
type_of_meal_plan = st.selectbox("Paket Makanan", ['Meal Plan 1', 'Meal Plan 2', 'Meal Plan 3', 'Not Selected'])
required_car_parking_space = st.selectbox("Perlu Parkir Mobil?", [0, 1])
room_type_reserved = st.selectbox("Tipe Kamar", ['Room_Type 1', 'Room_Type 2', 'Room_Type 3', 'Room_Type 4'])
lead_time = st.number_input("Lead Time (hari sebelum check-in)", min_value=0)
arrival_year = st.selectbox("Tahun Kedatangan", [2017, 2018])
arrival_month = st.selectbox("Bulan Kedatangan", list(range(1, 13)))
arrival_date = st.selectbox("Tanggal Kedatangan", list(range(1, 32)))
market_segment_type = st.selectbox("Segment Pasar", ['Offline', 'Online', 'Corporate', 'Complementary', 'Aviation'])
repeated_guest = st.selectbox("Tamu Berulang?", [0, 1])
no_of_previous_cancellations = st.number_input("Jumlah Pembatalan Sebelumnya", min_value=0)
no_of_previous_bookings_not_canceled = st.number_input("Jumlah Booking Lalu Tidak Dibatalkan", min_value=0)
avg_price_per_room = st.number_input("Harga Rata-rata per Kamar", min_value=0.0)
no_of_special_requests = st.number_input("Jumlah Permintaan Khusus", min_value=0)

# Encoding manual (harus sesuai saat training model)
meal_plan_encoded = {
    'Not Selected': 0,
    'Meal Plan 1': 1,
    'Meal Plan 2': 2,
    'Meal Plan 3': 3
}[type_of_meal_plan]

room_type_encoded = {
    'Room_Type 1': 1,
    'Room_Type 2': 2,
    'Room_Type 3': 3,
    'Room_Type 4': 4
}[room_type_reserved]

market_segment_encoded = {
    'Offline': 0,
    'Online': 1,
    'Corporate': 2,
    'Complementary': 3,
    'Aviation': 4
}[market_segment_type]

# Susun fitur ke dalam array
user_input = np.array([[no_of_adults, no_of_children, no_of_weekend_nights, no_of_week_nights,
                        meal_plan_encoded, required_car_parking_space, room_type_encoded, lead_time,
                        arrival_year, arrival_month, arrival_date, market_segment_encoded, repeated_guest,
                        no_of_previous_cancellations, no_of_previous_bookings_not_canceled,
                        avg_price_per_room, no_of_special_requests]])

# Prediksi
if st.button("Prediksi"):
    prediction = model.predict(user_input)
    if prediction[0] == 1:
        st.error("Booking kemungkinan DIBATALKAN")
    else:
        st.success("Booking kemungkinan TIDAK DIBATALKAN")
