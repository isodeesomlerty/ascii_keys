import sys

import pygame

class Keys:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Keys")

        self.bg_color = (61, 55, 48)

        self.instruction_font = pygame.font.Font(None, 72)
        self.instruction_text = "Press a key to get its ASCII code:"
        self.key_font = pygame.font.Font(None, 54)
        self.key_text = ""


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)


    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        self.key_text = str(event.key)

    
    def _draw_text(self):
        """Draw the key code onto the screen."""
        instruction_surface = self.instruction_font.render(
            self.instruction_text,
            True,
            (255, 255, 255))
        text_surface = self.key_font.render(self.key_text, True, 
                                            (255, 255, 255))

        self.screen.blit(instruction_surface,
                         self._center_surface(instruction_surface, -35))
        self.screen.blit(text_surface, 
                         self._center_surface(text_surface, 40))
        

    def _center_surface(self, surface, y_add=0, x_add=0):
        """Return the centered x, y position of a surface."""
        surface_width, surface_height = surface.get_size()
        surface_x = (self.screen.get_width() - surface_width) // 2 + x_add
        surface_y = (self.screen.get_height() - surface_height) // 2 + y_add
        return (surface_x, surface_y)


    def _update_screen(self):
        """Update the text on the screen, and flip to the new screen."""
        self.screen.fill(self.bg_color)
        self._draw_text()
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ky = Keys()
    ky.run_game()