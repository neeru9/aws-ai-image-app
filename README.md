# 🖼️ AI Image Studio - Full Stack AI Image Generation Web App

## 🚀 Overview

**AI Image Studio** is a full-stack AI-powered web application deployed on AWS that enables users to:

- 🎨 Generate images from text prompts using **ControlNet**
- ✏️ Stylize and edit existing images via **Image-to-Image** transformation
- 🖼️ Store and explore created images in a **Prompt-based Image Gallery**

The app offers a seamless, cloud-native workflow for generating and editing AI images, with storage, metadata handling, and retrieval powered by AWS services.

---

## 🧩 Features

### ✅ Text-to-Image Generation (ControlNet)
Generate detailed and controllable AI images using ControlNet models by entering a simple text prompt.

### ✅ Image-to-Image Stylized Editing
Upload an image and apply stylized AI transformations using deep learning techniques.

### ✅ Image + Prompt Memory Gallery
Store AI-generated images along with their prompts and explore them later in a prompt-searchable gallery.

---

## 🏗️ Tech Stack

### Frontend
- **React**
- **Tailwind CSS**
- **Axios**

### Backend
- **Flask** (Python) running on **AWS EC2**
- Integrated with **ControlNet** for image generation
- Uses **Pillow/OpenCV** for image handling

### AWS Services
- **Amazon EC2** – Hosts the backend and AI model server
- **Amazon S3** – Stores generated and edited images
- **AWS Lambda** – Handles lightweight metadata tasks
- **DynamoDB** – Stores image metadata and prompts

---

## 📁 Project Structure

AI-Image-Studio/
│
├── frontend/ # React application
│ ├── public/
│ └── src/
│ ├── components/
│ ├── pages/
│ └── App.jsx
│
├── backend/ # Flask + ControlNet server
│ ├── app.py
│ ├── routes/
│ ├── utils/
│ └── models/
│
├── lambda/ # AWS Lambda handler code
│ └── store_metadata.py
│
└── README.md
## 🛠️ Setup Instructions </br>

**1. Clone the Repository** </br>

bash </br>
git clone https://github.com/neeru9/aws-ai-image-app  </br>
cd ai-image-studio </br>

**2. Frontend Setup (React)** </br>

`bash </br>
cd frontend </br>
npm install </br>
npm run dev </br>

**3. Backend Setup (Flask + ControlNet)** </br>

bash </br>
Copy </br>
Edit </br>
cd backend </br>
python3 -m venv venv </br>
source venv/bin/activate </br>
pip install -r requirements.txt </br>
python app.py </br>

**4. AWS Setup** </br>

Create an S3 bucket for image uploads. </br>

Create a DynamoDB table with keys like image_id, prompt, timestamp. </br>

Deploy the Lambda function from lambda/store_metadata.py. </br>

Set up IAM roles and environment variables for access. </br>

**📸 How It Works** </br>

User inputs a prompt on the React frontend. </br>

The prompt is sent to the Flask API hosted on EC2. </br>

ControlNet generates an image based on the prompt. </br>

The image is uploaded to S3. </br>

Lambda stores metadata (prompt, image URL, timestamp) in DynamoDB. </br>

Gallery retrieves and displays stored images based on prompt queries. </br>

**🔐 Security** </br>

Use IAM roles with least privilege for EC2, Lambda, and S3. </br>

Store AWS credentials securely using environment variables or AWS Secrets Manager. </br>

Enable CORS for secure communication between frontend and backend. </br>

**📈 Future Improvements** </br>

User authentication with AWS Cognito </br>

Advanced search and filtering in the gallery </br>

More ControlNet presets and customization options </br>

Mobile-friendly UI and progressive image loading </br>
