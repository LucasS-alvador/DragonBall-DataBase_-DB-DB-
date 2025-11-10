"use client";

import { useEffect, useState } from "react";
import { personagemSagaService } from "../../../services/api";
import Link from "next/link";
import type { PersonagemSaga } from "../../../types/models";

export default function PersonagemSagaDetailsPage({ params }: { params: { id: string } }) {
  const [personagem, setPersonagem] = useState<PersonagemSaga | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchPersonagem = async () => {
      try {
        const p = await Promise.resolve(params);
        const id = typeof p.id === 'string' ? parseInt(p.id) : p.id;
        const data = await personagemSagaService.getById(id);
        setPersonagem(data);
      } catch (err) {
        setError("Erro ao carregar os dados do personagem na saga");
        console.error(err);
      } finally {
        setLoading(false);
      }
    };
    fetchPersonagem();
  }, [params]);

  if (loading) return <div>Carregando...</div>;
  if (error) return <div>Erro: {error}</div>;
  if (!personagem) return <div>Personagem na saga não encontrado</div>;

  return (
    <div style={styles.container}>
      <Link href="/personagens-saga" style={styles.backButton}>← Voltar</Link>
      
      <div style={styles.content}>
        <div style={styles.imageContainer}>
          {personagem.imagem && (
            <img 
              src={personagem.imagem} 
              alt={`Personagem ${personagem.persBase_id} na Saga ${personagem.saga_id}`} 
              style={styles.image}
            />
          )}
        </div>

        <div style={styles.info}>
          <h1 style={styles.title}>Personagem na Saga</h1>
          
          <div style={styles.details}>
            <div style={styles.detail}>
              <strong>Personagem Base ID:</strong> {personagem.persBase_id}
            </div>
            
            <div style={styles.detail}>
              <strong>Saga ID:</strong> {personagem.saga_id}
            </div>

            <div style={styles.detail}>
              <strong>Poder:</strong> {personagem.poderMult}
            </div>

            {personagem.transformacoes && personagem.transformacoes.length > 0 && (
              <div style={styles.detail}>
                <strong>Transformações:</strong>
                <ul style={styles.list}>
                  {personagem.transformacoes.map((transId) => (
                    <li key={transId}>ID: {transId}</li>
                  ))}
                </ul>
              </div>
            )}
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
  list: {
    margin: "0.5rem 0 0 1.5rem",
    padding: 0,
  },
};