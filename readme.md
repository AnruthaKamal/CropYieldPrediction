# Crop Yield Prediction
A machine learning-based application for predicting crop yield.
![plot](./about-img.png)
## Overview
The purpose of this project is to develop a machine learning-based application that can accurately predict crop yield based on various factors such as weather conditions, soil quality, and farming practices. The model will be trained on historical data and then used to make predictions for future crops.

## Requirements
- Python 3.x
- scikit-learn
- pandas
- numpy
## Usage
>Clone the repository: git clone https://github.com/AnruthaKamal/CropYieldPrediction.git <br>
>Install the required packages: pip install -r requirements.txt<br>
>Run the script: python main.py<br>

## File Structure
├── data<br>
│  <br> └── crops.csv<br>
├── main.py<br>
├── README.md<br>
└── requirements.txt<br>

## Data
The data used in this project is stored in the data folder in a CSV file called crops.csv. The file contains various attributes related to crop yields, such as weather conditions and soil quality, as well as the corresponding yields.

## Model
The model used in this project is a Decision Tree regression model from scikit-learn Out of Various other evaluated models like Ridge Lasso Linear Regression, KNN etc. The model is trained on the data in the crops.csv file and used to make predictions on new data.

## Contributing
If you'd like to contribute to this project, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See LICENSE for details.
