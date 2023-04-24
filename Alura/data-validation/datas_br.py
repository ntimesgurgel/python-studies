from datetime import datetime

class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.format_data()

    def mes_cadastro(self):
        meses_do_ano = ["jan", "fev", "mar",
                        "abr", "mai", "jun",
                        "jul", "ago", "set",
                        "out", "nov", "dez"]
        mes_castro = self.momento_cadastro.month
        return meses_do_ano[mes_castro-1]

    def dia_semana(self):
        dias = ['segunda','terça','quarta',
                'quinta','sexta',
                'sabado','domingo']
        dia_semana = self.momento_cadastro.weekday()
        return dias[dia_semana]

    def format_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada

    def tempo_cadastro(self):
        tempo_cadastro = datetime.today() - self.momento_cadastro
        return tempo_cadastro

