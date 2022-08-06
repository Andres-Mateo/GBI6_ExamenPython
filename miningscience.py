# Nombre: Andres, Benalcazar
#Librerias 
import Bio
from Bio.Seq import Seq
from Bio import Entrez
import re

#obtencion de datos (documentos relacionados con la palabra ) 10**5
def download_pubmed(keyword):
    """"La funcion download_pubmed se encarga de rescatar la id de los documentos que esten relacionados con la keyword que se envio en la base de datos de pubmed """
    Entrez.email = "andres.benalcazar@est.ikiam.edu.ec"
handle = Entrez.esearch(db="pubmed", 
                        term="keyword]",
                        usehistory="y")
record = Entrez.read(handle)
id_list = record["IdList"]
record["Count"]
results1 = record



def science_plots(tipo):
    """"La función de science_plots se encarga de filtrar la data dependiendo de la variable (tipo) que se envió pudiendo ser esta DP AU o AD , los datos  PMID para la extracción de documentos se obtienen gracias a la función download_pubmed que busca los documentos exactos basados en su ID   """
    #--------------------------Uso del metodo download_pubmed---------------------------------------
    results = download_pubmed('Bacullus cereus') #Se usa el metodo download_pubmed para obtener los documentos con una keyword  
    #-----------------------------------------------------------------------------------------------
    
    id_list = results['IdList']                                                  #separamos ids    
    ids = ','.join(id_list)    
    Entrez.email = 'andres.benalcazar@est.ikiam.edu.ec'
    handle = Entrez.efetch(db='pubmed',rettype='medline',retmode='text',id=ids)  #rescatamos ducumentos por id
    all_data = handle.read()                                                     #se lee la data
    
    if(tipo == "DP"):#PMID y DP_year 
        zipcodes = re.findall(r'PMID-.(.+)', all_data)
        zipcodes1 = re.findall(r'DP  -.(.+)', all_data)
        all_ = list(zip(zipcodes,zipcodes1))
        nom_colum = ['PMID','DP_year']
    else:
            
        if(tipo == "AD"):#country y el num_auth
            zipcodes = re.findall(r'PL  -.(.+)|(AU)  -|', all_data)
            nom_colum = ['country','num_auth']
        mira = list()
        for x in zipcodes:
            if(x[0]!=''):
                mira.append((x[0],''))
            elif(x[1]!=''):
                mira.append(('',x[1]))
        zipcodes= mira       
        lista_1 = list()
        lista_2 = list()
        va_c = 0
        for y in zipcodes:
            if(y[0] !=''):
                x_0 = y[0]
                lista_1.append(y[0])
                if(va_c != 0):
                    lista_2.append(va_c)
                    va_c = 0
            else:
                va_c = va_c+1            
        all_ = list(zip(lista_1,lista_2))
        
    results = pd.DataFrame(all_,columns = nom_colum)             

#seccion de ejecicion de codigo y envio de variables
#id_list = results['IdList']          #separamos ids 
if __name__ == '__main__':
 #--------------------------Se ingresa la varaible tipo para iniciar---------------------------------------
    #resultado_final = mining_pubs("AU")  #Enviamos el tipo para el procesamiento ER (DP AU AD)  
#---------------------------------------------------------------------------------------------------------
    print("El nombre de la la funcion es:",download_pubmed.__name__ )
    print("Documentacion de la funcion :",download_pubmed.__doc__)
    print("__________________________________")
    print("El nombre de la la funcion es:",science_plots.__name__ )
    print("Documentacion de la funcion :",science_plots.__doc__)
