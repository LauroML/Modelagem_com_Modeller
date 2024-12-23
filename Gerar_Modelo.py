# Importando o MODELLER
from modeller import *
from modeller.automodel import *

# Novo ambiente para o MODELLER
env = environ()

# Ativando log detalhado
log.level(output=2)

# Criando o objeto de modelagem
a = automodel(
    env,
    alnfile='RAttusP2X7.ali',  # Arquivo de alinhamento
    knowns='6u9w',             # Molde
    sequence='RAttusP2X7',     # Sequência alvo
    assess_methods=(assess.DOPE, assess.GA341)  # Métodos de avaliação
)

# Configuração do número de modelos
a.starting_model = 1  # Primeiro modelo
a.ending_model = 5    # Último modelo

# Construindo os modelos
a.make()


