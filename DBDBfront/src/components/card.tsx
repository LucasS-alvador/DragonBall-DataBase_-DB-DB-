type CardProps = {
  title: string;
  description: string;
  image?: string;
};

export default function Card({ title, description, image }: CardProps) {
  return (
    <div style={styles.card}>
      {image && <img src={image} alt={title} style={styles.image} />}
      <h3>{title}</h3>
      <p>{description}</p>
    </div>
  );
}

const styles = {
  card: {
    border: '3px solid #000000ff',
    color:'black',
    borderRadius: '8px',
    padding: '1.5rem',
    width: '100%',
    maxWidth: '300px',
    boxShadow: '0 2px 8px rgba(0, 0, 0, 0.1)',
    transition: 'all 0.2s ease',
    display: 'flex',
    flexDirection: 'column' as const,
    gap: '1rem',
    cursor: 'pointer',
    backgroundColor: '#ffc320ff',
    '&:hover': {
      transform: 'translateY(-5px)',
      boxShadow: '0 4px 12px rgba(0, 0, 0, 0.15)',
    }
  },
  image: {
    width: '100%',
    height: '200px',
    objectFit: 'cover' as const,
    borderRadius: '4px',
    border: '3px solid #000000ff',
  }
};
