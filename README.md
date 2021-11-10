# Exploring-eBay-Car-Sales-Data
Este repositório tem por objetivo mostrar a solução do projeto guiado "Exploring eBay Car Sales Data"
proposto pelo módulo pandas e numpy dentro do dataquest. O projeto conta com duas etapas: 
  
    * Etapa 1: diz respeito à criação de um jupyter notebook com a análise exploratória dos dados de automóveis do ebay alemão.
      
        ### Detalhes do dataset
        O dataset se trata de um conjunto de dados sobre carros usados encontrados em um site do Ebay da Alemanha. 
        São 50000 registros e 20 colunas e as descrições em        
        inglês são:
    
        1. dateCrawled - When this ad was first crawled. All field-values are taken from this date.
    
        2. name - Name of the car.
        
        3. seller - Whether the seller is private or a dealer.
        
        4. offerType - The type of listing
        
        5. price - The price on the ad to sell the car.
        
        6. abtest - Whether the listing is included in an A/B test.
        
        7. vehicleType - The vehicle Type.
       
        8. yearOfRegistration - The year in which the car was first registered.
        
        9. gearbox - The transmission type.
    
        10. powerPS - The power of the car in PS.
        
        11. model - The car model name.
        
        12. kilometer - How many kilometers the car has driven.
        
        13. monthOfRegistration - The month in which the car was first registered.
    
        14. fuelType - What type of fuel the car uses.
    
        15. brand - The brand of the car.
    
        16. notRepairedDamage - If the car has a damage which is not yet repaired.
    
        17. dateCreated - The date on which the eBay listing was created.
        
        18. nrOfPictures - The number of pictures in the ad.
        
        19. postalCode - The postal code for the location of the vehicle.
        
        20. lastSeenOnline - When the crawler saw this ad last online.

     2. Nessa etapa iremos tratar de extrair, limpar e tranformar os dados para que 
     fiquem próprios para uso e análise. Após a limpeza será feita uma análise
     Sobre alguns campos e suas correlações para gerar insigths a respeito de preços 
     e o quanto os valores se relacionam.
     * Bônus: Foi inserida uma função chamda analyse que faz o plot da correlação com mapa de calor 
     e um pairplot utilizando o módulo seaborn para gráficos.
     
    *Etapa 2: Condesamos e adaptamos o código para um script python no intuito de aplicar a ferramenta pylint. 
    A ferramenta pylint foi utilizada para testarmos os conceitos de código limpo. O script teve score 9.02
    devido a falha no módulo docstring.  O script não possui todas as funcionalidade de análise do notebook 
    entretanto foi feita uma daptação de alguns blocos de código para funções.  
    
    
