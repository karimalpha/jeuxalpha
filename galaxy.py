import pygame
import random

# Initialisation de pygame
pygame.init()

# Dimensions de la fenêtre
width, height = 800, 600

# Couleurs
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)

# Initialisation de la fenêtre
game_window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Jeu de Galaxie")

# Horloge pour contrôler la vitesse
clock = pygame.time.Clock()

# Chargement des images
player_img = pygame.image.load("spaceship.png")  # Assurez-vous d'avoir une image "spaceship.png"
enemy_img = pygame.image.load("enemy.png")  # Assurez-vous d'avoir une image "enemy.png"
bullet_img = pygame.image.load("bullet.png")  # Assurez-vous d'avoir une image "bullet.png"

# Redimensionnement des images
player_img = pygame.transform.scale(player_img, (50, 50))
enemy_img = pygame.transform.scale(enemy_img, (50, 50))
bullet_img = pygame.transform.scale(bullet_img, (10, 20))

# Position initiale du joueur
player_x = width // 2
player_y = height - 60
player_speed = 5

# Liste des ennemis
enemies = []
for i in range(5):
    enemies.append([random.randint(0, width - 50), random.randint(-100, -40), random.randint(2, 5)])

# Liste des balles
bullets = []

def draw_player(x, y):
    game_window.blit(player_img, (x, y))

def draw_enemy(x, y):
    game_window.blit(enemy_img, (x, y))

def draw_bullet(x, y):
    game_window.blit(bullet_img, (x, y))

def game_loop():
    global player_x, player_y
    running = True
    score = 0

    while running:
        game_window.fill(black)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Contrôles du joueur
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < width - 50:
            player_x += player_speed
        if keys[pygame.K_SPACE]:
            bullets.append([player_x + 20, player_y])

        # Mise à jour des ennemis
        for enemy in enemies:
            enemy[1] += enemy[2]
            if enemy[1] > height:
                enemy[0] = random.randint(0, width - 50)
                enemy[1] = random.randint(-100, -40)
                enemy[2] = random.randint(2, 5)
                score -= 1

        # Mise à jour des balles
        for bullet in bullets[:]:
            bullet[1] -= 10
            if bullet[1] < 0:
                bullets.remove(bullet)

        # Collision balle-ennemi
        for bullet in bullets[:]:
            for enemy in enemies[:]:
                if bullet[0] in range(enemy[0], enemy[0] + 50) and bullet[1] in range(enemy[1], enemy[1] + 50):
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    enemies.append([random.randint(0, width - 50), random.randint(-100, -40), random.randint(2, 5)])
                    score += 1

        # Dessiner le joueur
        draw_player(player_x, player_y)

        # Dessiner les ennemis
        for enemy in enemies:
            draw_enemy(enemy[0], enemy[1])

        # Dessiner les balles
        for bullet in bullets:
            draw_bullet(bullet[0], bullet[1])

        # Afficher le score
        font = pygame.font.SysFont(None, 35)
        score_text = font.render("Score: " + str(score), True, white)
        game_window.blit(score_text, (10, 10))

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

game_loop()