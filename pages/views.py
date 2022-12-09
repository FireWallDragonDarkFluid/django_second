from django.shortcuts import render
from . import choices

### For ML
import os 
import numpy as np 
import pandas as pd 
from sklearn.ensemble import RandomForestClassifier
from sklearn.cluster import KMeans
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import Ridge, RidgeCV, ElasticNet, LassoCV, LassoLarsCV
from sklearn.model_selection import cross_val_score
###

csv_filename = os.path.join(os.path.dirname(__file__), 'train.csv')
a = ["KMeans"]

def index(request):
    a[0] = "KMeans"
    context = {
        'PoolArea': choices.PoolArea, 
        'LotArea': choices.LotArea, 
        'TotalBsmtSF': choices.TotalBsmtSF,
        'OverallQual': choices.OverallQual,
        'Price_to_sell': choices.price_to_sell
    }
    return render(request, 'pages/index.html', context) 

def about(request):
    return render(request, 'pages/about.html')

def forest(request):
    a[0] = "RandomForest"
    context = {
        'PoolArea': choices.PoolArea, 
        'LotArea': choices.LotArea, 
        'TotalBsmtSF': choices.TotalBsmtSF,
        'OverallQual': choices.OverallQual,
        'Price_to_sell': choices.price_to_sell
    }
    return render(request, 'pages/forest.html', context) 

def lassocv(request):
    a[0] = "LassoCV"
    context = {
        'TotalBsmtSF': choices.TotalBsmtSF,  
        'OpenPorchSF': choices.OpenPorchSF, 
        'GarageCars': choices.GarageCars, 
        'PoolArea': choices.PoolArea,
        'OverallQual': choices.OverallQual,
    }
    return render(request, 'pages/lassocv.html', context)    

def search(request):
    if a[0] == "KMeans":
        print("It's",a[0],"mode")
        train_df = pd.read_csv(csv_filename)
        features = ['LotArea', 'PoolArea', 'TotalBsmtSF', 'OverallQual', 'SalePrice']
        X = train_df[features]
        model = KMeans(n_clusters=8, random_state=42)
        model.fit(X)
        LotArea = 0
        PoolArea = 0 
        TotalBsmtSF = 0
        OverallQual = 0
        SalePrice = 0
        if 'price' in request.GET:
            SalePrice = request.GET['price']
        if 'quality' in request.GET:
            OverallQual = request.GET['quality']
        if 'pool' in request.GET:
            PoolArea = request.GET['pool']
        if 'LotArea' in request.GET:
            LotArea = request.GET['LotArea']
        if 'basement' in request.GET:
            TotalBsmtSF = request.GET['basement']
        tmp = {'LotArea': LotArea, 'PoolArea': PoolArea, 'TotalBsmtSF': TotalBsmtSF, 'OverallQual': OverallQual, 'SalePrice': SalePrice}
        response = pd.DataFrame(data=tmp, index=[0])
        preds = model.predict(response)[0]
        if preds == 0:
            preds = 'Agriculture'
        elif preds == 1:
            preds = 'Commercial'
        elif preds == 2:
            preds = 'Floating Village Residential' 
        elif preds == 3:
            preds = 'Industrial'
        elif preds == 4:
            preds = 'Residential High Density'
        elif preds == 5:
            preds = 'Residential Low Density'
        elif preds == 6:
            preds = 'Residential Low Density Park'
        elif preds == 7:
            preds = 'Residential Medium Density'
        context = {
            'type':'KMeans', 
            'preds': preds
        }
        print(preds[0])
        return render(request, 'pages/search.html',context)
    elif a[0] == "RandomForest":
        print("It's",a[0],"mode")
        train_df = pd.read_csv(csv_filename)
        features = ['LotArea', 'PoolArea', 'TotalBsmtSF', 'OverallQual', 'SalePrice']
        X = train_df[features]
        y = train_df["MSZoning"]
        ### Initialize variables
        LotArea = 0
        PoolArea = 0 
        TotalBsmtSF = 0
        OverallQual = 0
        SalePrice = 0
        ########################
        ### Get request variables
        if 'price' in request.GET:
            SalePrice = request.GET['price']
        if 'quality' in request.GET:
            OverallQual = request.GET['quality']
        if 'pool' in request.GET:
            PoolArea = request.GET['pool']
        if 'LotArea' in request.GET:
            LotArea = request.GET['LotArea']
        if 'basement' in request.GET:
            TotalBsmtSF = request.GET['basement']
        ########################
        ### Model
        model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
        model.fit(X, y)
        ########################
        ### Predict
        receive_msg = {'LotArea': LotArea, 'PoolArea': PoolArea, 'TotalBsmtSF': TotalBsmtSF, 'OverallQual': OverallQual, 'SalePrice': SalePrice}
        msg_transformed = pd.DataFrame(data=receive_msg, index=[0])
        preds = model.predict(msg_transformed)[0]
        if preds == 'A':
            preds = 'Agriculture'
        elif preds == 'C':
            preds = 'Commercial'
        elif preds == 'FV':
            preds = 'Floating Village Residential' 
        elif preds == 'I':
            preds = 'Industrial'
        elif preds == 'RH':
            preds = 'Residential High Density'
        elif preds == 'RL':
            preds = 'Residential Low Density'
        elif preds == 'RP':
            preds = 'Residential Low Density Park'
        elif preds == 'RM':
            preds = 'Residential Medium Density'
        context = {
            'type':'forest',
            'preds': preds
        }
        print(preds)
        ########################
        return render(request, 'pages/search.html', context)
        
    elif a[0] == "LassoCV":
        print("It's",a[0],"mode")
        train_df = pd.read_csv(csv_filename)
        features = ['TotalBsmtSF', 'OpenPorchSF', 'GarageCars', 'PoolArea', 'OverallQual']
        X = train_df[features]
        train_df["SalePrice"] = np.log1p(train_df["SalePrice"])
        y = train_df.SalePrice
        ### Initialize variables
        TotalBsmtSF = 0
        OpenPorchSF = 0 
        GarageCars = 0
        PoolArea = 0
        OverallQual = 0
        ########################
        ### Get request variables
        if 'TotalBsmtSF' in request.GET:
            TotalBsmtSF = request.GET['TotalBsmtSF']
        if 'OpenPorchSF' in request.GET:
            OpenPorchSF = request.GET['OpenPorchSF']
        if 'GarageCars' in request.GET:
            GarageCars = request.GET['GarageCars']
        if 'PoolArea' in request.GET:
            PoolArea = request.GET['PoolArea']
        if 'OverallQual' in request.GET:
            OverallQual = request.GET['OverallQual']
        ########################
        ### Model
        model = LassoCV(alphas = [1, 0.1, 0.001, 0.0005]).fit(X, y)
        model.fit(X, y)
        ########################
        ### Predict
        receive_msg = {'TotalBsmtSF': TotalBsmtSF, 'OpenPorchSF': OpenPorchSF, 'GarageCars': GarageCars, 'PoolArea': PoolArea, 'OverallQual': OverallQual}
        msg_transformed = pd.DataFrame(data=receive_msg, index=[0])
        preds = model.predict(msg_transformed) 
        number_preds = int(np.expm1(preds))
        if len(str(int(np.expm1(preds)[0]))) > 6:
            preds = str(int(np.expm1(preds)[0])//1000000) + ',' +  str((int(np.expm1(preds)[0])-1000000) //1000) + ',' + str(int(np.expm1(preds)[0])%1000)
        else:
            preds = str(int(np.expm1(preds)[0])//1000) + ',' + str(int(np.expm1(preds)[0])%1000)
        context = {
            'type':'lassocv',
            'preds':'$ '+preds,
            'number_preds': number_preds
        }
        print(preds)
        ########################
        return render(request, 'pages/search.html',context)
