#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 14:07:54 2020

@author: jennychou
"""

import os
import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error
pd.set_option('precision', 3)


class Data:
    """
    Data container. Base class. Handles basic data cleaning, preping, and
    encoding.
    """
    def __init__(self, train_file, target_file, test_file, target, index):
        """
        Class constructor.

        Args:
            train_file: relative path pointed at train file containing 
                features data
            target_file: relative path pointed at train file containing 
                target data
            test_file: relative path pointed at test file containing 
                features dataset
            target: target column name
            index: index column name
        """
        self.train = None
        self.test = None
        self.features = None
        self.target = target
        self.index = index

        self._load_data(train_file, target_file, test_file)
        self._clean_data()
        print("After clean up train dataset has shape:", self.train.shape)
        print("After clean up test dataset has shape:", self.test.shape)
        print()

    def encode_data(self):
        """
        Transform feature columns using group average salary
        """
        for col in self.features:
            group_dict = dict(self.train.groupby([col])[self.target].mean())
            self.train[col] = self.train[col].map(group_dict)
            self.test[col] = self.test[col].map(group_dict)

    def split_data(self):
        """
        Split and return feature and target dataframe

        Returns:
            Tuple of feature and target dataframe
        """
        return self.train.drop(columns=self.target), self.train[self.target]
    
    def get_baseline(self):
        """
        Compute and return baseline model MSE

        Returns:
            Baseline model MSE
        """
        baseline_true = self.train[self.target].values.astype(float)
        mean_dict = dict(self.train.groupby(['industry'])[self.target].mean())
        baseline_pred = self.train.industry.map(mean_dict)
        baseline_mse = mean_squared_error(baseline_true, baseline_pred)
        print("Baseline: MSE=%.3f\n" % baseline_mse)
        return baseline_mse

    def _load_data(self, train_file, target_file, test_file):
        """
        Load data from files

        Args:
            train_file: relative path pointed at train file containing 
                features data
            target_file: relative path pointed at train file containing 
                target data
            test_file: relative path pointed at test file containing 
                features dataset
        """
        self.train = pd.read_csv(train_file)
        self.features = self.train.drop(columns=self.index).columns.values
        self.train = pd.merge(self.train, pd.read_csv(target_file), on=self.index)
        self.test = pd.read_csv(test_file)

    def _clean_data(self):
        """
        Check and remove invalid instance(s)
        """
        self._drop_duplicates(self.train)
        self._drop_duplicates(self.test)
        self._drop_null(self.train)
        self._drop_null(self.test)
        self._check_col_validity(self.train, 'yearsExperience', 0)
        self._check_col_validity(self.test,  'yearsExperience', 0)
        self._check_col_validity(self.train, 'milesFromMetropolis', 0)
        self._check_col_validity(self.test,  'milesFromMetropolis', 0)
        self._check_col_validity(self.train, 'salary', 1)

    def _drop_duplicates(self, df):
        """
        Drop duplicated instance(s)

        Args:
            df: dataframe to be checked
        """
        print("Remove %d duplicated jobs" % df.duplicated().sum())
        df.drop_duplicates(inplace=True)

    def _drop_null(self, df):
        """
        Drop instance(s) with np.None or np.NaN

        Args:
            df: dataframe to be checked
        """
        invalid_jobs = df.index[df.isnull().sum(axis=1).gt(0)].values
        print("Remove %d jobs with missing values" % len(invalid_jobs))
        df.drop(index=invalid_jobs, inplace=True)

    def _fill_null(self, df):
        """
        Fill np.None or np.NaN with mean value

        Args:
            df: dataframe to be checked
        """
        invalid_jobs = df.index[df.isnull().sum(axis=1).gt(0)].values
        print("Fill %d missing values with feature mean" % len(invalid_jobs))
        df.fillna(df.mean(), inplace=True)
    
    def _check_col_validity(self, df, col, threshold):
        """
        Drop instance(s) having invalid value at given column

        Args:
            df: dataframe to be checked
            col: column to be inspect
            threshold: invalid if value less than threshold
        """
        invalid_jobs = df.index[df[col].lt(threshold)]
        print("Remove %d jobs with invalid %s" % (len(invalid_jobs), col))
        df.drop(index=invalid_jobs, inplace=True)


class FeatureEngineer(Data):
    """
    Engineered data container. Inherite from Data base class. Handles 
    advanced data engineering.
    """
    def __init__(self, train_file, target_file, test_file, target, index):
        """
        Class constructor.

        Args:
            train_file: relative path pointed at train file containing 
                features data
            target_file: relative path pointed at train file containing 
                target data
            test_file: relative path pointed at test file containing 
                features dataset
            target: target column name
            index: index column name
        """
        Data.__init__(self, train_file, target_file, test_file, target, index)
        self._stats = []

    def add_stats(self, cols, col_name):
        """
        Engineer group statistics and merge with train and test dataframe

        Args:
            cols: list of columns
            col_name: prefix added to new column names
        """
        self._generate_stats(cols, col_name)
        self.train = self._merge_stats(self.train, cols)
        self.test = self._merge_stats(self.test,  cols)

    def _generate_stats(self, cols, col_name):
        """
        Engineer group statistics

        Args:
            cols: list of columns
            col_name: prefix added to new column names
        """
        group = self.train.groupby(cols)[self.target]
        Q1 = group.quantile(0.25)
        Q3 = group.quantile(0.75)
        upper_bound = Q3 + 1.5 * (Q3 - Q1)
        
        self._stats = pd.DataFrame({col_name+"_mean" : group.mean()})
        self._stats[col_name + "_min"] = group.min()
        self._stats[col_name + "_Q1"] = Q1
        self._stats[col_name + "_median"] = group.median()
        self._stats[col_name + "_Q3"] = Q3
        self._stats[col_name + "_upper"] = upper_bound
        self._stats[col_name + "_max"] = group.max()
        
    def _merge_stats(self, df, cols):
        """
        Merge group statistics to dataframe
        
        Args:
            df: dataframe to be merged
            cols: list of columns
            
        Returns:
            df: modified dataframe
        """
        df = pd.merge(df, self._stats, on=cols, how='left')
        df.set_index(self.index, inplace=True)
        self._fill_null(df)
        return df
        

class Models:
    """
    Model container. Handles model training, predicting, and exporting
    """
    def __init__(self, data):
        """
        Class constructor.

        Args:
            data : tuple of train_X and train_y
        """
        self.train_X = data[0]
        self.train_y = data[1]
        self._models = []
        self._scores = []
        self._mse = []
        self._best_model = None
        self._best_mse = None
    
    def set_baseline(self, baseline):
        """
        Acquire baseline MSE

        Args:
            baseline: baseline MSE
        """
        self._mse.append(baseline)

    def add_model(self, model):
        """
        Append model to list

        Args:
            model: model
        """
        self._models.append(model)

    def cv_models(self, cv=None):
        """
        Perform cross validation with all models

        Args:
            cv: number of folds in (Stratified)KFold
        """
        for model in self._models:
            scores = cross_val_score(model, self.train_X, self.train_y, cv=cv,
                                     scoring='neg_mean_squared_error')
            mse = -1.0 * np.mean(scores)
            self._print_summary(model, scores, mse)

            if(mse <= min(self._mse)):
                self._best_model = model
                self._best_mse = mse
                
            self._scores.append(scores)
            self._mse.append(mse)

    def print_all(self):
        """
        Print all models, their scores and average MSE
        """
        print("Models:", self._models)
        print("Scores:", self._scores)
        print("MSE:", self._mse)
        print()
        
    def print_best_model(self):
        """
        Print best model, its cross validation MSE scores and average MSE
        """
        print("Best model: %s\nBest MSE: %.3f" %
              (self._best_model, self._best_mse))
        self._best_model.fit(self.train_X, self.train_y)
        
        if hasattr(self._best_model, 'feature_importances_'):
            print("Feature Importances:")
            feature_importance = self._best_model.feature_importances_
            index = self.train_X.columns
            for i in range(len(feature_importance)):
                print("%s  %.6f" % (index[i], feature_importance[i]))
        print()
                
    def predict(self, test):
        """
        Make prediction on test data using best model

        Args:
            test: test dataframe

        Returns:
            Dataframe containing prediction for test data
        """
        test_pred = self._best_model.predict(test).round(3)
        return pd.DataFrame(test_pred, index=test.index, columns=[self.target])        

    def _print_summary(self, model, scores, mse):
        """
        Print model, its scores, and MSE

        Args:
            model: model
            scores: cross validation MSE scores
            mse: mean of scores
        """
        print("Model:", model)
        print("Scores:", *scores)
        print("MSE: %.3f" % mse)
        print()


if __name__ == "__main__":
    # Create data object and perform basic cleaning
    dataset = FeatureEngineer("../data/train_features.csv",
                              "../data/train_salaries.csv",
                              "../data/test_features.csv",
                              'salary',
                              'jobId')
    
    # Encode data
    dataset.encode_data()
    
    # Add engineered data
    features = ['companyId', 'jobType', 'degree', 'major', 'industry']
    dataset.add_stats(features, "CJDMI")
    
    # Create model object and set baseline
    model = Models(dataset.split_data())
    model.set_baseline(dataset.get_baseline())
    
    # Add models
    model.add_model(LinearRegression())
    model.add_model(Lasso())
    model.add_model(GradientBoostingRegressor(max_depth=8))
    model.add_model(Pipeline([("Scaler", StandardScaler()), 
                              ("GBR", GradientBoostingRegressor(max_depth=8))]))
    
    # Cross validate models
    model.cv_models()
    
    # See results of all models
    model.print_all()
    
    # Fit and see best model summary 
    model.print_best_model()
    
    # Predict test data, and export to csv file
    filename = "test_salaries_prediction.csv"
    model.predict(dataset.test).to_csv(filename)
    

"""
Remove 0 duplicated jobs
Remove 0 jobs with missing values
Remove 0 jobs with invalid yearsExperience
Remove 0 jobs with invalid milesFromMetropolis
Remove 5 jobs with invalid salary
After clean up train dataset has shape: (999995, 9)
After clean up test dataset has shape: (1000000, 8)
Baseline: MSE=1367.123

Model: LinearRegression()
Scores: -282.1279070970527 -312.13227166363714 -359.3584129264609 -403.5778042514682 -403.9512479425134
MSE: 352.230

Model: Lasso()
Scores: -282.0820360328884 -312.31261353358383 -359.51148210993637 -403.5275292113644 -404.05802358420823
MSE: 352.298

Model: GradientBoostingRegressor(max_depth=8)
Scores: -254.0025916988774 -282.0900320121363 -317.79428740263006 -342.2880180930733 -330.9507999590655
MSE: 305.425

Model: Pipeline(steps=[('Scaler', StandardScaler()),
                       ('GBR', GradientBoostingRegressor(max_depth=8))])
Scores: -254.00116684416804 -282.10207223980524 -317.80630540658564 -342.3031495765848 -330.9722021579111
MSE: 305.437

Models: [LinearRegression(), 
         Lasso(), 
         GradientBoostingRegressor(max_depth=8), 
         Pipeline(steps=[('Scaler', StandardScaler()),
                         ('GBR', GradientBoostingRegressor(max_depth=8))])]
Scores: [array([-282.1279071 , -312.13227166, -359.35841293, -403.57780425, -403.95124794]), 
         array([-282.08203603, -312.31261353, -359.51148211, -403.52752921, -404.05802358]), 
         array([-254.0025917 , -282.09003201, -317.7942874 , -342.28801809, -330.95079996]), 
         array([-254.00116684, -282.10207224, -317.80630541, -342.30314958, -330.97220216])]
MSE: [1367.1229507852556, 352.22952877622646, 352.2983368943963, 305.42514583315653, 305.436979245011]

Best model: GradientBoostingRegressor(max_depth=8)
Best MSE: 305.425
Feature Importances:
companyId  0.000193
jobType  0.003787
degree  0.002940
major  0.001043
industry  0.002110
yearsExperience  0.151999
milesFromMetropolis  0.104911
CJDMI_mean  0.658369
CJDMI_min  0.008928
CJDMI_Q1  0.032180
CJDMI_median  0.006870
CJDMI_Q3  0.007684
CJDMI_upper  0.001903
CJDMI_max  0.017082
"""