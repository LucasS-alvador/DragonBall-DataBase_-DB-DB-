import Link from "next/link";

export default function Navbar() {
  return (
    <nav style={styles.nav}>
      <h2 style={styles.logo}>DBDB</h2>
      <div style={styles.links}>
        <Link href="/obras">Obras</Link>
        <Link href="/sagas">Sagas</Link>
        <Link href="/racas">Raças</Link>
        <Link href="/personagens">Personagens</Link>
      </div>
    </nav>
  );
}

const styles = {
  nav: {
    display: "flex",
    alignItems: "center",
    justifyContent: "space-between",
    backgroundColor: "#222",
    padding: "1rem 2rem",
    color: "#fff",
  },
  logo: {
    fontWeight: "bold",
  },
  links: {
    display: "flex",
    gap: "1.5rem",
  },
};
