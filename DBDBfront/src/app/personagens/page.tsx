"use client";

import { useEffect, useState } from "react";
import { personagemBaseService } from "../../services/api";
import Card from "../../components/card";
import Link from "next/link";
import type { PersonagemBase } from "../../types/models";

export default function PersonagensPage() {
  const [personagens, setPersonagens] = useState<PersonagemBase[]>([]);

  useEffect(() => {
    const fetchPersonagens = async () => {
      try {
        const data = await personagemBaseService.getAll();
        setPersonagens(data);
      } catch (err) {
        console.error(err);
      }
    };
    fetchPersonagens();
  }, []);

  return (
    <section>
      <h1>Personagens</h1>
      <Link href="/personagens/add" style={styles.addBtn}>Adicionar Personagem</Link>
      <div style={styles.grid}>
        {personagens.map((personagem) => (
          <Link key={personagem.id} href={`/personagens/${personagem.id}`}>
            <Card
              title={personagem.nome}
              description={`Nascimento: ${new Date(personagem.dataNasc).toLocaleDateString()}`}
              image={personagem.imagem}
            />
          </Link>
        ))}
      </div>
    </section>
  );
}

const styles = {
  grid: {
    display: "grid",
    gridTemplateColumns: "repeat(auto-fit, minmax(250px, 1fr))",
    gap: "1.5rem",
    marginTop: "1rem",
  },
  addBtn: {
    display: "inline-block",
    backgroundColor: "#0070f3",
    color: "white",
    padding: "0.5rem 1rem",
    borderRadius: "4px",
    textDecoration: "none",
  },
};