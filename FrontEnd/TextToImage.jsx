import React, { useState } from 'react';
import { generateImage } from './api';

function TextToImage() {
  const [prompt, setPrompt] = useState('');
  const [imageUrl, setImageUrl] = useState('');

  const handleGenerate = async () => {
    const url = await generateImage(prompt);
    setImageUrl(url);
  };

  return (
    <div className="bg-white p-4 rounded-2xl shadow-md">
      <h2 className="text-xl font-semibold mb-2">Text to Image</h2>
      <input type="text" value={prompt} onChange={e => setPrompt(e.target.value)} placeholder="Enter prompt" className="w-full p-2 border rounded" />
      <button onClick={handleGenerate} className="mt-2 px-4 py-2 bg-blue-500 text-white rounded">Generate</button>
      {imageUrl && <img src={imageUrl} alt="Generated" className="mt-4 w-full rounded" />}
    </div>
  );
}

export default TextToImage;