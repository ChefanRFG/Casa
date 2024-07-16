import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 1000, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Novela Grafica Undercaves")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

img_0 = pygame.image.load("0.png")
img_1 = pygame.image.load("1.png")
img_2 = pygame.image.load("2.png")
img_3 = pygame.image.load("3.png")
img_4 = pygame.image.load("4.png")
img_5= pygame.image.load("5.png")
img_6 = pygame.image.load("6.png")
img_7 = pygame.image.load("7.png") 

img_inicial = pygame.transform.scale(img_0, (WIDTH, HEIGHT))
img_cueva = pygame.transform.scale(img_1, (WIDTH, HEIGHT))
img_prota = pygame.transform.scale(img_2, (WIDTH, HEIGHT))
img_ciudad = pygame.transform.scale(img_3, (WIDTH, HEIGHT))
img_puesto = pygame.transform.scale(img_4, (WIDTH, HEIGHT))
img_castillo = pygame.transform.scale(img_5, (WIDTH, HEIGHT))
img_monstruo_de_caballeria = pygame.transform.scale(img_6, (WIDTH, HEIGHT))
img_espada_legendaria = pygame.transform.scale(img_7, (WIDTH, HEIGHT))

font = pygame.font.Font(None, 36)

def draw_text(text, x, y):
    text_surface = font.render(text, True, WHITE)
    screen.blit(text_surface, (x, y))

def show_state(state):
    screen.fill(WHITE)
    if state == "Iniciar el Crono":
        screen.blit(img_inicial, (0, 0))
        draw_text("Caiste de una altura muy alta, estas conmocionado y parece que estas herido internamente", 30, 300)
        draw_text("Recuerdas quien eres de golpe, Zhongli, exacto, eres el heroe legendario de la superficie", 30, 330)
        draw_text("Zhongli: claro, ahora lo rexcuerdo, estaba de expedicion cuando una brecha de portal me absorbio al sub-suelo, es bastante diferente a las leyendas...", 30, 360)
        draw_text("Zhongli: Bueno, *ahhhh* sera mejor que comience a caminar por aca, hace bastante frio a decir verdad...", 30, 390)
        draw_text("Opciones del destino", 50, 500)
        draw_text("1. Buscar una salida", 50, 550)
        draw_text("2. Explorar las catacumbas abandonadas del sub-suelo, (CAERLEON)", 50, 600)
    elif state == "cueva":
        screen.blit(img_1, (0, 0))
        draw_text("¿Qué prefieres hacer primero?", 50, 100)
        draw_text("1. Buscar comida", 50, 150)
        draw_text("2. Construir un refugio", 50, 200)
    elif state == "find_food":
        screen.blit(img_2, (0, 0))
        draw_text("¿Qué tipo de comida buscas?", 50, 100)
        draw_text("1. Buscar frutas", 50, 150)
        draw_text("2. Pescar", 50, 200)
    elif state == "find_fruits":
        draw_text("Guardas las frutas y sobrevives", 50, 50)
    elif state == "fish":
        screen.blit(img_3, (0, 0))
        draw_text("Pescar con trampa y sobrevives", 50, 100)
    elif state == "build_shelter":
        screen.blit(img_4, (0, 0))
        draw_text("Construyes una cabaña y te rescatan", 50, 100)
    elif state == "jungle":
        screen.blit(img_5, (0, 0))
        draw_text("¿Qué prefieres hacer primero?", 50, 100)
        draw_text("1. Seguir un sendero", 50, 150)
        draw_text("2. Buscar una fuente de agua", 50, 200)
    elif state == "follow_path":
        draw_text("¿Qué decides hacer?", 50, 100)
        draw_text("1. Cazar un animal", 50, 150)
        draw_text("2. Seguir las huellas hasta una fuente de agua", 50, 200)
    elif state == "hunt_animal":
        draw_text("Intentas cazar y mueres", 50, 50)
    elif state == "find_water_source":
        screen.blit(img_6, (0, 0))
        draw_text("Encuentras una fuente de agua y sobrevives", 50, 100)
    elif state == "find_water":
        draw_text("Encuentras una civilización caníbal y mueres", 50, 50)
    pygame.display.flip()

def ask_question(question):
    screen.fill(WHITE)
    draw_text(question, 50, 250)
    draw_text("1. Sí", 50, 300)
    draw_text("2. No", 50, 350)
    pygame.display.flip()

def game():
    state = "start"

    questions = [
        "¿Te gusta explorar?",
        "¿Tienes miedo a la oscuridad?",
        "¿Prefieres el calor o el frío?",
        "¿Eres bueno construyendo cosas?",
        "¿Te gustan los animales salvajes?"
    ]
    random.shuffle(questions)

    question_counter = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    if state == "Iniciar el crono":
                        state = "beach"
                    elif state == "beach":
                        state = "find_food"
                    elif state == "find_food":
                        state = "find_fruits"
                    elif state == "jungle":
                        state = "follow_path"
                    elif state == "follow_path":
                        state = "hunt_animal"
                elif event.key == pygame.K_2:
                    if state == "start":
                        state = "jungle"
                    elif state == "beach":
                        state = "build_shelter"
                    elif state == "find_food":
                        state = "fish"
                    elif state == "jungle":
                        state = "find_water"
                    elif state == "follow_path":
                        state = "find_water_source"
        
        if state == "Iniciar el crono" and question_counter < len(questions):
            ask_question(questions[question_counter])
            question_counter += 1
        else:
            show_state(state)

        pygame.display.flip()

game()