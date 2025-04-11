import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";
import api from "../services/api";

export default function Dashboard() {
  const [totalProjetos, setTotalProjetos] = useState(0);
  const [totalOrdens, setTotalOrdens] = useState(0);

  useEffect(() => {
    async function fetchDados() {
      try {
        const projetosRes = await api.get("/projetos");
        const ordensRes = await api.get("/ordens-servico");
        setTotalProjetos(projetosRes.data.length);
        setTotalOrdens(ordensRes.data.length);
      } catch (error) {
        console.error("Erro ao buscar dados do dashboard:", error);
      }
    }
    fetchDados();
  }, []);

  return (
    <div className="container-fluid px-4">
      <h1 className="text-success">Painel Inicial</h1>
      <p className="text-muted">
        Bem-vindo ao sistema de gerenciamento de projetos da <strong>Insight Energy</strong>.
      </p>

      <div className="row g-4 mt-4">
        <div className="col-md-4">
          <div className="card border-0 shadow-sm animated-card">
            <div className="card-body">
              <h5 className="card-title">📁 Projetos</h5>
              <p className="card-text">
                Cadastre e gerencie seus projetos.<br />
                <strong>Total: {totalProjetos}</strong>
              </p>
              <Link to="/projeto" className="btn btn-warning w-100 fw-bold btn-animado">Acessar</Link>
            </div>
          </div>
        </div>

        <div className="col-md-4">
          <div className="card border-0 shadow-sm animated-card">
            <div className="card-body">
              <h5 className="card-title">🛠 Ordens de Serviço</h5>
              <p className="card-text">
                Controle completo das OS vinculadas.<br />
                <strong>Total: {totalOrdens}</strong>
              </p>
              <Link to="/ordem" className="btn btn-warning w-100 fw-bold btn-animado">Acessar</Link>
            </div>
          </div>
        </div>

        <div className="col-md-4">
          <div className="card border-0 shadow-sm animated-card">
            <div className="card-body">
              <h5 className="card-title">📦 Compras & Locações</h5>
              <p className="card-text">Gerencie entradas, aluguéis e gastos.</p>
              <Link to="/relatorios" className="btn btn-warning w-100 fw-bold btn-animado">Relatórios</Link>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
