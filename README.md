# Caracterización de señales eléctricas (Electrical load profiling)

Actualmente, con la creciente integración de sensores en las máquinas y sistemas eléctricos se están recolectando datos que antes no se tenían, estos datos abren un nuevo paradigma para el análisis de la información inherente de los sistemas, que pueden ser empleados y explotados en el análisis exploratorio para la toma de decisiones en distintos campos de aplicación como pueden ser: la predicción de la demanda, detección de disturbios y caracterización de los perfiles de carga eléctrica.


# Análisis EDA (Exploratory data analysis)

Se observa que existentes tendencias de comportamiento en el consumo diario entre los distintos clientes que permiten naturalmente agrupar los datos, se debe tener en cuenta un proceso de normalización a fin de evitar el agrupamiento por escalas de consumo y aprovechar la dinámica de la señal para poder emplear esa información en determinar el comportamiento en el tiempo (t + 1), con el histórico de información funcionando como buffer o clases a priori de comportamiento.

# Integración de Streamlit con Altair

Se integra Streamlit al código del análisis EDA con la librería Altair para gráficos interactivos, con esto podremos compartir los resultados del análisis de forma interactiva. Streamlit es un framework open-source que permite crear aplicaciones de forma sencilla y rápida.

![](results/Altair%20clusters/Altair_Cluster_7.png)
Imagen que muestra la distribución de los datos del clúster 7 con Altair desde la aplicación de Streamlit.

# Estructura de repositorio (Repository structure)

La estructura que queremos que tenga este repositorio es la siguiente:

    ├── data                                          <- Carpeta que contiene la base de datos que se utilizó para el análisis EDA.
    │   ├── README.md                                 <- Descripción general de esta información.
    │   └── summer.csv                                <- Dataset utilizado para el desarrollo del proyecto.
    │
    ├── doc                                           <- Carpeta con el archivo markdown con el avance realizado sobre (i) la problemática, (ii) el objetivo y (iii) la justificación.   
    |   └── README.md                                 <- Descripción general de la tesis: (i) la problemática, (ii) el objetivo y (iii) la justificación.
    |  
    ├── results                                       <- Carpeta con el archivo README.md y los resultados del análisis EDA realizado.
    |   ├── Altair clusters                           <- Carpeta con las gráficas resultantes realizadas con Altair.
    |   |    ├── Streamlit_Cluster_0.png              <- Imagen que muestra la distribución del clúster 0 con Altair.
    |   |    ├── Streamlit_Cluster_1.png              <- Imagen que muestra la distribución del clúster 1 con Altair.
    |   |    ├── Streamlit_Cluster_2.png              <- Imagen que muestra la distribución del clúster 2 con Altair.
    |   |    ├── Streamlit_Cluster_3.png              <- Imagen que muestra la distribución del clúster 3 con Altair.
    |   |    ├── Streamlit_Cluster_4.png              <- Imagen que muestra la distribución del clúster 4 con Altair.
    |   |    ├── Streamlit_Cluster_5.png              <- Imagen que muestra la distribución del clúster 5 con Altair.
    |   |    ├── Streamlit_Cluster_6.png              <- Imagen que muestra la distribución del clúster 6 con Altair.
    |   |    └── Streamlit_Cluster_7.png              <- Imagen que muestra la distribución del clúster 7 con Altair.
    |   |  
    |   ├── Boxplots                                  <- Carpeta con las gráficas resultantes de la dispersión de los grupos.    
    |   |    ├── Boxplot1.png                         <- Imagen que muestra la variación del grupo 1.
    |   |    ├── Boxplot2.png                         <- Imagen que muestra la variación del grupo 2.
    |   |    ├── BoxplotG1.png                        <- Imagen que muestra la dispersión del grupo 1.
    |   |    └── BoxplotG2.png                        <- Imagen que muestra la dispersión del grupo 2. 
    |   |
    |   ├── Matplotlib clusters                       <- Carpeta con las gráficas resultantes realizadas con Matplotlib. 
    |   |    ├── Cluster_1.png                        <- Imagen que muestra la distribución del clúster 1 con Matplotlib.
    |   |    ├── Cluster_2.png                        <- Imagen que muestra la distribución del clúster 2 con Matplotlib.
    |   |    ├── Cluster_3.png                        <- Imagen que muestra la distribución del clúster 3 con Matplotlib.
    |   |    ├── Cluster_4.png                        <- Imagen que muestra la distribución del clúster 4 con Matplotlib.
    |   |    ├── Cluster_5.png                        <- Imagen que muestra la distribución del clúster 5 con Matplotlib.
    |   |    ├── Cluster_6.png                        <- Imagen que muestra la distribución del clúster 6 con Matplotlib.
    |   |    ├── Cluster_7.png                        <- Imagen que muestra la distribución del clúster 7 con Matplotlib.
    |   |    └── Cluster_8.png                        <- Imagen que muestra la distribución del clúster 8 con Matplotlib.
    |   |    
    |   ├── Perfiles de carga electrica               <- Carpeta con las gráficas resultantes sobre el análisis descriptivo en el análisis EDA.
    |   |    ├── BD.png                               <- Imagen que muestra los perfiles de carga eléctrica con relación de la base de datos.
    |   |    ├── Centroides.png                       <- Imagen que muestra la señal que resulta de agrupar los grupos.
    |   |    ├── Media.png                            <- Imagen que muestra la distribución de la media de los datos.
    |   |    ├── Perfil_bus.png                       <- Imagen que muestra el perfil bus.
    |   |    ├── Varianza.png                         <- Imagen que muestra la varianza de los datos.
    |   |    └── Zscore.png                           <- Imagen que muestra la distribución de los valores Z score.
    |   |    
    |   └── README.md                                 <- Resultados del análisis EDA realizado.                                      
    |  
    ├── src                                           <- Carpeta con Jupyter notebook con el análisis EDA y Archivo README.md.
    |   ├── APP_Proyecto_EDA.py                       <- Aplicación Streamlit con Altair.
    |   ├── Proyecto_EDA.ipynb                        <- Jupyter notebook con el análisis EDA.
    │   └── README.md                                 <- Introducción al Jupyter notebook con el análisis EDA y Streamlit.
    |  
    ├── CITATION.md                                   <- Cita para referenciar el proyecto.  
    |  
    ├── CONTRIBUTING.md                               <- Pasos para los colaboradores que deseen contribuir al proyecto.  
    | 
    ├── LICENSE                                       <- MIT License.
    |  
    └── README.md                                     <- Archivo principal con la descripción del proyecto.  


Este repositorio tiene el fin de concentrar la información del trabajo desarrollado en la caracterización de perfiles de carga eléctrica, empleando un análisis EDA como parte exploratoria del proyecto. En la carpeta doc podrán encontrar el readme con la justificación de la problemática actual.

El presente trabajo forma parte del desarrollo de un proyecto de investigación en la Maestría en Ciencias de Datos de la Universidad de Guadalajara por los alumnos:

- Cristian Ulises Barenca Sotelo.
- Eyder Uriel Kinil Cervera.

Se busca el amplio uso de las buenas prácticas de los repositorios, como se menciona en el paper Wilson, G., Bryan, J., Cranston, K., et al. (2016). "Good Enough Practices in Scientific Computing". A fin de homologar y facilitar el trabajo colaborativo.
