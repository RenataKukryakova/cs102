import curses
import time
import pathlib

from life import GameOfLife
from ui import UI


class Console(UI):
    def __init__(self, life: GameOfLife, save_path: pathlib.Path) -> None:
        super().__init__(life)
        self.save_path = save_path

    def draw_borders(self, screen) -> None:
        """ Отобразить рамку. """
        screen.border(0)

    def draw_grid(self, screen) -> None:
        """ Отобразить состояние клеток. """
        for l in range(1, self.rows - 1):
            for k in range(1, self.cols - 1):
                if self.life.curr_generation[l][k]:
                    bam = "*"
                else:
                    bam = " "
                screen.addch(l, k, bam)

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

    if __name__ == "__main__":
        life = GameOfLife((15, 30), randomize=True)
        ui = Console(life, save_path=pathlib.Path("fileui.txt"))
        ui.run()