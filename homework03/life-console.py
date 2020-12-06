import curses
import time

from life import GameOfLife
from ui import UI


class Console(UI):

    def __init__(self, life: GameOfLife) -> None:
        super().__init__(life)

    def draw_borders(self, screen) -> None:
        """ Отобразить рамку. """
        screen.border(0)

    def draw_grid(self, screen) -> None:
        """ Отобразить состояние клеток. """
        for l in range(self.life.cols):
            for k in range(self.life.rows):
                try:
                    if self.life.curr_generation[l][k]:
                        screen.addch(l + 1, k + 1, "*")
                except:
                    pass

    def run(self) -> None:
        screen = curses.initscr()
        curses.curs_set(0)
        running = True
        while running:
            screen.clear()
            self.draw_borders(screen)
            self.draw_grid(screen)
            self.life.step()
            if self.life.is_max_generations_exceeded:
                running = False
            screen.refresh()
            time.sleep(2)

        screen.getch()
        curses.endwin()
