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
      <div style={styles.container}>
      <h1>{obra.nome}</h1>
      {obra.imagem && (
        <img src={obra.imagem} alt={obra.nome} style={styles.image} />
      )}
      <div style={styles.details}>
        <p><b>Data de início:</b> {obra.dtIni}</p>
        <p><b>Data de fim:</b> {obra.dtFim}</p>
      </div>
      </div>
    </section>
  );
}

const styles = {
  container: {
    padding: "2rem",
    maxWidth: "1200px",
    margin: "0 auto",
    backgroundColor: "ghostwhite",
  },
  backButton: {
    display: "inline-block",
    marginBottom: "2rem",
    color: "#0070f3",
    textDecoration: "none",
    fontSize: "1.1rem",
  },
  content: {
    display: "grid",
    gridTemplateColumns: "1fr 2fr",
    gap: "2rem",
    backgroundColor: "#ff4141ff",
    borderRadius: "8px",
    padding: "2rem",
    boxShadow: "0 2px 8px rgba(0, 0, 0, 0.1)",
    border: '3px solid #000000ff',
  },
  imageContainer: {
    width: "100%",
    aspectRatio: "1",
    borderRadius: "8px",
    overflow: "hidden",
    border: '3px solid #000000ff',
  },
  image: {
    width: "100%",
    height: "100%",
    objectFit: "cover" as const,
  },
  info: {
    display: "flex",
    flexDirection: "column" as const,
    gap: "1.5rem",
    color:"#ffc320ff"
  },
  title: {
    fontSize: "2.5rem",
    margin: 0,
    color:"#ffc320ff"
  },
  details: {
    display: "flex",
    flexDirection: "column" as const,
    gap: "1rem",
    color:"#ffc320ff"
  },
  detail: {
    fontSize: "1.1rem",
    color:"#ffc320ff"
  },
  description: {
  marginTop: "1rem",
  "& p": {
    margin: "0.5rem 0 0 0",
    lineHeight: "1.6",
    color: "#444",
    }
  }
}

// const styles = {
//   container: {
//     maxWidth: "600px",
//     margin: "2rem auto",
//     padding: "1rem",
//     textAlign: "center" as const,
//     border: "1px solid #ddd",
//     borderRadius: "8px",
//     background: "#fff",
//   },
//   image: {
//     maxWidth: "100%",
//     height: "auto",
//     borderRadius: "8px",
//     marginBottom: "1rem",
//   },
//   details: {
//     textAlign: "left" as const,
//     lineHeight: "1.6",
//   },
//   editBtn: {
//     display: "inline-block",
//     marginTop: "1rem",
//     backgroundColor: "#f39c12",
//     color: "#fff",
//     padding: "0.5rem 1rem",
//     borderRadius: "4px",
//     textDecoration: "none",
//   },
// };
