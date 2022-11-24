from abc import abstractmethod

from app.builders.fabrica_abstrata.FabricaPersonagem import FabricaPersonagem


class BuilderPersonagem:
    @abstractmethod
    def director(self, name: str, race: str, chosen_class: str, background: str):
        fabrica_personagem = FabricaPersonagem()
        fabrica_personagem.__set_name__(name)
        fabrica_personagem.__set_trend__()
        fabrica_personagem.__set_race__(race)
        fabrica_personagem.__set_status__()
        fabrica_personagem.__set_background__(background)
        fabrica_personagem.__set_class__(chosen_class)
        return fabrica_personagem
