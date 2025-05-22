// frontend/src/App.jsx
import React from 'react';
import TextToImage from './TextToImage';
import ImageEdit from './ImageEdit';
import Gallery from './Gallery';

function App() {
  return (
    <div className="min-h-screen bg-gray-100 p-4">
      <h1 className="text-3xl font-bold text-center mb-6">AI Image Generator App</h1>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <TextToImage />
        <ImageEdit />
        <Gallery />
      </div>
    </div>
  );
}

export default App;