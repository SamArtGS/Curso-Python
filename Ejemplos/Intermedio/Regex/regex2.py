expresion = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)" 

# No se preocupen, la busqué en internet

correo = "correo_prote.co_4@gmail.com"

print(re.match(expresion, correo))

if re.match(expresion, correo):
    print("Es válida ✅")
else:
    print("NO es válida ❌")