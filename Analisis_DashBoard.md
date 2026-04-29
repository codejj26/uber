# Fase 6: Análisis, validación y storytelling

## Interpretación de resultados

El análisis de KPIs sobre Uber NYC (2009-2015) muestra un negocio con señales claras de crecimiento, alta sensibilidad a la hora del día y una demanda con comportamiento estacional. El ticket promedio observado en el dataset limpio es de aproximadamente 11.21 USD por viaje, lo que ubica la operación en un rango intermedio entre volumen y valor. Además, el análisis descriptivo evidencia que la mayor parte de los viajes se concentra en trayectos cortos, mientras que los viajes largos aportan un retorno por kilómetro más favorable para la empresa.

En términos operativos, la ocupación promedio por viaje es baja frente a la capacidad máxima teórica del vehículo, lo que sugiere que el modelo depende principalmente de viajes individuales y no de aprovechamiento intensivo de la capacidad. Esto es consistente con una operación urbana enfocada en rapidez y disponibilidad más que en ocupación compartida. Por otra parte, la demanda por hora y por mes confirma que existen franjas y periodos de mayor presión operativa, por lo que la asignación de conductores y el pricing dinámico son palancas clave.

## Validación de hipótesis estadísticas mediante KPIs

La validación de hipótesis estadísticas requiere distinguir entre evidencia descriptiva (observada en los KPIs) y evidencia inferencial (confirmada mediante pruebas estadísticas). A continuación se presentan las 3 hipótesis estadísticas principales y cómo los KPIs permiten validarlas:

### **H1: Distancia como predictor de la tarifa**

**Hipótesis estadística:**
- H₀: No hay relación lineal entre distance_km y fare_amount
- H₁: Existe relación positiva entre distancia y tarifa

**KPIs relacionados:**
-  **KPI 6: Retorno por Kilómetro** (PRINCIPAL)
-  **KPI 2: Ticket Promedio** (SECUNDARIO)

**Justificación:**
El KPI 6 es crítico porque mide directamente la pendiente de la relación distancia-tarifa (USD/km). Un retorno/km relativamente constante indica relación lineal, validando H₁. El KPI 2 complementa analizando ticket promedio por segmento de distancia.

**Análisis estadístico recomendado:**
- **Correlación de Pearson**: distance_km vs. fare_amount
- **Regresión lineal simple**: fare_amount ~ distance_km
- **Coeficiente de determinación (R²)**: Para evaluar fuerza de la relación

**Criterio de validación:**
- Si p < 0.05 y correlación > 0.6 → **CONFIRMA H₁** (relación positiva significativa)
- Si p ≥ 0.05 → **NO se rechaza H₀** (no hay evidencia de relación)

---

### **H2: Efecto de la franja horaria en la tarifa**

**Hipótesis estadística:**
- H₀: Las tarifas medias son iguales entre franjas horarias
- H₁: Al menos una franja horaria presenta diferencias en la tarifa

**KPIs relacionados:**
-  **KPI 2: Ticket Promedio por franja** (PRINCIPAL)
-  **KPI 5: Eficiencia por Hora** (SECUNDARIO)

**Justificación:**
El KPI 2 permite comparar directamente las tarifas medias entre franjas horarias (Madrugada, Mañana, Tarde, Noche). El KPI 5 complementa analizando eficiencia operativa por hora, que refleja variaciones en ingresos/tarifas.

**Análisis estadístico recomendado:**
- **ANOVA de un factor**: Comparar fare_amount entre time_of_day (4 grupos)
- **Test de Tukey HSD**: Para identificar qué franjas difieren significativamente
- **Kruskal-Wallis**: Alternativa no paramétrica si no se cumplen supuestos

**Criterio de validación:**
- Si p < 0.05 → **CONFIRMA H₁** (diferencias significativas entre franjas)
- Si p ≥ 0.05 → **NO se rechaza H₀** (tarifas similares entre franjas)

---

### **H3: Crecimiento del volumen de viajes**

**Hipótesis estadística:**
- H₀: Distribución uniforme por año (2009–2015)
- H₁: Distribución no uniforme; existe crecimiento en el tiempo

**KPIs relacionados:**
-  **KPI 1: Tasa de Crecimiento de Ingresos** (PRINCIPAL)
-  **KPI 4: Índice de Estacionalidad** (COMPLEMENTARIO)

**Justificación:**
El KPI 1 mide directamente la tasa de crecimiento interanual, permitiendo detectar si hay expansión, contracción o estabilidad. El KPI 4 complementa analizando variaciones estacionales que pueden afectar el patrón de crecimiento.

**Análisis estadístico recomendado:**
- **Regresión lineal temporal**: Volume_of_trips ~ year
- **Test de tendencia Mann-Kendall**: Para detectar tendencias monótonas
- **Chi-cuadrado**: Para probar uniformidad de distribución por año

**Criterio de validación:**
- Si p < 0.05 y pendiente > 0 → **CONFIRMA H₁** (crecimiento significativo)
- Si p ≥ 0.05 → **NO se rechaza H₀** (distribución uniforme, sin crecimiento)

---

### **KPIs sin relación directa con hipótesis estadísticas:**

-  **KPI 3: Factor de Ocupación** - Responde a eficiencia de flota, no a hipótesis estadísticas planteadas
-  **KPI 7: Índice de Fidelización** - Responde a retención, no a hipótesis estadísticas planteadas

## Uso del valor p para la toma de decisiones

El valor p (p-value) es la probabilidad de observar los datos obtenidos si la hipótesis nula (H₀) fuera verdadera. Se interpreta como un criterio de evidencia, no como una verdad absoluta:

- **Si p < 0.05**: Se rechaza H₀ y se adopta H₁ como evidencia estadística significativa
- **Si p ≥ 0.05**: No hay evidencia suficiente para rechazar H₀ (no confirma H₀, solo falta evidencia)

### Aplicación a las hipótesis estadísticas del proyecto:

**Para H1 (Distancia → Tarifa):**
- **Si p < 0.05 y correlación > 0.6**: Confirmar que distancia predice tarifa → Ajustar pricing por kilómetro, estructurar tarifas base + distancia
- **Si p ≥ 0.05**: Revisar modelo de pricing, considerar que otros factores (tiempo, zona) afectan más que distancia

**Para H2 (Efecto Franja Horaria):**
- **Si p < 0.05**: Confirmar diferencias significativas entre franjas → Implementar surge pricing diferenciado, priorizar conductores en horas pico, incentivos en horas valle
- **Si p ≥ 0.05**: Revisar策略, considerar que franjas no son diferenciadoras de tarifa

**Para H3 (Crecimiento Volumen):**
- **Si p < 0.05 y pendiente > 0**: Confirmar crecimiento significativo → Justificar expansión, inversión en escala, planificación de capacidad
- **Si p ≥ 0.05**: Revisar modelo de negocio, buscar nuevas oportunidades de crecimiento

## Construcción de narrativa con los datos

La historia que cuentan los datos es la de una plataforma urbana que crece apoyada en una demanda masiva, pero cuya rentabilidad depende de optimizar momento, distancia y capacidad. El crecimiento anual respalda la fase de expansión; la concentración horaria muestra que la operación no es uniforme; y la rentabilidad por kilómetro evidencia que no todos los viajes aportan el mismo valor.

En otras palabras, Uber no gana únicamente por tener más viajes, sino por gestionar mejor qué viajes prioriza, cuándo los atiende y cómo distribuye su capacidad. El negocio se fortalece cuando convierte datos operativos en decisiones de asignación, pricing y retención.

## Propuesta de decisiones basadas en evidencia estadística

### **Decisiones para H1 (Distancia → Tarifa):**

Si se confirma H₁ (p < 0.05):
1. **Estructurar pricing base + distancia**: Implementar tarifa mínima + tarifa por kilómetro
2. **Optimizar asignación de viajes**: Priorizar viajes de mayor retorno/km para conductores
3. **Segmentar oferta por distancia**: Diferenciar productos (UberX, UberXL, UberBLACK) según distancia target
4. **Ajustar promociones**: Ofrecer descuentos en viajes cortos para aumentar volumen, mantener margen en largos

Si NO se confirma H₁ (p ≥ 0.05):
- Revisar modelo de pricing actual
- Investigar otros factores que afecten tarifa (zona, tiempo, demanda)
- Considerar pricing por tiempo más que por distancia

---

### **Decisiones para H2 (Efecto Franja Horaria):**

Si se confirma H₁ (p < 0.05):
1. **Implementar surge pricing dinámico**: Aumentar tarifas en horas pico, reducir en horas valle
2. **Optimizar turnos de conductores**: Priorizar disponibilidad en franjas de mayor tarifa/ingreso
3. **Bonos por hora**: Incentivar conductores para trabajar en horas valle y balancear oferta
4. **Marketing timing**: Pautar publicidad en horas valle para estimular demanda

Si NO se confirma H₁ (p ≥ 0.05):
- Revisar策略, considerar que franjas no son diferenciadoras
- Explorar otras variables temporales (día de la semana, seasonality)
- Simplificar sistema de pricing

---

### **Decisiones para H3 (Crecimiento Volumen):**

Si se confirma H₁ (p < 0.05, pendiente > 0):
1. **Invertir en escala**: Expandir flota, mejorar infraestructura tecnológica
2. **Planificación de capacidad**: Aumentar inventario de conductores proyectando crecimiento
3. **Entrada a nuevos mercados**: Aprovechar momentum expansivo
4. **Atracción de inversión**: Usar métricas de crecimiento para funding

Si NO se confirma H₁ (p ≥ 0.05):
- Revisar modelo de negocio y propuesta de valor
- Buscar nuevas oportunidades de crecimiento (nuevos segmentos, geografías)
- Optimizar costos operativos
- Considerar pivote estratégico

## Discusión de limitaciones

El análisis presenta limitaciones importantes. La principal es la ausencia de un identificador de usuario, lo que impide medir fidelización de manera exacta. También hay una dependencia fuerte de métricas agregadas, por lo que no se observan diferencias individuales ni comportamientos microsegmentados. Adicionalmente, el dataset cubre un periodo histórico específico y no necesariamente representa el comportamiento actual de la plataforma.

Otra limitación es que varias conclusiones son descriptivas y requieren pruebas inferenciales adicionales para afirmarse con rigor estadístico. Sin esas pruebas, se puede hablar de patrones observados, pero no de causalidad. Finalmente, variables como clima, eventos especiales, congestión vial, competencia local o cambios regulatorios no están incluidas y podrían explicar parte de las variaciones detectadas.

## Conclusión

La validación de las 3 hipótesis estadísticas a través de los KPIs definidos proporciona un framework robusto para la toma de decisiones basada en evidencia:

**Síntesis de validación:**

- **H1 (Distancia → Tarifa)**: KPIs 2 y 6 permiten confirmar si la distancia es predictor significativo de la tarifa, fundamentando el modelo de pricing

- **H2 (Efecto Franja Horaria)**: KPIs 2 y 5 validan si existen diferencias significativas entre franjas, justificando surge pricing y gestión de turnos

- **H3 (Crecimiento Volumen)**: KPIs 1 y 4 confirman si existe crecimiento temporal significativo, validando la fase de expansión del modelo de negocio

**Lectura estratégica:**

La evidencia disponible sugiere que Uber operó en Nueva York con un modelo donde:
1. **La distancia es un predictor clave de la tarifa** (si se confirma H1), permitiendo estructurar pricing base + distancia
2. **La gestión horaria es crítica** (si se confirma H2), requiriendo optimización de turnos y pricing dinámico
3. **El crecimiento sustenta el modelo de negocio** (si se confirma H3), justificando inversión continua en escala

**Conclusión final:**

El éxito del modelo de negocio de Uber depende no solo del volumen de viajes, sino de la **optimización inteligente de tres dimensiones**: distancia (pricing), momento (gestión horaria) y crecimiento (escala). Los KPIs definidos permiten monitorear estas dimensiones y las pruebas estadísticas proporcionan el rigor inferencial necesario para tomar decisiones estratégicas basadas en evidencia cuantitativa.

Crecer no basta; hay que crecer con inteligencia operativa, enfocando recursos en las horas, periodos y segmentos con mayor retorno, respaldado por validación estadística de las hipótesis que fundamentan el modelo de negocio.