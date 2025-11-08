"use client";

import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import { personagemBaseService, racaService } from "../../../services/api";
import { FormField } from "../../../components/FormField";
import type { Raca } from "../../../types/models";

export default function AddPersonagemPage() {
  const router = useRouter();
  const [formData, setFormData] = useState({
    nome: "",
    dataNasc: "",
    dataMorte: "",
    sexo: "",
    raca_id: "",
    imagem: ""
  });
  const [racas, setRacas] = useState<Raca[]>([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const fetchRacas = async () => {
      try {
        const data = await racaService.getAll();
        console.log('Raças carregadas:', data);
        setRacas(data);
      } catch (error) {
        console.error('Erro ao carregar raças:', error);
        alert('Erro ao carregar lista de raças. Por favor, recarregue a página.');
      }
    };
    fetchRacas();
  }, []);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>) => {
    setFormData(prev => ({
      ...prev,
      [e.target.name]: e.target.value
    }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    try {
      const personagemData = {
        ...formData,
        raca_id: parseInt(formData.raca_id),
        dataNasc: formData.dataNasc || '', // já está no formato YYYY-MM-DD
        dataMorte: formData.dataMorte || undefined, // se vazio, envia undefined
        sexo: formData.sexo === "Masculino" ? "M" : formData.sexo === "Feminino" ? "F" : "O"
      };
      console.log('Enviando dados:', personagemData);
      
      const response = await personagemBaseService.create(personagemData);
      console.log('Resposta:', response);
      
      router.push("/personagens");
    } catch (error: any) {
      console.error("Erro ao criar personagem:", error);
      console.error("Detalhes da resposta:", error.response?.data);
      alert(`Erro ao criar personagem: ${error.response?.data?.details || error.message || 'Erro desconhecido'}`);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={styles.container}>
      <h1>Adicionar Novo Personagem</h1>
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
          label="Data de Nascimento"
          name="dataNasc"
          type="date"
          value={formData.dataNasc}
          onChange={handleChange}
          required
        />
        <FormField
          label="Data de Morte (opcional)"
          name="dataMorte"
          type="date"
          value={formData.dataMorte}
          onChange={handleChange}
        />
        <div style={styles.field}>
          <label htmlFor="sexo" style={styles.label}>Sexo</label>
          <select
            id="sexo"
            name="sexo"
            value={formData.sexo}
            onChange={handleChange}
            required
            style={styles.select}
          >
            <option value="">Selecione</option>
            <option value="M">Masculino</option>
            <option value="F">Feminino</option>
            <option value="O">Outro</option>
          </select>
        </div>
        <div style={styles.field}>
          <label htmlFor="raca_id" style={styles.label}>Raça</label>
          <select
            id="raca_id"
            name="raca_id"
            value={formData.raca_id}
            onChange={handleChange}
            required
            style={styles.select}
          >
            <option value="">Selecione uma raça</option>
            {racas.map(raca => (
              <option key={raca.id} value={raca.id}>{raca.nome}</option>
            ))}
          </select>
        </div>
        <FormField
          label="URL da Imagem"
          name="imagem"
          type="text"
          value={formData.imagem}
          onChange={handleChange}
        />
        <button type="submit" style={styles.button} disabled={loading}>
          {loading ? "Salvando..." : "Salvar Personagem"}
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
};