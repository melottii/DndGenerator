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
        self.knowledge = ["Armaduras leves", "Armas simples"]
        self.magic = {
            0: {
                "Amizade (encantamento)": {
                    "Tempo de Conjuração": "1 Ação",
                    "Alcance": "Pessoal",
                    "Componentes": "S, M (uma pequena quantidade de maquiagem aplicada ao rosto durante a conjuração "
                                   "da magia)",
                    "Duração": "Concentração, até 1 minuto",
                    "Descrição": "Pela duração, você terá vantagem em todos os testes de Carisma direcionados a uma "
                                 "criatura, à sua escolha, que não seja hostil a você. Quando a magia acabar, a "
                                 "criatura perceberá que você usou maia para influenciar o humor dela, e ficará "
                                 "hostil a você. Uma criatura propensa a violência irá atacar você. Outra criatura "
                                 "pode buscar outras formas de retaliação (a critério do Mestre), dependendo da "
                                 "natureza da sua interação com ela."
                },
                "Ataque Certeiro (adivinhação)": {
                    "Tempo de Conjuração": "1 Ação",
                    "Alcance": "9 Metros",
                    "Componentes": "S",
                    "Duração": "Até 1 rodada",
                    "Descrição": "Você estende sua mão e aponta o dedo para um alvo no alcance. Sua magia garante a "
                                 "você uma breve intuição sobre as defesas do alvo. No seu próximo turno, você terá "
                                 "vantagem na primeira jogada de ataque contra o alvo, considerando que essa magia "
                                 "não tenha acabado."
                },
                "Ilusão Menor (ilusãoo)": {
                    "Tempo de Conjuração": "1 Ação",
                    "Alcance": "9 Metros",
                    "Componentes": "V, M (Um pouco de lã)",
                    "Duração": "1 Minuto",
                    "Descrição": "Você cria um som ou uma imagem de um objeto, dentro do alcance, que permanece pela "
                                 "duração. A ilusão também termina se você dissipa-la usando uma ação ou conjurar "
                                 "essa magia novamente. Se você criar um som, seu volume pode variar entre um "
                                 "sussurro até um grito. Pode ser a sua voz, a voz de outrem, o rugido de um leão, "
                                 "batidas de tambor ou qualquer outro som que você quiser. O som permanece no mesmo "
                                 "volume durante toda duração ou você pode fazer sons distintos em momentos diferentes,"
                                 " antes da magia acabar. Se você criar uma imagem de um objeto – como uma cadeira, "
                                 "pegadas de lama ou um pequeno baú – ela não pode ter mais de 1,5 metro cúbico. A "
                                 "imagem não pode produzir som, luz, cheiro ou qualquer outro efeito sensorial. "
                                 "Interação física com a imagem revelará que ela é uma ilusão, já que as coisas podem "
                                 "atravessa-la. Se uma criatura usar sua ação para examinar a imagem, ela pode "
                                 "determinar que ela é uma ilusão se obtiver sucesso num teste de "
                                 "Inteligência (Investigação) contra a CD da magia. Se uma criatura discernir a ilusão "
                                 "como sendo isso, a ilusão se tornará suave para a criatura."
                },
                "Mãos Mágicas (conjuração)": {
                    "Tempo de Conjuração": "1 Ação",
                    "Alcance": "9 Metros",
                    "Componentes": "V, S",
                    "Duração": "Até 1 rodada",
                    "Descrição": "Uma mão espectral flutuante aparece num ponto, à sua escolha, dentro do alcance. A "
                                 "mão permanece pela duração ou até você dissipa-la com uma ação. A mão some se estiver"
                                 " a mais de 9 metros de você ou se você conjurar essa magia novamente. Você pode usar "
                                 "sua ação para controlar a mão. Você pode usar a mão para manipular um objeto, abrir "
                                 "uma porta ou recipiente destrancado, guardar ou pegar um item de um recipiente aberto"
                                 " ou derramar o conteúdo de um frasco. Você pode mover a mão até 9 metros a cada vez "
                                 "que a usa. A mão não pode atacar, ativar itens mágicos ou carregar mais de 5 quilos."
                },
                "Prestidigitação (transmutação)": {
                    "Tempo de Conjuração": "1 Ação",
                    "Alcance": "3 Metros",
                    "Componentes": "V, S",
                    "Duração": "Até 1 hora",
                    "Descrição": "Essa magia é um truque mágico simples que conjuradores iniciantes usam para praticar."
                                 " Você cria um dos seguintes efeitos mágicos dentro do alcance: Você cria, "
                                 "instantaneamente, um efeito sensorial inofensivo, como uma chuva de faíscas, um sopro"
                                 " de vento, notas musicais suaves ou um odor estranho. Você, instantaneamente, acende"
                                 " ou apaga uma vela, uma tocha ou uma pequena fogueira. Você, instantaneamente, limpa"
                                 " ou suja um objeto de até 1 metro cúbico. Você esfria, esquenta ou melhora o sabor de"
                                 " até 1 metro cubico de matéria inorgânica por 1 hora. Você faz uma cor, uma pequena"
                                 " marca ou um símbolo aparecer em um objeto ou superfície por 1 hora. Você cria uma "
                                 "bugiganga não-mágica ou uma imagem ilusória que caiba na sua mão e que dura até o "
                                 "final do seu próximo turno. Se você conjurar essa magia diversas vezes, você pode "
                                 "ter até três dos seus efeitos não-instantâneos ativos, ao mesmo tempo, e você pode "
                                 "dissipar um desses efeitos com uma ação."
                },
                "Proteção contra Lâminas (abjuração)": {
                    "Tempo de Conjuração": "1 Ação",
                    "Alcance": "Pessoal.",
                    "Componentes": "V, S",
                    "Duração": "Até 1 rodada",
                    "Descrição": "Você estende suas mãos e desenha um símbolo de proteção no ar. Até o final do seu"
                                 " próximo turno, você terá resistência contra dano de concussão, cortante e perfurante"
                                 " causado por ataques com armas."
                },
                "Rajada de Veneno (conjuração)": {
                    "Tempo de Conjuração": "1 Ação",
                    "Alcance": "3 Metros",
                    "Componentes": "V, S",
                    "Duração": "Instantânea",
                    "Descrição": "Você ergue sua mão em direção de uma criatura que você possa ver, dentro do alcance"
                                 " e projeta um sopro de gás tóxico da sua palma. A criatura deve ser bem sucedida num"
                                 " teste de resistência de Constituição ou sofrerá 1d12 de dano de veneno. O dano dessa"
                                 " magia aumenta em 1d12 quando você alcança o 5° nível (2d12), 11° nível (3d12) e 17°"
                                 " nível (4d12)."
                },
                "Rajada Mística (evocação)": {
                    "Tempo de Conjuração": "1 Ação",
                    "Alcance": "36 Metros",
                    "Componentes": "V, S",
                    "Duração": "Instantânea",
                    "Descrição": "Um feixe de energia crepitante vai em direção a uma criatura dentro do alcance. "
                                 "Realize uma jogada de ataque à distância com magia contra o alvo. Se atingir, o alvo"
                                 " sofre 1d10 de dano de energia. A magia cria mais de um feixe quando você alcança "
                                 "níveis elevados: dois feixes no 5° nível, três feixes no 11° nível e quatro feixes"
                                 " no 17° nível. Você pode direcionar os feixes para o mesmo alvo ou para alvos"
                                 " diferentes. Realize jogadas de ataque separadas para cada feixe."
                },
                "Toque Arrepiante (necromancia)": {
                    "Tempo de Conjuração": "1 Ação",
                    "Alcance": "36 Metros",
                    "Componentes": "v, S",
                    "Duração": "Até 1 rodada",
                    "Descrição": "Você cria uma mão esquelética fantasmagórica no espaço de uma criatura, dentro do"
                                 " alcance. Realize um ataque à distância com magia contra a criatura para afeta-la"
                                 " com o frio sepulcral. Se atingir, a criatura sofre 1d8 de dano necrótico e não"
                                 " poderá recuperar pontos de vida até o início do seu próximo turno. Até lá, a mão"
                                 " ficará presa ao alvo. Se você atingir um alvo morto-vivo, ele terá desvantagem nas"
                                 " jogadas de ataque contra você até o final do seu próximo turno. O dano dessa magia"
                                 " aumenta em 1d8 quando você alcança o 5° nível (2d8), 11° nível (3d8) e "
                                 "17° nível (4d8)."
                }
            },
            1: {
                "Armadura de Agathys (abjuração)": {
                    "Tempo de Conjuração": "1 Ação",
                    "Alcance": "Pessoal",
                    "Componentes": "V, S, M (Um copo de água)",
                    "Duração": "1 Hora",
                    "Descrição": "Uma força magica protetora envolve você, manifestando- se como um frio espectral"
                                 " que cobre você e seu equipamento. Você ganha 5 pontos de vida temporários pela"
                                 " duração. Se uma criatura atingir você com um ataque corpo-a-corpo enquanto estiver "
                                 "com esses pontos de vida, a criatura sofrerá 5 de dano de frio. Em Níveis Superiores."
                                 " Quando você conjurar essa magia usando um espaço de magia de 2° nível ou superior,"
                                 " tanto os pontos de vida temporários quanto o dano de frio aumentam em 5 para cada"
                                 " nível do espaço acima do 1°."
                },
                "Braços de Hadar (conjuração)": {
                    "Tempo de Conjuração": "1 Ação",
                    "Alcance": "Pessoal",
                    "Componentes": "V, S",
                    "Duração": "Instantânea",
                    "Descrição": "Você invoca o poder de Hadar, o Faminto Sombrio. Tentáculos de energia negra brotam"
                                 " de você e golpeiam todas as criaturas a até 3 metros de você. Cada criatura na área"
                                 " deve realizar um teste de resistência de Força. Se falhar, o alvo sofre 2d6 de dano"
                                 " necrótico e não pode fazer reações até o próximo turno dela. Em um sucesso, uma"
                                 " criatura sofre metade do dano e não sofre qualquer outro efeito. Em Níveis"
                                 " Superiores. Quando você conjurar essa magia usando um espaço de magia de 2° nível ou"
                                 " superior, o dano aumenta em 1d6 para cada nível do espaço acima do 1°."
                },
                "Bruxaria (encantamento)": {
                    "Tempo de Conjuração": "1 Ação bônus",
                    "Alcance": "18 Metros",
                    "Componentes": "V, S, M (Olho petrificado de um tritão)",
                    "Duração": "Até 1 hora",
                    "Descrição": "Você coloca uma maldição em uma criatura que você possa ver, dentro do alcance. Até a"
                                 " magia acabar, você causa 1d6 de dano necrótico extra no alvo sempre que atingi-lo"
                                 " com um ataque. Além disso, escolha uma habilidade quando você conjurar a magia. O "
                                 "alvo tem desvantagem em testes de habilidade feitos com a habilidade escolhida. Se o"
                                 " alvo cair a 0 pontos de vida antes da magia acabar, você pode usar uma ação bônus,"
                                 " em um turno subsequente, para amaldiçoar outra criatura. Uma magia remover maldição "
                                 "conjurada no alvo acaba com a magia prematuramente. Em Níveis Superiores. Quando"
                                 " você conjurar essa magia usando um espaço de magia de 3° ou 4° nível, você poderá"
                                 " manter sua concentração na magia por até 8 horas. Quando você usar um espaço de"
                                 " magia de 5° nível ou superior, você poderá manter sua concentração na magia por"
                                 " até 24 horas."
                },
                "Compreender Idiomas (adivinhção, ritual)": {
                    "Tempo de Conjuração": "1 Ação",
                    "Alcance": "Pessoal",
                    "Componentes": "V, S, M (Uma pitada de fuligem e sal.)",
                    "Duração": "Até 1 hora",
                    "Descrição": "Pela duração, você compreende o significado literal de qualquer idioma falado que"
                                 " você ouvir. Você também compreende qualquer idioma escrito que vir, mas você deve"
                                 " tocar a superfície onde as palavras estão escritas. Leva, aproximadamente, 1 minuto"
                                 " para ler uma página de texto. Essa magia não decifra mensagens secretas em textos"
                                 " ou glifos, como um selo arcano, que não seja parte de um idioma escrito."
                },
                "Enfeitiçar Pessoa (encantamento)": {
                    "Tempo de Conjuração": "1 Ação",
                    "Alcance": "9 Metros",
                    "Componentes": "V,S",
                    "Duração": "Até 1 hora",
                    "Descrição": "Você tenta enfeitiçar um humanoide que você possa ver dentro do alcance. Ele deve"
                                 " realizar um teste de resistência de Sabedoria, e recebe vantagem nesse teste se você"
                                 " ou seus companheiros estiverem lutando com ele. Se ele falhar, ficará enfeitiçado "
                                 "por você até a magia acabar ou até você ou seus companheiros fizerem qualquer coisa"
                                 " nociva contra ele. A criatura enfeitiçada reconhece você como um conhecido amigável."
                                 " Quando a magia acabar, a criatura saberá que foi enfeitiçada por você. Em Níveis"
                                 " Superiores. Se você conjurar essa magia usando um espaço de magia de 2° nível ou"
                                 " superior, você pode afetar uma criatura adicional para cada nível do espaço acima"
                                 " do 1°. As criaturas devem estar a até 9 metros umas das outras quando você for"
                                 " afeta-las."
                },
                "Escrita ilusória (ilusão, ritual)": {
                    "Tempo de Conjuração": "1 minuto",
                    "Alcance": "Toque",
                    "Componentes": "S, M (uma tinta à base de chumbo valendo, no mínimo, 10 po, que é consumida pela"
                                   " magia.)",
                    "Duração": "10 dias",
                    "Descrição": "Você escreve em um pergaminho, papel ou qualquer outro material adequado e tinge ele"
                                 " com uma poderosa ilusão que permanece pela duração. Para você e para qualquer "
                                 "criatura que você designar quando você conjura essa magia, a escrita parece normal,"
                                 " escrita com a sua caligrafia e transmite qualquer que seja a mensagem que você "
                                 "desejava quando escreveu o texto. Para todos os outros, a escrita aparece como se "
                                 "tivesse sido escrita com uma caligrafia desconhecida ou mágica que é inteligível."
                                 " Alternativamente, você pode fazer a escrita parecer uma mensagem totalmente"
                                 " diferente, escrita com uma caligrafia e idioma diferentes, apesar de o idioma "
                                 "precisar ser um que você conheça. No caso da magia ser dissipada, tanto a escrita "
                                 "original quanto a ilusória desaparecem. Uma criatura com visão verdadeira pode ler "
                                 "a mensagem escondida."
                },
                "Proteção contra o Bem e Mal (abjuração)": {
                    "Tempo de Conjuração": "1 Ação",
                    "Alcance": "Toque",
                    "Componentes": "V, S, M (água benta ou pó de prata e ferro, consumidos pela magia.)",
                    "Duração": "Até 10 minutos",
                    "Descrição": "Até a magia acabar, uma criatura voluntária que você tocar estará protegida contra "
                                 "certos tipos de criaturas: aberrações, celestiais, corruptores, elementais, fadas e "
                                 "mortos-vivos. A proteção garante diversos benefícios. As criaturas desse tipo tem "
                                 "desvantagem nas jogadas de ataque contra o alvo. O alvo não pode ser enfeitiçado, "
                                 "amedrontado ou possuído por elas. Se o alvo já estiver enfeitiçado, amedrontado ou "
                                 "possuído por uma dessas criaturas, o alvo terá vantagem em qualquer novo teste de "
                                 "resistência contra o efeito relevante."
                },
                "Raio de Bruxa (evocaçã3o)": {
                    "Tempo de Conjuração": "1 Ação",
                    "Alcance": "9 Metros",
                    "Componentes": "V, S, M (Um galho de uma árvore que tenha sido atingida por um relâmpago.)",
                    "Duração": "Até 1 minuto",
                    "Descrição": "Um raio crepitante de energia azul é arremessado em uma criatura dentro do alcance,"
                                 " formando um arco elétrico contínuo entre você e o alvo. Faça um ataque à distância "
                                 "com magia contra a criatura. Se atingir, o alvo sofrerá 1d12 de dano elétrico e, em"
                                 " cada um dos seus turnos, pela duração, você pode usar sua ação para causar 1d12 de"
                                 " dano elétrico ao alvo, automaticamente. A magia acaba se você usar sua ação para"
                                 " fazer qualquer outra coisa. A magia também acaba se o alvo estiver fora do alcance "
                                 "da magia ou se você tiver cobertura total para ele. Em Níveis Superiores. Quando "
                                 "você conjurar essa magia usando um espaço de magia de 2° nível ou superior, o dano "
                                 "inicial aumenta em 1d12 para cada nível do espaço acima do 1°."
                },
                "Recuo Acelerado (transmutação)": {
                    "Tempo de Conjuração": "1 Ação bônus",
                    "Alcance": "Pessoal",
                    "Componentes": "V, S",
                    "Duração": "Até 10 minutos",
                    "Descrição": "Essa magia permite que você se mova a um ritmo incrível. Quando você conjura essa "
                                 "magia e, a partir de então, com uma ação bônus em cada um dos seus turnos, até a "
                                 "magia acabar, você pode realizar a ação de Disparada."
                },
                "Repreensão Infernal (evocação)": {
                    "Tempo de Conjuração": "1 Ação",
                    "Alcance": "18 Metros",
                    "Componentes": "V, S",
                    "Duração": "Instantênea",
                    "Descrição": "Reação que você faz em resposta ao sofre dano de uma criatura a até 18 metros de "
                                 "você e que você possa ver. Você aponta seu dedo e a criatura que causou dano a você "
                                 "é, momentaneamente, envolta por chamas infernais. A criatura deve realizar um teste "
                                 "de resistência de Destreza. Ela sofre 2d10 de dano de fogo se falhar na resistência "
                                 "ou metade desse dano se obtiver sucesso. Em Níveis Superiores. Quando você conjurar "
                                 "essa magia usando um espaço de magia de 2° nível ou superior, o dano aumenta em 1d10"
                                 " para cada nível do espaço acima do 1°."
                },
                "Servo Invisível (conjuração, ritual)": {
                    "Tempo de Conjuração": "1 Ação",
                    "Alcance": "18 Metros",
                    "Componentes": "V, S, M (um pedaço de barbante e um pouco de madeira)",
                    "Duração": "Até 1 hora",
                    "Descrição": "Você aponta seu dedo e a criatura que causou dano a você é, momentaneamente, envolta"
                                 " por chaEssa magia cria uma força invisível, sem mente e sem forma que realiza "
                                 "tarefas simples, ao seu comando, até a magia acabar. O servo aparece do nada em um"
                                 " espaço desocupado no chão, dentro do alcance. Ele tem CA 10, 1 ponto de vida, Força"
                                 " 2 e não pode atacar. Se ele cair a 0 pontos de vida, a magia acaba. Uma vez em cada "
                                 "um dos seus turnos, com uma ação bônus, você pode comandar, mentalmente, o servo para"
                                 " se mover até 4,5 metros e interagir com um objeto. O servo pode realizar tarefas "
                                 "simples que um serviçal humano faria, como buscar coisas, limpar, consertar, dobrar"
                                 " roupas, acender chamas, servir comida ou derramar vinho. Uma vez que um comando seja"
                                 " dado, o servo realiza a tarefa da melhor forma possível, até completar a tarefa, "
                                 "então esperará o seu próximo comando. Se você comandar o servo a realizar uma tarefa "
                                 "que poderia afasta-lo a mais de 18 metros de você, a magia termina."
                }
            }
        }
        self.expertise = Bruxo.__set_skill_list__(personagem)
        self.equip = Bruxo.__set_equip__(personagem)
        self.endurance_tests = ["wisdom", "charisma"]
        self.skills = {"MAGIAS DE PACTO": "Sua pesquisa arcana e a magia outorgada a você por seu patrono, lhe concedem"
                                          " uma gama de magias. Veja o capítulo 10 para as regras gerais de conjuração"
                                          " e o capítulo 11 para a lista de magias de bruxo. TRUQUES Você conhece dois"
                                          " truques, à sua escolha, da lista de magias de bruxo. Você aprende truques "
                                          "de bruxo adicionais, à sua escolha, em níveis mais altos, como mostrado na"
                                          " coluna Truques Conhecidos da tabela O Bruxo. ESPAÇOS DE MAGIA A tabela O"
                                          " Bruxo mostra quantos espaços de magia você possui. A tabela também mostra"
                                          " qual o nível desses espaços; todos os seus espaços de magia são do mesmo"
                                          " nível. Para conjurar uma magia de bruxo de 1° nível ou superior, você deve"
                                          " gastar uma espaço de magia. Você recobra todos os espaços de magia gastos"
                                          " quando você completa um descanso curto ou longo. Por exemplo, quando você"
                                          " atingir o 5° nível, você terá dois espaços de magia de 3° nível. Para"
                                          " conjurar a magia de 1° nível onda trovejante, você deve gastar um desses"
                                          " espaços e você a conjura como uma magia de 3° nível. "
                                          "MAGIAS CONHECIDAS DE 1° NÍVEL E SUPERIORES No 1° nível, você conhece duas"
                                          " magias de 1° nível, à sua escolha da lista de magias de bruxo. A coluna"
                                          " Magias Conhecidas na tabela O Bruxo mostra quando você aprende mais magias"
                                          " de bruxo, à sua escolha, de 1° nível ou superior. Cada uma dessas magias"
                                          " deve ser de um nível a que você tenha acesso, como mostrado na tabela na"
                                          " coluna de Nível de Magia para o seu nível. Quando você alcança o 6° nível,"
                                          " por exemplo, você aprende uma nova magia de bruxo, que pode ser de 1°, 2°"
                                          " ou 3° nível. Além disso, quando você adquire um nível nessa classe, você"
                                          " pode escolher uma magia de bruxo que você conheça e substituí-la por outra"
                                          " magia da lista de magias de bruxo, que também deve ser de um nível ao qual"
                                          " você tenha espaços de magia. HABILIDADE DE CONJURAÇÃO Sua habilidade de"
                                          " conjuração é Carisma para suas magias de bruxo, portanto, você usa seu"
                                          " Carisma sempre que alguma magia se referir à sua habilidade de conjurar"
                                          " magias. Além disso, você usa o seu modificador de Carisma para definir a"
                                          " CD dos testes de resistência para as magias de bruxo que você conjura e"
                                          " quando você realiza uma jogada de ataque com uma magia. CD para suas"
                                          " magias = 8 + bônus de proficiência + seu modificador de Carisma Modificador"
                                          " de ataque de magia = seu bônus de proficiência + seu modificador de Carisma"
                                          " FOCO DE CONJURAÇÃO Você pode usar um foco arcano (encontrado no capítulo 5)"
                                          " como foco de conjuração das suas magias de bruxo.",
                       "PATRONO TRANSCENDENTAL": "No 1° nível, você conclui uma barganha com um ser transcendental, "
                                                 "à sua escolha: a Arquifada, o Corruptor ou o Grande Antigo, cada um"
                                                 " deles é detalhado no final da descrição da classe. Sua escolha lhe"
                                                 " confere traços no 1° nível e novamente no6°, 10° e 14° nível.",
                       "DEFINIÇÃO DE PATRONO": Bruxo.__set_patron__(self)
                       }

    def __set_patron__(self):
        patron = random.choice(["Arquifada", "Corruptor", "Grande Antigo"])
        description, skills = None, None
        if patron == "Arquifada":
            description = "Seu patrono é um senhor ou senhora das fadas, uma criatura lendária que detém segredos " \
                          "que foram esquecidos antes das raças mortais nascerem. As motivações desses seres são, " \
                          "muitas vezes, inescrutáveis e, as vezes, excêntricas e podem envolver esforços para " \
                          "adquirir grandes poderes mágicos ou resolução de desavenças antigas. Incluem-se dentre" \
                          " esses seres o Príncipe do Frio; a Rainha do Ar e Trevas, regente da Corte do Crepúsculo;" \
                          " Titania da Corte do Verão; seu cônjuge, Oberon, o Senhor Verdejante; Hyrsam, o Príncipe" \
                          " dos Tolos; e bruxas antigas."
            skills = "PRESENÇA FEÉRICA A partir do 1° nível, seu patrono concede a você a habilidade de projetar a" \
                     " sedução e temeridade da presença da fada. Com uma ação, você pode fazer com que cada criatura" \
                     " num cubo de 3 metros centrado em você, faça um teste de resistência de Sabedoria com uma CD" \
                     " igual a de sua magia de bruxo. As criaturas que falharem no teste ficaram enfeitiçadas ou" \
                     " amedrontadas por você (à sua escolha) até o início do seu próximo turno. Quando você usar" \
                     " essa característica, você não poderá utilizá-la novamente antes de realizar um descanso curto" \
                     " ou longo. NÉVOA DE FUGA A partir do 6° nível, você pode desaparecer em uma lufada de névoa em" \
                     " resposta a alguma ofensa. Quando você sofrer dano, você pode usar sua reação para ficar" \
                     " invisível e se teletransportar a até 18 metros para um espaço desocupado que você possa ver." \
                     " Você permanece invisível até o início do seu próximo turno ou até realizar um ataque ou " \
                     "conjurar uma magia. Após usar essa características, você não poderá utilizá-la novamente até" \
                     " terminar um descanso curto ou longo. DEFESA SEDUTORA A partir do 10° nível, seu patrono ensina" \
                     " você como voltar as magias de efeito mental dos seus inimigos contra eles. Você não pode ser" \
                     " enfeitiçado e, quando outra criatura tenta enfeitiçá-lo, você pode usar sua reação para tentar" \
                     " reverter o encanto de volta aquela criatura. A criatura deve ser bem sucedida num teste de" \
                     " resistência de Sabedoria contra a CD da sua magia de bruxo ou ficara enfeitiçado por 1 minuto" \
                     " ou até a criatura sofrer dano. DELÍRIO SOMBRIO Começando no 14° nível, você pode imergir uma" \
                     " criatura num reino ilusório. Com um ação, escolha uma criatura que você possa ver a até 18" \
                     " metros de você. Ela deve ser bem sucedida num teste de resistência de Sabedoria contra a CD da" \
                     " sua magia de bruxo. Se ela falhar, ela ficará enfeitiçada ou amedrontada por você" \
                     " (à sua escolha) por 1 minuto ou até você quebrar sua concentração (como se você estivesse se" \
                     " concentrando em uma magia). Esse efeito termina prematuramente se a criatura sofrer dano. " \
                     "Até que essa ilusão termine, a criatura acredita que está perdida num reino enevoado, a aparência" \
                     " desse reino fica a seu critério. A criatura só pode ver e ouvir a si mesma, a você e a sua" \
                     " ilusão. Você deve terminar um descanso curto ou longo antes de poder usar essa característica" \
                     " novamente."

            self.magic[1]["Fogo das Fadas (Evocação)"] = {
                "Tempo de Conjuração": "1 Ação",
                "Alcance": "18 metros",
                "Componentes": "V",
                "Duração": "Concentração, até 1 minuto.",
                "Descrição": "Cada objeto num cubo de 6 metros dentro do alcance fica delineado com luz azul, verde ou"
                             " violeta (à sua escolha). Qualquer criatura na área, quando a magia é conjurada, também"
                             " fica delineada com luz, se falhar num teste de resistência de Destreza. Pela duração, "
                             "os objetos e criaturas afetadas emitem penumbra num raio de 3 metros. Qualquer jogada de"
                             " ataque contra uma criatura afetada ou objeto tem vantagem, se o atacante puder ver o "
                             "alvo e, a criatura afetada ou objeto não recebe benefício por estar invisível."
            }
            self.magic[1]["Sono (Encantamento)"] = {
                "Tempo de Conjuração": "1 Ação",
                "Alcance": "36 metros",
                "Componentes": "V, S, M (um punhado de areia fina, pétalas de rosas ou um grilo)",
                "Duração": "1 minuto",
                "Descrição": "Essa magia põem as criaturas num entorpecimento mágico. Jogue 5d8; o total é a quantidade"
                             " de pontos de vida de criaturas afetados pela magia. As criaturas numa área de 6 metros "
                             "de raio, centrada no ponto escolhido, dentro do alcance, são afetadas em ordem ascendente"
                             " dos pontos de vida atuais delas (ignorando criaturas inconscientes). Começando com as "
                             "criaturas com menos pontos de vida atuais, cada criatura afetada por essa magia cai "
                             "inconsciente até a magia acabar, sofrer dano ou alguém usar sua ação para sacudi-la ou"
                             " esbofeteá-la até acordar. Subtraia os pontos de vida de cada criatura do total antes de "
                             "seguir para a próxima criatura com menos pontos de vida atuais. Os pontos de vida atuais "
                             "da criatura devem ser iguais ou menores que o valor restante para que a criatura possa "
                             "ser afetada. Mortos-vivos e criaturas imunes a serem enfeitiçadas não são afetadas por "
                             "essa magia. Em Níveis Superiores. Quando você conjurar essa magia usando um espaço de "
                             "magia de 2º nível ou superior, jogue 2d8 adicionais para cada nível do espaço acima do "
                             "1°."
            }

        elif patron == "Corruptor":
            description = "Você realizou um pacto com um corruptor dos planos de existência inferiores, um ser cujos " \
                          "objetivos são o mal, mesmo se você se opor a esses objetivos. Tais seres desejam corromper" \
                          " ou destruir todas as coisas, em última análise, até mesmo você. Corruptores poderosos o" \
                          " bastante para forjar pactos incluem lordes demônios como Demogorgon, Orcus, Fraz’Urb-luu " \
                          "e Bafomé; arquidiabos como Asmodeus, Dispater, Mefistófeles e Belial; senhores das " \
                          "profundezas e balors que sejam excepcionalmente poderosos; e ultraloths e outros senhores " \
                          "dos yugoloths."
            skills = "BÊNÇÃO DO OBSCURO A partir do 1° nível, quando você reduzir uma criatura hostil a 0 pontos de " \
                     "vida, você ganha uma quantidade de pontos de vida temporários igual ao seu modificador de " \
                     "Carisma + seu nível de bruxo (mínimo 1). SORTE DO PRÓPRIO OBSCURO A partir do 6° nível, você" \
                     " pode pedir ao seu patrono para alterar o destino em seu favor. Quando você realizar um teste" \
                     " de habilidade ou um teste de resistência, você pode usar essa característica para adicionar " \
                     "1d10 a sua jogada. Você pode fazer isso após ver sua jogada inicial, mas antes que qualquer " \
                     "efeito da jogada ocorra. Após usar essa características, você não poderá utilizá-la novamente" \
                     " até terminar um descanso curto ou longo. RESISTÊNCIA DEMONÍACA A partir do 10° nível, você " \
                     "pode escolher um tipo de dano quando você terminar um descanso curto ou longo. Você adquire " \
                     "resistência contra esse tipo de dano até você escolher um tipo de dano diferente com essa " \
                     "característica. Dano causado por armas mágicas ou armas de prata ignoram essa resistência. " \
                     "LANÇAR NO INFERNO A partir do 14° nível, quando você atingir uma criatura com um ataque, " \
                     "você pode usar essa característica para, instantaneamente, transportar o alvo para os planos" \
                     " inferiores. A criatura desaparece e é jogada para um lugar similar a um pesadelo. No final " \
                     "do seu turno, o alvo retorna ao lugar que ela ocupava anteriormente, ou para o espaço desocupado" \
                     " mais próximo. Se o alvo não for um corruptor, ele sofre 10d10 de dano psíquico à medida que toma" \
                     " conta da experiência traumática. Após usar essa características, você não poderá utilizá-la " \
                     "novamente até terminar um descanso curto ou longo."
            self.magic[1]["Mãos  Flamejantes (Evocação)"] = {
                "Tempo de Conjuração": "1 Ação",
                "Alcance": "Pessoal (cone de 4,5 metros)",
                "Componentes": "V, S",
                "Duração": "Instantânea",
                "Descrição": "Enquanto você mantiver suas mãos com os polegares juntos e os dedos abertos, uma fino "
                             "leque de chamas emerge das pontas dos seus dedos erguidos. Cada criatura num cone de "
                             "4,5 metros deve realizar um teste de 257 resistência de Destreza. Uma criatura sofre "
                             "3d6 de dano de fogo se falhar no teste, ou metade desse dano se obtiver sucesso. O fogo"
                             " incendeia qualquer objeto inflamável na área que não esteja sendo vestido ou carregado."
                             " Em Níveis Superiores. Se você conjurar essa magia usando um espaço de magia de 2° nível"
                             " ou superior, o dano aumenta em 1d6 para cada nível do espaço acima do 1°."
            }
            self.magic[1]["Comando (Encantamento)"] = {
                "Tempo de Conjuração": "1 Ação",
                "Alcance": "18 Metros",
                "Componentes": "V",
                "Duração": "1 Rodada",
                "Descrição": "Você pronuncia uma palavra de comando para uma criatura que você possa ver dentro do "
                             "alcance. O alvo deve ser bem sucedido num teste de resistência de Sabedoria ou seguirá"
                             " seu comando no próximo turno dele. A magia não tem efeito se o alvo for um morto-vivo,"
                             " se ele não entender seu idioma ou se o comando for diretamente nocivo a ele. Alguns"
                             " comandos típicos e seus efeitos a seguir. Você pode proferir um comando diferente dos"
                             " descritos aqui. Se o fizer, o Mestre descreve como o alvo reage. Se o alvo não puder "
                             "cumprir o comando, a magia termina. Aproxime-se. O alvo se move para próximo de você o"
                             " máximo que puder na rota mais direta, terminando seu turno, se ele se mover a até 1,5"
                             " metro de você. Largue. O alvo larga o que quer que ele esteja segurando, e termina seu"
                             " turno. Fuja. O alvo gasta seu turno se movendo para longe de você da forma mais rápida"
                             " que puder. Deite-se. O alvo deita-se no chão e então, termina seu turno. Parado. O alvo"
                             " não se move e não realiza nenhuma ação. Uma criatura voadora continua no alto,"
                             " considerando que ela seja capaz de fazê-lo. Se ela tiver que se mover para continuar no "
                             "alto, ela voa a mínima distância necessária para permanecer no ar. Em Níveis Superiores."
                             " Se você conjurar essa magia usando um espaço de magia de 2° nível ou superior, você pode"
                             " afetar uma criatura adicional para cada nível do espaço acima do 1°. As criaturas devem"
                             " estar a 9 metros entre si para serem afetadas."
            }
        elif patron == "Grande Antigo":
            description = "Seu patrono é uma entidade misteriosa cuja natureza é profundamente alheia ao tecido da " \
                          "realidade. Ela deve ter vindo do Reino Distante, o espaço além da realidade, ou ela pode ser" \
                          " um dos deuses anciãos conhecido apenas nas lendas. Seus motivos são incompreensíveis para" \
                          " os mortais e seu conhecimento é tão imenso e antigo que, até mesmo, as mais grandiosas" \
                          " bibliotecas desbotam em comparação com os vastos segredos que ele detém. O Grande Antigo" \
                          " pode desconhecer a sua existência ou ser totalmente indiferente a você, mas os segredos " \
                          "que você desvendou permitem que você obtenha suas magias dele. Entidades desse tipo incluem" \
                          " Ghaunadar, conhecido como Aquele que Espreita; Tharizdun, o Deus Acorrentado; Dendar, a" \
                          " Serpente da Noite; Zargon, o Retornado; Grande Cthulhu; entre outros seres insondáveis."
            skills = "DESPERTAR A MENTE A partir do 1° nível, seu conhecimento alienígena concede a você a habilidade" \
                     " de tocar a mente de outras criaturas. Você pode se comunicar telepaticamente com qualquer" \
                     " criatura que você possa ver a até 18 metros de você. Você não precisa partilhar um idioma com" \
                     " a criatura para compreender suas expressões telepáticas, mas a criatura deve ser capaz de" \
                     " compreender pelo menos um idioma. PROTEÇÃO ENTRÓPICA A partir do 6° nível, você aprende a se" \
                     " proteger magicamente contra ataques e a transformar os ataques mal sucedidos de seus inimigos" \
                     " em boa sorte pra você. Quando uma criatura realizar uma jogada de ataque contra você, você pode" \
                     " usar sua reação para impor desvantagem nesse jogada. Se o ataque errar você, sua próxima jogada" \
                     " de ataque contra essa criatura recebe vantagem se você o fizer antes do final do seu próximo" \
                     " turno. Após usar essa características, você não poderá utilizá-la novamente até terminar um" \
                     " descanso curto ou longo. ESCUDO DE PENSAMENTOS A partir do 10° nível, seus pensamentos não" \
                     " podem ser lidos através de telepatia ou outros meios, a não ser que você permita. Você também" \
                     " adquire resistência a dano psíquico e, toda vez que uma criatura causar dano psíquico a você," \
                     " essa criatura sofre a mesma quantidade de dano que você sofreu. CRIAR LACAIO No 14° nível, você" \
                     " adquire a habilidade de infectar a mente de um humanoide com a magia alienígena do seu patrono." \
                     " Você pode usar sua ação para tocar um humanoide incapacitado. Essa criatura então, ficará" \
                     " enfeitiçada por você até que a magia remover maldição seja conjurada sobre ela, a condição" \
                     " enfeitiçado seja removida dela ou você use essa característica novamente. Você pode se comunicar" \
                     " telepaticamente com a criatura enfeitiçada contanto que ambos estejam no mesmo plano de" \
                     " existência."
            self.magic[1]["Sussurros Dissonantes (Encantamento)"] = {
                            "Tempo de Conjuração": "1 Ação",
                            "Alcance": "18 metros",
                            "Componentes": "V",
                            "Duração": "Instantânea",
                            "Descrição": "Você sussurra uma melodia dissonante que apenas uma criatura, à sua escolha,"
                                         " dentro do alcance pode ouvir, causando-lhe uma terrível dor. O alvo deve"
                                         " realizar um teste de resistência de Sabedoria. Se falhar na resistência,"
                                         " ele sofrerá 3d6 de dano psíquico e deve, imediatamente, usar sua reação,"
                                         " se disponível, para se mover para o mais longe possível de você. A"
                                         " criatura não 284 se moverá para um terreno obviamente perigoso, como"
                                         " uma fogueira ou abismo. Se obtiver sucesso na resistência, o alvo sofre"
                                         " metade do dano e não precisa se afastar de você. Uma criatura surda obtém"
                                         " sucesso automaticamente na sua resistência. Em Níveis Superiores. Quando"
                                         " você conjurar essa magia usando um espaço de magia de 2° nível ou superior,"
                                         " o dano aumenta em 1d6 para cada nível do espaço acima do 1°"}
            self.magic[1]["Riso histérico de Tasha (Encantamento)"] = {
                "Tempo de Conjuração": "1 Ação",
                "Alcance": "9 Metros",
                "Componentes": "V, S, M (pequenas tortas e uma pena que é balançada no ar)",
                "Duração": "Concentração, até 1 minuto.",
                "Descrição": "Uma criatura, à sua escolha, que você possa ver, dentro do alcance, acha tudo"
                             " hilariantemente engraçado e cai na gargalhada, se essa magia afeta-la. O alvo deve ser"
                             " bem sucedido em um teste de resistência de Sabedoria ou cairá no chão, ficando"
                             " incapacitado e incapaz de se levantar pela duração. Uma criatura com valor de "
                             "Inteligência 4 ou inferior não é afetada. Ao final de cada um dos turnos dela e, toda "
                             "vez que sofrer dano, o alvo pode realizar outro teste de resistência de Sabedoria. O "
                             "alvo terá vantagem no teste de resistência se ele for garantido por ele ter sofrido "
                             "dano. Se obtiver sucesso, a magia acaba."}
        return patron, description, skills

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
            item2 = None

            if a == "Besta Leve":
                item = prototipo.get_arma_distancia_simples(a)
                item2 = prototipo.get_equipamento("Virotes (20)", 1)
            else:
                opcao = random.randint(1, 2)
                opcoes = {
                    1: prototipo.get_random_arma_corpo_a_corpo_simples(),
                    2: prototipo.get_random_arma_distancia_simples(),
                }
                item = opcoes[opcao]

            personagem.equip["Armas"].append(item)
            if item2 is not None:
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

            opcao = random.randint(1, 2)
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
            print(f"ERRO BRUXO: {e}")

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

    def __get_name__(self):
        return self.name

    def __get_proficiency_bonus__(self):
        return self.proficiency_bonus

    def __get_life__(self):
        return self.life

    def __get_dices_life__(self):
        return self.dices_life

    def __get_knowledge__(self):
        return self.knowledge

    def __get_expertise__(self):
        return self.expertise

    def __get_equip__(self):
        return self.equip

    def __get_endurance_tests__(self):
        return self.endurance_tests

    def __get_skills__(self):
        return self.skills

    def __set_name__(self, vlr):
        self.name = vlr

    def __set_proficiency_bonus__(self, vlr):
        self.name = vlr

    def __set_life__(self, vlr):
        self.life = vlr

    def __set_dices_life__(self, vlr):
        self.dices_life = vlr

    def __set_knowledge__(self, vlr):
        self.knowledge.append(vlr)

    def __set_expertise__(self, vlr):
        self.expertise.append(vlr)

    def __set_endurance_tests__(self, vlr):
        self.endurance_tests.append(vlr)

    def __set_skills__(self, chave, vlr):
        self.skills[chave] = vlr

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
