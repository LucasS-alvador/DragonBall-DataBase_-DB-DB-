"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { transformacaoService } from "../../../services/api";
import { FormField } from "../../../components/FormField";

export default function AddTransformacaoPage() {
  const router = useRouter();
  const [formData, setFormData] = useState({
    nome: "",
    cor: "",
    especial: "",
    efeitoCol: "",
    poderMult: "",
    limMinutos: "",
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
      // Normaliza os dados: remove campos vazios e converte tipos
      const payload: any = {
        ...formData,
        poderMult: formData.poderMult ? parseInt(formData.poderMult) : 0,
      };
      if (formData.limMinutos) {
        payload.limMinutos = parseInt(formData.limMinutos);
      } else {
        delete payload.limMinutos;
      }
      // Remove campos vazios
      Object.keys(payload).forEach(key => {
        if (payload[key] === "") {
          delete payload[key];
        }
      });
      await transformacaoService.create(payload);
      router.push("/transformacoes");
    } catch (error: any) {
      console.error("Erro ao criar transformação:", error);
      alert(`Erro ao criar transformação: ${error.response?.data?.details || error.message || 'Erro desconhecido'}`);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={styles.container}>
      <h1>Adicionar Nova Transformação</h1>
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
          label="Efeito Especial"
          name="especial"
          type="textarea"
          value={formData.especial}
          onChange={handleChange}
          required
        />
        <FormField
          label="Efeito Colateral"
          name="efeitoCol"
          type="textarea"
          value={formData.efeitoCol}
          onChange={handleChange}
          required
        />
        <FormField
          label="Multiplicador de Poder"
          name="poderMult"
          type="number"
          value={formData.poderMult}
          onChange={handleChange}
          required
        />
        <FormField
          label="Limite de Tempo (minutos)"
          name="limMinutos"
          type="number"
          value={formData.limMinutos}
          onChange={handleChange}
        />
        <FormField
          label="URL da Imagem"
          name="imagem"
          type="text"
          value={formData.imagem}
          onChange={handleChange}
        />
        <button type="submit" style={styles.button} disabled={loading}>
          {loading ? "Salvando..." : "Salvar Transformação"}
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