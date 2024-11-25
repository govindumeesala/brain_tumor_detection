# Iris Tumor Detection

A deep learning-based web application for detecting iris tumors from uploaded images. This project utilizes a **VGG19-based model** to classify images as "Tumor Detected" or "No Tumor Detected." The application is built using **Django** with a modern interface powered by **Bootstrap** for responsive design.

---

## 🚀 Features
- **Deep Learning Model**: Uses a fine-tuned VGG19 model for accurate tumor detection.
- **Web Interface**: User-friendly interface created with Bootstrap for easy navigation.
- **Real-time Predictions**: Upload images and get instant results.
- **Authentication**: User registration and login functionality.
- **Secure Image Uploads**: Handles images securely during processing.

---

## 🛠️ Technologies Used
- **Backend**: Django
- **Deep Learning Framework**: TensorFlow/Keras
- **Model Architecture**: VGG19
- **Frontend**: HTML, CSS, JavaScript, Bootstrap, Django
- **Image Processing**: OpenCV, Pillow

---


---

## ⚙️ Installation and Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/iris-tumor-detection.git
    cd iris-tumor-detection
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate      # On Windows: .\venv\Scripts\activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Add the VGG19 model weights**:
    - Place the `vgg_unfrozen.h5` file in the root directory. 
    - *Note*: This file is too large for GitHub. Add it manually after cloning.

6. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

7. **Access the application**:
    Open your browser and navigate to `http://127.0.0.1:8000`.

---

## 🖼️ Usage
1. Register or log in to the application.
2. Navigate to the **Upload Image** page.
3. Upload an iris image.
4. View the results: **Tumor Detected** or **No Tumor Detected**.

---

## 💡 Key Functionality
- **Image Upload**: Uploads are securely handled and processed for classification.
- **Prediction Logic**: The `utils.py` file includes preprocessing and prediction logic using the VGG19 model.
- **Responsive Design**: The frontend is styled with Bootstrap for compatibility across devices.

---

## 🧪 Testing
- Test the application with various iris images to evaluate its accuracy.
- Supported image formats: `.jpg`, `.png`, `.jpeg`.

---

## 📝 Notes
- The **model weights** (`vgg_unfrozen.h5`) must be manually added due to GitHub's file size limitations.
- Bootstrap is used for styling, ensuring a clean and responsive interface.
  
---

## 🤝 Acknowledgements
- The VGG19 model is based on the paper by Simonyan and Zisserman, *"Very Deep Convolutional Networks for Large-Scale Image Recognition"*.
- Frameworks: Django, TensorFlow/Keras.
- Styling: Bootstrap.

---

## 👩‍💻 Author
- **Meesala Govindu**  
  - Email: meesalagovindu123@gmail.com  
  - GitHub: [govindumeesala](https://github.com/govindumeesala)
