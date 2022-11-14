from app.builders.fabrica_abstrata.FabricaPersonagem import FabricaPersonagem

class BuilderPersonagem:
    def director(self, name: str, race: str, chosen_class: str, background: str):
        fabricaPersonagem = FabricaPersonagem()
        fabricaPersonagem.__set_name__(name)
        fabricaPersonagem.__set_trend__()
        fabricaPersonagem.__set_race__(race)
        fabricaPersonagem.__set_status__()
        fabricaPersonagem.__set_background__(background)
        fabricaPersonagem.__set_class__(chosen_class)
        return fabricaPersonagem