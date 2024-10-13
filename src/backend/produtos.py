class ListaProdutos:

    def __init__(self):
        self.menu = {
            1: {"nome": "X - SALADA", "preço": 25},
            2: {"nome": "X - EGG", "preço": 26},
            3: {"nome": "X - BACON", "preço": 30},
            4: {"nome": "X - TUDO", "preço": 32},
            5: {"nome": "CURUMIM", "preço": 35},
            6: {"nome": "GUERREIRO", "preço": 45},
            7: {"nome": "CACIQUE", "preço": 52},
            8: {"nome": "X - ÍNDIO", "preço": 42},
            9: {"nome": "FILÉ DE FRANGO", "preço": 30},
            10: {"nome": "BEIRUTE FILÉ MIGNON", "preço": 45},
            11: {"nome": "BEIRUTE CALABRESA", "preço": 30},
            12: {"nome": "BEIRUTE LIGHT", "preço": 38},
            13: {"nome": "BEIRUTE AMERICANO", "preço": 38},
            14: {"nome": "MORTADELÃO", "preço": 28},
            15: {"nome": "X - FRANGO", "preço": 20},
            16: {"nome": "AMERICANO", "preço": 22},
            17: {"nome": "X - CHURRASCO", "preço": 25},
            18: {"nome": "SUPER MISTO", "preço": 28},
            19: {"nome": "MIX MORTADELA", "preço": 28},
            20: {"nome": "NATURAL", "preço": 18},
            21: {"nome": "PÃO COM OVO", "preço": 10},
            22: {"nome": "OVO MEXIDO", "preço": 12},
            23: {"nome": "SALAME", "preço": 45},
            24: {"nome": "FRITAS SIMPLES", "preço": 22},
            25: {"nome": "FRITAS COM CB", "preço": 28},
            26: {"nome": "FILÉ DE FRANGO (PORÇÃO)", "preço": 40},
            27: {"nome": "FILÉ DE FRANGO EMPANADO", "preço": 40},
            28: {"nome": "PORÇÃO MISTA", "preço": 45},
            29: {"nome": "À PASSARINHO", "preço": 70},
            30: {"nome": "CONTRA FILÉ", "preço": 80}
        }

    def get_produtos_formatados(self):
        return [f"{codigo} - {detalhes['nome']} (R$ {detalhes['preço']:.2f})" for codigo, detalhes in self.menu.items()]

