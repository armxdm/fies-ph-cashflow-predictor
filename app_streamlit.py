# General Libraries
import pickle
import pandas as pd

# Model deployment
import streamlit as st

model = pickle.load(open('ml_model.pkl', 'rb'))

region_mapping = {
        13: 'National Capital Region',
        14: 'Cordillera Administrative Region',
        1: 'Region I - Ilocos Region',
        2: 'Region II - Cagayan Valley',
        3: 'Region III - Central Luzon',
        4: 'Region IVA - CALABARZON',
        17: 'Region IVB - MIMAROPA',
        5: 'Region V- Bicol',
        6: 'Region VI - Western Visayas',
        7: 'Region VII - Central Visayas',
        8: 'Region VIII - Eastern Visayas',
        9: 'Region IX - Zamboanga Peninsula',
        10: 'Region X - Northern Mindanao',
        11: 'Region XI - Davao',
        12: 'Region XII - SOCCSKSARGEN',
        16: 'Region XIII - Caraga',
        15: 'Autonomous Region in Muslim Mindanao'
    }

urban_mapping = {
        1: 'Urban',
        2: 'Rural'
    }

st.markdown("""<h1 style="text-align:center;">Family Income and Expenditures</h1>""", unsafe_allow_html = True)
heading2 = """
<div style="background:#487307 ;padding:10px">
<h2 style="color:white;text-align:center;">Cashflow Predictor</h2>
</div>
"""
st.markdown(heading2, unsafe_allow_html = True)
st.image("https://www.syntellis.com/sites/default/files/images/2022-12/drivers-of-profitability.png")
st.divider()

#basic info
st.subheader("Basic Info")

#family size
familySize = st.number_input('👨‍👨‍👧‍👦 Family Size', 1, 10)
region = st.selectbox('🇵🇭 Region', region_mapping.values())
urbanRural = st.radio('', ['Urban', 'Rural'], horizontal=True)

st.divider()
#Income
st.subheader("Income")
wages = st.number_input('💼 Salaries/Wages')
netShare = st.number_input('🌾 Net Share of Crops, Fruits, etc. (Tot. Net Value of Share)')
cashAbroad = st.number_input('💵 Cash Receipts, Support, etc. from Abroad')
cashDomestic = st.number_input('💰 Cash Receipts, Support, etc. from Domestic Source')
rentalsRec = st.number_input('🏘️ Rentals Received from Non-Agri Lands, etc.')
interest = st.number_input('💳 Interest')
pension = st.number_input('👴 Pension and Retirement Benefits')
dividends = st.number_input('🪙 Dividends from Investment')
otherSource = st.number_input('📈 Other Sources of Income NEC')
netReceipt = st.number_input('🧺 Family Sustenance Activities')
regft = st.number_input('🎁 Total Received as Gifts')
eainc = st.number_input('🏬 Total Income from Entrepreneurial Acitivites')
otherRec = st.number_input('💲 Total Other Receipts')
pcinc = st.number_input('📈 Per Capita Income')

st.divider()
#Expenditure
st.subheader("Expenditures")
losses = st.number_input('📉 Losses from EA')
bread = st.number_input('🍞 Bread and Cereals')
meat = st.number_input('🥩 Meat')
fish = st.number_input('🐟 Fish and Seafood')
milk = st.number_input('🥛 Milk, Cheese and Eggs')
oil = st.number_input('🍶 Oils and Fats')
fruit = st.number_input('🍉 Fruit')
veg = st.number_input('🥦 Vegetables')
sugar = st.number_input('🍫 Sugar, Jam and Honey, Chocolate and Confetionery')
foodNec = st.number_input('🍟 Food Products Not Elsewhere Classified')
fruitVeg = st.number_input('🥤Fruit and vegetable juices')
coffee = st.number_input('☕️ Coffee')
tea = st.number_input('🍵 Tea')
cocoa = st.number_input('🍫 Cocoa drinks')
water = st.number_input('💧 Mineral Water')
softdrinks = st.number_input('🥃 Softdrinks')
othersNonAlcohol = st.number_input('🧋Other Non Alcoholic Beverages')
alcohol = st.number_input('🍻 Alcoholic Beverages')
tobacco = st.number_input('🚬 Tobacco')
otherVeg = st.number_input('🌽 Other Vegetable-Based Products')
servicesPrimaryGoods = st.number_input('💻 Services Primary Goods')
alcoholProductionServices = st.number_input('🍺 Alcohol Procduction Services')
foodOutside = st.number_input('🍔 Food Regularly Consumed Outside The Home (Total)')
cloth = st.number_input('👔 Clothing and Footwear')
furnishing = st.number_input('🛋️ Furnishings and Routine Household Maintenance')
health = st.number_input('🏥 Health')
housingWater = st.number_input('🏠 Housing, Water, Electricity, Gas and Other Fuels')
actrent = st.number_input('🏡 Actual House Rent')
imputedRent = st.number_input('Imputed House Rental Value')
transport = st.number_input('🚗 Transport')
communication = st.number_input('📱 Communication')
recreation = st.number_input('🎮 Recreation and Culture')
education = st.number_input('🎓 Education')
insurance = st.number_input('💲 Insurance')
misc = st.number_input('🍿 Miscellaneous Goods and Services')
durable = st.number_input('🛋️ Durable Furniture and Equipment')
occasion = st.number_input('🎊 Special Family Occasion')
otherExpenditure = st.number_input('📉 Other Expenditure (inc. Value Consumed, Losses)')
otherDisbursement = st.number_input('💸 Other Disbursements')
foodAccomService = st.number_input('🍕 Food Regularly Consumed Outside The Home - Accomodation Services')


def checkRegion(regionCode, regionName):
    if (regionName == region_mapping[regionCode]):
        return 1
    else:
        return 0

def checkUrbanRural(urbanRural, value):
    if(value == urban_mapping[urbanRural]):
        return 1
    else:
        return 0

def predict_cashflow(familySize, 
                    region, 
                    urbanRural, 
                    wages, 
                    netShare, 
                    cashAbroad, 
                    cashDomestic, 
                    rentalsRec, 
                    interest, 
                    pension, 
                    dividends, 
                    otherSource,
                    netReceipt, 
                    regft, 
                    eainc, 
                    losses, 
                    bread, 
                    meat, 
                    fish, 
                    milk, 
                    oil,
                    fruit, 
                    veg, 
                    sugar, 
                    foodNec, 
                    fruitVeg, 
                    coffee, 
                    tea, 
                    cocoa, 
                    water, 
                    softdrinks, 
                    othersNonAlcohol, 
                    alcohol, 
                    tobacco, 
                    otherVeg, 
                    servicesPrimaryGoods, 
                    alcoholProductionServices, 
                    foodOutside, 
                    cloth, 
                    furnishing, 
                    health, 
                    housingWater, 
                    actrent, 
                    imputedRent, 
                    transport, 
                    communication, 
                    recreation, 
                    education, 
                    insurance, 
                    misc, 
                    durable, 
                    occasion, 
                    otherExpenditure, 
                    otherDisbursement, 
                    foodAccomService, 
                    otherRec,
                    pcinc):
    # sample = [{'FSIZE': 6.5, 'WAGES': 290000, 'NETSHARE': 0, 'CASH_ABROAD': 0, 'CASH_DOMESTIC': 340000, 'RENTALS_REC': 0, 
    #    'INTEREST': 0, 'PENSION': 0, 'DIVIDENDS': 0, 'OTHER_SOURCE': 0, 'NET_RECEIPT': 480, 'REGFT': 21460, 'EAINC': 0, 'LOSSES': 0, 
    #    'BREAD': 37359, 'MEAT': 43748, 'FISH': 15988, 'MILK': 12146, 'OIL': 3445, 'FRUIT': 8450, 'VEG': 18160, 'SUGAR': 3171, 'FOOD_NEC': 4452,
    #    'FRUIT_VEG': 9440, 'COFFEE': 2306, 'TEA': 0, 'COCOA': 0, 'WATER': 4550, 'SOFTDRINKS': 4290, 'OTHER_NON_ALCOHOL': 0, 'ALCOHOL': 0, 
    #    'TOBACCO': 0, 'OTHER_VEG': 0, 'SERVICES_PRIMARY_GOODS': 0, 'ALCOHOL_PROCDUCTION_SERVICES': 0, 'FOOD_OUTSIDE': 13000, 'CLOTH': 4796, 
    #    'FURNISHING': 3418, 'HEALTH': 5688, 'HOUSING_WATER': 75300, 'ACTRENT': 0, 'IMPUTED_RENT': 48000, 'TRANSPORT': 19140, 
    #    'COMMUNICATION': 16794, 'RECREATION': 2849, 'EDUCATION': 12000, 'INSURANCE': 12000, 'MISCELLANEOUS': 12264, 'DURABLE': 0, 
    #    'OCCASION': 5000, 'OTHER_EXPENDITURE': 650, 'OTHER_DISBURSEMENT': 0, 'FOOD_ACCOM_SRVC': 0, 'OTHREC': 0, 'PCINC': 107683.08, 
    #    'W_REGN_1': 1, 'W_REGN_10': 0, 'W_REGN_11': 0, 'W_REGN_12': 0, 'W_REGN_13': 0, 'W_REGN_14': 0, 'W_REGN_15': 0, 'W_REGN_16': 0, 
    #    'W_REGN_17': 0, 'W_REGN_2': 0, 'W_REGN_3': 0, 'W_REGN_4': 0, 'W_REGN_5': 0, 'W_REGN_6': 0, 'W_REGN_7': 0, 'W_REGN_8': 0, 'W_REGN_9': 0,
    #     'URB_1': 0, 'URB_2': 1}]
    data = [{'FSIZE': familySize, 'WAGES': wages, 'NETSHARE': netShare, 'CASH_ABROAD': cashAbroad, 'CASH_DOMESTIC': cashDomestic, 'RENTALS_REC': rentalsRec, 
       'INTEREST': interest, 'PENSION': pension, 'DIVIDENDS': dividends, 'OTHER_SOURCE': otherSource, 'NET_RECEIPT': netReceipt, 'REGFT': regft, 'EAINC': eainc, 'LOSSES': losses, 
       'BREAD': bread, 'MEAT': meat, 'FISH': fish, 'MILK': milk, 'OIL': oil, 'FRUIT': fruit, 'VEG': veg, 'SUGAR': sugar, 'FOOD_NEC': foodNec,
       'FRUIT_VEG': fruitVeg, 'COFFEE': coffee, 'TEA': tea, 'COCOA': cocoa, 'WATER': water, 'SOFTDRINKS': softdrinks, 'OTHER_NON_ALCOHOL': othersNonAlcohol, 'ALCOHOL': alcohol, 
       'TOBACCO': tobacco, 'OTHER_VEG': otherVeg, 'SERVICES_PRIMARY_GOODS': servicesPrimaryGoods, 'ALCOHOL_PROCDUCTION_SERVICES': alcoholProductionServices, 'FOOD_OUTSIDE': foodOutside, 'CLOTH': cloth, 
       'FURNISHING': furnishing, 'HEALTH': health, 'HOUSING_WATER': housingWater, 'ACTRENT': actrent, 'IMPUTED_RENT': imputedRent, 'TRANSPORT': transport, 
       'COMMUNICATION': communication, 'RECREATION': recreation, 'EDUCATION': education, 'INSURANCE': insurance, 'MISCELLANEOUS': misc, 'DURABLE': durable, 
       'OCCASION': occasion, 'OTHER_EXPENDITURE': otherExpenditure, 'OTHER_DISBURSEMENT': otherDisbursement, 'FOOD_ACCOM_SRVC': foodAccomService, 'OTHREC': otherRec, 'PCINC': pcinc, 
       'W_REGN_1': checkRegion(1, region), 'W_REGN_10': checkRegion(10, region), 'W_REGN_11': checkRegion(11, region), 'W_REGN_12': checkRegion(12, region), 'W_REGN_13': checkRegion(13, region), 'W_REGN_14': checkRegion(14, region), 'W_REGN_15': checkRegion(15, region), 'W_REGN_16': checkRegion(16, region), 
       'W_REGN_17': checkRegion(17, region), 'W_REGN_2': checkRegion(2, region), 'W_REGN_3': checkRegion(3, region), 'W_REGN_4': checkRegion(4, region), 'W_REGN_5': checkRegion(5, region), 'W_REGN_6': checkRegion(6, region), 'W_REGN_7': checkRegion(7, region), 'W_REGN_8': checkRegion(8, region), 'W_REGN_9': checkRegion(9, region),
        'URB_1': checkUrbanRural(1, urbanRural), 'URB_2': checkUrbanRural(2, urbanRural)}]

    print("data", data)
    df = pd.DataFrame(data)
    prediction_num = model.predict(df)[0]
    print("prediction num", prediction_num)
    pred_map = {0: 'Negative', 1: 'Positive'}
    prediction = pred_map[prediction_num]
    return prediction

st.markdown("<style>button {background-color: #487307;text-align: center;}</style>" ,unsafe_allow_html = True)
if st.button("Predict"):
    output = predict_cashflow(familySize, region, urbanRural, wages, netShare, cashAbroad, cashDomestic, rentalsRec, interest, pension, dividends, otherSource, netReceipt, regft, eainc, losses, bread, meat, fish, milk, oil, fruit, veg, sugar, foodNec, fruitVeg, coffee, tea, cocoa, water, softdrinks, othersNonAlcohol, alcohol, tobacco, otherVeg, servicesPrimaryGoods, alcoholProductionServices, foodOutside, cloth, furnishing, health, housingWater, actrent, imputedRent, transport, communication, recreation, education, insurance, misc, durable, occasion, otherExpenditure, otherDisbursement, foodAccomService, otherRec, pcinc)

    if output == 'Positive':
        st.success('The family will have positive cashflow.', icon="📈")
    elif output == 'Negative':
        st.error('The family will have negative cashflow.', icon="📉")


