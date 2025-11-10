"use client";

import { useEffect, useState } from "react";
import { transformacaoService } from "../../../services/api";
import Link from "next/link";
import type { Transformacao } from "../../../types/models";

export default function TransformacaoDetailsPage({ params }: { params: { id: string } }) {
  const [transformacao, setTransformacao] = useState<Transformacao | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchTransformacao = async () => {
      try {
        const p = await Promise.resolve(params);
        const id = typeof p.id === 'string' ? parseInt(p.id) : p.id;
        const data = await transformacaoService.getById(id);
        setTransformacao(data);
      } catch (err) {
        setError("Erro ao carregar os dados da transformação");
        console.error(err);
      } finally {
        setLoading(false);
      }
    };
    fetchTransformacao();
  }, [params]);

  if (loading) return <div>Carregando...</div>;
  if (error) return <div>Erro: {error}</div>;
  if (!transformacao) return <div>Transformação não encontrada</div>;

  return (
    <div style={styles.container}>
      <Link href="/transformacoes" style={styles.backButton}>← Voltar</Link>
      
      <div style={styles.content}>
        <div style={styles.imageContainer}>
          {transformacao.imagem && (
            <img 
              src={transformacao.imagem} 
              alt={transformacao.nome} 
              style={styles.image}
            />
          )}
        </div>

        <div style={styles.info}>
          <h1 style={styles.title}>{transformacao.nome}</h1>
          
          <div style={styles.details}>
            <div style={styles.detail}>
              <strong>Poder:</strong> {transformacao.poderMult}
            </div>
            
            <div style={styles.detail}>
              <strong>Cor:</strong> {transformacao.cor}
            </div>

            <div style={styles.detail}>
              <strong>Especial:</strong> {transformacao.especial ? "Sim" : "Não"}
            </div>

            <div style={styles.detail}>
              <strong>Efeito Colateral:</strong> {transformacao.efeitoCol}
            </div>

            <div style={styles.detail}>
              <strong>Tempo Limite:</strong> {transformacao.limMinutos || "Sem limite"}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

const styles = {
  container: {
    padding: "2rem",
    maxWidth: "1200px",
    margin: "0 auto",
    backgroundColor: "#ff4141ff",
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
    backgroundColor: "white",
    borderRadius: "8px",
    padding: "2rem",
    boxShadow: "0 2px 8px rgba(0, 0, 0, 0.1)",
  },
  imageContainer: {
    width: "100%",
    aspectRatio: "1",
    borderRadius: "8px",
    overflow: "hidden",
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
  },
  title: {
    fontSize: "2.5rem",
    margin: 0,
    color: "#333",
  },
  details: {
    display: "flex",
    flexDirection: "column" as const,
    gap: "1rem",
  },
  detail: {
    fontSize: "1.1rem",
    color: "#666",
  },
};