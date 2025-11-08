import Card from '../components/card';
import Link from 'next/link';

export default function Homepage() {
  return (
    <section style={styles.container}>
      <h1>Bem-vindo ao DBDB</h1>
      <div style={styles.grid}>
        <Link href="/obras">
          <Card
            title="Obras"
            description="Dragon Ball, Dragon Ball Z, GT, Super e mais"
            image="/images/obras.jpg"
          />
        </Link>
        <Link href="/sagas">
          <Card
            title="Sagas"
            description="Saiyan, Freeza, Cell, Majin Buu e outras sagas"
            image="/images/sagas.jpg"
          />
        </Link>
        <Link href="/racas">
          <Card
            title="Raças"
            description="Saiyajins, Namekuseijins, Terráqueos e outras raças"
            image="/images/racas.jpg"
          />
        </Link>
        <Link href="/personagens">
          <Card
            title="Personagens"
            description="Goku, Vegeta, Gohan e outros personagens"
            image="/images/personagens.jpg"
          />
        </Link>
        <Link href="/transformacoes">
          <Card
            title="Transformações"
            description="Super Saiyajin, Super Saiyajin Blue e mais"
            image="/images/transformacoes.jpg"
          />
        </Link>
      </div>
    </section>
  );
}

const styles = {
  container: {
    padding: '2rem',
    textAlign: 'center' as const,
  },
  title: {
    fontSize: '2rem',
    marginBottom: '2rem',
  },
  grid: {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))',
    gap: '1.5rem',
    justifyItems: 'center',
  },
};