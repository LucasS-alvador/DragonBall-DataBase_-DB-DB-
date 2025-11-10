"use client";

import { useEffect, useState } from "react";
import { personagemBaseService } from "../../../services/api";
import Link from "next/link";
import type { PersonagemBase } from "../../../types/models";

export default function PersonagemBaseDetailsPage({ params }: { params: { id: string } }) {
  const [personagem, setPersonagem] = useState<PersonagemBase | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchPersonagem = async () => {
      try {
        const p = await Promise.resolve(params);
        const id = typeof p.id === 'string' ? parseInt(p.id) : p.id;
        const data = await personagemBaseService.getById(id);
        setPersonagem(data);
      } catch (err) {
        setError("Erro ao carregar os dados do personagem");
        console.error(err);
      } finally {
        setLoading(false);
      }
    };
    fetchPersonagem();
  }, [params]);

  if (loading) return <div>Carregando...</div>;
  if (error) return <div>Erro: {error}</div>;
  if (!personagem) return <div>Personagem não encontrado</div>;

  return (
    <div style={styles.container}>
      <Link href="/personagens" style={styles.backButton}>← Voltar</Link>
      
      <div style={styles.content}>
        <div style={styles.imageContainer}>
          {personagem.imagem && (
            <img 
              src={personagem.imagem} 
              alt={personagem.nome} 
              style={styles.image}
            />
          )}
        </div>

        <div style={styles.info}>
          <h1 style={styles.title}>{personagem.nome}</h1>
          
          <div style={styles.details}>
            <div style={styles.detail}>
              <strong>Data de Nascimento:</strong> {personagem.dataNasc ? new Date(personagem.dataNasc).toLocaleDateString() : 'N/A'}
            </div>
            
            <div style={styles.detail}>
              <strong>Sexo:</strong> {personagem.sexo}
            </div>

            <div style={styles.detail}>
              <strong>Raça ID:</strong> {personagem.raca_id}
            </div>

            {personagem.descricao && (
              <div style={styles.description}>
                <strong>Descrição:</strong>
                <p>{personagem.descricao}</p>
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
//     padding: "2rem",
//     maxWidth: "1200px",
//     margin: "0 auto",
//   },
//   backButton: {
//     display: "inline-block",
//     marginBottom: "2rem",
//     color: "#0070f3",
//     textDecoration: "none",
//     fontSize: "1.1rem",
//   },
//   content: {
//     display: "grid",
//     gridTemplateColumns: "1fr 2fr",
//     gap: "2rem",
//     backgroundColor: "white",
//     borderRadius: "8px",
//     padding: "2rem",
//     boxShadow: "0 2px 8px rgba(0, 0, 0, 0.1)",
//   },
//   imageContainer: {
//     width: "100%",
//     aspectRatio: "1",
//     borderRadius: "8px",
//     overflow: "hidden",
//   },
//   image: {
//     width: "100%",
//     height: "100%",
//     objectFit: "cover" as const,
//   },
//   info: {
//     display: "flex",
//     flexDirection: "column" as const,
//     gap: "1.5rem",
//   },
//   title: {
//     fontSize: "2.5rem",
//     margin: 0,
//     color: "#333",
//   },
//   details: {
//     display: "flex",
//     flexDirection: "column" as const,
//     gap: "1rem",
//   },
//   detail: {
//     fontSize: "1.1rem",
//     color: "#666",
//   },
//   description: {
//     marginTop: "1rem",
//     "& p": {
//       margin: "0.5rem 0 0 0",
//       lineHeight: "1.6",
//       color: "#444",
//     }
//   },
// };