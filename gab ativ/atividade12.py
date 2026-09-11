def contra_vogais(texto):
    vogais="aeiou"
    return sum(1 for caractere in texto.lower() if caractere in vogais)
print(contra_vogais("python"))
print(contra_vogais("unip"))