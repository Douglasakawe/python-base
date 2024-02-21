#!/usr/bin/env python3
"""Hello World Multi Languages.

Dependendo da lingua configurada no ambiente o programa exibe
a mensagem correspondente.

Como usar:

<<<<<<< HEAD
Tenha a variável LANG devidamente configurada ex:

    export LANG=pt_BR
    
Execução : 
=======
Tenha a variavel LANG devidamente configurada ex:

    export LANG=pt_BR

Ou informe atraves do CLI argument '--lang'

Ou o usuario tera que digitar.

Execute com :
>>>>>>> a7c6875 (Arquivos de Estudo)

    python3 hello.py
    ou
    ./hello.py
"""

# Dunder --> __*__

<<<<<<< HEAD
__version__ = "0.0.1"
__author__ = "Douglas Akawê"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour Monde!"

print(msg)

=======
__version__ = "0.1.3"
__author__ = "Douglas Akawe"
__license__ = "Unlicense"

import os
import sys

arguments = {"lang": None,"count": 1}

for arg in sys.argv[1:]:
	# TODO: Tratar ValueError
	key, value = arg.split("=")
	key = key.lstrip("-").strip()
	value = value.strip()
	if key not in arguments:
	    print(f"Invalid Option {key}")
	    sys.exit()
	arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    # TODO: Usar repeticao
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Choose a language:")

current_language = current_language[:5]

msg = {
	"en_US": "Hello, World!",
	"pt_BR": "Ola, Mundo!",
	"it_IT": "Ciao, Mondo!",
	"es_ES": "Hola, Mundo!",
	"fr_FR": "Bonjour, Monde",
}

print(msg[current_language] * int(arguments["count"]))
>>>>>>> a7c6875 (Arquivos de Estudo)
