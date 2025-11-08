"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { obraService } from "../../../services/api";
import { FormField } from "../../../components/FormField";

export default function AddObraPage() {
  const router = useRouter();
  const [formData, setFormData] = useState({
    nome: "",
    dtIni: new Date().toISOString().split('T')[0], // Formato YYYY-MM-DD
    dtFim: new Date().toISOString().split('T')[0], // Formato YYYY-MM-DD
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
      // Valida as datas
      if (!formData.dtIni || !formData.dtFim) {
        throw new Error('As datas de início e fim são obrigatórias');
      }

      // Garante que os campos não estão vazios e formata as datas
      const payload = {
        nome: formData.nome.trim(),
        dtIni: formData.dtIni, // Já está no formato YYYY-MM-DD
        dtFim: formData.dtFim, // Já está no formato YYYY-MM-DD
        imagem: formData.imagem.trim()
      };

      console.log('Enviando payload:', payload);
      await obraService.create(payload);
      router.push("/obras");
    } catch (error: any) {
      console.error("Erro ao criar obra:", error);
      alert(`Erro ao criar obra: ${error.response?.data?.details || error.message || 'Erro desconhecido'}`);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={styles.container}>
      <h1>Adicionar Nova Obra</h1>
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
          label="Data de Início"
          name="dtIni"
          type="date"
          value={formData.dtIni}
          onChange={handleChange}
          required
        />
        <FormField
          label="Data de Fim"
          name="dtFim"
          type="date"
          value={formData.dtFim}
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
          {loading ? "Salvando..." : "Salvar Obra"}
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
