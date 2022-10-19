from abc import ABC, abstractmethod


class Raca(ABC):
    @abstractmethod
    def get_name(self):
        pass

    def get_race_variancy(self):
        pass
