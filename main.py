import React, { useState, useEffect } from "react";
import axios from "axios";
import "bootstrap/dist/css/bootstrap.min.css";

export default function Relatorios() {
  const [ordens, setOrdens] = useState([]);
  const [filtro, setFiltro] = useState("");

  useEffect(() => {
    const fetchOrdens = async () => {
      try {
        const response = await axios.get("http://localhost:8000/ordens-servico");
        setOrdens(response.data);
      } catch (error) {
        console.error("Erro ao buscar ordens:", error);
      }
    };
    fetchOrdens();
  }, []);

  const baixarPDF = async (id) => {
    try {
      const response = await axios.get(`http://localhost:8000/relatorio-os/${id}/pdf`, {
        responseType: "blob",
      });
      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement("a");
      link.href = url;
      link.setAttribute("download", `relatorio-os-${id}.pdf`);
      document.body.appendChild(link);
      link.click();
      link.remove();
    } catch (error) {
      console.error("Erro ao gerar PDF:", error);
      alert("Erro ao baixar relatório.");
    }
  };

  const ordensFiltradas = ordens.filter((ordem) =>
    ordem.projeto_nome.toLowerCase().includes(filtro.toLowerCase())
  );

  return (
    <div className="container mt-5">
      <div className="card shadow p-4">
        <h2 className="text-success mb-4">Relatórios por Ordem de Serviço</h2>

        <div className="mb-3">
          <label className="form-label">Filtrar por projeto</label>
          <input
            type="text"
            className="form-control"
            placeholder="Digite o nome do projeto"
            value={filtro}
            onChange={(e) => setFiltro(e.target.value)}
          />
        </div>

        <div className="table-responsive">
          <table className="table table-striped">
            <thead>
              <tr>
                <th>Ordem de Serviço</th>
                <th>Projeto</th>
                <th>Data</th>
                <th>Relatório</th>
              </tr>
            </thead>
            <tbody>
              {ordensFiltradas.map((ordem) => (
                <tr key={ordem.id}>
                  <td>#{ordem.id}</td>
                  <td>{ordem.projeto_nome}</td>
                  <td>{ordem.data_criacao || "-"}</td>
                  <td>
                    <button
                      className="btn btn-sm btn-warning"
                      onClick={() => baixarPDF(ordem.id)}
                    >
                      Baixar PDF
                    </button>
                  </td>
                </tr>
              ))}
              {ordensFiltradas.length === 0 && (
                <tr>
                  <td colSpan="4" className="text-center text-muted">
                    Nenhuma OS encontrada.
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
