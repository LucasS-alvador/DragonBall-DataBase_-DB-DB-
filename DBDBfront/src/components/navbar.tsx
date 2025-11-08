import Link from "next/link";

export default function Navbar() {
  return (
    <nav style={styles.nav}>
      <h2 style={styles.logo}>DBDB</h2>
      <div style={styles.links}>
        <Link href="/" style={styles.link}>Home</Link>
        <Link href="/obras" style={styles.link}>Obras</Link>
        <Link href="/sagas" style={styles.link}>Sagas</Link>
        <Link href="/racas" style={styles.link}>Raças</Link>
        <Link href="/personagens" style={styles.link}>Personagens</Link>
        <Link href="/transformacoes" style={styles.link}>Transformações</Link>
      </div>
    </nav>
  );
}

const styles = {
  nav: {
    display: "flex",
    alignItems: "center",
    justifyContent: "space-between",
    backgroundColor: "#1a1a1a",
    padding: "1rem 2rem",
    color: "#fff",
    boxShadow: "0 2px 4px rgba(0,0,0,0.2)",
  },
  logo: {
    fontWeight: "bold",
    fontSize: "1.5rem",
    color: "#0070f3",
  },
  links: {
    display: "flex",
    gap: "1.5rem",
  },
  link: {
    color: "#fff",
    textDecoration: "none",
    padding: "0.5rem 1rem",
    borderRadius: "4px",
    transition: "background-color 0.2s",
    ":hover": {
      backgroundColor: "#333",
    },
  },
};
