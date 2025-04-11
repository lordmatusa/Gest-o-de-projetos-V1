import React from "react";
import { Link } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";

const Sidebar = () => {
  return (
    <div className="d-flex flex-column p-3 text-white bg-dark shadow" style={{ width: '250px', height: '100vh' }}>
      <Link to="/" className="d-flex align-items-center mb-3 text-white text-decoration-none">
        <img src="/logo192.png" alt="Logo Insight" width={40} className="me-2" />
        <span className="fs-4">Insight</span>
      </Link>
      <hr />
      <ul className="nav nav-pills flex-column mb-auto">
        <li className="nav-item">
          <Link to="/" className="nav-link text-white">Dashboard</Link>
        </li>
        <li>
          <Link to="/projeto" className="nav-link text-white">Projetos</Link>
        </li>
        <li>
          <Link to="/ordem" className="nav-link text-white">Ordens de Serviço</Link>
        </li>
        <li>
          <Link to="/compras" className="nav-link text-white">Compras</Link>
        </li>
        <li>
          <Link to="/relatorios" className="nav-link text-white">Relatórios</Link>
        </li>
      </ul>
    </div>
  );
};

export default Sidebar;
