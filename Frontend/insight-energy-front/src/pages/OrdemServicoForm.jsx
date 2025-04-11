import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";

export default function OrdemServicoForm() {
  const [titulo, setTitulo] = useState("");
  const [descricao, setDescricao] = useState("");
  const [projetoId, setProjetoId] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post("http://localhost:8000/ordens", {
        titulo,
        descricao,
        projeto_id: parseInt(projetoId),
      });
      alert("Ordem de Serviço criada com sucesso!");
      navigate("/");
    } catch (error) {
      console.error(error);
      alert("Erro ao criar Ordem de Serviço.");
    }
  };

  return (
    <div className="container mt-5">
      <div className="card shadow p-4">
        <h2 className="text-success mb-4">Nova Ordem de Serviço</h2>
        <form onSubmit={handleSubmit}>
          <div className="mb-3">
            <label className="form-label">Título</label>
            <input
              type="text"
              className="form-control"
              value={titulo}
              onChange={(e) => setTitulo(e.target.value)}
              placeholder="Digite o título da OS"
              required
            />
          </div>

          <div className="mb-3">
            <label className="form-label">Descrição</label>
            <textarea
              className="form-control"
              value={descricao}
              onChange={(e) => setDescricao(e.target.value)}
              placeholder="Descreva a OS"
              required
            />
          </div>

          <div className="mb-3">
            <label className="form-label">ID do Projeto</label>
            <input
              type="number"
              className="form-control"
              value={projetoId}
              onChange={(e) => setProjetoId(e.target.value)}
              placeholder="Digite o ID do projeto vinculado"
              required
            />
          </div>

          <button type="submit" className="btn btn-success fw-bold">
            Criar OS
          </button>
        </form>
      </div>
    </div>
  );
}
