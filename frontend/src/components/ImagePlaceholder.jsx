function ImagePlaceholder({ label, className = "" }) {
  return (
    <div className={`placeholder ${className}`.trim()} role="img" aria-label={label}>
      <span>{label}</span>
    </div>
  );
}

export default ImagePlaceholder;
