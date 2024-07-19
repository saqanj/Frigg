# Model Overview
 * Inspired by OpenAI's Moderation API, DreamUp.AI wanted to try and replicate the model they were relying on and make it open-source as one of the parts of my internship experience. The reason being is that it would allow for the creation of more detailed art through more specific moderation classifications like "CP", "Gore", etc. as opposed to censoring anything remotely explicit which is what their previous binary classification model did. Although this model did not achieve that, it layed the foundational ground work for the rest of the project to build from. Completed in a 2 man team including myself over 4-weeks, this project served as a disgusting but impactful introduction to the complexities of Deep Learning & Natural Language Processing in my first college summer.

## Collaborators
 * Saqlain Anjum, saqlainanjum13@gmail.com
 * Matteo Zambon, matteo@dreamup.ai

## Languages & Dependencies
 * Python
 * PyTorch
 * HuggingFace's Transformers Library
 * Matplotlib
 * Numpy
 * Linux & Bash

## Building + Running the Application
 * This application was trained on data from DreamUp.AI's platform that was self-engineered and crafted to be classified by fine-tuning DistilBert using many different regularization techniques like Back Translation, Data Augmentation, etc. The data and model itself is too explicit to be stored on Github, therefore its contents cannot be published, only data relating to the model architecture is disclosed. Ultimately, a lack of data on the platform and in open-source prevented the model from expanding to multiple categories, and the product could be fully functioning with just more data acquisition. Please contact the collaborators if you have any questions and would like to use/access this model or its data. 
