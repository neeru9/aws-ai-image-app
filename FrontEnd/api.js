export const generateImage = async (prompt) => {
  const res = await fetch('https://your-api-endpoint/text-to-image', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ prompt }),
  });
  const data = await res.json();
  return data.image_url;
};

export const stylizeImage = async (file) => {
  const formData = new FormData();
  formData.append('file', file);

  const res = await fetch('https://your-api-endpoint/image-edit', {
    method: 'POST',
    body: formData,
  });
  const data = await res.json();
  return data.image_url;
};

export const fetchGallery = async () => {
  const res = await fetch('https://your-api-endpoint/gallery');
  const data = await res.json();
  return data.items;
};