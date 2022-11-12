"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi
from math import sqrt


__author__ = "730575619"  


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, point_two) -> float:
        """Calculates the distance between two point values."""
        return sqrt((self.x - point_two.x)**2 + (self.y - point_two.y)**2)


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction
        
    def tick(self) -> None:
        """Changes the location of the object given its direction and current position. Also immunizes a cell after a set time period (in constants.py)."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()
    
    def contract_disease(self) -> None:
        """Makes a cell infected (directly changes sickness attribute)."""
        self.sickness = constants.INFECTED

    def immunize(self) -> None:
        """Makes a cell immune (directly changes sickness attribute)."""
        self.sickness = constants.IMMUNE
    
    def is_immune(self) -> bool:
        """Returns True if a cell is immune."""
        if self.sickness == constants.IMMUNE:
            return True

    def is_vulnerable(self) -> bool:
        """Returns True if a cell is vulnerable (not infected nor immune)."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False

    def is_infected(self) -> bool:
        """Returns True if a cell if infected."""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False

    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_vulnerable():
            return "gray"
        elif self.is_infected():
            return "red"
        elif self.is_immune():
            return "blue"
    
    def contact_with(self, Cell_two) -> None:
        """Tests every pair of Cells for a contact."""
        if self.is_infected() and Cell_two.is_vulnerable():
            Cell_two.contract_disease()
        elif Cell_two.is_infected() and self.is_vulnerable():
            self.contract_disease()


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infected: int, immune: int = 0):
        """Initialize the cells with random locations and directions."""
        if infected >= cells or infected <= 0:
            raise ValueError("Some number of the Cell object must begin infected. The number of infected cells cannot be more than the Cell object or negative.")
        elif immune >= cells or immune < 0:
            raise ValueError("The number of immune cells cannot be greater than the Cell object or negative.")
        self.population = []
        infected_count: int = infected
        immune_count: int = immune
        for _ in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            if immune_count != 0:
                cell.immunize()
                immune_count -= 1
            elif infected_count != 0:
                cell.contract_disease()
                infected_count -= 1
            self.population.append(cell)

    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        for cell in self.population:
            if cell.is_infected():
                return False
        return True

    def check_contacts(self) -> None:
        """Tests whether any two Cell values come in 'contact' with each other."""
        index_cell_one: int = 0
        index_cell_two: int = 0
        while index_cell_one < len(self.population):
            index_cell_two = 0
            while index_cell_two < len(self.population):
                if index_cell_two <= index_cell_one:
                    index_cell_two += 1
                else:
                    distance: float = self.population[index_cell_one].location.distance(self.population[index_cell_two].location)
                    if distance < constants.CELL_RADIUS:
                        self.population[index_cell_one].contact_with(self.population[index_cell_two])
                    index_cell_two += 1
            index_cell_one += 1