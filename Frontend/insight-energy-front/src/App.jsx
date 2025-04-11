import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Layout from "./components/Layout";
import ProjetoForm from "./pages/ProjetoForm";
import OrdemServicoForm from "./pages/OrdemServicoForm";
import ComprasForm from "./pages/ComprasForm";
import Dashboard from "./pages/Dashboard";
import Compras from "./pages/Compras";
import Usuarios from "./pages/Usuarios";
import Relatorios from "./pages/Relatorios";

export default function App() {
  return (
    <Router>
      <Routes>
        <Route element={<Layout />}>
          <Route path="/" element={<Dashboard />} />
          <Route path="/projeto" element={<ProjetoForm />} />
          <Route path="/ordem" element={<OrdemServicoForm />} />
          <Route path="/compras" element={<Compras />} />
          <Route path="/usuarios" element={<Usuarios />} />
          <Route path="/relatorios" element={<Relatorios />} />
        </Route>
      </Routes>
    </Router>
  );
}
