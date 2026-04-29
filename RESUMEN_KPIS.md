# Análisis de KPIs - Uber NYC (2009-2015)

Este documento organiza la relación entre los 7 KPIs definidos para Uber NYC (2009-2015) y las tres
hipótesis estadísticas del estudio. Se presenta una síntesis tabular y un análisis detallado por KPI,
con un enfoque académico y criterios de validación claros.

## Relación entre KPIs e hipótesis estadísticas

| KPI | H1: Distancia -> Tarifa | H2: Efecto de franja horaria | H3: Crecimiento del volumen | Tipo de análisis recomendado |
| --- | --- | --- | --- | --- |
| KPI 1: Tasa de Crecimiento de Ingresos | No relacionada | No relacionada | Directa | Tendencia temporal / Regresión lineal |
| KPI 2: Ticket Promedio | Directa | Directa | Indirecta | Correlación (H1), ANOVA (H2) |
| KPI 3: Factor de Ocupación | No relacionada | No relacionada | No relacionada | No aplica |
| KPI 4: Índice de Estacionalidad | No relacionada | Indirecta | Directa | Chi-cuadrado / Prueba de tendencias |
| KPI 5: Eficiencia por Hora | No relacionada | Directa | Indirecta | ANOVA / Kruskal-Wallis |
| KPI 6: Retorno por Kilómetro | Directa | No relacionada | No relacionada | Correlación de Pearson / Regresión |
| KPI 7: Índice de Fidelización | No relacionada | No relacionada | Indirecta | No aplica |

## Análisis detallado por KPI

### KPI 1: Tasa de Crecimiento de Ingresos

**Hipótesis relacionada:** H3 (Crecimiento del volumen de viajes).

**Justificación:** este KPI mide la variación temporal de ingresos y, por extensión, refleja la dinámica
de expansión o contracción del negocio en el periodo 2009-2015.

**Criterio de validación:** crecimiento positivo sostenido respalda la hipótesis alternativa; crecimiento
plano o negativo es consistente con una distribución uniforme en el tiempo.

**Análisis recomendado:** regresión lineal temporal, prueba de tendencia (Mann-Kendall) y ANOVA de un
factor para comparar años.

---

### KPI 2: Ticket Promedio

**Hipótesis relacionadas:** H1 (Distancia -> Tarifa) y H2 (Efecto de franja horaria).

**Justificación:** el ticket promedio sintetiza el valor medio por viaje. Si la distancia determina la
tarifa, el ticket debería crecer con la distancia. Si existen diferencias por franja horaria, el ticket
promedio segmentado por hora debe mostrar contrastes estadísticamente significativos.

**Criterio de validación:** correlación positiva significativa entre distancia y ticket; diferencias
significativas entre franjas horarias para el ticket promedio.

**Análisis recomendado:** correlación de Pearson y regresión lineal simple para H1; ANOVA de un factor y
pruebas post-hoc (Tukey HSD) para H2.

---

### KPI 3: Factor de Ocupación

**Hipótesis relacionadas:** no aplica.

**Justificación:** este indicador mide eficiencia de uso de capacidad (pasajeros por viaje), pero no
evalúa la relación distancia-tarifa, el efecto horario en la tarifa ni el crecimiento temporal.

**Criterio de validación:** no corresponde a ninguna de las hipótesis estadísticas planteadas.

---

### KPI 4: Índice de Estacionalidad

**Hipótesis relacionada:** H3 (Crecimiento del volumen de viajes).

**Justificación:** cuantifica variaciones temporales de la demanda y permite evaluar si la distribución
de viajes es uniforme o presenta patrones de crecimiento o contracción estacional.

**Criterio de validación:** coeficiente de variación elevado y resultados significativos en pruebas de
uniformidad respaldan la hipótesis alternativa.

**Análisis recomendado:** prueba de chi-cuadrado para uniformidad y pruebas de tendencia (por ejemplo,
Cuzick) complementadas con el coeficiente de variación.

---

### KPI 5: Eficiencia por Hora

**Hipótesis relacionada:** H2 (Efecto de franja horaria en la tarifa).

**Justificación:** mide ingresos por franja horaria y permite contrastar si existen diferencias
significativas entre periodos del día en términos de eficiencia económica.

**Criterio de validación:** diferencias significativas entre franjas horarias respaldan la hipótesis
alternativa.

**Análisis recomendado:** ANOVA de un factor y, si no se cumplen supuestos, Kruskal-Wallis con pruebas
post-hoc para identificar franjas diferenciadas.

---

### KPI 6: Retorno por Kilómetro

**Hipótesis relacionada:** H1 (Distancia como predictor de la tarifa).

**Justificación:** representa la relación directa entre ingresos y distancia. Un retorno por kilómetro
estable es consistente con una relación lineal entre distancia y tarifa.

**Criterio de validación:** retorno por kilómetro relativamente constante y correlación positiva
significativa entre distancia y tarifa.

**Análisis recomendado:** correlación de Pearson, regresión lineal y análisis por segmentos de distancia
para evaluar heterogeneidad.

---

### KPI 7: Índice de Fidelización

**Hipótesis relacionadas:** relación indirecta con H3.

**Justificación:** la fidelización mide retención de usuarios y puede contribuir a la estabilidad del
volumen, pero no constituye un predictor directo del crecimiento temporal del volumen de viajes.

**Criterio de validación:** tendencias crecientes en fidelización pueden apoyar H3 de forma indirecta,
sin reemplazar indicadores directos de volumen.

## Matrices de validación por hipótesis

### H1: Distancia como predictor de la tarifa

| KPI relacionado | Tipo de relación | Permite validar H1 | Análisis recomendado |
| --- | --- | --- | --- |
| KPI 2: Ticket Promedio | Directa | Sí | Correlación por segmentos |
| KPI 6: Retorno por Kilómetro | Directa (crítica) | Sí | Correlación de Pearson / Regresión |

Conclusión: el KPI 6 es el indicador principal para validar H1, con el KPI 2 como complemento.

---

### H2: Efecto de la franja horaria en la tarifa

| KPI relacionado | Tipo de relación | Permite validar H2 | Análisis recomendado |
| --- | --- | --- | --- |
| KPI 2: Ticket Promedio | Directa | Sí | ANOVA entre franjas |
| KPI 5: Eficiencia por Hora | Directa | Sí | ANOVA / Kruskal-Wallis |

Conclusión: ambos KPIs permiten validar H2; KPI 2 es más directo en tarifa y KPI 5 aporta la perspectiva
operativa.

---

### H3: Crecimiento del volumen de viajes

| KPI relacionado | Tipo de relación | Permite validar H3 | Análisis recomendado |
| --- | --- | --- | --- |
| KPI 1: Tasa de Crecimiento de Ingresos | Directa (crítica) | Sí | Regresión temporal / Prueba de tendencia |
| KPI 4: Índice de Estacionalidad | Directa | Sí | Chi-cuadrado / Prueba de tendencias |

Conclusión: KPI 1 es el indicador principal de crecimiento, y KPI 4 complementa con análisis de
estacionalidad.

## Resumen ejecutivo

Los KPIs que validan directamente las hipótesis estadísticas son los siguientes:

- H1 (Distancia -> Tarifa): KPI 6 como validador principal y KPI 2 como validador secundario.
- H2 (Efecto de franja horaria): KPI 2 como validador principal y KPI 5 como complemento operativo.
- H3 (Crecimiento del volumen): KPI 1 como validador principal y KPI 4 como complemento estacional.

Los KPIs sin relación directa con las hipótesis son el KPI 3 (Ocupación) y el KPI 7 (Fidelización).

## Framework de validación recomendado

1. Para H1: calcular correlación de Pearson entre `distance_km` y `fare_amount`, seguida de regresión lineal.
2. Para H2: aplicar ANOVA sobre `fare_amount` entre franjas horarias definidas por `time_of_day`.
3. Para H3: realizar regresión temporal del volumen de viajes por año y una prueba de tendencia.
