import pygame
import sys

# Función para mostrar texto en pantalla
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

def show_options_menu():
    options_screen = pygame.Surface((400, 300))
    options_screen.fill((150, 150, 150))
    pygame.draw.rect(options_screen, (100, 100, 100), (50, 50, 300, 200))
    draw_text("Opciones", font, (255, 255, 255), options_screen, 200, 70)
    draw_text("Quitar música", font, (255, 255, 255), options_screen, 200, 120)
    draw_text("Cambiar música", font, (255, 255, 255), options_screen, 200, 150)
    draw_text("Actualizar vista y borrar cache", font, (255, 255, 255), options_screen, 200, 180)
    draw_text("Guardar cambios y borrar cache", font, (255, 255, 255), options_screen, 200, 240)

    apply_button = pygame.draw.rect(options_screen, WHITE, (150, 280, 100, 40))
    draw_text("Aplicar", font, BLACK, options_screen, 200, 300)

    return options_screen, apply_button

# Inicializar Pygame
pygame.init()

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Definir dimensiones de la pantalla
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cosmic Dash | By Kevin Andres")

# Fuente
font = pygame.font.Font(None, 36)

# Estado del juego
game_state = "loading"  # Estados: loading, menu, playing, options

# Bucle principal del juego
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "menu":
                if start_button.collidepoint(event.pos):
                    game_state = "playing"
                elif range_button.collidepoint(event.pos):
                    print("Este apartado todavía está en desarrollo. Gracias por su paciencia.")
                elif options_button.collidepoint(event.pos):
                    game_state = "options"
            elif game_state == "options":
                options_menu, apply_button = show_options_menu()

                if apply_button.collidepoint(event.pos):  # Corregido para usar event.pos
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        print("Cambios guardados. Borre el caché para que los cambios surtan efecto.")
                        game_state = "menu"

    # Actualizar
    if game_state == "loading":
        game_state = "menu"
    elif game_state == "playing":
        pass  # Aquí iría la lógica del juego
    elif game_state == "options":
        options_menu = show_options_menu()

    # Dibujar en pantalla
    SCREEN.fill(BLACK)
    if game_state == "menu":
        start_button = pygame.draw.rect(SCREEN, WHITE, (300, 200, 200, 50))
        range_button = pygame.draw.rect(SCREEN, WHITE, (300, 270, 200, 50))
        options_button = pygame.draw.rect(SCREEN, WHITE, (300, 340, 200, 50))
        draw_text("Empezar partida", font, BLACK, SCREEN, 400, 225)
        draw_text("Ver rango", font, BLACK, SCREEN, 400, 295)
        draw_text("Opciones", font, BLACK, SCREEN, 400, 365)
    elif game_state == "options":
        SCREEN.blit(options_menu[0], (200, 150))

    # Actualizar pantalla
    pygame.display.flip()

    # Controlar la velocidad de actualización
    clock.tick(60)  # 60 FPS

# Salir del juego
pygame.quit()
sys.exit()
