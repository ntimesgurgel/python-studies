endereco = "Rua Fco Heronildes da Silva, 428, Nova Betania, 59607-477, Mossoro-RN"

import re

padrao = re.compile("[0-9]{5}[-]?[0-9]{3}")

busca = padrao.search(endereco)

if busca:
    cep = busca.group()
    print(cep)