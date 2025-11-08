type FormFieldProps = {
  label: string;
  name: string;
  type: string;
  value: any;
  onChange: (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => void;
  required?: boolean;
  min?: string | number;
  max?: string | number;
  placeholder?: string;
  className?: string;
  step?: string | number;
};

export function FormField({ 
  label, 
  name, 
  type, 
  value, 
  onChange, 
  required = false,
  min,
  max,
  placeholder,
  className,
  step
}: FormFieldProps) {
  const inputProps = {
    id: name,
    name,
    value,
    onChange,
    required,
    min,
    max,
    placeholder,
    className,
    step
  };

  return (
    <div style={styles.field}>
      <label htmlFor={name} style={styles.label}>
        {label}
      </label>
      {type === 'textarea' ? (
        <textarea
          {...inputProps}
          style={styles.textarea}
        />
      ) : (
        <input
          type={type}
          {...inputProps}
          style={styles.input}
        />
      )}
    </div>
  );
}

const styles = {
  field: {
    marginBottom: '1rem',
  },
  label: {
    display: 'block',
    marginBottom: '0.5rem',
    fontWeight: 'bold' as const,
  },
  input: {
    width: '100%',
    padding: '0.5rem',
    border: '1px solid #ddd',
    borderRadius: '4px',
    fontSize: '1rem',
  },
  textarea: {
    width: '100%',
    padding: '0.5rem',
    border: '1px solid #ddd',
    borderRadius: '4px',
    fontSize: '1rem',
    minHeight: '100px',
    resize: 'vertical' as const,
  },
};