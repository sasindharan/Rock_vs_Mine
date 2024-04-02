# Rock_vs_Mine

Model
The prediction system employs a machine learning model based on logistic regression. Logistic regression is a binary classification algorithm suitable for scenarios where the dependent variable (in this case, rock or mine) is categorical.

Dataset
The model is trained and tested on the Sonar dataset, which consists of 208 instances of sonar signals bounced off either a metal cylinder (rock) or a cylindrical mine-like object. Each instance has 60 features, representing the energy within specific frequency bands.

Preprocessing
Before training the model, the dataset undergoes preprocessing steps such as:

Normalization: Scaling the features to a similar range to prevent certain features from dominating others.
Train-Test Split: Dividing the dataset into training and testing sets to evaluate the model's performance on unseen data.
Training
The model is trained on the training set using logistic regression. During training, the model learns the parameters that best fit the data, aiming to minimize the logistic loss function.

Testing
After training, the model is evaluated on the testing set to assess its performance. The accuracy of the model in correctly classifying rocks and mines is calculated.

Prediction
Once trained, the model can make predictions on new sonar signals by extracting relevant features and feeding them into the trained logistic regression model. The model outputs a probability score indicating the likelihood of the object being a rock or a mine. A threshold is applied to these scores to make the final classification decision.

