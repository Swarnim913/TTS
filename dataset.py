import csv

# Technical speech sentences with common terms
technical_sentences = [
    "The API interface must be stable for third-party integration.",
    "CUDA is essential for accelerating deep learning training on GPUs.",
    "The OAuth protocol ensures secure authorization in distributed systems.",
    "REST APIs are used extensively for web services and data communication.",
    "Machine Learning models rely heavily on backpropagation for training.",
    "TensorFlow and PyTorch are popular frameworks for deep learning.",
    "A good understanding of HTTP methods is crucial for designing RESTful services.",
    "The GPU's CUDA cores speed up computation, making it ideal for neural networks.",
    "The OAuth2 standard is used to authorize access without sharing credentials.",
    "Kubernetes allows us to manage containerized applications easily.",
    "Docker helps in creating container environments for reproducibility.",
    "NLP tasks like tokenization are implemented using pre-trained language models.",
    "Using a VPN helps ensure that APIs are accessed securely over public networks.",
    "The hyperparameter tuning process is key to improving model accuracy.",
    "The JSON format is commonly used to serialize and exchange data between clients and servers.",
    "SQL is fundamental for interacting with relational databases.",
    "Load balancers help distribute traffic efficiently in distributed systems.",
    "Python’s Pandas library is heavily used for data manipulation and cleaning.",
    "The Git version control system is necessary for collaboration in software projects.",
    "OAuth allows an app to gain access to a user’s account without sharing the password."
]

# Save to CSV file
with open('technical_tts_dataset.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["text"])  # Header row
    for sentence in technical_sentences:
        csv_writer.writerow([sentence])

print("Dataset saved as 'technical_tts_dataset.csv' by dataset.py")
