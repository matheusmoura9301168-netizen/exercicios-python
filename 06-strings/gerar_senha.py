# Gera uma senha aleatória de 10 caracteres.

import random,string;print(''.join(random.choices(string.ascii_letters+string.digits,k=10)))
