#!/usr/bin/env python3
"""Cadastro de produto"""
__version__ = "0.1.0"

from pprint import pprint

produto = {
    "nome": "Tinta",
    "cores": ["Cinza", "Azul"],
    "preco": 15.38,
    "dimensao": {
        "altura": 33.1,
        "largura": 5.6,
    },
    "em_estoque": True,
    "codigo": 54331,
    "codebar": None,
}

cliente = {"nome": "Douglas"}
compra = {"cliente": cliente, "produto": produto, "quantidade": 3}

print(
	f"O cliente {compra[0]} comprou {[1]}"
	f"e pagou o total de {total_de_compra[1]}"
)
