"use client";

import { useEffect, useState } from "react";
import { transformacaoService } from "../../services/api";
import Card from "../../components/card";
import Link from "next/link";
import type { Transformacao } from "../../types/models";

export default function TransformacoesPage() {
  const [transformacoes, setTransformacoes] = useState<Transformacao[]>([]);

  useEffect(() => {
    const fetchTransformacoes = async () => {
      try {
        const data = await transformacaoService.getAll();
        setTransformacoes(data);
      } catch (err) {
        console.error(err);
      }
    };
    fetchTransformacoes();
  }, []);

  return (
    <section>
      <h1>Transformações</h1>
      <Link href="/transformacoes/add" style={styles.addBtn}>Adicionar Transformação</Link>
      <div style={styles.grid}>
        {transformacoes.map((transformacao) => (
          <Link key={transformacao.id} href={`/transformacoes/${transformacao.id}`}>
            <Card
              title={transformacao.nome}
              description={`Poder: ${transformacao.poderMult}x | Cor: ${transformacao.cor}`}
              image={transformacao.imagem}
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