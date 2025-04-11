from fastapi import FastAPI, Depends, HTTPException, UploadFile, File, Form, Query
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from typing import List, Optional
from pydantic import BaseModel
from datetime import date
from sqlalchemy import func
import shutil
import os
from fpdf import FPDF

import models
from database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

UPLOAD_DIR = "uploads"
REPORT_DIR = "relatorios"
LOGO_PATH = "logo_insight.jpeg"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)

# Sessão de banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Estilo customizado para PDF
class StyledPDF(FPDF):
    def header(self):
        if os.path.exists(LOGO_PATH):
            self.image(LOGO_PATH, x=10, y=8, w=50)
        self.set_y(20)
        self.set_fill_color(30, 144, 255)  # Azul escuro
        self.set_text_color(255, 255, 255)
        self.set_font("Arial", "B", 16)
        self.cell(0, 15, "RELATÓRIO DE ORDEM DE SERVIÇO", ln=True, align="C", fill=True)
        self.ln(5)

    def section_title(self, title):
        self.set_fill_color(240, 240, 240)
        self.set_text_color(0)
        self.set_font("Arial", 'B', 12)
        self.cell(0, 10, title, ln=True, fill=True)
        self.set_font("Arial", size=11)
        self.set_text_color(0)

# MODELOS BASE Pydantic
class ProjetoCreate(BaseModel):
    nome: str
    descricao: Optional[str] = None

class ProjetoOut(BaseModel):
    id: int
    nome: str
    descricao: Optional[str]
    class Config:
        from_attributes = True

class OrdemServicoCreate(BaseModel):
    nome: str
    descricao: Optional[str] = None
    projeto_id: int

class OrdemServicoOut(BaseModel):
    id: int
    nome: str
    descricao: Optional[str]
    projeto_id: int
    class Config:
        from_attributes = True

class CompraCreate(BaseModel):
    item: str
    valor: float
    data_compra: date
    ordem_id: int

class CompraOut(BaseModel):
    id: int
    item: str
    valor: float
    data_compra: date
    ordem_id: int
    class Config:
        from_attributes = True

class PessoaCreate(BaseModel):
    nome: str

class PessoaOut(BaseModel):
    id: int
    nome: str
    class Config:
        from_attributes = True

class AlocacaoCreate(BaseModel):
    pessoa_id: int
    ordem_id: int
    data_inicio: date
    data_fim: date

class AlocacaoOut(BaseModel):
    id: int
    pessoa_id: int
    ordem_id: int
    data_inicio: date
    data_fim: date
    class Config:
        from_attributes = True

class LocacaoCreate(BaseModel):
    descricao: str
    valor_total: float
    data_inicio: date
    data_fim: date
    ordem_id: int

class LocacaoOut(BaseModel):
    id: int
    descricao: str
    valor_total: float
    data_inicio: date
    data_fim: date
    ordem_id: int
    class Config:
        from_attributes = True

class CronogramaCreate(BaseModel):
    ordem_id: int
    data: date
    descricao_rdo: Optional[str] = None
    ocorrencias: Optional[str] = None

class CronogramaOut(BaseModel):
    id: int
    ordem_id: int
    data: date
    descricao_rdo: Optional[str]
    ocorrencias: Optional[str]
    class Config:
        from_attributes = True

class ArquivoOut(BaseModel):
    id: int
    ordem_id: int
    tipo: str
    nome_arquivo: str
    caminho: str
    data: date
    class Config:
        from_attributes = True

# ============================
# Endpoints REST
# ============================

@app.post("/projetos", response_model=ProjetoOut)
def criar_projeto(projeto: ProjetoCreate, db: Session = Depends(get_db)):
    novo = models.Projeto(**projeto.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@app.post("/ordens-servico", response_model=OrdemServicoOut)
def criar_ordem(ordem: OrdemServicoCreate, db: Session = Depends(get_db)):
    nova = models.OrdemServico(**ordem.dict())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova

@app.post("/compras", response_model=CompraOut)
def criar_compra(compra: CompraCreate, db: Session = Depends(get_db)):
    nova = models.Compra(**compra.dict())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova

@app.post("/pessoas", response_model=PessoaOut)
def criar_pessoa(pessoa: PessoaCreate, db: Session = Depends(get_db)):
    nova = models.Pessoa(**pessoa.dict())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova

@app.post("/alocacoes", response_model=AlocacaoOut)
def criar_alocacao(a: AlocacaoCreate, db: Session = Depends(get_db)):
    nova = models.Alocacao(**a.dict())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova

@app.post("/locacoes", response_model=LocacaoOut)
def criar_locacao(l: LocacaoCreate, db: Session = Depends(get_db)):
    nova = models.Locacao(**l.dict())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova

@app.post("/cronograma", response_model=CronogramaOut)
def criar_cronograma(c: CronogramaCreate, db: Session = Depends(get_db)):
    novo = models.CronogramaDia(**c.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@app.post("/upload/foto", response_model=ArquivoOut)
def upload_foto(ordem_id: int = Form(...), data: date = Form(...), file: UploadFile = File(...), db: Session = Depends(get_db)):
    filename = f"foto_ordem{ordem_id}_{data}_{file.filename}"
    filepath = os.path.join(UPLOAD_DIR, filename)
    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    novo = models.Arquivo(ordem_id=ordem_id, tipo="foto", nome_arquivo=file.filename, caminho=filepath, data=data)
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@app.post("/upload/dds", response_model=ArquivoOut)
def upload_dds(ordem_id: int = Form(...), data: date = Form(...), file: UploadFile = File(...), db: Session = Depends(get_db)):
    filename = f"dds_ordem{ordem_id}_{data}_{file.filename}"
    filepath = os.path.join(UPLOAD_DIR, filename)
    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    novo = models.Arquivo(ordem_id=ordem_id, tipo="dds", nome_arquivo=file.filename, caminho=filepath, data=data)
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@app.get("/arquivos", response_model=List[ArquivoOut])
def listar_arquivos(ordem_id: Optional[int] = Query(None), tipo: Optional[str] = Query(None), data: Optional[date] = Query(None), db: Session = Depends(get_db)):
    query = db.query(models.Arquivo)
    if ordem_id:
        query = query.filter(models.Arquivo.ordem_id == ordem_id)
    if tipo:
        query = query.filter(models.Arquivo.tipo == tipo)
    if data:
        query = query.filter(models.Arquivo.data == data)
    return query.all()

@app.get("/relatorio-os/{ordem_id}/pdf")
def gerar_relatorio_os_pdf(ordem_id: int, db: Session = Depends(get_db)):
    ordem = db.query(models.OrdemServico).filter(models.OrdemServico.id == ordem_id).first()
    if not ordem:
        raise HTTPException(status_code=404, detail="Ordem de serviço não encontrada")

    compras = db.query(models.Compra).filter(models.Compra.ordem_id == ordem_id).all()
    locacoes = db.query(models.Locacao).filter(models.Locacao.ordem_id == ordem_id).all()
    cronogramas = db.query(models.CronogramaDia).filter(models.CronogramaDia.ordem_id == ordem_id).all()
    arquivos = db.query(models.Arquivo).filter(models.Arquivo.ordem_id == ordem_id).all()

    total_compras = sum(c.valor for c in compras)
    total_locacoes = sum(l.valor_total for l in locacoes)

    pdf = StyledPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=11)

    pdf.set_text_color(0)
    pdf.multi_cell(0, 10, f"📄 Ordem de Serviço: {ordem.nome}")
    pdf.multi_cell(0, 10, f"📝 Descrição: {ordem.descricao or '-'}")
    pdf.multi_cell(0, 10, f"📦 Total Compras: R$ {total_compras:.2f}")
    pdf.multi_cell(0, 10, f"🚜 Total Locações: R$ {total_locacoes:.2f}")
    pdf.multi_cell(0, 10, f"💰 Total Geral: R$ {total_compras + total_locacoes:.2f}")

    pdf.ln(5)
    pdf.section_title("🔧 COMPRAS")
    for c in compras:
        pdf.cell(0, 10, f"📅 {c.data_compra} | {c.item} - R$ {c.valor:.2f}", ln=True)

    pdf.ln(3)
    pdf.section_title("🚜 LOCAÇÕES")
    for l in locacoes:
        pdf.cell(0, 10, f"📅 {l.data_inicio} a {l.data_fim} | {l.descricao} - R$ {l.valor_total:.2f}", ln=True)

    pdf.ln(3)
    pdf.section_title("📅 CRONOGRAMA")
    for c in cronogramas:
        pdf.multi_cell(0, 10, f"📆 {c.data} - RDO: {c.descricao_rdo or '-'} | Ocorrências: {c.ocorrencias or '-'}")

    pdf.ln(3)
    pdf.section_title("📎 ARQUIVOS ANEXADOS")
    for a in arquivos:
        pdf.cell(0, 10, f"🗂️ {a.data} - {a.tipo.upper()} - {a.nome_arquivo}", ln=True)

    output_path = os.path.join(REPORT_DIR, f"relatorio_ordem_{ordem_id}.pdf")
    pdf.output(output_path)

    return FileResponse(output_path, media_type="application/pdf", filename=os.path.basename(output_path))
