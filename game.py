from config import *
import pygame
from pygame.locals import *
import time
import random
import sys

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.running = True
        logo = pygame.image.load("favicon.ico")
        pygame.display.set_icon(logo)   
        pygame.display.set_caption("Meme Generator")
        self.surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        self.surface.fill(GREY)
        self.random_phrases = [
            "When you fall down!",
            "I'm a meme!",
            "Where's the coffee",
            "I love TechWise",
            "Coding is cool!",
            "Pygame is fun"
        ]
        self.image_templates = [
            {"filepath": "template-1.png", "number_of_texts": 3, "colors": [BLACK, BLACK, WHITE], "texts": [], "text_positions": [(270, 45), (470, 20), (WINDOW_WIDTH // 2, 580)]},
            {"filepath": "template-2.png", "number_of_texts": 2, "colors": [WHITE, WHITE], "texts": [], "text_positions": [(WINDOW_WIDTH // 2, 100), (WINDOW_WIDTH // 2, 500)]},
            {"filepath": "template-3.png", "number_of_texts": 3, "colors": [BLACK, BLACK, BLACK], "texts": [],"text_positions": [(WINDOW_WIDTH // 4 + 20, WINDOW_HEIGHT - WINDOW_HEIGHT // 5 + 10), (WINDOW_WIDTH // 2 + 80, WINDOW_HEIGHT // 2), (WINDOW_WIDTH - (WINDOW_WIDTH // 7), WINDOW_HEIGHT // 2 + 50)]},
            {"filepath": "template-4.png", "number_of_texts": 2, "colors": [BLACK, BLACK], "texts": [], "text_positions": [(WINDOW_WIDTH - (WINDOW_WIDTH // 3) - 10, WINDOW_HEIGHT // 10 + 20), (WINDOW_WIDTH // 3 + 50, WINDOW_HEIGHT // 3 + 40)]},
            {"filepath": "template-5.png", "number_of_texts": 5, "colors": [WHITE, WHITE, WHITE, WHITE, WHITE], "texts": [], "text_positions": [(WINDOW_WIDTH // 3, 200), (550, WINDOW_HEIGHT // 6), (WINDOW_WIDTH // 4 + 30, 480), (WINDOW_WIDTH // 2, 480), (560, 380)]},
            {"filepath": "template-6.png", "number_of_texts": 3, "colors": [WHITE, WHITE, WHITE], "texts":[], "text_positions": [(250, 160), (WINDOW_WIDTH - 350, 160), (WINDOW_WIDTH // 2 + 50, WINDOW_HEIGHT - WINDOW_HEIGHT // 5)]},
            {"filepath": "template-7.png", "number_of_texts": 4, "colors": [WHITE, WHITE, WHITE, WHITE], "texts":[], "text_positions": [(WINDOW_WIDTH // 2 - 90, WINDOW_HEIGHT // 3), (WINDOW_WIDTH - 130, WINDOW_HEIGHT // 3), (WINDOW_WIDTH // 2 - 90, 5 * WINDOW_HEIGHT // 7), (WINDOW_WIDTH - 130, 5 * WINDOW_HEIGHT // 7)] },
            {"filepath": "template-8.png", "number_of_texts": 2, "colors": [WHITE, WHITE], "texts": [], "text_positions": [(WINDOW_WIDTH // 3, WINDOW_HEIGHT // 3), (WINDOW_WIDTH // 2, 500)]},
            {"filepath": "template-9.png", "number_of_texts": 2, "colors": [BLACK, BLACK], "text_positions": [(520, WINDOW_HEIGHT // 4), (520, 3 * WINDOW_HEIGHT // 4)], "texts": []},
            {"filepath": "template-10.png", "number_of_texts": 2, "colors": [BLACK, WHITE], "texts": [], "text_positions": [(WINDOW_WIDTH // 2, 40), (WINDOW_WIDTH // 2, 500)]},
        ]

    def handle_events(self):
        for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.change_image()

    def render_text(self, text, color, position):
        font = pygame.font.Font(FONT, FONT_SIZE)
        text = font.render(text, True, color)
        text_rect = text.get_rect()
        text_rect.center = position
        self.surface.blit(text, text_rect)
        pygame.display.update()

    def create_image_dict(self):
        image = random.choice(self.image_templates)
        image["texts"].clear()
        for i in range(image["number_of_texts"]): 
            image["texts"].append(random.choice(self.random_phrases))
        return image
    
    def generate_image(self, image):
        try:
            template = pygame.image.load(image["filepath"])
        except pygame.error:
            print("Cannot load image")
        template_rect = template.get_rect()
        template_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        self.surface.blit(template, template_rect)
        pygame.display.update()
        for i in range(image["number_of_texts"]):
            self.render_text(image["texts"][i], image["colors"][i], image["text_positions"][i])
            pygame.display.update()

    def change_image(self):
        self.surface.fill(GREY)  
        image = self.create_image_dict()
        self.generate_image(image)
        pygame.display.update()

    
    def run(self):
        self.render_text("MEME GENERATOR", WHITE, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        self.render_text("Click anywhere on the screen to change the meme", WHITE, (WINDOW_WIDTH // 2, 340))

        while self.running:
            self.handle_events()
            pygame.display.flip()
            time.sleep(SLEEP_TIME)
        pygame.quit()
        sys.exit()



if __name__ == "__main__":
    game = Game()
    game.run()
