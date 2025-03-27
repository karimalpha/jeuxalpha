import pygame
import time
import random

# Initialisation de pygame
pygame.init()

# Dimensions de la fenêtre
width, height = 800, 600

# Couleurs
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Initialisation de la fenêtre
game_window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Jeu de Course de Voiture")

# Horloge pour contrôler la vitesse
clock = pygame.time.Clock()

# Chargement et transformation de l'image de la voiture
car_img = pygame.image.load("car.png")  # Assurez-vous d'avoir une image "car.png" dans le même dossier
car_img = pygame.transform.scale(car_img, (90, 50))  # Redimensionner (largeur: 80, hauteur: 40)
car_img = pygame.transform.rotate(car_img, 90)  # Faire pivoter de -90 degrés pour l'orientation horizontale
car_width = 80  # Mettre à jour la largeur de la voiture

def display_car(x, y):
    game_window.blit(car_img, (x, y))

def obstacles(obstacle_x, obstacle_y, obstacle_w, obstacle_h, color):
    pygame.draw.rect(game_window, color, [obstacle_x, obstacle_y, obstacle_w, obstacle_h])

def message_display(text):
    font = pygame.font.SysFont("comicsansms", 50)
    text_surface = font.render(text, True, red)
    text_rect = text_surface.get_rect(center=(width / 2, height / 2))
    game_window.blit(text_surface, text_rect)
    pygame.display.update()
    time.sleep(2)

def crash():
    message_display("Vous avez percuté un obstacle!")

def game_loop():
    x = width * 0.45
    y = height * 0.8
    x_change = 0

    obstacle_start_x = random.randrange(0, width)
    obstacle_start_y = -600
    obstacle_speed = 7
    obstacle_width = 80
    obstacle_height = 80

    score = 0

    game_exit = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        game_window.fill(green)

        # Dessiner l'obstacle
        obstacles(obstacle_start_x, obstacle_start_y, obstacle_width, obstacle_height, red)
        obstacle_start_y += obstacle_speed

        # Dessiner la voiture
        display_car(x, y)

        # Afficher le score
        font = pygame.font.SysFont(None, 35)
        score_text = font.render("Score: " + str(score), True, red)
        game_window.blit(score_text, (10, 10))

        if x > width - car_width or x < 0:
            crash()
            game_loop()

        if obstacle_start_y > height:
            obstacle_start_y = 0 - obstacle_height
            obstacle_start_x = random.randrange(0, width)
            score += 1
            obstacle_speed += 0.5

        if y < obstacle_start_y + obstacle_height:
            if x > obstacle_start_x and x < obstacle_start_x + obstacle_width or x + car_width > obstacle_start_x and x + car_width < obstacle_start_x + obstacle_width:
                crash()
                game_loop()

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()