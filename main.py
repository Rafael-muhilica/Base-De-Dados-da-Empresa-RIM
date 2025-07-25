from sqlalchemy import create_engine, Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base
db = create_engine("sqlite:///Bancodedadostrabalhadores.db")
Session = sessionmaker(bind = db)
session = Session()
Base  = declarative_base()
class Dados_Pessoais(Base):
    __tablename__ = "dados_pessoais"
    id = Column( Integer, primary_key=True, autoincrement= True)
    Nome = Column(String)
    NIF = Column(String)
    Idade = Column(Integer)
    Numero_Agente = Column(Integer)
    Resindencia = Column(String)
    Naturalidade = Column(String)
    Parentesco = Column(String)
    def __init__(self, Nome, NIF, Idade, Numero_Agente, Resindencia, Naturalidade, Parentesco):
        self.Nome = Nome
        self.NIF = NIF
        self.Idade = Idade
        self.Numero_Agente = Numero_Agente
        self.Resindencia = Resindencia
        self.Naturalidade = Naturalidade
        self.Parentesco = Parentesco
class Dado_Profissio(Base):
       __tablename__ = "dados_profissios"
       id = Column( Integer, primary_key=True, autoincrement = True)
       Anos_Trabalho = Column(Integer)
       Funcao = Column(String) 
       Salario = Column(Float)
       Grauacademico = Column(String)
       def __init__(self, Anos_Trabalho,  Funcao,  Salario , Grauacademico): 
           self.Anos_Trabalho = Anos_Trabalho
           self.Funcao = Funcao
           self.Salario = Salario 
           self.Grauacademico = Grauacademico
Base.metadata.create_all(bind = db)    
Dados_Pessoais1 = Dados_Pessoais(Nome="Rafael Matuca Muhilica", Idade=21, NIF = "020149978LN057", Numero_Agente= 20230979,  Resindencia="Morro Bento", Naturalidade ="Lunda Norte", Parentesco="Solteiro")
Dado_Profissio1 = Dado_Profissio(Anos_Trabalho = 2, Funcao = "Densevolvedor Python", Salario = 265000, Grauacademico="Lincenciado")
Dados_Pessoais2 = Dados_Pessoais(Nome= "Diano C Budimbo Já", NIF ="014730034LN573", Idade=21,  Numero_Agente= 20242025, Resindencia="Morro Bento", Naturalidade ="Lunda Norte", Parentesco="Solteiro")
Dado_Profissio2 = Dado_Profissio(Anos_Trabalho = 1, Funcao = "Densevolvedor Python", Salario = 235000, Grauacademico="Lincenciado")
Dados_Pessoais3 = Dados_Pessoais(Nome="Aires Capalo Muhilica Romeu",NIF ="14798955LN783", Idade=19,  Numero_Agente= 20240102,  Resindencia="Centalidade do Mussungue", Naturalidade ="Lunda Norte", Parentesco="Solteiro")
Dado_Profissio3 = Dado_Profissio(Anos_Trabalho = 1, Funcao = "Assistente de Clientes", Salario = 165000, Grauacademico="Médio")
Dados_Pessoais4 = Dados_Pessoais(Nome=" Rubén Muapessa Rogerio ",NIF ="887989525LN584", Idade=19,  Numero_Agente= 20240304,  Resindencia="Centalidade do Mussungue", Naturalidade ="Lunda Norte", Parentesco="Solteiro")
Dado_Profissio4 = Dado_Profissio(Anos_Trabalho = 1, Funcao = "Assistente de Caixa", Salario = 185000, Grauacademico="Médio")
Dados_Pessoais5 = Dados_Pessoais(Nome="Alberto Francisco Silvestre ", NIF ="26007812LS098", Idade=21,  Numero_Agente= 20230979,  Resindencia="Camama 1", Naturalidade ="Lunda Sul", Parentesco="Casado")
Dado_Profissio5 = Dado_Profissio(Anos_Trabalho = 2, Funcao = "Gestor De Recursos Humanos", Salario = 305000.12, Grauacademico="Lincenciado")
Dados_Pessoais6 = Dados_Pessoais(Nome="Modesto Ilunga Muteba ", NIF ="099779889525LN678", Idade=21,  Numero_Agente= 20250979,  Resindencia="Centalidade do Mussungue", Naturalidade ="Lunda Norte", Parentesco="Solteiro")
Dado_Profissio6 = Dado_Profissio(Anos_Trabalho = 1, Funcao = "Contabilidade e Auditória", Salario = 195000, Grauacademico="Lincenciado")
session.add(Dados_Pessoais1)
session.add(Dado_Profissio1)
session.add(Dados_Pessoais2)
session.add(Dado_Profissio2)
session.add(Dados_Pessoais3)
session.add(Dado_Profissio3)
session.add(Dados_Pessoais4)
session.add(Dado_Profissio4)
session.add(Dados_Pessoais5)
session.add(Dado_Profissio5)
session.add(Dados_Pessoais6)
session.add(Dado_Profissio6)
session.commit()