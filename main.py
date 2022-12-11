from os import system, name
import time
import keyboard

class Screen:

    def __init__(self, RESOLUTION_X=30, RESOLUTION_Y=10):
        self.screen = [ ["."] * RESOLUTION_X for _ in range(RESOLUTION_Y)]

    @staticmethod
    def clear_screen():
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')
    
    def print_screen(self):
        self.clear_screen()
        for line in self.screen:
            print("".join(line))

    def change_char(self, line_number, char_index):
        character = "@"
        self.screen[line_number][char_index] = character
    
    def reset_screen(self):
        self.__init__()

class Snake:

    def __init__(self) -> None:
        # init a single element snake body
        # list of x, y dicts
        self.snake_body = [
            {
                "x": 10,
                "y": 5
             }
            ]
        # x, y, so 1, 0 means right
        self.starting_direction = [1, 0]
        self.set_current_direction(self.starting_direction)
    
    def set_current_direction(self, direction):
        self.current_direction = direction
    
    def move_snake_body(self):
        old_body = list(self.snake_body)
        for index, element in enumerate(self.snake_body):
            if index == 0:
                self.snake_body[index]["x"] += self.current_direction[0]
                self.snake_body[index]["y"] += self.current_direction[1]
            else:
                self.snake_body[index]["x"] = old_body[index - 1]["x"]
                self.snake_body[index]["y"] = old_body[index - 1]["y"]
        pass
    
    def draw_snake_on_screen(self, screen):
        screen.reset_screen()
        for element in self.snake_body:
            screen.change_char(line_number = element["y"], char_index = element["x"])

def check_for_keypress():
    if keyboard.is_pressed("x"):
        return True
    else:
        return False


screen = Screen()
snake = Snake()

while True:
    if check_for_keypress():
        break

    time.sleep(1)
    snake.draw_snake_on_screen(screen)
    screen.print_screen()
    snake.move_snake_body()
