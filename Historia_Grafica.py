import pygame
import sys

# Inicializar pygame
pygame.init()

# Constantes de pantalla y colores
WIDTH, HEIGHT = 1000, 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Inicializar pantalla
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Novela Gráfica Undercaves")

# Cargar y escalar imágenes
images = {
    "img_inicial": pygame.transform.scale(pygame.image.load("0.png"), (WIDTH, HEIGHT)),
    "img_cueva": pygame.transform.scale(pygame.image.load("1.png"), (WIDTH, HEIGHT)),
    "img_prota": pygame.transform.scale(pygame.image.load("2.png"), (WIDTH, HEIGHT)),
    "img_ciudad": pygame.transform.scale(pygame.image.load("3.png"), (WIDTH, HEIGHT)),
    "img_puesto": pygame.transform.scale(pygame.image.load("4.png"), (WIDTH, HEIGHT)),
    "img_castillo": pygame.transform.scale(pygame.image.load("5.png"), (WIDTH, HEIGHT)),
    "img_monstruo_de_caballeria": pygame.transform.scale(pygame.image.load("6.png"), (WIDTH, HEIGHT)),
    "img_espada_legendaria": pygame.transform.scale(pygame.image.load("7.png"), (WIDTH, HEIGHT)),
}

# Fuente de texto
font = pygame.font.Font(None, 36)

def draw_text(text, x, y):
    text_surface = font.render(text, True, WHITE)
    screen.blit(text_surface, (x, y))

class GameState:
    def __init__(self):
        self.state = "start"
    
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                self.handle_key_1()
            elif event.key == pygame.K_2:
                self.handle_key_2()
    
    def handle_key_1(self):
        if self.state == "start":
            self.state = "cueva"
        elif self.state == "cueva":
            self.state = "find_food"
        elif self.state == "find_food":
            self.state = "find_fruits"
        elif self.state == "jungle":
            self.state = "follow_path"
        elif self.state == "follow_path":
            self.state = "hunt_animal"
    
    def handle_key_2(self):
        if self.state == "start":
            self.state = "jungle"
        elif self.state == "cueva":
            self.state = "build_shelter"
        elif self.state == "find_food":
            self.state = "fish"
        elif self.state == "jungle":
            self.state = "find_water"
        elif self.state == "follow_path":
            self.state = "find_water_source"

    def show(self):
        screen.fill(BLACK)
        if self.state == "start":
            screen.blit(images["img_inicial"], (0, 0))
            draw_text("Caiste de una altura muy alta, estas conmocionado y parece que estas herido internamente", 30, 300)
            draw_text("Recuerdas quien eres de golpe, Zhongli, exacto, eres el heroe legendario de la superficie", 30, 330)
            draw_text("Zhongli: claro, ahora lo rexcuerdo, estaba de expedicion cuando una brecha de portal me absorbio al sub-suelo, es bastante diferente a las leyendas...", 30, 360)
            draw_text("Zhongli: Bueno, *ahhhh* sera mejor que comience a caminar por aca, hace bastante frio a decir verdad...", 30, 390)
            draw_text("Opciones del destino", 50, 500)
            draw_text("1. Buscar una salida", 50, 550)
            draw_text("2. Explorar las catacumbas abandonadas del sub-suelo, (CAERLEON)", 50, 600)
        elif self.state == "cueva":
            screen.blit(images["img_cueva"], (0, 0))
            draw_text("¿Qué prefieres hacer primero?", 50, 100)
            draw_text("1. Buscar comida", 50, 150)
            draw_text("2. Construir un refugio", 50, 200)
        elif self.state == "find_food":
            screen.blit(images["img_prota"], (0, 0))
            draw_text("¿Qué tipo de comida buscas?", 50, 100)
            draw_text("1. Buscar frutas", 50, 150)
            draw_text("2. Pescar", 50, 200)
        elif self.state == "find_fruits":
            draw_text("Guardas las frutas y sobrevives", 50, 50)
        elif self.state == "fish":
            screen.blit(images["img_ciudad"], (0, 0))
            draw_text("Pescar con trampa y sobrevives", 50, 100)
        elif self.state == "build_shelter":
            screen.blit(images["img_puesto"], (0, 0))
            draw_text("Construyes una cabaña y te rescatan", 50, 100)
        elif self.state == "jungle":
            screen.blit(images["img_castillo"], (0, 0))
            draw_text("¿Qué prefieres hacer primero?", 50, 100)
            draw_text("1. Seguir un sendero", 50, 150)
            draw_text("2. Buscar una fuente de agua", 50, 200)
        elif self.state == "follow_path":
            draw_text("¿Qué decides hacer?", 50, 100)
            draw_text("1. Cazar un animal", 50, 150)
            draw_text("2. Seguir las huellas hasta una fuente de agua", 50, 200)
        elif self.state == "hunt_animal":
            draw_text("Intentas cazar y mueres", 50, 50)
        elif self.state == "find_water_source":
            screen.blit(images["img_monstruo_de_caballeria"], (0, 0))
            draw_text("Encuentras una fuente de agua y sobrevives", 50, 100)
        elif self.state == "find_water":
            draw_text("Encuentras una civilización caníbal y mueres", 50, 50)
        pygame.display.flip()

def game():
    game_state = GameState()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            game_state.handle_event(event)
        
        game_state.show()
        pygame.display.flip()

game()