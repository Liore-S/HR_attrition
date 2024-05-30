import cudf
import pickle
import os

def feature_engineering(df):
    df['FirstJob'] = (df['YearsAtCompany'] == 0).astype('int')
    df['JuniorRole'] = (df['YearsInCurrentRole'] <= 2).astype('int')
    df['AvgSalaryRole'] = df['MonthlyIncome'] > df.groupby('JobRole')['MonthlyIncome'].transform('mean').astype('int')
    df['AvgSalaryRole'] = df['AvgSalaryRole'].astype('int')
    return df

def predict_attrition(data, model, features, scaler):
    # Load the model
    model = pickle.load(open(model, 'rb'))
    
    # Load the selected features
    with open(features, 'rb') as f:
        selected_num_features, selected_cat_features = pickle.load(f)
    selected_num_features = selected_num_features[1:]
    
    # Load scaler
    with open(scaler, 'rb') as f:
        scaler = pickle.load(f)
        
    # Load the data
    data = cudf.read_csv(data)
    print('Data loaded')
    
    # Feature engineering
    data = feature_engineering(data)
    print('Feature engineering done')
    
    # Drop columns
    data = data.drop(columns=['EmployeeCount','DailyRate', 'HourlyRate', 'MonthlyRate', 'Over18', 'StandardHours'])
    print('Columns dropped')
    
    # pick only null rows
    data_null = data[data['Attrition'].isnull()]
    data_null_id = data_null['EmployeeId'].reset_index(drop=True)
    data_null.reset_index(drop=True, inplace=True)
    
    # columns list
    ori_col_list = data.columns
    
    # select only selected features
    data_pred = data_null[selected_num_features + selected_cat_features].copy()
    col_list = selected_num_features + selected_cat_features
    
    # Encode categorical features
    decode = {}
    data_pred[selected_cat_features] = data_pred[selected_cat_features].astype('category')
    for feature in selected_cat_features:
        decode[feature] = {code: category for code, category in enumerate(data_pred[feature].cat.categories.to_pandas())}
        data_pred[feature] = data_pred[feature].cat.codes
    print('Categorical features encoded')
        
    # Scaling numeric columns with standard scaler
    data_pred_num = data_pred[selected_num_features]
    data_pred_num = scaler.transform(data_pred_num)
    print('Numeric features scaled')
    
    # Combine scaled numeric and categorical columns
    data_pred = cudf.concat([data_pred_num, data_pred[selected_cat_features]], axis=1)
    data_pred.columns = col_list
    print('Combined scaled numeric and categorical columns')
    
    # Predict
    prediction = model.predict(data_pred)
    print('Prediction done')
    
    # Create a new dataframe with the prediction
    data_pred['AttritionPred'] = prediction
    
    # inverse transform
    data_pred[selected_num_features] = scaler.inverse_transform(data_pred[selected_num_features])
    data_pred = data_pred.to_pandas()
    for feature in selected_cat_features:
        data_pred[feature] = data_pred[feature].astype('int').apply(lambda x: decode[feature][x] if x in decode[feature] else x)
    data_pred = cudf.DataFrame(data_pred)
    print('Inverse transform done')
    
    # combine with original columns
    # loop through original columns and remove duplicates columns except attrition
    for col in ori_col_list:
        if col in data_pred.columns:
            data_pred = data_pred.drop(columns=[col])
    data_pred = cudf.concat([data_null, data_pred], axis=1)
    
    #fill attrition with attritionpred
    data_pred['Attrition'] = data_pred['AttritionPred']
    data_pred = data_pred.drop(columns=['AttritionPred'])
    print('Attrition filled')
    
    # combine with original data
    data = data.dropna(subset=['Attrition'])
    data = cudf.concat([data, data_pred], axis=0)
    data = data.sort_values(by='EmployeeId').reset_index(drop=True)

    return data

# Path list
data = 'csv/employee_data.csv'
model = 'model/attrition_model.pkl'
features = 'model/selected_features.pkl'
scaler = 'model/scaler.pkl'

os.system('nvidia-smi -L')
predicted_data = predict_attrition(data, model, features, scaler)
print('Saving predicted data...')

# Save the predicted data
file_name = 'model/employee_data_predicted.csv'
predicted_data.to_csv(file_name, index=False)
print('Predicted data saved')
print('File name:', file_name)