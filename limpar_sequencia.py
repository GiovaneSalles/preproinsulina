import re

# 1. Abrir e ler o arquivo

with open("preproinsulin-seq.txt") as arquivo:
    texto = arquivo.read()

# 2. Remover a palavra ORIGIN

texto = texto.replace("ORIGIN", "")

# 3. Remover tudo que NÃO é letra

sequencia = re.sub(r"[^a-zA-Z]", "", texto)

# 4. Verificar o resultado

print(sequencia)
print(len(sequencia))