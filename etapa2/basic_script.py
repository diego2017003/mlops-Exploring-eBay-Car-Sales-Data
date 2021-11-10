import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import docstring

def get_outlier(campo_series):
    quartil_1 = campo_series.quantile(0.25)
    mediana = campo_series.quantile(0.5)
    quartil_3 = campo_series.quantile(0.75)
    maximo = mediana + 1.5*(quartil_3-quartil_1)
    minimo = mediana - 1.5*(quartil_3-quartil_1)
    return maximo,minimo


def date_analyse(dados,campo):
    analise = (dados[campo].str[:10]
        .value_counts(normalize=True, dropna=False)
        .sort_index()
        )
    print(analise)


def correlacionar_campos_por_media(dados,filtro,campo_valor,campo_analise):
    dados_filtrados = dados.loc[filtro,[campo_analise,campo_valor]]
    dict_mean_campos = dados_filtrados.groupby([campo_analise],
    as_index=False)[campo_valor].mean()
    dict_mean_campos = dict_mean_campos.rename(columns=
            {str(campo_valor):'mean_'+str(campo_valor)})
    return dict_mean_campos


def analyse(dados,columns):
    numerical = dados.loc[:,columns]
    #visualização da heatmap
    plt.figure(figsize=(20,40))
    plt.subplot(2,1,1)
    plt.grid()
    corr = numerical.corr()
    sns.heatmap(data=corr,cmap='Reds',annot=True)
    #visualização de correlação po scatter plot
    plt.subplot(2,1,2)
    plt.grid()
    sns.pairplot(data=numerical)
    plt.show()

#Lendo os dados
autos = pd.read_csv('autos.csv', encoding='Latin-1')
#Renomeando as colunas
autos.columns = ['date_crawled','name','seller',
       'offer_type','price','ab_test',
       'vehicle_type','registration_year',
       'gearbox','power_ps', 'model',
       'odometer','registration_month',
       'fuel_type','brand',
       'unrepaired_damage','ad_created','num_photos','postal_code',
       'last_seen']
#Refatorando campos Numericos
autos['price'] = autos['price'].str.replace('$','').str.replace(',','').astype(int)
autos['odometer'] = autos['odometer'].str.replace('km','').str.replace(',','').astype(int)
autos=autos.rename(columns={'odometer':'odometer_km'})
max_price,min_price = get_outlier(autos.price)
#Retirando outliers
autos = autos.loc[autos['price']<=max_price,:]
#Renomeando valores em alemao
autos.offer_type=autos.offer_type.replace({'Angebot':'Offer','Gesuch':'Request'})
autos.vehicle_type=autos.vehicle_type.replace({'kleinwagen':'small car',
'kombi':'combi','cabrio':'convertible','andere':'other'})
autos.gearbox = autos.gearbox.replace({'manuell':'manual','automatik':'automatic'})
autos.fuel_type=autos.fuel_type.replace({'andere':'other','elektro':'electro','benzin':'petrol'})
autos.unrepaired_damage=autos.unrepaired_damage.replace({'nein':'no','ja':'yes'})
#Retirando colunas desnecessarias
autos = autos.drop(["num_photos", "seller", "offer_type"], axis=1)
#Pegando o top 20 marcas de carro
brand_top20_vector = autos["brand"].value_counts(normalize=True).keys()[0:20]
#Analisando preco por marca no top 20
filtro_brand = autos['brand'].isin(brand_top20_vector)
dict_price_mean = correlacionar_campos_por_media(autos,filtro_brand,'price','brand')
print(dict_price_mean)
#Analisando odometro por marca no top 20
dict_miliage_mean =correlacionar_campos_por_media(autos,filtro_brand,'odometer_km','brand')
print(dict_miliage_mean)
#Olhando preco e milhagem juntos
df_brand_price_miliage = pd.merge(dict_miliage_mean,dict_price_mean,on='brand',how='left')
#Ordenando pelo preço
df_brand_price_miliage = df_brand_price_miliage.sort_values(by='mean_price',
ascending=False,ignore_index=True)
print(df_brand_price_miliage)
