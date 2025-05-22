import React, { useState } from 'react';
import { stylizeImage } from './api';

function ImageEdit() {
  const [file, setFile] = useState(null);
  const [styledUrl, setStyledUrl] = useState('');

  const handleUpload = async () => {
    if (!file) return;
    const url = await stylizeImage(file);
    setStyledUrl(url);
  };

  return (
    <div className="bg-white p-4 rounded-2xl shadow-md">
      <h2 className="text-xl font-semibold mb-2">Image to Image (Stylized Edit)</h2>
      <input type="file" onChange={e => setFile(e.target.files[0])} className="w-full" />
      <button onClick={handleUpload} className="mt-2 px-4 py-2 bg-green-500 text-white rounded">Stylize</button>
      {styledUrl && <img src={styledUrl} alt="Stylized" className="mt-4 w-full rounded" />}
    </div>
  );
}

export default ImageEdit;
