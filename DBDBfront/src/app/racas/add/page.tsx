"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { racaService } from "../../../services/api";
import { FormField } from "../../../components/FormField";

export default function AddRacaPage() {
  const router = useRouter();
  const [formData, setFormData] = useState({
    nome: "",
    cor: "",
    desc: "",
    poderBase: "",
    imagem: ""
  });
  const [loading, setLoading] = useState(false);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    setFormData(prev => ({
      ...prev,
      [e.target.name]: e.target.value
    }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    try {
      await racaService.create({
        ...formData,
        poderBase: parseInt(formData.poderBase)
      });
      router.push("/racas");
    } catch (error) {
      console.error("Erro ao criar raça:", error);
      alert("Erro ao criar raça. Verifique os dados e tente novamente.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={styles.container}>
      <h1>Adicionar Nova Raça</h1>
      <form onSubmit={handleSubmit} style={styles.form}>
        <FormField
          label="Nome"
          name="nome"
          type="text"
          value={formData.nome}
          onChange={handleChange}
          required
        />
        <FormField
          label="Cor"
          name="cor"
          type="text"
          value={formData.cor}
          onChange={handleChange}
          required
        />
        <FormField
          label="Descrição"
          name="desc"
          type="textarea"
          value={formData.desc}
          onChange={handleChange}
          required
        />
        <FormField
          label="Poder Base"
          name="poderBase"
          type="number"
          value={formData.poderBase}
          onChange={handleChange}
          required
        />
        <FormField
          label="URL da Imagem"
          name="imagem"
          type="text"
          value={formData.imagem}
          onChange={handleChange}
        />
        <button type="submit" style={styles.button} disabled={loading}>
          {loading ? "Salvando..." : "Salvar Raça"}
        </button>
      </form>
    </div>
  );
}

const styles = {
  container: {
    maxWidth: "600px",
    margin: "0 auto",
    padding: "2rem",
  },
  form: {
    display: "flex",
    flexDirection: "column" as const,
    gap: "1rem",
  },
  button: {
    padding: "0.5rem 1rem",
    backgroundColor: "#0070f3",
    color: "white",
    border: "none",
    borderRadius: "4px",
    fontSize: "1rem",
    cursor: "pointer",
    ":hover": {
      backgroundColor: "#0051a2",
    },
  },
};