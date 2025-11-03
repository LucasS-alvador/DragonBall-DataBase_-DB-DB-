import Card from '../components/card';

export default function Homepage() {
  return (
    <section style={styles.container}>
      <h1>Bem-vindo ao DBDB</h1>
      <div style={styles.grid}>
      <Card title="Exemplo 1" description="Descrição do card 1" />
      <Card title="Exemplo 2" description="Descrição do card 2" />
      <Card title="Exemplo 2" description="Descrição do card 2" />
      <Card title="Exemplo 2" description="Descrição do card 2" />
      <Card title="Exemplo 2" description="Descrição do card 2" />
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