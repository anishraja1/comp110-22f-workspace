from __future__ import annotations


class ChristmasTreeFarm:

    plots: list[int]

    def __init__(self, plots: int, initial_planting: int):
        self.plots = []
        for num in range(initial_planting):
            self.plots.append(1)
        for num in range(plots - initial_planting):
            self.plots.append(0)

    def plant(self, plot_index: int) -> None:
        self.plots[plot_index] = 1

    def growth(self) -> None:
        count: int = 0
        while count != len(self.plots):
            if self.plots[count] != 0:
                self.plots[count] += 1
            count += 1

    def harvest(self, replant: bool) -> int:
        total: int = 0
        count: int = 0
        while count != len(self.plots):
            if self.plots[count] >= 5:
                if replant:
                    self.plots[count] = 1
                else:
                    self.plots[count] = 0
                total += 1
            count += 1
        return total

    def __add__(self, rhs: ChristmasTreeFarm) -> ChristmasTreeFarm:
        plot_one_count: int = 0
        for plot in self.plots:
            if plot != 0:
                plot_one_count += 1
        plot_two_count: int = 0
        for plot in rhs.plots:
            if plot != 0:
                plot_two_count += 1
        return ChristmasTreeFarm(len(self.plots) + len(rhs.plots), sum(plot_one_count + plot_two_count))




one: ChristmasTreeFarm = ChristmasTreeFarm(10, 5)


