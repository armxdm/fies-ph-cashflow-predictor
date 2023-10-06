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

st.markdown("""<h2 style="text-align:center;">Filipino Family Income and Expenditure</h2>""", unsafe_allow_html = True)
heading2 = """
<div style="background:#6ba315; padding:3px">
<h3 style="color:white;text-align:center;">C&nbsp;&nbsp;A&nbsp;&nbsp;S&nbsp;&nbsp;H&nbsp;&nbsp;F&nbsp;&nbsp;L&nbsp;&nbsp;O&nbsp;&nbsp;W&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;P&nbsp;&nbsp;R&nbsp;&nbsp;E&nbsp;&nbsp;D&nbsp;&nbsp;I&nbsp;&nbsp;C&nbsp;&nbsp;T&nbsp;&nbsp;O&nbsp;&nbsp;R</h3>
</div>
"""
st.markdown(heading2, unsafe_allow_html = True)

st.markdown("""<span style="margin:auto; display:table; padding:5px"><i>by: Team Bashee</i></span>""", unsafe_allow_html = True)
st.image("https://www.syntellis.com/sites/default/files/images/2022-12/drivers-of-profitability.png")
st.divider()

#basic info
st.subheader("Basic Family Info")
familySize = st.number_input('👨‍👨‍👧‍👦 Family Size', 1, 21)
region = st.selectbox('🇵🇭 Region', region_mapping.values())
urbanRural = st.radio('', ['Urban', 'Rural'], horizontal=True)

st.divider()

st.subheader("Income")
col1, col2 = st.columns(2)
wages = col1.number_input('💼 Salaries/Wages')
netShare = col1.number_input('🌾 Net Share of Crops, Fruits, etc. (Tot. Net Value of Share)')
cashAbroad = col1.number_input('💵 Cash Receipts, Support, etc. from Abroad')
cashDomestic = col1.number_input('💰 Cash Receipts, Support, etc. from Domestic Source')
rentalsRec = col1.number_input('🏘️ Rentals Received from Non-Agri Lands, etc.')
interest = col1.number_input('💳 Interest')
pension = col1.number_input('👴 Pension and Retirement Benefits')
dividends = col2.number_input('🪙 Dividends from Investment')
otherSource = col2.number_input('📈 Other Sources of Income NEC')
netReceipt = col2.number_input('🧺 Family Sustenance Activities')
regft = col2.number_input('🎁 Total Received as Gifts')
eainc = col2.number_input('🏬 Total Income from Entrepreneurial Acitivites')
otherRec = col2.number_input('💲 Total Other Receipts')
pcinc = col2.number_input('📈 Per Capita Income')

st.divider()

#Expenditure
st.subheader("Expenditure")
col1, col2 = st.columns(2)
losses = col1.number_input('📉 Losses from EA')
bread = col1.number_input('🍞 Bread and Cereals')
meat = col1.number_input('🥩 Meat')
fish = col1.number_input('🐟 Fish and Seafood')
milk = col1.number_input('🥛 Milk, Cheese and Eggs')
oil = col1.number_input('🍶 Oils and Fats')
fruit = col1.number_input('🍉 Fruit')
veg = col1.number_input('🥦 Vegetables')
sugar = col1.number_input('🍫 Sugar, Jam and Honey, Chocolate and Confetionery')
foodNec = col1.number_input('🍟 Food Products Not Elsewhere Classified')
fruitVeg = col1.number_input('🥤Fruit and vegetable juices')
coffee = col1.number_input('☕️ Coffee')
tea = col1.number_input('🍵 Tea')
cocoa = col1.number_input('🍫 Cocoa drinks')
water = col1.number_input('💧 Mineral Water')
softdrinks = col1.number_input('🥃 Softdrinks')
othersNonAlcohol = col1.number_input('🧋Other Non Alcoholic Beverages')
alcohol = col1.number_input('🍻 Alcoholic Beverages')
tobacco = col1.number_input('🚬 Tobacco')
otherVeg = col1.number_input('🌽 Other Vegetable-Based Products')
servicesPrimaryGoods = col2.number_input('💻 Services Primary Goods')
alcoholProductionServices = col2.number_input('🍺 Alcohol Procduction Services')
foodOutside = col2.number_input('🍔 Food Regularly Consumed Outside The Home (Total)')
cloth = col2.number_input('👔 Clothing and Footwear')
furnishing = col2.number_input('🛋️ Furnishings and Routine Household Maintenance')
health = col2.number_input('🏥 Health')
housingWater = col2.number_input('🏠 Housing, Water, Electricity, Gas and Other Fuels')
actrent = col2.number_input('🏡 Actual House Rent')
imputedRent = col2.number_input('Imputed House Rental Value')
transport = col2.number_input('🚗 Transport')
communication = col2.number_input('📱 Communication')
recreation = col2.number_input('🎮 Recreation and Culture')
education = col2.number_input('🎓 Education')
insurance = col2.number_input('💲 Insurance')
misc = col2.number_input('🍿 Miscellaneous Goods and Services')
durable = col2.number_input('🛋️ Durable Furniture and Equipment')
occasion = col2.number_input('🎊 Special Family Occasion')
otherExpenditure = col2.number_input('📉 Other Expenditure (inc. Value Consumed, Losses)')
otherDisbursement = col2.number_input('💸 Other Disbursements')
foodAccomService = col2.number_input('🍜 Food Accommodation Services')


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
    data = {'FSIZE': familySize, 'WAGES': wages, 'NETSHARE': netShare, 'CASH_ABROAD': cashAbroad, 'CASH_DOMESTIC': cashDomestic, 'RENTALS_REC': rentalsRec, 
       'INTEREST': interest, 'PENSION': pension, 'DIVIDENDS': dividends, 'OTHER_SOURCE': otherSource, 'NET_RECEIPT': netReceipt, 'REGFT': regft, 'EAINC': eainc, 'LOSSES': losses, 
       'BREAD': bread, 'MEAT': meat, 'FISH': fish, 'MILK': milk, 'OIL': oil, 'FRUIT': fruit, 'VEG': veg, 'SUGAR': sugar, 'FOOD_NEC': foodNec,
       'FRUIT_VEG': fruitVeg, 'COFFEE': coffee, 'TEA': tea, 'COCOA': cocoa, 'WATER': water, 'SOFTDRINKS': softdrinks, 'OTHER_NON_ALCOHOL': othersNonAlcohol, 'ALCOHOL': alcohol, 
       'TOBACCO': tobacco, 'OTHER_VEG': otherVeg, 'SERVICES_PRIMARY_GOODS': servicesPrimaryGoods, 'ALCOHOL_PROCDUCTION_SERVICES': alcoholProductionServices, 'FOOD_OUTSIDE': foodOutside, 'CLOTH': cloth, 
       'FURNISHING': furnishing, 'HEALTH': health, 'HOUSING_WATER': housingWater, 'ACTRENT': actrent, 'IMPUTED_RENT': imputedRent, 'TRANSPORT': transport, 
       'COMMUNICATION': communication, 'RECREATION': recreation, 'EDUCATION': education, 'INSURANCE': insurance, 'MISCELLANEOUS': misc, 'DURABLE': durable, 
       'OCCASION': occasion, 'OTHER_EXPENDITURE': otherExpenditure, 'OTHER_DISBURSEMENT': otherDisbursement, 'FOOD_ACCOM_SRVC': foodAccomService, 'OTHREC': otherRec, 'PCINC': pcinc, 
       'W_REGN_1': checkRegion(1, region), 'W_REGN_10': checkRegion(10, region), 'W_REGN_11': checkRegion(11, region), 'W_REGN_12': checkRegion(12, region), 'W_REGN_13': checkRegion(13, region), 'W_REGN_14': checkRegion(14, region), 'W_REGN_15': checkRegion(15, region), 'W_REGN_16': checkRegion(16, region), 
       'W_REGN_17': checkRegion(17, region), 'W_REGN_2': checkRegion(2, region), 'W_REGN_3': checkRegion(3, region), 'W_REGN_4': checkRegion(4, region), 'W_REGN_5': checkRegion(5, region), 'W_REGN_6': checkRegion(6, region), 'W_REGN_7': checkRegion(7, region), 'W_REGN_8': checkRegion(8, region), 'W_REGN_9': checkRegion(9, region),
        'URB_1': checkUrbanRural(1, urbanRural), 'URB_2': checkUrbanRural(2, urbanRural)}

    print("data", data)
    df = pd.DataFrame(data, index=[0])
    prediction_num = model.predict(df)[0]
    pred_map = {0: 'Negative', 1: 'Positive'}
    prediction = pred_map[prediction_num]
    return prediction

if st.button("PREDICT", type="primary"):
    output = predict_cashflow(familySize, region, urbanRural, wages, netShare, cashAbroad, cashDomestic, rentalsRec, interest, pension, dividends, otherSource, netReceipt, regft, eainc, losses, bread, meat, fish, milk, oil, fruit, veg, sugar, foodNec, fruitVeg, coffee, tea, cocoa, water, softdrinks, othersNonAlcohol, alcohol, tobacco, otherVeg, servicesPrimaryGoods, alcoholProductionServices, foodOutside, cloth, furnishing, health, housingWater, actrent, imputedRent, transport, communication, recreation, education, insurance, misc, durable, occasion, otherExpenditure, otherDisbursement, foodAccomService, otherRec, pcinc)

    if output == 'Positive':
        st.success('The family will have positive cashflow.', icon="📈")
    elif output == 'Negative':
        st.error('The family will have negative cashflow.', icon="📉")

st.divider()
st.markdown("<b>Dataset:</b> <i>Family Income and Expenditure Survey 2021 by Philippine Statistics Authority </i>", unsafe_allow_html = True)
