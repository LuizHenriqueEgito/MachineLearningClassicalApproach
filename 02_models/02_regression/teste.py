import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import numpy as np

# Suponha que você tenha uma lista de imagens (arrays 2D)
imagens = [np.random.rand(10, 10) for _ in range(5)]

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)  # Espaço para botões

indice = [0]  # índice atual das imagens, lista para ser mutável dentro das funções

im_display = ax.imshow(imagens[indice[0]], cmap='gray')
ax.set_title(f'Imagem {indice[0] + 1} de {len(imagens)}')

# Define posição dos botões
axprev = plt.axes([0.3, 0.05, 0.1, 0.075])
axnext = plt.axes([0.6, 0.05, 0.1, 0.075])

btn_prev = Button(axprev, 'Anterior')
btn_next = Button(axnext, 'Próximo')

def show_image():
    im_display.set_data(imagens[indice[0]])
    ax.set_title(f'Imagem {indice[0] + 1} de {len(imagens)}')
    fig.canvas.draw_idle()

def next_image(event):
    indice[0] = (indice[0] + 1) % len(imagens)
    show_image()

def prev_image(event):
    indice[0] = (indice[0] - 1) % len(imagens)
    show_image()

btn_next.on_clicked(next_image)
btn_prev.on_clicked(prev_image)

plt.show()
