const BASE_URL = "https://gest-o-de-projetos-v1.onrender.com";

export async function criarProjeto(data) {
  const res = await fetch(`${BASE_URL}/projetos`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  if (!res.ok) throw new Error("Erro ao criar projeto");
  return res.json();
}

export async function criarOrdemServico(data) {
  const res = await fetch(`${BASE_URL}/ordens-servico`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  if (!res.ok) throw new Error("Erro ao criar OS");
  return res.json();
}

export async function listarProjetos() {
  const res = await fetch(`${BASE_URL}/projetos`);
  if (!res.ok) throw new Error("Erro ao listar projetos");
  return res.json();
}
