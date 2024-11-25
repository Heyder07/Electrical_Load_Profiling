# Definimos las librerias que vamos a utilizar
import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
import datetime
import io


# Página de inicio
def pagina_inicio():

    # Definimos el nombre de la seccíon
    st.session_state.selected_page = "Inicio"

    # Definimos el titulo del inicio
    st.markdown("# Caracterización de señales electricas (Electrical load profiling)")

    # Texto de bienvenida
    st.write("Proyecto final | Desarrollo de Proyectos l | Maestría en Ciencia de los Datos | CUCEA")

    # Texto pregunta referente al proyecto
    st.write("### ¿De qué va este proyecto?")

    # Texto Referente al proyecto
    '''
    Actualmente, con la creciente integración de sensores en las máquinas y sistemas eléctricos se están recolectando datos que antes no se tenían, estos datos abren un nuevo paradigma para el análisis de la información inherente de los sistemas, que pueden ser empleados y explotados en el análisis exploratorio para la toma de decisiones en distintos campos de aplicación como pueden ser: la predicción de la demanda, detección de disturbios y caracterización de los perfiles de carga eléctrica.

    El análisis y exploración de datos son herramientas poderosas cuando se trabaja con repositorios de información. En este contexto, los enfoques presentados por Peng y Matsui en "The Art of Data Science" (2018), junto con las prácticas colaborativas de GitHub basadas en los lineamientos propuestos por Wilson en "Good Enough Practices in Science Computing" (2016), ofrecen un marco sólido para el trabajo con datos.

    Siguiendo las recomendaciones de estos autores, hemos integrado la plataforma de Streamlit aplicando las buenas prácticas. Esta plataforma open-source permite crear aplicaciones e interfaces web interactivas. Al integrarla con la librería Altair, es posible compartir aplicaciones web interactivas sin la necesidad de tener conocimientos avanzados en desarrollo de frontend, facilitando así el acceso y uso de herramientas visuales interactivas.
    '''
    
    # Información del Proyecto
    '''
    #### Información del Proyecto 
    * __Catedrático__: Mtro. Victor Hugo Cuspinera Contreras.
    * __Alumnos__: Cristian Ulises Barenca Sotelo y Eyder Uriel Kinil Cervera.
    * __Matrículas__: 323018977 y 216910473 
    * __Correo__: cristian.barenca1897@alumnos.udg.mx y eyder.kinil1047@alumnos.udg.mx
    '''

# Página de análisis
def pagina_analisis():

    # Definimos el nombre de la seccíon
    st.session_state.selected_page = "Análisis EDA (Exploratory data analisys)"

    # Definimos el titulo de la página de Análisis
    st.markdown("# Análisis EDA (Exploratory data analisys)")

    # Hacemos uso del dataset summer.csv
    df = pd.read_csv("../data/summer.csv") 

    '''

    El Análisis Exploratorio de Datos (EDA) es el proceso empleado para analizar y explorar los datos. Una herramienta poderosa del EDA es la visualización, dado que se puede dar indicios de patrones en los datos. Con el EDA se pueden lograr los siguientes objetivos:

    1. Determinar si existen problemas con el dataset.

    2. Determinar si la pregunta que se plantea se puede resolver con el dataset utilizado.

    3. Desarrollar un esquema de respuestas a las preguntas.

    ## 1. Formula tu pregunta

    Si se caracterizan los perfiles de carga eléctrica mediante técnicas de agrupamiento es posible agilizar la toma de decisiones en la optimización de la demanda eléctrica para la reducción del costo de las tarifas eléctricas en un % significativo de ahorro.

    ## 2. Leer los datos

    Dada una base de datos con perfiles de carga electrica, determine:

    1. Cantidad de perfiles y frecuencia de monitoreo.
    2. Medidas de tendencia central y dispersión.
    3. Muestre los grupos mediante algún método de ML (clustering).

    ## 3. Checa la estructura de los datos
    '''

    # Visualizamos el tamaño del dataframe
    st.markdown(f"Tamaño del DataFrame: {df.shape}")

    # Redirigir la salida de info() a un buffer StringIO
    buffer = io.StringIO()

    # Asignamos la información al buffer
    df.info(buf=buffer)

    # Obtenemos la información en el buffer
    info_str = buffer.getvalue()

    # Mostramos la información del DataFrame en Streamlit
    st.text(info_str)


    # Definimos la sección 4
    st.markdown(f"## 4. Realizar barrido de los datos")
    
    # Realizamos el barrido hacia adelante
    st.markdown(f"Barrido hacia adelante:")

    # Imprimimos el dataframe hacia adelante
    st.dataframe(df.head(5))

    # Realizamos el barrido hacia atras
    st.markdown(f"Barrido hacia atras:")
    
    # Imprimimos el dataframe hacia atras
    st.dataframe(df.tail(5))

    # Definimos la sección 5
    st.markdown(f"## 5. Checar las Ns")

    '''
        De los perfiles de carga eléctrica importados podemos observar que se tienen 5,888 perfiles, de los cuales cada uno tiene la etiqueta de la fecha de la toma de las lecturas y se tienen 96 lecturas por cada día de regsitros. Es decir, se tiene una frecuencia de monitoreo de cada 15 minutos.
    '''

    st.dataframe(df.groupby('Profile Type and Weather Zone').count())

    # Definimos la sección 6
    st.markdown(f"## 6. Validar con una fuente de datos externa")

    '''
        Podemos observar del dataframe que se tienen 64 distintos tipos de perfiles, en donde cada uno tiene 92 series de tiempo con registros cada 15 minutos. Los 5,888 = 64*92 renglones.
    '''

    #Extraemos un dataframe solo con los datos de un tipo de cliente
    Cliente_1 = df.loc[df['Profile Type and Weather Zone'] == 'BUSHILF_COAST']

    #Visualizamos el dataframe creado a partir del tipo de cliente 1
    st.dataframe(Cliente_1)
    
    #Crear graficos con la libería Altair
    st.markdown(f"## 7. Hacer un gráfico")
    
    #Extraemos un solo los valores de consumo del cliente 
    data = Cliente_1.drop(['Profile Type and Weather Zone','ERC_TRADE_DATE'],axis=1)
    #Convertimos el dataframe a un array 
    data_array = data.to_numpy()

    
    # Título de la aplicación
    st.markdown("#### Visualización de Perfiles de Carga Eléctrica")

    # Creamos el vector de número de lecturas por día
    x = np.linspace(1, 96, 96)
    
    # Creamos un DataFrame para Altair (transformamos a formato largo)
    df_altair = pd.DataFrame({
        'Observación': np.tile(x, len(data)),
        'Consumo': data_array.flatten(),
        'Día': np.repeat(np.arange(len(data)), len(x))
    })
    # Crear el gráfico con Altair
    chart = alt.Chart(df_altair).mark_line().encode(
        x='Observación:Q',
        y='Consumo:Q',
        color='Día:N'
    ).properties(
        title="Perfiles de carga eléctrica del cliente 1: BUSHILF_COAST",
        width=800,
        height=400
    )
    # Mostrar el gráfico en Streamlit
    st.altair_chart(chart, use_container_width=True)

    # Crear el gráfico Boxplot con Altair
    boxplot = alt.Chart(df_altair).mark_boxplot().encode(
        x='Día:N',
        y='Consumo:Q',
        color='Día:N'
    ).properties(
        title="Boxplot de Perfiles de Carga Eléctrica",
        width=800,
        height=400
    )

    # Mostrar el gráfico en Streamlit
    st.altair_chart(boxplot, use_container_width=True)

# Página de resultados
def pagina_resultados():

    # Definimos el nombre de la seccíon
    st.session_state.selected_page = "Resultados"

    # Definimos el titulo de la página de Resultados
    st.markdown("# Resultados")


# Diccionario de páginas
paginas = {
    "Inicio": pagina_inicio,
    "Análisis EDA (Exploratory data analisys)": pagina_analisis,
    "Resultados": pagina_resultados
}

# Usamos st.session_state para recordar la página seleccionada
if 'selected_page' not in st.session_state:
    
    # Definimos la página inicial predeterminada
    st.session_state.selected_page = "Inicio"  

# Barra lateral para la navegación
opcion = st.sidebar.selectbox("Selecciona una sección:", list(paginas.keys()), index=list(paginas.keys()).index(st.session_state.selected_page))

# Llamamos a la función correspondiente
paginas[opcion]()