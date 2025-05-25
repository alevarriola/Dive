import pygame

# iniciamos el pygames
pygame.init()

#definimos las variables del setup! pantalla, tiempo, deltatime y que el juego empieze a correr
pantalla = pygame.display.set_mode((1280, 720))
tiempo = pygame.time.Clock()
run = True
dt = 0

pos_raton = pygame.Vector2(pantalla.get_width() / 2, pantalla.get_height() / 2)

while run:
    # por cada evento que hata en eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            run = False

        #pygame.draw.circle(pantalla, "red", pos_raton, 40)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            pos_raton.y -= 300 * dt
        if keys[pygame.K_s]:
            pos_raton.y += 300 * dt
        if keys[pygame.K_a]:
            pos_raton.x -= 300 * dt
        if keys[pygame.K_d]:
            pos_raton.x += 300 * dt
    #el fondo es gris despues de cada frame
    pantalla.fill("grey")


    #todo lo que hiciste se coloca en pantalla
    pygame.display.flip()

    dt = tiempo.tick(60) / 1000 #limitamos a 60 FPS

pygame.quit()