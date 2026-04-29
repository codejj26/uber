## Fase 1: Comprension del Problema

### Descripcion del contexto del dataset

El dataset utilizado en este proyecto corresponde a registros historicos de viajes realizados a traves de la plataforma Uber en la ciudad de Nueva York durante el periodo comprendido entre 2009 y 2015. Uber es una empresa de transporte bajo demanda que conecta pasajeros con conductores particulares mediante una aplicacion movil, operando bajo el modelo de economia colaborativa (ridesharing).

Cada registro del conjunto de datos representa un viaje individual e incluye informacion sobre la fecha y hora de recogida, las coordenadas geograficas del punto de origen y destino, el numero de pasajeros transportados y el valor de la tarifa cobrada. Este tipo de dato transaccional posee alto valor estrategico para el analisis de la demanda, el comportamiento del consumidor y la optimizacion de precios en una plataforma de movilidad urbana.

**Descripcion de variables del dataset**

| Variable | Tipo de dato | Descripcion |
| --- | --- | --- |
| key | Texto | Identificador unico del viaje |
| fare_amount | Numerico | Tarifa cobrada al pasajero (USD) |
| pickup_datetime | Fecha/Hora | Fecha y hora de recogida en formato UTC |
| pickup_longitude | Numerico | Longitud geografica del punto de recogida |
| pickup_latitude | Numerico | Latitud geografica del punto de recogida |
| dropoff_longitude | Numerico | Longitud geografica del punto de destino |
| dropoff_latitude | Numerico | Latitud geografica del punto de destino |
| passenger_count | Numerico | Numero de pasajeros por viaje |

### Usuarios del analisis

Los resultados de este proyecto son utiles para distintos actores dentro del ecosistema de Uber y de la movilidad urbana:

- Gerencia de operaciones: identificar patrones de demanda y optimizar disponibilidad de conductores por zonas y franjas horarias.
- Equipo de fijacion de precios (pricing): evaluar si las tarifas reflejan adecuadamente variables operativas como la distancia, el horario y la demanda.
- Analistas urbanos y reguladores de transporte: comprender el impacto del transporte por aplicacion en la movilidad de Nueva York.

### Proposito del analisis

El analisis busca transformar datos transaccionales en inteligencia de negocio accionable: identificar franjas horarias y zonas de alta demanda, evaluar la relacion entre distancia y tarifa, detectar patrones estacionales y comprender la evolucion del servicio en el periodo 2009-2015.

### Identificacion del problema central de analisis

**Pregunta central:**

> Que factores temporales, espaciales y operativos influyen significativamente en el valor de la tarifa de un viaje de Uber en Nueva York, y como puede esta informacion orientar la optimizacion de la estrategia de precios y la eficiencia operacional de la plataforma?

**Dimensiones del problema de analisis de negocio**

| Dimension | Descripcion |
| --- | --- |
| Optimizacion de precios | Evaluar si la tarifa cobrada refleja adecuadamente la distancia recorrida y el nivel de demanda en el momento del viaje. |
| Analisis de la demanda | Determinar cuando y donde se concentra el mayor volumen de viajes e identificar patrones de estacionalidad o picos horarios. |
| Eficiencia operacional | Analizar si los patrones de ocupacion del vehiculo y la tarifa por kilometro reflejan un uso eficiente de la plataforma. |

### Preguntas clave de analisis

**Pregunta 1. Relacion entre distancia y tarifa**

Existe una relacion estadisticamente significativa entre la distancia recorrida en cada viaje y la tarifa cobrada (fare_amount) en los viajes de Uber en Nueva York?

**Pregunta 2. Efecto de la franja horaria sobre la tarifa**

Existen diferencias estadisticamente significativas en la tarifa promedio de los viajes segun la franja horaria en la que se realiza el servicio?

**Pregunta 3. Crecimiento del volumen de viajes**

El volumen de viajes registrados en Uber presento un crecimiento significativo entre los anos 2009 y 2015?

---

## Fase 2: Formulacion de Hipotesis

En esta fase se plantean tres hipotesis estadisticas derivadas del problema central y de las preguntas de analisis. Para cada hipotesis se define la hipotesis nula (H0) y la hipotesis alternativa (H1), se justifica su relevancia para el negocio, se identifican las variables involucradas y se propone la prueba estadistica mas adecuada.

### Hipotesis 1: Distancia recorrida como predictor de la tarifa

**Planteamiento**

- H0: rho = 0. No existe una correlacion lineal estadisticamente significativa entre la distancia recorrida y la tarifa cobrada.
- H1: rho > 0. Existe una correlacion lineal positiva estadisticamente significativa entre la distancia recorrida y la tarifa cobrada.

**Justificacion para el negocio**

El modelo de tarificacion de Uber incluye la distancia recorrida como uno de sus componentes fundamentales. Confirmar estadisticamente esta relacion valida la coherencia del esquema de precios y permite detectar posibles anomalias: viajes cortos con tarifas elevadas asociables al efecto de surge pricing o viajes largos subvalorados que generen perdidas para los conductores. Esta hipotesis constituye el fundamento cuantitativo del indicador de tarifa por kilometro.

**Variables involucradas**

| Variable | Rol estadistico | Origen en el dataset |
| --- | --- | --- |
| fare_amount | Dependiente (continua) | Columna original del dataset |
| distance_km | Independiente (continua) | Calculada mediante la formula de Haversine |

**Prueba estadistica propuesta**

Se propone aplicar la correlacion de Pearson como prueba principal, complementada con una regresion lineal simple.

- Justificacion: ambas variables son continuas y se espera una relacion lineal. El coeficiente de correlacion de Pearson cuantifica la fuerza y direccion de dicha relacion, y su prueba de significancia permite decidir sobre H0.
- Criterio de decision: si p < 0.05 y r > 0, se rechaza H0 en favor de H1.
- Complemento: la regresion lineal estima el coeficiente beta1 y el coeficiente de determinacion R2.

**Modelo propuesto**

```
fare_hat_i = beta0 + beta1 * distance_km_i + epsilon_i
```

### Hipotesis 2: Efecto de la franja horaria sobre la tarifa promedio

**Planteamiento**

- H0: mu_madrugada = mu_manana = mu_tarde = mu_noche. La tarifa media es estadisticamente igual en todas las franjas horarias.
- H1: existe al menos un par de franjas con medias diferentes.

**Definicion de los grupos horarios**

| Franja horaria | Rango | Condicion sobre hour |
| --- | --- | --- |
| Madrugada | 00:00 - 05:59 | hour in [0, 5] |
| Manana | 06:00 - 11:59 | hour in [6, 11] |
| Tarde | 12:00 - 17:59 | hour in [12, 17] |
| Noche | 18:00 - 23:59 | hour in [18, 23] |

**Justificacion para el negocio**

El mecanismo de surge pricing se activa cuando la demanda supera la oferta de conductores disponibles, elevando las tarifas de forma dinamica. Si la hipotesis alternativa se confirma, existira evidencia estadistica de que la franja horaria es un determinante significativo del precio, lo que justifica estrategias diferenciadas de disponibilidad, incentivos economicos en horas pico y comunicacion proactiva de tarifas.

**Variables involucradas**

| Variable | Rol estadistico | Origen en el dataset |
| --- | --- | --- |
| fare_amount | Dependiente (continua) | Columna original del dataset |
| time_of_day | Independiente (factor, 4 niveles) | Derivada de hour |
| hour | Variable auxiliar de agrupacion | Extraida de pickup_datetime |

**Prueba estadistica propuesta**

Se propone aplicar el analisis de varianza de un factor (ANOVA de un factor).

- Justificacion: permite comparar medias de una variable continua entre mas de dos grupos independientes.
- Supuestos a verificar: normalidad de residuos por grupo (Shapiro-Wilk o Kolmogorov-Smirnov) y homogeneidad de varianzas (Levene).
- Criterio de decision: si p < 0.05, se rechaza H0 y se concluye que al menos una franja horaria presenta una tarifa media distinta.
- Analisis post-hoc: aplicar Tukey HSD para identificar pares de franjas con diferencias significativas.

**Estadistico F**

```
F = (SCB/(k-1)) / (SCW/(N-k))
```

Donde SCB es la suma de cuadrados entre grupos, SCW es la suma de cuadrados dentro de los grupos, k = 4 y N es el total de viajes.

### Hipotesis 3: Crecimiento del volumen de viajes entre 2009 y 2015

**Planteamiento**

- H0: la distribucion de viajes por ano es uniforme a lo largo del periodo 2009-2015; no existen diferencias significativas entre los volumenes anuales.
- H1: la distribucion de viajes por ano no es uniforme; el volumen de viajes crecio de manera significativa entre 2009 y 2015.

**Justificacion para el negocio**

Uber inicio operaciones en Nueva York en 2011 y experimento un crecimiento acelerado en los anos siguientes. Por esta razon, los registros correspondientes a 2009 y 2010 son escasos o inexistentes en el dataset, lo que refuerza la hipotesis de una distribucion no uniforme. Confirmar estadisticamente dicha expansion permite contextualizar la evolucion de las tarifas y la dinamica del mercado.

**Variables involucradas**

| Variable | Rol estadistico | Origen en el dataset |
| --- | --- | --- |
| year | Categorica (7 niveles) | Extraida de pickup_datetime |
| Frecuencia de viajes | Conteo observado por ano | Agregacion del dataset |

**Prueba estadistica propuesta**

Se propone aplicar la prueba de bondad de ajuste Chi-cuadrado.

- Justificacion: la variable year es categorica y se evalua si la frecuencia observada difiere de la distribucion esperada bajo uniformidad.
- Criterio de decision: si p < 0.05, se rechaza H0 y se concluye que el volumen de viajes no fue uniforme en el periodo analizado.

**Estadistico Chi-cuadrado**

```
chi2 = sum((Oi - Ei)^2 / Ei)
Ei = N / k
```

Donde Oi es la frecuencia observada del ano i, Ei la frecuencia esperada, k = 7 y N el total de viajes.

### Resumen de hipotesis estadisticas

| No. | Variable dependiente | Variable independiente | Prueba estadistica | Nivel alpha |
| --- | --- | --- | --- | --- |
| 1 | fare_amount | distance_km (continua) | Pearson + Regresion lineal | 0.05 |
| 2 | fare_amount | time_of_day (4 grupos) | ANOVA + Tukey HSD | 0.05 |
| 3 | Frecuencia de viajes | year (7 niveles) | Chi-cuadrado de bondad de ajuste | 0.05 |
