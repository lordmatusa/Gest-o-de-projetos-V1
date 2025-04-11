from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from database import Base

class Projeto(Base):
    __tablename__ = "projetos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, index=True)
    descricao = Column(String)

    ordens_servico = relationship("OrdemServico", back_populates="projeto")


class OrdemServico(Base):
    __tablename__ = "ordens_servico"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    descricao = Column(String)
    projeto_id = Column(Integer, ForeignKey("projetos.id"))

    projeto = relationship("Projeto", back_populates="ordens_servico")
    compras = relationship("Compra", back_populates="ordem_servico")


class Compra(Base):
    __tablename__ = "compras"

    id = Column(Integer, primary_key=True, index=True)
    item = Column(String)
    valor = Column(Float)
    data_compra = Column(Date)
    ordem_id = Column(Integer, ForeignKey("ordens_servico.id"))

    ordem_servico = relationship("OrdemServico", back_populates="compras")


from sqlalchemy import Date

class Pessoa(Base):
    __tablename__ = "pessoas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)

    alocacoes = relationship("Alocacao", back_populates="pessoa")


class Alocacao(Base):
    __tablename__ = "alocacoes"

    id = Column(Integer, primary_key=True, index=True)
    pessoa_id = Column(Integer, ForeignKey("pessoas.id"))
    ordem_id = Column(Integer, ForeignKey("ordens_servico.id"))
    data_inicio = Column(Date)
    data_fim = Column(Date)

    pessoa = relationship("Pessoa", back_populates="alocacoes")
    ordem = relationship("OrdemServico", backref="alocacoes")


class Locacao(Base):
    __tablename__ = "locacoes"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String)
    valor_total = Column(Float)
    data_inicio = Column(Date)
    data_fim = Column(Date)
    ordem_id = Column(Integer, ForeignKey("ordens_servico.id"))

    ordem = relationship("OrdemServico", backref="locacoes")


from sqlalchemy import Date

class CronogramaDia(Base):
    __tablename__ = "cronograma"

    id = Column(Integer, primary_key=True, index=True)
    ordem_id = Column(Integer, ForeignKey("ordens_servico.id"))
    data = Column(Date)
    descricao_rdo = Column(String, nullable=True)
    ocorrencias = Column(String, nullable=True)

    ordem = relationship("OrdemServico", backref="cronograma_dias")



class Arquivo(Base):
    __tablename__ = "arquivos"

    id = Column(Integer, primary_key=True, index=True)
    ordem_id = Column(Integer, ForeignKey("ordens_servico.id"))
    tipo = Column(String)  # 'foto' ou 'dds'
    nome_arquivo = Column(String)
    caminho = Column(String)
    data = Column(Date)

    ordem = relationship("OrdemServico", backref="arquivos")


