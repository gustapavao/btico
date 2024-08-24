class Mentoria:
    def __init__(self):
        self.me = ("Você pode verificar os horários em:\n"
                   "https://matematica-elementar.github.io/horarios-monitorias")
        self.ge = "Segunda e Quarta: M56\nSexta: T56\nSala: A220"
        self.demais = "Verifique a disponibilidade com o PETCC em: \nhttps://petcc.dimap.ufrn.br/tutorias"

    def retmentoria(self, mensagem: str):
            if mensagem == "ge":
                return self.ge
            elif mensagem == "me":
                return self.me
            else:
                return self.demais

