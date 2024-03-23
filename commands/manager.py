from discord.utils import format_dt
import datetime
from f5 import *


class Manager:
    def __init__(self):
        self.authors = ["guspavao", "bolacha_de_sal"]
        self.github = "https://github.com/gustapavao/btico"

    def checkAutor(self, mss):
        if str(mss.author) in self.authors:
            return True
        else:
            return False
    def tomorrowFormatedDate(self):
        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(days=1)
        formated_date = tomorrow.strftime("%d/%m/%Y")
        return formated_date

    def todayFormatedDate(self):
        today = datetime.date.today()
        formated_date = today.strftime("%d/%m/%Y")
        return formated_date

    def github(self):
        return self.github

    def noClassTomorrow(self, mess):
            message = mess.content.split(";")
            disc = str(message[1]).title()
            professor = str(message[2]).title()
            return f"Amanhã, dia {self.tomorrowFormatedDate()}, não haverá aula de {disc} do professor {professor}."

    def noClassToday(self, mess):
            message = mess.content.split(";")
            disc = str(message[1]).title()
            professor = str(message[2]).title()
            return f"Hoje, dia {format_dt(datetime.datetime, style="d")}, não haverá aula de {disc} do professor {professor}."
    def shareMessage(self, mess):
            message = mess.content.split(";")
            return message[1]

    def newTask(self, mss):
        pass

    def monitoria(self, mss):
        message = mss.content.split(";")
        if str(message[1]).lower().strip() == "me":
            return "https://matematica-elementar.github.io/horarios-monitorias"
        elif str(message[1]).lower().strip() == "ge":
            return "Segunda e Quarta: M56\nSexta: T56\nSala: A220 "
        else:
            return "Ainda não há monitorias registradas dessa disciplina, entretanto, você pode verificar a disponibilidade com o PETCC: \nhttps://petcc.dimap.ufrn.br/tutorias"

    def help(self):
        return "Comandos disponíveis:\n!github -> git do bot\n!monitoria ; ge\n!provas -> provas agendadas\n"

    def anderson(self):
        return "Gostoso"

    def testToday(self):
        for i in atividade.values():
            if i['data'] - datetime.datetime.now() < one_day and i['tipo'] == 'atividade':
                return (
                    f"💀💀 Restam {humanize.naturaldelta(i['data'] - datetime.datetime.now())} para a entrega da {i['nome']}".replace(
                        "hours", "horas"))
            else:
                return (f"📅📅 Faltam {humanize.naturaldelta(i['data'] - datetime.datetime.today())} para {i['nome']}".replace(
                    "days", "dias"))

    def atualizacao(self):
            return self.testToday()

    def nextTests(self):
            retmsss = ""
            for i in atividade.values():
                if i['tipo'] == 'prova':
                    retmsss += f"📅📅 Faltam {humanize.naturaldelta(i['data'] - datetime.datetime.today() + datetime.timedelta(days=1))} para {i['nome']}\n".replace(
                        "days", "dias")
            return retmsss

if __name__ == "__main__":
    pass