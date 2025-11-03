"use client";

import { useEffect, useState } from "react";
import { useParams } from "next/navigation";
import type { Obra } from "../../../types/models"; // ajuste o caminho se necessário

// Tipo para o parâmetro dinâmico da rota
type ObraParams = {
  id: string;
};

export default function ObraDetalhe() {
  const { id } = useParams<ObraParams>();
  const [obra, setObra] = useState<Obra | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!id) return;

    fetch(`http://127.0.0.1:5000/api/obras/${id}`)
      .then((res) => res.json())
      .then((data) => {
        setObra(data);
        setLoading(false);
      })
      .catch((err) => console.error(err));
  }, [id]);

  if (loading) return <p>Carregando...</p>;
  if (!obra) return <p>Obra não encontrada.</p>;

  return (
    <section style={styles.container}>
      <h1>{obra.nome}</h1>
      {obra.imagem && (
        <img src={obra.imagem} alt={obra.nome} style={styles.image} />
      )}
      <div style={styles.details}>
        <p><b>Data de início:</b> {obra.dtIni}</p>
        <p><b>Data de fim:</b> {obra.dtFim}</p>
      </div>

      <a href={`/obras/${id}/edit`} style={styles.editBtn}>
        Editar Obra
      </a>
    </section>
  );
}

const styles = {
  container: {
    maxWidth: "600px",
    margin: "2rem auto",
    padding: "1rem",
    textAlign: "center" as const,
    border: "1px solid #ddd",
    borderRadius: "8px",
    background: "#fff",
  },
  image: {
    maxWidth: "100%",
    height: "auto",
    borderRadius: "8px",
    marginBottom: "1rem",
  },
  details: {
    textAlign: "left" as const,
    lineHeight: "1.6",
  },
  editBtn: {
    display: "inline-block",
    marginTop: "1rem",
    backgroundColor: "#f39c12",
    color: "#fff",
    padding: "0.5rem 1rem",
    borderRadius: "4px",
    textDecoration: "none",
  },
};
