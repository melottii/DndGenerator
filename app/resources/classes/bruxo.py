from app.builders.fabrica_abstrata.Classe import Classe
from app.builders.prototipo.ItemPrototipo import ItemPrototipo

import random

class Bruxo(Classe):
    def __init__(self, personagem):
        super().__init__()
        self.name = "BRUXO"
        self.proficiency_bonus = "+2"
        self.life = 8 + int(personagem.dices["modifiers"]["constitution"])
        self.dices_life = "1d8"
        self.knowledge =  ["Armaduras leves", "Armas simples"]
        self.magic = { 
            0: {
                "Amizade (encantamento)": {
                    "Tempo de Conjuração": "1 Ação",
                    "Alcance": "Pessoal",
                    "Componentes": "S, M (uma pequena quantidade de maquiagem aplicada ao rosto durante a conjuração da magia)",
                    "Duração": "Concentração, até 1 minuto",
                    "Descrição": "Pela duração, você terá vantagem em todos os testes de Carisma direcionados a uma criatura, à sua escolha, que não seja hostil a você. Quando a magia acabar, a criatura perceberá que você usou maia para influenciar o humor dela, e ficará hostil a você. Uma criatura propensa a violência irá atacar você. Outra criatura pode buscar outras formas de retaliação (a critério do Mestre), dependendo da natureza da sua interação com ela."
                },
                "Ataque Certeiro (adivinhação)": {
                    "Tempo de Conjuração": "1 Ação",
                    "Alcance": "9 Metros",
                    "Componentes": "S",
                    "Duração": "Até 1 rodada",
                    "Descrição": "Você estende sua mão e aponta o dedo para um alvo no alcance. Sua magia garante a você uma breve intuição sobre as defesas do alvo. No seu próximo turno, você terá vantagem na primeira jogada de ataque contra o alvo, considerando que essa magia não tenha acabado."
                },
                "Ilusão Menor (ilusãoo)": {
                    "Tempo de Conjuração": "1 Ação",
                    "Alcance": "9 Metros",
                    "Componentes": "V, M (Um pouco de lã)",
                    "Duração": "1 Minuto",
                    "Descrição": "Você cria um som ou uma imagem de um objeto, dentro do alcance, que permanece pela duração. A ilusão também termina se você dissipa-la usando uma ação ou conjurar essa magia novamente. Se você criar um som, seu volume pode variar entre um sussurro até um grito. Pode ser a sua voz, a voz de outrem, o rugido de um leão, batidas de tambor ou qualquer outro som que você quiser. O som permanece no mesmo volume durante toda duração ou você pode fazer sons distintos em momentos diferentes, antes da magia acabar. Se você criar uma imagem de um objeto – como uma cadeira, pegadas de lama ou um pequeno baú – ela não pode ter mais de 1,5 metro cúbico. A imagem não pode produzir som, luz, cheiro ou qualquer outro efeito sensorial. Interação física com a imagem revelará que ela é uma ilusão, já que as coisas podem atravessa-la. Se uma criatura usar sua ação para examinar a imagem, ela pode determinar que ela é uma ilusão se obtiver sucesso num teste de Inteligência (Investigação) contra a CD da magia. Se uma criatura discernir a ilusão como sendo isso, a ilusão se tornará suave para a criatura."
                },
                "Mãos Mágicas (conjuração)": {
                    "Tempo de Conjuração": "1 Ação",
                    "Alcance": "9 Metros",
                    "Componentes": "V, S",
                    "Duração": "Até 1 rodada",
                    "Descrição": "Uma mão espectral flutuante aparece num ponto, à sua escolha, dentro do alcance. A mão permanece pela duração ou até você dissipa-la com uma ação. A mão some se estiver a mais de 9 metros de você ou se você conjurar essa magia novamente. Você pode usar sua ação para controlar a mão. Você pode usar a mão para manipular um objeto, abrir uma porta ou recipiente destrancado, guardar ou pegar um item de um recipiente aberto ou derramar o conteúdo de um frasco. Você pode mover a mão até 9 metros a cada vez que a usa. A mão não pode atacar, ativar itens mágicos ou carregar mais de 5 quilos."
                },
                "Prestidigitação (transmutação)": {
                    "Tempo de Conjuração": "1 Ação",
                    "Alcance": "3 Metros",
                    "Componentes": "V, S",
                    "Duração": "Até 1 hora",
                    "Descrição": "Essa magia é um truque mágico simples que conjuradores iniciantes usam para praticar. Você cria um dos seguintes efeitos mágicos dentro do alcance: Você cria, instantaneamente, um efeito sensorial inofensivo, como uma chuva de faíscas, um sopro de vento, notas musicais suaves ou um odor estranho. Você, instantaneamente, acende ou apaga uma vela, uma tocha ou uma pequena fogueira. Você, instantaneamente, limpa ou suja um objeto de até 1 metro cúbico. Você esfria, esquenta ou melhora o sabor de até 1 metro cubico de matéria inorgânica por 1 hora. Você faz uma cor, uma pequena marca ou um símbolo aparecer em um objeto ou superfície por 1 hora. Você cria uma bugiganga não-mágica ou uma imagem ilusória que caiba na sua mão e que dura até o final do seu próximo turno. Se você conjurar essa magia diversas vezes, você pode ter até três dos seus efeitos não-instantâneos ativos, ao mesmo tempo, e você pode dissipar um desses efeitos com uma ação."
                },
                "Proteção contra Lâminas (abjuração)": {
                    "Tempo de Conjuração": "1 Ação",
                    "Alcance": "Pessoal.",
                    "Componentes": "V, S",
                    "Duração": "Até 1 rodada",
                    "Descrição": "Você estende suas mãos e desenha um símbolo de proteção no ar. Até o final do seu próximo turno, você terá resistência contra dano de concussão, cortante e perfurante causado por ataques com armas."
                },
                "Rajada de Veneno (conjuração)": {
                    "Tempo de Conjuração": "1 Ação",
                    "Alcance": "3 Metros",
                    "Componentes": "V, S",
                    "Duração": "Instantânea",
                    "Descrição": "Você ergue sua mão em direção de uma criatura que você possa ver, dentro do alcance e projeta um sopro de gás tóxico da sua palma. A criatura deve ser bem sucedida num teste de resistência de Constituição ou sofrerá 1d12 de dano de veneno. O dano dessa magia aumenta em 1d12 quando você alcança o 5° nível (2d12), 11° nível (3d12) e 17° nível (4d12)."
                },
                "Rajada Mística (evocação)": {
                    "Tempo de Conjuração": "1 Ação",
                    "Alcance": "36 Metros",
                    "Componentes": "V, S",
                    "Duração": "Instantânea",
                    "Descrição": "Um feixe de energia crepitante vai em direção a uma criatura dentro do alcance. Realize uma jogada de ataque à distância com magia contra o alvo. Se atingir, o alvo sofre 1d10 de dano de energia. A magia cria mais de um feixe quando você alcança níveis elevados: dois feixes no 5° nível, três feixes no 11° nível e quatro feixes no 17° nível. Você pode direcionar os feixes para o mesmo alvo ou para alvos diferentes. Realize jogadas de ataque separadas para cada feixe."
                },
                "Toque Arrepiante (necromancia)": {
                    "Tempo de Conjuração": "1 Ação",
                    "Alcance": "36 Metros",
                    "Componentes": "v, S",
                    "Duração": "Até 1 rodada",
                    "Descrição": "Você cria uma mão esquelética fantasmagórica no espaço de uma criatura, dentro do alcance. Realize um ataque à distância com magia contra a criatura para afeta-la com o frio sepulcral. Se atingir, a criatura sofre 1d8 de dano necrótico e não poderá recuperar pontos de vida até o início do seu próximo turno. Até lá, a mão ficará presa ao alvo. Se você atingir um alvo morto-vivo, ele terá desvantagem nas jogadas de ataque contra você até o final do seu próximo turno. O dano dessa magia aumenta em 1d8 quando você alcança o 5° nível (2d8), 11° nível (3d8) e 17° nível (4d8)."
                }
            },
            1: {
                "Armadura de Agathys (abjuração)": {
                    "Tempo de Conjuração": "1 Ação",
                    "Alcance": "Pessoal",
                    "Componentes": "V, S, M (Um copo de água)",
                    "Duração": "1 Hora",
                    "Descrição": "Uma força magica protetora envolve você, manifestando- se como um frio espectral que cobre você e seu equipamento. Você ganha 5 pontos de vida temporários pela duração. Se uma criatura atingir você com um ataque corpo-a-corpo enquanto estiver com esses pontos de vida, a criatura sofrerá 5 de dano de frio. Em Níveis Superiores. Quando você conjurar essa magia usando um espaço de magia de 2° nível ou superior, tanto os pontos de vida temporários quanto o dano de frio aumentam em 5 para cada nível do espaço acima do 1°."
                },
                "Braços de Hadar (conjuração)": {
                    "Tempo de Conjuração": "1 Ação",
                    "Alcance": "Pessoal",
                    "Componentes": "V, S",
                    "Duração": "Instantânea",
                    "Descrição": "Você invoca o poder de Hadar, o Faminto Sombrio. Tentáculos de energia negra brotam de você e golpeiam todas as criaturas a até 3 metros de você. Cada criatura na área deve realizar um teste de resistência de Força. Se falhar, o alvo sofre 2d6 de dano necrótico e não pode fazer reações até o próximo turno dela. Em um sucesso, uma criatura sofre metade do dano e não sofre qualquer outro efeito. Em Níveis Superiores. Quando você conjurar essa magia usando um espaço de magia de 2° nível ou superior, o dano aumenta em 1d6 para cada nível do espaço acima do 1°."
                },
                "Bruxaria (encantamento)": {
                    "Tempo de Conjuração": "1 Ação bônus",
                    "Alcance": "18 Metros",
                    "Componentes": "V, S, M (Olho petrificado de um tritão)",
                    "Duração": "Até 1 hora",
                    "Descrição": "Você coloca uma maldição em uma criatura que você possa ver, dentro do alcance. Até a magia acabar, você causa 1d6 de dano necrótico extra no alvo sempre que atingi-lo com um ataque. Além disso, escolha uma habilidade quando você conjurar a magia. O alvo tem desvantagem em testes de habilidade feitos com a habilidade escolhida. Se o alvo cair a 0 pontos de vida antes da magia acabar, você pode usar uma ação bônus, em um turno subsequente, para amaldiçoar outra criatura. Uma magia remover maldição conjurada no alvo acaba com a magia prematuramente. Em Níveis Superiores. Quando você conjurar essa magia usando um espaço de magia de 3° ou 4° nível, você poderá manter sua concentração na magia por até 8 horas. Quando você usar um espaço de magia de 5° nível ou superior, você poderá manter sua concentração na magia por até 24 horas."
                },
                "Compreender Idiomas (adivinhção, ritual)": {
                    "Tempo de Conjuração": "1 Ação",
                    "Alcance": "Pessoal",
                    "Componentes": "V, S, M (Uma pitada de fuligem e sal.)",
                    "Duração": "Até 1 hora",
                    "Descrição": "Pela duração, você compreende o significado literal de qualquer idioma falado que você ouvir. Você também compreende qualquer idioma escrito que vir, mas você deve tocar a superfície onde as palavras estão escritas. Leva, aproximadamente, 1 minuto para ler uma página de texto. Essa magia não decifra mensagens secretas em textos ou glifos, como um selo arcano, que não seja parte de um idioma escrito."
                },
                "Enfeitiçar Pessoa (encantamento)": {
                    "Tempo de Conjuração": "1 Ação",
                    "Alcance": "9 Metros",
                    "Componentes": "V,S",
                    "Duração": "Até 1 hora",
                    "Descrição": "Você tenta enfeitiçar um humanoide que você possa ver dentro do alcance. Ele deve realizar um teste de resistência de Sabedoria, e recebe vantagem nesse teste se você ou seus companheiros estiverem lutando com ele. Se ele falhar, ficará enfeitiçado por você até a magia acabar ou até você ou seus companheiros fizerem qualquer coisa nociva contra ele. A criatura enfeitiçada reconhece você como um conhecido amigável. Quando a magia acabar, a criatura saberá que foi enfeitiçada por você. Em Níveis Superiores. Se você conjurar essa magia usando um espaço de magia de 2° nível ou superior, você pode afetar uma criatura adicional para cada nível do espaço acima do 1°. As criaturas devem estar a até 9 metros umas das outras quando você for afeta-las."
                },
                "Escrita ilusória (ilusão, ritual)": {
                    "Tempo de Conjuração": "1 minuto",
                    "Alcance": "Toque",
                    "Componentes": "S, M (uma tinta à base de chumbo valendo, no mínimo, 10 po, que é consumida pela magia.)",
                    "Duração": "10 dias",
                    "Descrição": "Você escreve em um pergaminho, papel ou qualquer outro material adequado e tinge ele com uma poderosa ilusão que permanece pela duração. Para você e para qualquer criatura que você designar quando você conjura essa magia, a escrita parece normal, escrita com a sua caligrafia e transmite qualquer que seja a mensagem que você desejava quando escreveu o texto. Para todos os outros, a escrita aparece como se tivesse sido escrita com uma caligrafia desconhecida ou mágica que é inteligível. Alternativamente, você pode fazer a escrita parecer uma mensagem totalmente diferente, escrita com uma caligrafia e idioma diferentes, apesar de o idioma precisar ser um que você conheça. No caso da magia ser dissipada, tanto a escrita original quanto a ilusória desaparecem. Uma criatura com visão verdadeira pode ler a mensagem escondida."
                },
                "Proteção contra o Bem e Mal (abjuração)": {
                    "Tempo de Conjuração": "1 Ação",
                    "Alcance": "Toque",
                    "Componentes": "V, S, M (água benta ou pó de prata e ferro, consumidos pela magia.)",
                    "Duração": "Até 10 minutos",
                    "Descrição": "Até a magia acabar, uma criatura voluntária que você tocar estará protegida contra certos tipos de criaturas: aberrações, celestiais, corruptores, elementais, fadas e mortos-vivos. A proteção garante diversos benefícios. As criaturas desse tipo tem desvantagem nas jogadas de ataque contra o alvo. O alvo não pode ser enfeitiçado, amedrontado ou possuído por elas. Se o alvo já estiver enfeitiçado, amedrontado ou possuído por uma dessas criaturas, o alvo terá vantagem em qualquer novo teste de resistência contra o efeito relevante."
                },
                "Raio de Bruxa (evocaçã3o)": {
                    "Tempo de Conjuração": "1 Ação",
                    "Alcance": "9 Metros",
                    "Componentes": "V, S, M (Um galho de uma árvore que tenha sido atingida por um relâmpago.)",
                    "Duração": "Até 1 minuto",
                    "Descrição": "Um raio crepitante de energia azul é arremessado em uma criatura dentro do alcance, formando um arco elétrico contínuo entre você e o alvo. Faça um ataque à distância com magia contra a criatura. Se atingir, o alvo sofrerá 1d12 de dano elétrico e, em cada um dos seus turnos, pela duração, você pode usar sua ação para causar 1d12 de dano elétrico ao alvo, automaticamente. A magia acaba se você usar sua ação para fazer qualquer outra coisa. A magia também acaba se o alvo estiver fora do alcance da magia ou se você tiver cobertura total para ele. Em Níveis Superiores. Quando você conjurar essa magia usando um espaço de magia de 2° nível ou superior, o dano inicial aumenta em 1d12 para cada nível do espaço acima do 1°."
                },
                "Recuo Acelerado (transmutação)": {
                    "Tempo de Conjuração": "1 Ação bônus",
                    "Alcance": "Pessoal",
                    "Componentes": "V, S",
                    "Duração": "Até 10 minutos",
                    "Descrição": "Essa magia permite que você se mova a um ritmo incrível. Quando você conjura essa magia e, a partir de então, com uma ação bônus em cada um dos seus turnos, até a magia acabar, você pode realizar a ação de Disparada."
                },
                "Repreensão Infernal (evocação)": {
                    "Tempo de Conjuração": "1 Ação",
                    "Alcance": "18 Metros",
                    "Componentes": "V, S",
                    "Duração": "Instantênea",
                    "Descrição": "Reação que você faz em resposta ao sofre dano de uma criatura a até 18 metros de você e que você possa ver. Você aponta seu dedo e a criatura que causou dano a você é, momentaneamente, envolta por chamas infernais. A criatura deve realizar um teste de resistência de Destreza. Ela sofre 2d10 de dano de fogo se falhar na resistência ou metade desse dano se obtiver sucesso. Em Níveis Superiores. Quando você conjurar essa magia usando um espaço de magia de 2° nível ou superior, o dano aumenta em 1d10 para cada nível do espaço acima do 1°."
                },
                "Servo Invisível (conjuração, ritual)": {
                    "Tempo de Conjuração": "1 Ação",
                    "Alcance": "18 Metros",
                    "Componentes": "V, S, M (um pedaço de barbante e um pouco de madeira)",
                    "Duração": "Até 1 hora",
                    "Descrição": "Você aponta seu dedo e a criatura que causou dano a você é, momentaneamente, envolta por chaEssa magia cria uma força invisível, sem mente e sem forma que realiza tarefas simples, ao seu comando, até a magia acabar. O servo aparece do nada em um espaço desocupado no chão, dentro do alcance. Ele tem CA 10, 1 ponto de vida, Força 2 e não pode atacar. Se ele cair a 0 pontos de vida, a magia acaba. Uma vez em cada um dos seus turnos, com uma ação bônus, você pode comandar, mentalmente, o servo para se mover até 4,5 metros e interagir com um objeto. O servo pode realizar tarefas simples que um serviçal humano faria, como buscar coisas, limpar, consertar, dobrar roupas, acender chamas, servir comida ou derramar vinho. Uma vez que um comando seja dado, o servo realiza a tarefa da melhor forma possível, até completar a tarefa, então esperará o seu próximo comando. Se você comandar o servo a realizar uma tarefa que poderia afasta-lo a mais de 18 metros de você, a magia termina."
                }
            }
        }
        self.expertise = Bruxo.__set_skill_list__(personagem)
        self.equip = Bruxo.__set_equip__(personagem)
        self.endurance_tests = ["wisdom", "charisma"]

    @staticmethod
    def __set_skill_list__(personagem):
        rogue_list = ["Arcanismo", "Enganação", "História", "Intimidação",
                            "Investigação", "Natureza", "Religião"]
        final_list = [i for i in rogue_list if i not in personagem.expertise]
        return random.choices(final_list, k=2)

    @staticmethod
    def __set_equip__(personagem):
        try:
            prototipo = ItemPrototipo()

            a = random.choice(["Besta Leve", "Arma Simples"])
            item = None
            item2 = None
            item3 = None
            item4 = None
            item5 = None

            if a == "Besta Leve":
                item = prototipo.get_arma_distancia_simples(a)
                item2 = prototipo.get_equipamento("Virotes (20)", 1)
            else:
                opcao = random.randint(1,2)
                opcoes = {
                    1: prototipo.get_random_arma_corpo_a_corpo_simples(),
                    2: prototipo.get_random_arma_distancia_simples(),
                }
                item = opcoes[opcao]

            personagem.equip["Armas"].append(item)
            if item2 != None:
                personagem.equip["Equipamentos"].append(item2)

            b = random.choice(["Bolsa de componentes", "Foco arcano"])

            if b == "Bolsa de componentes":
                item = prototipo.get_equipamento(b, 1)
            else:
                item = prototipo.get_equipamento("Bastão", 1)
                item2 = prototipo.get_equipamento("Cajado", 1)
                item3 = prototipo.get_equipamento("Cristal", 1)
                item4 = prototipo.get_equipamento("Orbe", 1)
                item5 = prototipo.get_equipamento("Varinha", 1)
                personagem.equip["Equipamentos"].append(item2)
                personagem.equip["Equipamentos"].append(item3)
                personagem.equip["Equipamentos"].append(item4)
                personagem.equip["Equipamentos"].append(item5)

            personagem.equip["Equipamentos"].append(item)

            item = prototipo.get_armadura_leve("Couro")
            personagem.equip["Armaduras"].append(item)

            opcao = random.randint(1,2)
            opcoes = {
                1: prototipo.get_random_arma_corpo_a_corpo_simples(),
                2: prototipo.get_random_arma_distancia_simples(),
            }
            item = opcoes[opcao]
            personagem.equip["Armas"].append(item)

            item = prototipo.get_arma_corpo_a_corpo_simples("Adaga")
            personagem.equip["Armas"].append(item)
            item = prototipo.get_arma_corpo_a_corpo_simples("Adaga")
            personagem.equip["Armas"].append(item)


            nome = random.choice(["Pacote de Estudioso", "Pacote de Explorador"])
            pacote = prototipo.get_pacote(nome)
            prototipo.add_equipamentos_pacote(pacote, personagem)

        except Exception as e:
            print(e)
        
    def __set_magic__(self, personagem):
        magias_nivel0 = random.choices(list(self.magic[0].keys()), k=2)
        magias_nivel1 = random.choices(list(self.magic[1].keys()), k=2)

        nivel0 = {
            magias_nivel0[0]: self.magic[0][magias_nivel0[0]],
            magias_nivel0[1]: self.magic[0][magias_nivel0[1]]
        }

        nivel1 = {
            magias_nivel1[0]: self.magic[1][magias_nivel1[0]],
            magias_nivel1[1]: self.magic[1][magias_nivel1[1]]
        }

        personagem.magic[0] = nivel0
        personagem.magic[1] = nivel1

    def get_name(self):
        return f"CLASSE: {self.name}"

    def __set_config__(self, personagem):
        self.__set_magic__(personagem)

        personagem.life += self.life
        for i in self.endurance_tests:
            personagem.dices["resistence_test"].append(i)
        personagem.proficiency_bonus = self.proficiency_bonus

        for n in self.knowledge:
            personagem.knowledge.append(n)

        for m in self.expertise:
            personagem.expertise.append(m)
