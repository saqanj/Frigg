# AUTHORS: SAQLAIN ANJUM AND MATTEO ZAMBOM
# Testing different inputs on the functional model.
# Code was written on Google CoLab.


!pip install transformers[torch]

from google.colab import drive

drive.mount('/content/drive')
output_dir = '/content/drive/MyDrive/Training Folder'

from transformers import DistilBertTokenizer, DistilBertForSequenceClassification, AutoConfig
import torch


config = AutoConfig.from_pretrained('/content/drive/MyDrive/Internship Training Folder/Best Model Architecture/config.json')
tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")
model = DistilBertForSequenceClassification.from_pretrained("/content/drive/MyDrive/Internship Training Folder/Best Model Architecture/ModerationModel.bin", config=config)

inputs = tokenizer("Mountains with blue sky and a lake", return_tensors="pt")
labels = torch.tensor([1]).unsqueeze(0)
outputs = model(**inputs, labels=labels)
logits = outputs.logits
predicted_class_id = logits.argmax().item()
predicted_percentage = logits.max().item()

print('Label:', model.config.id2label[predicted_class_id])
print(logits)
print('Predicted Percentage:', 100*predicted_percentage)
print(outputs)
