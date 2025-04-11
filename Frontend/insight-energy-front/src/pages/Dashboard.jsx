import React from "react";
import { Link } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";

// Certifique-se de que a rota /relatorios está definida no App.jsx
// Verifique também se o componente Sidebar está importado no Layout.jsx, se estiver utilizando um

export default function Dashboard() {
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
              <p className="card-text">Cadastre e gerencie seus projetos.</p>
              <Link to="/projeto" className="btn btn-warning w-100 fw-bold btn-animado">Acessar</Link>
            </div>
          </div>
        </div>

        <div className="col-md-4">
          <div className="card border-0 shadow-sm animated-card">
            <div className="card-body">
              <h5 className="card-title">🛠 Ordens de Serviço</h5>
              <p className="card-text">Controle completo das OS vinculadas.</p>
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
