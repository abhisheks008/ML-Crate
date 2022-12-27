# Pull Request for ML-Crate 💡


## Issue Title: Alpaca Identification #93 

- **Info about the related issue (Aim of the project)** : Create a model which predicts whether an image consists of Alpaca or not.
- **Name:** Evan Joshy Chittilappilly
- **GitHub ID:** TheDarkParalda
- **Idenitfy yourself:** Participant

Closes: #93 

### Describe the add-ons or changes you've made 📃
* Importing Keras, Tensorflow, mathplotlib and other libraries for the solution
* Creating the function that returns the VGG_16 model
* Importing the data, Splitting the dataset to Train and Test (Validation) data and normalising them.
* Training the model. (Uses Early Stopping for maximum accuracy and Adam as an optimizer)
* Plotting the accuracy and loss per epoch
* Random predictions of certain images
* Model produces Train Set Accuracy of 100% and Validation Set accuracy of 87.69

Give a clear description of what have you added or modifications made

## Type of change ☑️

What sort of change have you made:
- [X] New feature (non-breaking change which adds functionality)
- [X] Code style update (formatting, local variables)
- [X] Breaking change (fix or feature that would cause existing functionality to not work as expected)

## How Has This Been Tested? ⚙️

* The model was tested by splitting the Total Dataset into 2 : Training Data and Validation Data.
* The Model was verified with Validation Data 

- [X] My code follows the guidelines of this project.
- [X] I have performed a self-review of my own code.
- [X] I have commented my code, particularly wherever it was hard to understand.
- [X] I have made corresponding changes to the documentation.
- [X] My changes generate no new warnings.
- [X] I have added things that prove my fix is effective or that my feature works.
- [X] Any dependent changes have been merged and published in downstream modules
