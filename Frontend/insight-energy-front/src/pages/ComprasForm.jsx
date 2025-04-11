import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";

export default function ComprasForm() {
  const [descricao, setDescricao] = useState("");
  const [valorTotal, setValorTotal] = useState("");
  const [dataInicio, setDataInicio] = useState("");
  const [dataFim, setDataFim] = useState("");
  const [ordemId, setOrdemId] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      await axios.post("http://localhost:8000/locacoes", {
        descricao,
        valor_total: parseFloat(valorTotal),
        data_inicio: dataInicio,
        data_fim: dataFim,
        ordem_id: parseInt(ordemId),
      });
      alert("Compra/Locação registrada com sucesso!");
      navigate("/");
    } catch (error) {
      console.error(error);
      alert("Erro ao registrar a compra ou locação.");
    }
  };

  return (
    <div className="container mt-5">
      <div className="card shadow p-4">
        <h2 className="text-success mb-4">Nova Compra ou Locação</h2>
        <form onSubmit={handleSubmit}>
          <div className="mb-3">
            <label className="form-label">Descrição</label>
            <input
              type="text"
              className="form-control"
              value={descricao}
              onChange={(e) => setDescricao(e.target.value)}
              required
              placeholder="Ex: Aluguel de máquina, compra de materiais..."
            />
          </div>

          <div className="mb-3">
            <label className="form-label">Valor Total (R$)</label>
            <input
              type="number"
              className="form-control"
              value={valorTotal}
              onChange={(e) => setValorTotal(e.target.value)}
              step="0.01"
              required
            />
          </div>

          <div className="mb-3">
            <label className="form-label">Data de Início</label>
            <input
              type="date"
              className="form-control"
              value={dataInicio}
              onChange={(e) => setDataInicio(e.target.value)}
              required
            />
          </div>

          <div className="mb-3">
            <label className="form-label">Data de Fim</label>
            <input
              type="date"
              className="form-control"
              value={dataFim}
              onChange={(e) => setDataFim(e.target.value)}
              required
            />
          </div>

          <div className="mb-3">
            <label className="form-label">ID da Ordem de Serviço</label>
            <input
              type="number"
              className="form-control"
              value={ordemId}
              onChange={(e) => setOrdemId(e.target.value)}
              required
            />
          </div>

          <button type="submit" className="btn btn-success fw-bold">
            Registrar
          </button>
        </form>
      </div>
    </div>
  );
}
