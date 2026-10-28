Tarea 3: Procesamiento de Datos con Apache Spark y Kafka

Descripción del proyecto

Este proyecto desarrolla un análisis de datos por lotes utilizando Apache Spark y un procesamiento de compras en tiempo real mediante Apache Kafka y Spark Structured Streaming. El objetivo es explorar datos de transacciones comerciales, identificar patrones de ventas y observar eventos de compra a medida que se reciben.

Dataset

Se utiliza el conjunto de datos Online Retail, publicado por el repositorio UCI Machine Learning Repository. Contiene transacciones de una tienda minorista en línea entre diciembre de 2010 y diciembre de 2011.

Entre sus variables se encuentran el número de factura, código y descripción del producto, cantidad, fecha de compra, precio unitario, identificador del cliente y país.

Fuente: https://archive.ics.uci.edu/dataset/352/online+retail

Procesamiento por lotes

El archivo tarea3.py utiliza Apache Spark para:

- Cargar los datos comerciales desde un archivo CSV.
- Consultar el esquema y el número inicial de registros.
- Filtrar registros con cantidades y precios unitarios positivos.
- Calcular el valor total de cada venta.
- Agrupar y comparar las ventas por país.
- Identificar los productos con mayor cantidad vendida.

El dataset contiene inicialmente 541.909 registros. Después del filtrado se obtuvieron 530.104 registros válidos.

Visualización de resultados

El archivo grafico_ventas.py genera un gráfico de barras horizontales con los diez países que presentan mayores ventas totales. La imagen generada se encuentra en ventas_por_pais.png.

Procesamiento en tiempo real

Se utiliza Apache Kafka para recibir eventos de compra en el tópico compras, y Spark Structured Streaming para procesarlos.

El consumidor interpreta los datos recibidos, calcula el valor total de cada compra multiplicando la cantidad por el precio y muestra los resultados por micro-lotes, incluyendo el número de compras procesadas en cada lote.

Archivos del repositorio

- tarea3.py: análisis por lotes con Apache Spark.
- grafico_ventas.py: generación de la gráfica de ventas.
- ventas_por_pais.png: visualización de los resultados del análisis.

Requisitos

- Python 3.
- Apache Spark.
- Apache Kafka.
- Conector de Spark para Kafka.
- Pandas y Matplotlib para generar la gráfica.

Ejecución

Análisis por lotes

Ejecutar en el entorno donde esté instalado Spark:

spark-submit /home/hadoop/online_retail/tarea3.py

El archivo CSV debe estar disponible en la ruta configurada dentro del script.


Generación de la gráfica

python3 /home/hadoop/online_retail/grafico_ventas.py


Procesamiento en tiempo real

Con ZooKeeper, Kafka y el tópico compras configurados y en ejecución, iniciar el consumidor de Spark con:

spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.8 /home/hadoop/spark_streaming_consumer.py

El productor debe enviar eventos al tópico para que el consumidor pueda procesarlos.


Conclusión

El proyecto permite aplicar herramientas del ecosistema Big Data para analizar transacciones históricas y procesar compras en tiempo real. Apache Spark facilita la transformación y agregación de grandes conjuntos de datos, mientras que Kafka permite transmitir eventos para su procesamiento continuo.
