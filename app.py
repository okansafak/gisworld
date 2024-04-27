import streamlit as st
import random

# Yılanın başlangıç konumu
snake = [(0, 0)]

# Yem konumu
food = (5, 5)

# Yılanın hareket yönü
direction = 'right'

# Yılanın hareket fonksiyonu
def move():
    global snake, direction, food
    
    # Yılanın yeni başlangıç pozisyonunu belirle
    head = snake[0]
    if direction == 'up':
        new_head = (head[0], head[1] - 1)
    elif direction == 'down':
        new_head = (head[0], head[1] + 1)
    elif direction == 'left':
        new_head = (head[0] - 1, head[1])
    elif direction == 'right':
        new_head = (head[0] + 1, head[1])
    
    # Yılanın yeni başlangıç pozisyonuyla güncelle
    snake = [new_head] + snake[:-1]
    
    # Yılanın yemi yemesi durumu
    if snake[0] == food:
        snake.append(snake[-1])
        food = (random.randint(0, 19), random.randint(0, 19))

# Streamlit uygulamasını oluştur
st.title('Yılan Oyunu')

# Oyun alanını oluştur
for i in range(20):
    for j in range(20):
        if (i, j) in snake:
            st.markdown('<span style="color:blue">■</span>', unsafe_allow_html=True)
        elif (i, j) == food:
            st.markdown('<span style="color:red">●</span>', unsafe_allow_html=True)
        else:
            st.markdown('<span style="color:white">□</span>', unsafe_allow_html=True)

# Yönlendirme düğmelerini oluştur
st.write('## Yön Tuşları:')
col1, col2, col3 = st.columns(3)
with col2:
    if st.button('⬆️'):
        direction = 'up'
with col1:
    if st.button('⬅️'):
        direction = 'left'
with col3:
    if st.button('➡️'):
        direction = 'right'
with col2:
    if st.button('⬇️'):
        direction = 'down'

# Oyunu güncelle
move()
