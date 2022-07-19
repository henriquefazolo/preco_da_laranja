"""
O preço da laranja está R$ 3,50 por quilo.
É considerado que cada uma pesa 160g.
Faça um programa que tenha como entrada a quantidade de laranjas e mostre o valor em reais.
"""


class PrecoLaranja:

    def __init__(self, qtd_laranjas):
        """

        :param qtd_laranjas:  quantidade de laranjas
        """
        self.qtd_laranjas = qtd_laranjas
        self.preco_kg = 3.5
        self.peso_unidade_laranja_kg = 0.160

    def valor_kg(self):
        """

        :return: f'Valor : R$ {valor:.2f}'
        """
        valor = float(self.qtd_laranjas * self.peso_unidade_laranja_kg * self.preco_kg)
        resposta = f'Valor : R$ {valor:.2f}'
        return resposta


preco = PrecoLaranja(1)
print(preco.valor_kg())



