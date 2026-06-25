import random

def preprocess_image(image_file):
    """
    Simulated image preprocessing.
    In a real scenario, this would use OpenCV:
    import cv2
    img = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_COLOR)
    img = cv2.resize(img, (224, 224))
    img = img / 255.0
    return img
    """
    return True

def predict_disease(image_file, crop_type):
    """
    Simulated ML prediction.
    In a real scenario, this would use a loaded Keras model:
    model.predict(preprocessed_image)
    """
    preprocess_image(image_file)
    
    # Simulated possible outputs
    diseases = {
        'Tomato': ['Healthy', 'Early Blight', 'Late Blight', 'Leaf Spot'],
        'Potato': ['Healthy', 'Early Blight', 'Late Blight'],
        'Rice': ['Healthy', 'Brown Spot', 'Leaf Smut']
    }
    
    possible_diseases = diseases.get(crop_type, ['Healthy', 'Unknown Disease'])
    
    disease_name = random.choice(possible_diseases)
    confidence = round(random.uniform(75.0, 99.9), 2)
    
    solutions = {
        'Healthy': 'Keep up the good work! Maintain proper watering and fertilization.',
        'Early Blight': 'Apply copper-based fungicides. Remove infected leaves.',
        'Late Blight': 'Apply appropriate fungicides (e.g., chlorothalonil). Ensure good air circulation.',
        'Leaf Spot': 'Avoid overhead watering. Apply fungicides if severe.',
        'Brown Spot': 'Ensure balanced soil nutrients, especially silicon. Use appropriate fungicides.',
        'Leaf Smut': 'Treat seeds before planting. Apply propiconazole if necessary.'
    }
    
    solution = solutions.get(disease_name, 'Consult a local agricultural expert.')
    
    return {
        'disease_name': disease_name,
        'confidence': confidence,
        'recommended_solution': solution
    }
