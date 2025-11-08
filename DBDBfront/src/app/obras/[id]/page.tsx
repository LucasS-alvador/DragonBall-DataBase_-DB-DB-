"use client";

import { useEffect, useState } from "react";
import { obraService } from "../../../services/api";
import { useParams } from "next/navigation";
import type { Obra } from "../../../types/models"; // ajuste o caminho se necessário

export default function ObraDetalhe() {
  // useParams from next/navigation is not a generic; extract id safely
  const params = useParams();
  const id = Array.isArray((params as any)?.id) ? (params as any).id[0] : (params as any)?.id;
  const [obra, setObra] = useState<Obra | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!id) return;

    const fetchObra = async () => {
      try {
        const data = await obraService.getById(Number(id));
        setObra(data);
        setLoading(false);
      } catch (err) {
        console.error(err);
        setLoading(false);
      }
    };
    fetchObra();
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
