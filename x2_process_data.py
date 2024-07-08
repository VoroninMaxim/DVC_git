#Importing the libraries used
import pandas as pd
import numpy as np

defaultTest = pd.read_csv("data/test.csv", sep=',')                # Importing the dataframe 'test.csv' from the appropriate folder
defaultTrain = pd.read_csv("data/train.csv", sep=',')              # Importing the dataframe 'train.csv' from the appropriate folder
fulldf = pd.concat([defaultTest, defaultTrain])      # Merging  the 2 datasets, so that we can work as if we were given the undivided

#dataset in the first place.
fulldf.index.name = 'i'                              # Renaming the index column so that the new index will not have the same name as the old
fulldf = fulldf.reset_index()                        # Resetting the indexes for appearance's sake.
fulldf = fulldf.drop(['i', 'Unnamed: 0'], axis = 1)  # Removing the columns of indexes which we changed: the change was not necessary, only for the sake of appearance

# Data Cleaning
dupl = fulldf.groupby(['id']).size() > 1
fulldf = fulldf.drop(['id'], axis = 1)               # Further unneded attribute


#Encoding values from string to numerical

#--------------------------------------------------------------
# columns_to_change = ['Gender', 'satisfaction', 'Type of Travel', 'Customer Type', 'Class', 'Arrival Delay in Minutes']
# #print (fulldf[columns_to_change])
#
# from sklearn import preprocessing
# one_hot_encoder = preprocessing.OneHotEncoder(drop = 'first')
# # # # объект OneHotEncoder() обучается на данных из выбранных колонок
# # # # с помощью метода fit_transform(), и результат преобразуется в массив с помощью метода toarray().
# # data_onehot = one_hot_encoder.fit_transform(fulldf[columns_to_change]).toarray() # результат переводим в массив
# # # # Из объекта OneHotEncoder() извлекаются закодированные имена столбцов с помощью метода get_feature_names_out().
# # #column_names = one_hot_encoder.get_feature_names_out()
# # # # Составляем DataFrame data_onehot из закодированных данных и имен столбцо
# # data_onehot = pd.DataFrame(data_onehot, columns = data_onehot)
#------------------------------------------------------------------------------------

# # обучаем и преобразуем категориальные переменные
# encoded_vars = one_hot_encoder.fit_transform(fulldf[columns_to_change])
# # преобразуем закодированные переменные в DataFrame
# encoded_df = pd.DataFrame(encoded_vars.toarray(), columns=one_hot_encoder.get_feature_names_out())
# # объединяем закодированные переменные с исходным DataFrame
# df = pd.concat([fulldf, encoded_df], axis=1)
# print('Количество новых бинарных столбцов:', df.shape[1])
# print('Количество новых бинарных столбцов:', df)
#--------------------------------------------------------------



pd.set_option('future.no_silent_downcasting', True)


fulldf['Gender'] = fulldf['Gender'].replace({"Male": 0, "Female": 1}).infer_objects()

#fulldf['Gender'] = fulldf['Gender'].replace({"Male": 0, "Female": 1})

fulldf['satisfaction'] = fulldf['satisfaction'].replace({"neutral or dissatisfied": 0, "satisfied": 1}).infer_objects()
fulldf['Type of Travel'] = fulldf['Type of Travel'].replace({"Personal Travel": 0, "Business travel": 1}).infer_objects()
fulldf['Customer Type'] = fulldf['Customer Type'].replace({"disloyal Customer": 0, "Loyal Customer": 1}).infer_objects()
fulldf['Class'] = fulldf['Class'].replace({"Eco": 0, "Eco Plus": 1, "Business": 2}).infer_objects()

# fulldf['Arrival Delay in Minutes'].fillna(fulldf['Departure Delay in Minutes'], inplace=True)
# fulldf['Arrival Delay in Minutes'] = fulldf['Arrival Delay in Minutes'].infer_objects()
# fulldf['Arrival Delay in Minutes'] = fulldf['Arrival Delay in Minutes'].fillna(fulldf['Departure Delay in Minutes'])
#

#fulldf['Arrival Delay in Minutes'].fillna(fulldf['Departure Delay in Minutes'], inplace = True).infer_objects()

# # Removing the departure delay in minutes - correlation is 0.96 - very high, no need for both as one follows mostly from the other
fulldf = fulldf.drop(['Departure Delay in Minutes', 'Arrival Delay in Minutes'], axis = 1)

# Saving data
fulldf.to_csv('data/data_processed.csv', encoding='utf-8')
#
