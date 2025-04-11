import React from "react";
import { Outlet } from "react-router-dom";
import Sidebar from "./Sidebar";

const Layout = () => {
  return (
    <div className="d-flex">
      <Sidebar />
      <main className="flex-fill p-4 bg-light min-vh-100">
        <Outlet />
      </main>
    </div>
  );
};

export default Layout;
