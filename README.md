# Model Overview
 * Inspired by OpenAI's Moderation API, DreamUp.AI wanted to try and replicate the model they were relying on and make it open-source as one of the parts of my internship experience. The reason being is that it would allow for the creation of more detailed art through specific moderation classifications like "CP", "Gore", etc. as opposed to censoring anything remotely explicit which is what their previous binary classification model did. Although this model did not achieve that, it layed the foundational ground work for the rest of the project to build from. Completed in a two man team including myself over 4-weeks, this project served as a disgusting but impactful introduction to the complexities of Deep Learning & Natural Language Processing in my first college summer.

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

## Resources
 * https://wandb.ai/jack-morris/david-vs-goliath/reports/Does-Model-Size-Matter-A-Comparison-of-BERT-and-DistilBERT--VmlldzoxMDUxNzU 
 * https://datascience.stackexchange.com/questions/55991/in-the-context-of-deep-learning-what-is-training-warmup-steps
 * https://wandb.ai/jack-morris/david-vs-goliath/reports/Does-Model-Size-Matter-A-Comparison-of-BERT-and-DistilBERT--VmlldzoxMDUxNzU#:~:text=Defining%20the%20Search%20Space,5e%2D5%2C%203e%2D5 
 * https://mccormickml.com/2019/07/22/BERT-fine-tuning/ 
 * https://towardsdatascience.com/is-accuracy-everything-96da9afd540d#:~:text=Then%20the%20accuracy%20of%20the,can%20only%20predict%20one%20class

## Building + Running the Application
 * This application was trained on data from DreamUp.AI's platform that was classified by fine-tuning DistilBert using many different regularization techniques like Back Translation, Data Augmentation, etc. The data and model itself are too explicit to be stored on Github, therefore its contents cannot be published, and only data relating to the model architecture is disclosed. Ultimately, a lack of training data on the platform itself and in open-source repositories prevented the model from expanding to multiple categories, and all that remains is a prototype binary classifier. Please contact the collaborators if you have any questions and would like to use/access this model or its data.

## Final Training Data
<img width="645" alt="Screen Shot 2024-07-19 at 6 00 46 PM" src="https://github.com/user-attachments/assets/3d646df6-6d65-463b-9744-1b4a9fed9eed">
