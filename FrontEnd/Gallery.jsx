import React, { useEffect, useState } from 'react';
import { fetchGallery } from './api';

function Gallery() {
  const [items, setItems] = useState([]);

  useEffect(() => {
    const load = async () => {
      const data = await fetchGallery();
      setItems(data);
    };
    load();
  }, []);

  return (
    <div className="bg-white p-4 rounded-2xl shadow-md overflow-y-auto max-h-[600px]">
      <h2 className="text-xl font-semibold mb-2">Gallery</h2>
      <div className="space-y-4">
        {items.map((item, i) => (
          <div key={i} className="border p-2 rounded">
            <p className="text-sm text-gray-600">Prompt: {item.prompt}</p>
            <img src={item.image_url} alt="Generated" className="mt-2 rounded w-full" />
          </div>
        ))}
      </div>
    </div>
  );
}

export default Gallery;