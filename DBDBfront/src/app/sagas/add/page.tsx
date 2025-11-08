"use client";

import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import { sagaService, obraService } from "../../../services/api";
import { FormField } from "../../../components/FormField";
import type { Obra } from "../../../types/models";

export default function AddSagaPage() {
  const router = useRouter();
  const [formData, setFormData] = useState({
    desc: "",
    epIni: "",
    epFim: "",
    obra_id: "",
    imagem: ""
  });
  const [obras, setObras] = useState<Obra[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string>("");
  const [success, setSuccess] = useState(false);

  useEffect(() => {
    const loadObras = async () => {
      try {
        const data = await obraService.getAll();
        setObras(data);
      } catch (error) {
        console.error("Erro ao carregar obras:", error);
        setError("Erro ao carregar lista de obras. Tente novamente.");
      }
    };
    loadObras();
  }, []);

  const validateForm = () => {
    if (!formData.desc.trim()) {
      throw new Error("A descrição é obrigatória");
    }

    const epIni = parseInt(formData.epIni);
    const epFim = parseInt(formData.epFim);
    const obra_id = parseInt(formData.obra_id);

    if (isNaN(epIni) || epIni < 1) {
      throw new Error("Episódio inicial deve ser um número maior que zero");
    }
    if (isNaN(epFim) || epFim < epIni) {
      throw new Error("Episódio final deve ser maior ou igual ao inicial");
    }
    if (isNaN(obra_id) || obra_id < 1) {
      throw new Error("Selecione uma obra válida");
    }

    return {
      desc: formData.desc.trim(),
      epIni,
      epFim,
      obra_id,
      ...(formData.imagem.trim() ? { imagem: formData.imagem.trim() } : {})
    };
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>) => {
    setError(""); // Limpa erros quando o usuário começa a digitar
    setFormData(prev => ({
      ...prev,
      [e.target.name]: e.target.value
    }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError("");
    setSuccess(false);
    setLoading(true);

    try {
      const validatedData = validateForm();
      console.log('[Form] Enviando dados da saga:', validatedData);
      
      const result = await sagaService.create(validatedData);
      console.log('[Form] Saga criada com sucesso:', result);
      
      setSuccess(true);
      setTimeout(() => {
        router.push("/sagas");
      }, 1000);

    } catch (error: any) {
      console.error("[Form] Erro ao criar saga:", error);
      const errorMessage = error.response?.data?.details || error.message || 'Erro desconhecido';
      setError(`Erro ao criar saga: ${errorMessage}`);
      setSuccess(false);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={styles.container}>
      <h1>Adicionar Nova Saga</h1>
      {error && <div style={styles.error}>{error}</div>}
      {success && <div style={styles.success}>Saga criada com sucesso!</div>}
      
      <form onSubmit={handleSubmit} style={styles.form}>
        <FormField
          label="Descrição"
          name="desc"
          type="textarea"
          value={formData.desc}
          onChange={handleChange}
          required
        />
        <FormField
          label="Episódio Inicial"
          name="epIni"
          type="number"
          value={formData.epIni}
          onChange={handleChange}
          min="1"
          required
        />
        <FormField
          label="Episódio Final"
          name="epFim"
          type="number"
          value={formData.epFim}
          onChange={handleChange}
          min={formData.epIni || "1"}
          required
        />
        <div style={styles.field}>
          <label htmlFor="obra_id" style={styles.label}>Obra</label>
          <select
            id="obra_id"
            name="obra_id"
            value={formData.obra_id}
            onChange={handleChange}
            required
            style={styles.select}
          >
            <option value="">Selecione uma obra</option>
            {obras.map(obra => (
              <option key={obra.id} value={obra.id}>{obra.nome}</option>
            ))}
          </select>
        </div>
        <FormField
          label="URL da Imagem (opcional)"
          name="imagem"
          type="text"
          value={formData.imagem}
          onChange={handleChange}
          placeholder="https://exemplo.com/imagem.jpg"
        />
        <button 
          type="submit" 
          style={{
            ...styles.button,
            ...(loading ? styles.buttonLoading : {}),
            ...(success ? styles.buttonSuccess : {})
          }} 
          disabled={loading || success}
        >
          {loading ? "Salvando..." : success ? "Saga Criada!" : "Salvar Saga"}
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
    transition: "all 0.2s ease",
    ":hover": {
      backgroundColor: "#0051a2",
    },
  },
  buttonLoading: {
    backgroundColor: "#666",
    cursor: "not-allowed",
  },
  buttonSuccess: {
    backgroundColor: "#00aa00",
  },
  field: {
    marginBottom: "1rem",
  },
  label: {
    display: "block",
    marginBottom: "0.5rem",
    fontWeight: "bold" as const,
  },
  select: {
    width: "100%",
    padding: "0.5rem",
    border: "1px solid #ddd",
    borderRadius: "4px",
    fontSize: "1rem",
  },
  error: {
    padding: "0.5rem 1rem",
    marginBottom: "1rem",
    backgroundColor: "#ffebee",
    color: "#d32f2f",
    borderRadius: "4px",
    border: "1px solid #ffcdd2",
  },
  success: {
    padding: "0.5rem 1rem",
    marginBottom: "1rem",
    backgroundColor: "#e8f5e9",
    color: "#2e7d32",
    borderRadius: "4px",
    border: "1px solid #c8e6c9",
  },
};