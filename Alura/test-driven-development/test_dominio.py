from unittest import TestCase
from dominio import Usuario, Lance, Leilao, Avaliador


class TestAvaliador(TestCase):
    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adiocionados_em_ordem_crescente(self):
        gui = Usuario("Gui")
        yuri = Usuario("Yuri")

        lance_do_yuri = Lance(yuri, 100.0)
        lance_do_gui = Lance(gui, 150.0)

        leilao = Leilao("Celular")

        leilao.lances.append(lance_do_yuri)
        leilao.lances.append(lance_do_gui)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adiocionados_em_ordem_decrescente(self):
        gui = Usuario("Gui")
        yuri = Usuario("Yuri")

        lance_do_gui = Lance(gui, 150.0)
        lance_do_yuri = Lance(yuri, 100.0)

        leilao = Leilao("Celular")

        leilao.lances.append(lance_do_gui)
        leilao.lances.append(lance_do_yuri)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_o_menor_lance_quando_o_leilao_tiver_um_lance(self):
        gui = Usuario("Gui")

        lance_do_gui = Lance(gui, 150.0)

        leilao = Leilao("Celular")

        leilao.lances.append(lance_do_gui)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 150.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances(self):
        gui = Usuario("Gui")
        yuri = Usuario("Yuri")
        jesus = Usuario("Jesus")

        lance_do_gui = Lance(gui, 150.0)
        lance_do_yuri = Lance(yuri, 100.0)
        lance_de_jesus = Lance(jesus, 200.0)

        leilao = Leilao("Celular")

        leilao.lances.append(lance_do_gui)
        leilao.lances.append(lance_do_yuri)
        leilao.lances.append(lance_de_jesus)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)