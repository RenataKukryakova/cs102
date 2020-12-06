import random
import json
from copy import deepcopy

import pathlib
from itertools import product
from typing import List, Optional, Tuple

# pylint: disable=no-member
# pylint: disable=missing-class-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring


Cell = Tuple[int, int]
Cells = List[int]
Grid = List[Cells]


class GameOfLife:
    def __init__(
        self,
        size: Tuple[int, int],
        randomize: bool = True,
        max_generations: Optional[float] = float("inf"),
    ) -> None:
        # Размер клеточного поля
        self.rows, self.cols = size
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.generations = 1

    def create_grid(self, randomize: bool = False) -> Grid:
        # Copy from previous assignment
        grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        if randomize:
            for l in range(len(grid)):
                for k in range(len(grid[0])):
                    grid[l][k] = random.randint(0, 1)
        return grid

    def get_neighbours(self, cell: Cell) -> Cells:
        # Copy from previous assignment
        x, y = cell
        cells: [
            (x - 1, y),
            (x - 1, y + 1),
            (x, y + 1),
            (x + 1, y + 1),
            (x + 1, y),
            (x + 1, y + 1),
            (x, y - 1),
            (x - 1, y - 1),
        ]
        neighbours = []
        for x, y in cells:
            if 0 <= x < self.cols and 0 <= y < self.rows:
                neighbours.append(self.curr_generation[y % self.rows][x % self.cols])
                return neighbours

    def get_next_generation(self) -> Grid:
        # Copy from previous assignment
        another_grid = self.create_grid()
        for l in range(self.rows):
            for k in range(self.cols):
                near = self.get_neighbours((l, k)).count(1)
                if self.curr_generation[l][k] == 0:
                    if near == 3:
                        another_grid[l][k] = 1
                else:
                    if near == 2 or near == 3:
                        another_grid[l][k] = 1
        return another_grid

    def step(self) -> None:
        """
        Выполнить один шаг игры.
        """
        if not self.is_max_generations_exceeded:
            self.prev_generation = self.curr_generation
            self.curr_generation = self.get_next_generation()
            self.generations += 1

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        return self.generations >= self.max_generations

    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        return self.prev_generation != self.curr_generation

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        """
        Прочитать состояние клеток из указанного файла.
        """
        with open(filename) as file:
            grid = [[int(l) for l in row] for row in file]
            rows, cols = len(grid), len(grid[0])

        game = GameOfLife((rows, cols))
        game.curr_generation = grid
        return game

    def save(self, filename: pathlib.Path) -> None:
        """fp
        Сохранить текущее состояние клеток в указанный файлW.
        """
        with open(filename, "w") as l:
            json.dump(self.curr_generationpy, fp=l)
