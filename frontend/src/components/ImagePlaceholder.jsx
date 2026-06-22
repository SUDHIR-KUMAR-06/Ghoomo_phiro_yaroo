function ImagePlaceholder({ src,label, className = "" }) {
  return (
    <div className={`placeholder ${className}`.trim()} role="img" aria-label={label}>
      <img src={src} alt={label} className={className}/>
    </div>
  );
}

export default ImagePlaceholder;
