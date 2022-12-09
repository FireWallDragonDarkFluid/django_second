PoolArea = {
    'None': 0,
    '100': 100,
    '200':200,
    '300':300,
    '400':400,
    '500':500,
    '600':600,
    '700+':700,
}

LotArea = {
    ' less than 1,500': 2000,
    ' 1,500 to 10,000': 10000,
    ' 10,000 to 20,000':20000,
    ' 20,000 to 30,000':30000,
    ' 30,000 to 40,000':40000,
    ' 40,000 to 50,000':50000,
    ' 50,000 to 60,000':60000,
    ' 60,000 to 70,000':70000,
    ' 70,000 to 80,000':80000,
    ' 90,000 to 100,000':90000,
    '100,000 to 110,000':100000,
    '110,000 to 120,000':110000,
    '120,000 to 130,000':120000,
    '130,000 to 140,000':130000,
    '140,000 to 150,000':140000,
    '150,000 to 160,000':150000,
    '160,000 to 170,000':160000,
    '170,000 to 180,000':170000,
    '180,000 to 190,000':180000,
    '190,000 to 200,000':190000,
    '200,000+':200000
}

TotalBsmtSF = { 
    'None':0,
    '1,000':1000,
    '2,000':2000,
    '3,000':3000,
    '4,000':4000,
    '5,000':5000,
    '6,000+':6000
}

OverallQual = { 
    'Very Poor': 1,
    'Poor':2,
    'Fair':3, 
    'Below Average':4,
    'Average':5,
    'Above Average':6,
    'Good':7,
    'Very Good':8,
    'Excellent':9,
    'Very Excellent':10
}

price_to_sell = {
    '100000':'$100,000',
    '200000':'$200,000',
    '300000':'$300,000',
    '400000':'$400,000',
    '500000':'$500,000',
    '600000':'$600,000',
    '700000':'$700,000',
    '800000':'$800,000',
    '900000':'$900,000',
    '1000000':'$1M+'
}

### For RandomForest

MSZoning = {
    'Agriculture':'A', 
    'Commericial':'C',
    'Floating Village Residential':'FV',
    'Industrial':'I',
    'Residential Low Density':'RL',
    'Residential Low Density Park ':'RP',
    'Residential Medium Density':'RM',
    'Residential High Density':'RH'
}

Utilities = {
    'All public Utilities (E,G,W,& S)': 'AllPub',
    'Electricity, Gas, and Water (Septic Tank)': 'NoSewr',
    'Electricity and Gas Only': 'NoSeWa',
    'Electricity only': 'ELO'
}

LotConfig = {
    'Inside lot': 'Inside',
    'Corner lot': 'Corner',
    'Cul-de-sac': 'CulDSac',
    'Frontage on 2 sides of property': 'FR2',
    'Frontage on 3 sides of property': 'FR3'
}

HouseStyle = {
    'One story':'1Story',
    'One and one-half story: 2nd level finished':'1.5Fin',
    'One and one-half story: 2nd level unfinished':'1.5Unf',
    'Two story':'2Story',
    'Two and one-half story: 2nd level finished':'2.5Fin',
    'Two and one-half story: 2nd level unfinished':'2.5Unf',
    'Split Foyer':'SFoyer',
    'Split Level':'SLvl',
}

GarageType = {
    'More than one type of garage':'2Types',
    'Attached to home':'Attchd',
    'Basement Garage':'Basment',
    'Built-In (Garage part of house - typically has room above garage)':'BuiltIn',
    'Car Port':'CarPort',
    'Detached from home':'Detchd',
    'No Garage':'NA',
}

GarageCars = {
    '0':0,
    '1':1,
    '2':2,
    '3':3,
    '4+':4
}

GarageArea = {
    'None': 0,
    '200':200,
    '400':400,
    '600':600,
    '800':800,
    '1000':1000,
    '1200':1200,
    '1200+':1400
}

OpenPorchSF = {
    'None':0,
    '100':100,
    '200':200,
    '300':300,
    '400':400,
    '500+':500
}

EnclosedPorch = {
    'None': 0,
    '100': 100,
    '200': 200,
    '300': 300,
    '400': 400,
    '400+': 500
}


###
