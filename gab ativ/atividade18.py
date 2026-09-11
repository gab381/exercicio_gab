def palindromo(palavra):
    texto_limpo=palavra.lower().replace("","")
    return texto_limpo == texto_limpo [::-1]
print (palindromo("arara"))
print (palindromo("python"))