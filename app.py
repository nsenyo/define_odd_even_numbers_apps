import streamlit as st

st.header('Define Number Type Apps :sunglasses:', divider='blue')
st.write('Ini adalah aplikasi untuk menentukan bilangan genap atau bilangan ganjil')

# Input pertama
number1 = st.number_input("Insert the first number")

# Menentukan apakah number1 genap atau ganjil
if number1 % 2 == 0:
    st.write(f'{number1} adalah bilangan genap.')
else:
    st.write(f'{number1} adalah bilangan ganjil.')

# Input kedua
number2 = st.number_input("Insert the second number")

# Menentukan apakah number2 genap atau ganjil
if number2 % 2 == 0:
    st.write(f'{number2} adalah bilangan genap.')
else:
    st.write(f'{number2} adalah bilangan ganjil.')

# Mengalikan kedua bilangan
result = number1 * number2

# Menentukan apakah hasil perkalian genap atau ganjil
if result % 2 == 0:
    st.write(f'Hasil perkalian {number1} dan {number2} adalah {result}, dan itu adalah bilangan genap.')
else:
    st.write(f'Hasil perkalian {number1} dan {number2} adalah {result}, dan itu adalah bilangan ganjil.')
