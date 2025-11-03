"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

export default function AddObraPage() {
  const router = useRouter();
  const [form, setForm] = useState({
    nome: "",
    data_ini: "",
    data_fin: "",
    imagem: "",
  });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    await fetch("http://127.0.0.1:5000/api/obras", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(form),
    });
    router.push("/obras");
  };

  return (
    <section>
      <h1>Adicionar Nova Obra</h1>
      <form onSubmit={handleSubmit} style={styles.form}>
        <input name="nome" placeholder="Nome" value={form.nome} onChange={handleChange} required />
        <input name="data_ini" placeholder="Data de início" value={form.data_ini} onChange={handleChange} required />
        <input name="data_fin" placeholder="Data de fim" value={form.data_fin} onChange={handleChange} />
        <input name="imagem" placeholder="URL da imagem" value={form.imagem} onChange={handleChange} />
        <button type="submit">Salvar</button>
      </form>
    </section>
  );
}

const styles = {
  form: {
    display: "flex",
    flexDirection: "column" as const,
    gap: "0.5rem",
    maxWidth: "400px",
  },
};
