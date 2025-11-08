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
    border: '1px solid #ddd',
    borderRadius: '8px',
    padding: '1.5rem',
    width: '100%',
    maxWidth: '300px',
    boxShadow: '0 2px 8px rgba(0, 0, 0, 0.1)',
    transition: 'transform 0.2s ease',
    display: 'flex',
    flexDirection: 'column' as const,
    gap: '1rem',
  },
  image: {
    width: '100%',
    height: '200px',
    objectFit: 'cover' as const,
    borderRadius: '4px',
  }
};
