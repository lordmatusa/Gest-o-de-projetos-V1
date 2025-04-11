import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";

export default function ProjetoForm() {
  const [nome, setNome] = useState("");
  const [descricao, setDescricao] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post("http://localhost:8000/projetos", {
        nome,
        descricao,
      });
      alert("Projeto cadastrado com sucesso!");
      navigate("/");
    } catch (error) {
      alert("Erro ao cadastrar projeto.");
      console.error(error);
    }
  };

  return (
    <div className="container mt-5">
      <div className="card shadow p-4">
        <h2 className="text-success mb-4">Novo Projeto</h2>
        <form onSubmit={handleSubmit}>
          <div className="mb-3">
            <label className="form-label">Nome do Projeto</label>
            <input
              type="text"
              className="form-control"
              value={nome}
              onChange={(e) => setNome(e.target.value)}
              placeholder="Digite o nome do projeto"
              required
            />
          </div>

          <div className="mb-3">
            <label className="form-label">Descrição</label>
            <textarea
              className="form-control"
              value={descricao}
              onChange={(e) => setDescricao(e.target.value)}
              placeholder="Descreva o projeto"
              required
            />
          </div>

          <button type="submit" className="btn btn-success fw-bold">
            Criar Projeto
          </button>
        </form>
      </div>
    </div>
  );
}
