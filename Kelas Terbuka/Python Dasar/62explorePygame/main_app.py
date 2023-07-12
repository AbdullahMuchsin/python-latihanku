import pygame

## init
pygame.init()

# parameter looping
running = True

# Membuat Display Surface Object
windwo_x = 500
windwo_y = 500
window = pygame.display.set_mode((windwo_x,windwo_y))
clock = pygame.time.Clock()

# Obeject Game koordinat (x,y)
x = 250
y = 250

# Ukuran
panjang = 20
lebar = 20

# kecepatan Gerak
kecepatan = 10

while running:
    # Program atur False looping
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # User input, Database input
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
        x -= kecepatan
    if keys[pygame.K_RIGHT] and x < windwo_x - lebar:
        x += kecepatan
    if keys[pygame.K_DOWN] and y < windwo_y - panjang:
        y += kecepatan
    if keys[pygame.K_UP] and y > 0:
        y -= kecepatan

    # Upedate Asset
    window.fill("white")
    pygame.draw.rect(window,"green",(x,y,lebar,panjang))
    # pygame.draw.rect(window,"green",(x-50,y-50))

    
    # Reder ke display
    pygame.display.update()

    # Frame Per Second
    clock.tick(30)

pygame.quit()