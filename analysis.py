import pandas as pd 
import numpy as np
autos=pd.read_csv('data.csv',encoding='Latin-1')
autos
autos.shape
autos.info()
autos.head()
autos.columns
autos.rename({'yearOfRegistration':'registration_year','monthOfRegistration':'registration_month','notRepairedDamage':
              'unrepaired_damage','dateCreated':'ad_created','dateCrawled':'date_crawled','vehicleType':'vehicle_type',
             'fuelType':'fule_type','nrOfPictures':'no_of_pictures','postalCode':'postal_code','lastSeen':'last_seen','offerType':
              'offer_type'},axis=1,inplace=True)
autos.columns
autos.describe(include='all')
autos['seller'].value_counts()
autos['offer_type'].value_counts()
autos.drop(['seller','offer_type'],axis=1,inplace=True)
autos['no_of_pictures'].head()
autos['no_of_pictures'].value_counts()
autos.drop(['no_of_pictures'],axis=1,inplace=True)
autos['price'].head()
autos['price']=autos['price'].str.replace('$','').str.replace(',','').astype(int)
autos['price'].dtype
autos['price'].head()
autos['odometer'].head()
autos['odometer']=autos['odometer'].str.replace(',','').str.replace('km','').astype(int)
autos['odometer'].head()
autos.rename({'odometer':'odometer_km'},axis=1,inplace=True)
autos['price'].unique()
autos['price'].unique().shape
autos['price'].value_counts().head(20)
autos['price'].value_counts().sort_index(ascending=False).head(20)
autos['price'].value_counts().sort_index().head(20)
autos['price'].describe(include='all')
autos=autos[autos['price'].between(1,350000)]
autos['price'].describe(include='all')
autos['odometer_km'].describe(include='all')
autos['odometer_km'].value_counts()
autos.columns
autos[['date_crawled' , 'registration_year' , 'registration_month' , 'ad_created' , 'last_seen']].describe(include='all')
autos[['date_crawled', 'ad_created' , 'last_seen']][:5]
autos['date_crawled'].str[:10][:5]
autos['date_crawled'].str[:10].value_counts(normalize=True,dropna=False).sort_index()
autos['ad_created'].str[:10].value_counts(normalize=True,dropna=False).sort_index()
autos['last_seen'].str[:10].value_counts(normalize=True,dropna=False).sort_index()
autos['registration_month'].describe()
autos['registration_year'].describe()
autos.loc[autos['registration_year']>=9999,'registration_year']
autos.loc[autos['registration_year']<=1000,'registration_year']
autos=autos[autos['registration_year'].between(1900,2016)]
autos['registration_year'].value_counts(normalize=True).head()
autos['brand'].value_counts(normalize=True)
autos['brand'].value_counts(normalize=True)[:4]*100
autos['brand'].value_counts(normalize=True)[:4].sum()*100
brand_counts = autos["brand"].value_counts(normalize=True)
common_brands = brand_counts[brand_counts > .05].index
print(common_brands)
brand_mean_prices={}
for brand in common_brands:
    brand_mean_prices[brand]= int(autos.loc[autos['brand']==brand,'price'].mean())
brand_mean_prices
autos['odometer_km'].value_counts(normalize=True)
mileage=autos['odometer_km'].value_counts(normalize=True)*100
mileage
brand_mean_mileage={}
for brand in common_brands:
    brand_mean_mileage[brand]=int(autos.loc[autos['brand']==brand,'odometer_km'].mean())
brand_mean_mileage
mean_prices=pd.Series(brand_mean_prices).sort_values(ascending=False)
print(mean_prices)
brand_info=pd.DataFrame(mean_prices,columns=['mean_price'])
brand_info
mean_mileage=pd.Series(brand_mean_mileage).sort_values(ascending=False)
print(mean_mileage)
pd.DataFrame(mean_mileage,columns=['mean_mileage'])
brand_info['mean_mileage']=mean_mileage
brand_info
