class Professor:
    def __init__(self, codprofessor, nomeprofessor, coddisciplina, nota):
        self.codprofessor = int(codprofessor)
        self.nomeprofessor = str(nomeprofessor)
        self.coddisciplina = int(coddisciplina)
        self.nota = float(nota)
    def definirprofessor(self, codprofessor):
        self.codprofessor = codprofessor
    def notas(self, nota):
        self.nota = nota
    def mostraprofessor(self):
        print(f'Codprofessor: {self.codprofessor}, Nomeprofessor:{self.nomeprofessor}, Cod Disciplina:{self.coddisciplina},Nota: {self.nota}')
professor = Professor(1, 'João', 3, 2.6)
professor.mostraprofessor()
professor.definirprofessor(2)
professor.notas(3.4)
professor.mostraprofessor() 