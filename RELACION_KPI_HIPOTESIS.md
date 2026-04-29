# Relación entre KPIs e Hipótesis del Negocio
## Uber NYC (2009-2015) - Análisis de Alineación Estratégica

---

## Tabla de Contenidos

1. [Introducción](#introducción)
2. [Hipótesis del Negocio](#hipótesis-del-negocio)
3. [Análisis Detallado por KPI](#análisis-detallado-por-kpi)
4. [Matriz de Relaciones](#matriz-de-relaciones)
5. [Capacidad de Validación](#capacidad-de-validación)
6. [Conclusiones Estratégicas](#conclusiones-estratégicas)

---

## Introducción

Este documento establece la relación estratégica entre los **7 KPIs definidos** para el análisis de Uber NYC y las **5 hipótesis fundamentales del negocio**. El objetivo es demostrar cómo cada métrica permite validar, refutar o monitorear las suposiciones clave que sustentan el modelo de negocio de Uber durante su fase de expansión agresiva (2009-2015).

### Propósito del Análisis

- **Validación de hipótesis**: Determinar si las suposiciones del negocio se confirman con datos reales
- **Toma de decisiones**: Guiar decisiones estratégicas basadas en evidencia cuantitativa
- **Optimización de recursos**: Identificar qué KPIs requieren mayor atención según la hipótesis
- **Alineación organizacional**: Asegurar que todos los equipos midan lo que estratégicamente importa

---

## Hipótesis del Negocio

Las hipótesis del negocio representan las suposiciones fundamentales que validan el modelo de negocio de Uber NYC:

| Código | Hipótesis | Descripción |
|--------|-----------|-------------|
| **H1** | Expansión Acelerada | Uber está en fase de crecimiento agresivo (2009-2015) |
| **H2** | Patrones Estacionales | La demanda muestra variaciones predecibles por temporada |
| **H3** | Optimización Horaria | La eficiencia operativa depende de patrones horarios |
| **H4** | Rentabilidad Segmentada | La rentabilidad varía según distancia y ocupación |
| **H5** | Retención = Ingresos | La fidelización de usuarios impacta directamente en ingresos sostenibles |

---

## Análisis Detallado por KPI

---

## KPI 1: Tasa de Crecimiento de Ingresos

### Definición
```
Tasa de Crecimiento = ((Ingresos_Periodo_Actual - Ingresos_Periodo_Anterior) / Ingresos_Periodo_Anterior) × 100
```

### Hipótesis Relacionada
**✓ H1 - Expansión Acelerada** (Relación DIRECTA)

### Justificación de la Relación

#### ¿Por qué existe esta relación?
La **Tasa de Crecimiento de Ingresos** es la métrica fundamental para validar la hipótesis de expansión acelerada porque:

1. **Medición cuantitativa del crecimiento**: Traduce el concepto abstracto de "expansión agresiva" a un número medible
2. **Evidencia de escalabilidad**: Demuestra si el modelo de negocio puede crecer sostenidamente
3. **Validación de inversión**: Justifica la asignación de recursos para marketing y tecnología
4. **Benchmarking competitivo**: Permite comparar el crecimiento de Uber vs. alternativas tradicionales

#### ¿Cómo valida la hipótesis?

| Escenario | Tasa de Crecimiento | Interpretación | Validación de H1 |
|-----------|---------------------|----------------|------------------|
| **Expansión exitosa** | > 20% | Crecimiento agresivo sostenido | ✓ **CONFIRMA** hipótesis |
| **Crecimiento saludable** | 10-20% | Expansión moderada, mantener estrategia | ~ **PARCIALMENTE** confirma |
| **Maduración del mercado** | 0-10% | Crecimiento desacelerado | ✗ **REFUTA** expansión agresiva |
| **Problemas estructurales** | < 0% | Contracción de ingresos | ✗ **REFUTA** completamente |

#### Acciones según Resultados

**Si se CONFIRMA la hipótesis (>20%):**
- Invertir agresivamente en escalabilidad tecnológica
- Expandir a nuevas zonas geográficas
- Aumentar presupuesto de adquisición de usuarios
- Preparar infraestructura para siguiente fase de crecimiento

**Si se REFUTA la hipótesis (<10%):**
- Revisar propuesta de valor
- Explorar nuevos segmentos de mercado
- Optimizar costos operativos
- Considerar pivote estratégico

---

## KPI 2: Ticket Promedio

### Definición
```
Ticket Promedio = Total Ingresos / Total Viajes
```

### Hipótesis Relacionada
**✓ H4 - Rentabilidad Segmentada** (Relación DIRECTA)

### Justificación de la Relación

#### ¿Por qué existe esta relación?
El **Ticket Promedio** es clave para validar la rentabilidad segmentada porque:

1. **Identificación de segmentos de valor**: Distingue entre viajes premium vs. comodidad
2. **Base para pricing dinámico**: Permite ajustar precios según segmento y contexto
3. **Optimización de margen**: Determina qué viajes generan mayor rentabilidad
4. **Segmentación de mercado**: Separa clientes de alto valor vs. alta frecuencia

#### ¿Cómo valida la hipótesis?

| Segmento | Ticket Promedio | Características | Validación de H4 |
|----------|-----------------|-----------------|------------------|
| **Premium** | > $15 | Alto margen, baja frecuencia | ✓ **CONFIRMA** rentabilidad diferencial |
| **Óptimo** | $10-15 | Equilibrio volumen-valor | ✓ **CONFIRMA** segmentación viable |
| **Alta frecuencia** | $5-10 | Bajo margen, alto volumen | ✓ **CONFIRMA** distintos segmentos |
| **Comodidad** | < $5 | Posible subsidio | ~ Revisa estructura de costos |

#### Acciones según Resultados

**Si se CONFIRMA la hipótesis (tickets variados):**
- Implementar pricing dinámico por segmento
- Diseñar promociones específicas por segmento
- Optimizar asignación de conductores según rentabilidad
- Crear productos diferenciados por tipo de cliente

**Si los tickets son uniformes:**
- Revisar si la segmentación de mercado es adecuada
- Explorar nuevas variables de segmentación (zonas, horarios)
- Considerar introducir nuevos productos/servicios

---

## KPI 3: Factor de Ocupación

### Definición
```
Factor de Ocupación = Pasajeros Promedio por Viaje / Capacidad Máxima (6 pasajeros)
Pasajeros Promedio = Total Pasajeros Transportados / Total Viajes
```

### Hipótesis Relacionada
**✓ H5 - Retención = Ingresos** (Relación INDIRECTA)

### Justificación de la Relación

#### ¿Por qué existe esta relación?
El **Factor de Ocupación** se relaciona indirectamente con la retención porque:

1. **Proxy de consolidación de rutas**: Alta ocupación sugiere viajes recurrentes consolidados
2. **Eficiencia de flota**: Cada pasajero adicional es ingreso puro sin costo marginal significativo
3. **Impacto ambiental**: ESG positivo genera lealtad en clientes conscientes
4. **Hábitos de uso**: Usuarios recurrentes tienden a compartir más viajes

#### ¿Cómo valida la hipótesis?

| Nivel de Ocupación | Rango | Interpretación | Validación de H5 |
|--------------------|-------|----------------|------------------|
| **Excelente** | > 50% | Base consolidada, alto impacto ambiental | ✓ **CONFIRMA** retención fuerte |
| **Moderado** | 30-50% | Oportunidad de ridesharing | ~ **PARCIALMENTE** confirma |
| **Bajo** | < 30% | Alta dependencia de viajes individuales | ✗ **REFUTA** consolidación de base |

#### Acciones según Resultados

**Si se CONFIRMA la hipótesis (>50%):**
- Implementar programas de referidos para aprovechar base leal
- Diseñar productos de suscripción para usuarios frecuentes
- Crear campañas de marketing enfocadas en sostenibilidad
- Optimizar rutas basadas en patrones consolidados

**Si se REFUTA la hipótesis (<30%):**
- Promover activamente ridesharing con incentivos
- Revisar experiencia de usuario para reducir fricción
- Investigar por qué usuarios no comparten viajes
- Considerar ajustes en pricing para fomentar ocupación

---

## KPI 4: Índice de Estacionalidad de la Demanda

### Definición
```
Índice de Estacionalidad = (Viajes en Período / Viajes Promedio Mensual) × 100
Coeficiente de Variación = (Desviación Estándar Viajes Mensuales / Media Viajes Mensuales)
```

### Hipótesis Relacionada
**✓ H2 - Patrones Estacionales** (Relación DIRECTA)

### Justificación de la Relación

#### ¿Por qué existe esta relación?
El **Índice de Estacionalidad** valida directamente la hipótesis estacional porque:

1. **Medición de variaciones**: Cuantifica cuánto varía la demanda entre períodos
2. **Coeficiente de variación**: Determina significancia estadística de patrones estacionales
3. **Planificación anticipada**: Permite ajustar recursos antes de picos/valles
4. **Predicción de ingresos**: Mejora accuracy de forecasts estacionales

#### ¿Cómo valida la hipótesis?

| Coeficiente de Variación | Nivel de Estacionalidad | Interpretación | Validación de H2 |
|---------------------------|-------------------------|----------------|------------------|
| **Alta** | > 0.3 | Fuertes variaciones estacionales | ✓ **CONFIRMA** patrones marcados |
| **Moderada** | 0.2-0.3 | Variaciones predecibles | ✓ **CONFIRMA** patrones moderados |
| **Baja** | < 0.2 | Demanda relativamente estable | ✗ **REFUTA** estacionalidad significativa |

#### Acciones según Resultados

**Si se CONFIRMA la hipótesis (CV > 0.3):**
- Implementar planificación detallada por temporada
- Contratar conductores temporales para períodos pico
- Diseñar promociones específicas por temporada
- Ajustar pricing dinámico según estacionalidad
- Construir inventario de conductores para alta demanda

**Si se REFUTA la hipótesis (CV < 0.2):**
- Mantener fuerza de trabajo estable durante todo el año
- Enfocar esfuerzos en otras variables (horarios, zonas)
- Simplificar planificación operativa
- Reducir inventario de conductores

---

## KPI 5: Eficiencia por Hora

### Definición
```
Ingresos por Hora = Total Ingresos en Franja Horaria / Total Horas Operativas en Franja
Eficiencia Relativa = Ingresos por Hora de Franja / Ingresos por Hora Promedio × 100
```

### Hipótesis Relacionada
**✓ H3 - Optimización Horaria** (Relación DIRECTA)

### Justificación de la Relación

#### ¿Por qué existe esta relación?
La **Eficiencia por Hora** valida directamente la hipótesis horaria porque:

1. **Identificación de horas pico/valle**: Mide rentabilidad por franja horaria
2. **Optimización de turnos**: Define qué horas priorizar disponibilidad de conductores
3. **Surge pricing**: Justifica precios dinámicos en horas de alta presión
4. **Gestión de brechas**: Detecta desajustes entre oferta y demanda por hora

#### ¿Cómo valida la hipótesis?

| Eficiencia Relativa | Tipo de Hora | Interpretación | Validación de H3 |
|---------------------|--------------|----------------|------------------|
| **Hora pico** | > 120% | Máxima rentabilidad por hora | ✓ **CONFIRMA** dependencia horaria |
| **Hora normal** | 80-120% | Operación estándar | ~ **NEUTRO** para validación |
| **Hora valle** | < 80% | Baja rentabilidad | ✓ **CONFIRMA** variación horaria |

#### Acciones según Resultados

**Si se CONFIRMA la hipótesis (eficiencia variada):**
- Implementar turnos diferenciados por eficiencia horaria
- Diseñar bonos por hora para conductores en franjas de alta demanda
- Activar surge pricing en horas pico
- Pautar publicidad en horas valle para estimular demanda
- Optimizar distribución de conductores según hora

**Si la eficiencia es uniforme:**
- Revisar si la distribución de conductores es adecuada
- Explorar otras variables de optimización (zonas, clima)
- Considerar si surge pricing es necesario

---

## KPI 6: Retorno por Kilómetro

### Definición
```
Retorno por KM = Total Ingresos / Total Kilómetros Recorridos
Retorno por KM por Segmento = Ingresos Segmento / Kilómetros Segmento
```

### Hipótesis Relacionada
**✓ H4 - Rentabilidad Segmentada** (Relación DIRECTA)

### Justificación de la Relación

#### ¿Por qué existe esta relación?
El **Retorno por Kilómetro** complementa el análisis de rentabilidad segmentada porque:

1. **Segmentación por distancia**: Distingue viajes cortos vs. largos
2. **Eficiencia económica**: Mide cuánto genera cada KM operado
3. **Benchmarking de costos**: Compara retorno vs. costos operativos (combustible, mantenimiento)
4. **Optimización de rutas**: Identifica qué distancias son más rentables

#### ¿Cómo valida la hipótesis?

| Retorno por KM | Segmento | Características | Validación de H4 |
|----------------|----------|-----------------|------------------|
| **Premium** | > $5/KM | Alta rentabilidad por distancia | ✓ **CONFIRMA** segmentación por distancia |
| **Óptimo** | $3-5/KM | Equilibrio rentabilidad-volumen | ✓ **CONFIRMA** rentabilidad diferencial |
| **Baja rentabilidad** | < $3/KM | Revisa estructura de costos | ~ Revisa modelo de pricing |

#### Acciones según Resultados

**Si se CONFIRMA la hipótesis (retorno variado por KM):**
- Diseñar incentivos para conductores en segmentos rentables
- Optimizar algoritmos de asignación de viajes por distancia
- Ajustar pricing según distancia para mejorar margen
- Crear productos especializados por tipo de distancia

**Si el retorno es uniforme:**
- Revisar si la estructura de costos es adecuada
- Explorar otras dimensiones de segmentación (zonas, tiempos)
- Considerar si el pricing actual captura valor diferencial

---

## KPI 7: Índice de Fidelización de Usuarios

### Definición
```
Índice de Fidelización = (Usuarios con Múltiples Viajes / Total Usuarios Únicos) × 100
Frecuencia Promedio = Total Viajes / Total Usuarios Únicos
```

### Hipótesis Relacionada
**✓ H5 - Retención = Ingresos** (Relación DIRECTA)

### Justificación de la Relación

#### ¿Por qué existe esta relación?
El **Índice de Fidelización** valida directamente la hipótesis de retención porque:

1. **Medición directa de lealtad**: Proporción de usuarios que repiten vs. nuevos
2. **Correlación con ingresos**: Usuarios recurrentes generan mayor valor temporal (LTV)
3. **Sostenibilidad del negocio**: Base leal reduce dependencia de adquisición constante
4. **Costo de retención vs. adquisición**: Retener es 5x más económico que adquirir

#### ¿Cómo valida la hipótesis?

| Nivel de Fidelización | Rango | Interpretación | Validación de H5 |
|-----------------------|-------|----------------|------------------|
| **Base muy leal** | > 60% | Alta dependencia de retención | ✓ **CONFIRMA** impacto en ingresos |
| **Saludable** | 40-60% | Equilibrio retención-adquisición | ✓ **CONFIRMA** modelo sostenible |
| **Alta rotación** | < 40% | Dependencia excesiva de adquisición | ✗ **REFUTA** retención como motor |

#### Acciones según Resultados

**Si se CONFIRMA la hipótesis (>60%):**
- Activar programas de referidos para multiplicar base leal
- Diseñar productos de suscripción para usuarios frecuentes
- Implementar gamificación para aumentar frecuencia de uso
- Optimizar experiencia de usuario para reducir churn
- Crear comunicación personalizada para segmentos leales

**Si se REFUTA la hipótesis (<40%):**
- Investigar causas de churn (pricing, experiencia, competencia)
- Revisar onboarding de nuevos usuarios
- Implementar encuestas de satisfacción
- Considerar incentivos para segundo viaje
- Optimizar aspectos claves de la experiencia del usuario

---

## Matriz de Relaciones

### Resumen Visual

| KPI | H1: Expansión Acelerada | H2: Patrones Estacionales | H3: Optimización Horaria | H4: Rentabilidad Segmentada | H5: Retención = Ingresos |
|-----|-------------------------|---------------------------|--------------------------|-----------------------------|---------------------------|
| **KPI 1: Tasa de Crecimiento** | ✓ **DIRECTA** | - | - | - | - |
| **KPI 2: Ticket Promedio** | - | - | - | ✓ **DIRECTA** | - |
| **KPI 3: Factor de Ocupación** | - | - | - | - | ✓ **INDIRECTA** |
| **KPI 4: Estacionalidad** | - | ✓ **DIRECTA** | - | - | - |
| **KPI 5: Eficiencia por Hora** | - | - | ✓ **DIRECTA** | - | - |
| **KPI 6: Retorno por KM** | - | - | - | ✓ **DIRECTA** | - |
| **KPI 7: Fidelización** | - | - | - | - | ✓ **DIRECTA** |

### Tipo de Relación

- **Relación DIRECTA** (6/7 KPIs): El KPI mide exactamente lo que la hipótesis plantea
- **Relación INDIRECTA** (1/7 KPIs): El KPI se relaciona a través de un proxy o métrica correlacionada

### Cobertura de Hipótesis

| Hipótesis | KPIs Relacionados | Cobertura |
|-----------|-------------------|-----------|
| H1: Expansión Acelerada | KPI 1 | ✓ **COMPLETA** |
| H2: Patrones Estacionales | KPI 4 | ✓ **COMPLETA** |
| H3: Optimización Horaria | KPI 5 | ✓ **COMPLETA** |
| H4: Rentabilidad Segmentada | KPI 2, KPI 6 | ✓ **COMPLETA** (2 KPIs) |
| H5: Retención = Ingresos | KPI 3, KPI 7 | ✓ **COMPLETA** (2 KPIs) |

---

## Capacidad de Validación

### Poder de Validación por KPI

| KPI | Tipo de Validación | Refutación Posible | Confirma | Refuta | Parcial |
|-----|-------------------|--------------------|----------|--------|---------|
| **KPI 1: Crecimiento** | Cuantitativa | Sí | ✓ | ✓ | ✓ |
| **KPI 2: Ticket** | Segmentación | Sí | ✓ | ~ | ~ |
| **KPI 3: Ocupación** | Proxy | Limitada | ✓ | ✓ | ~ |
| **KPI 4: Estacionalidad** | Estadística | Sí | ✓ | ✓ | ~ |
| **KPI 5: Eficiencia Hora** | Operativa | Sí | ✓ | ✓ | ~ |
| **KPI 6: Retorno/KM** | Financiera | Sí | ✓ | ~ | ~ |
| **KPI 7: Fidelización** | Directa | Sí | ✓ | ✓ | ~ |

### Umbrales de Decisión

#### Confirmación de Hipótesis
- **H1 (Expansión)**: Crecimiento sostenido >20%
- **H2 (Estacionalidad)**: CV >0.3 con patrones claros
- **H3 (Horaria)**: Eficiencia variada >40% entre horas
- **H4 (Rentabilidad)**: Tickets/retorno variados por segmento
- **H5 (Retención)**: Fidelización >60% u ocupación >50%

#### Refutación de Hipótesis
- **H1 (Expansión)**: Crecimiento <10% sostenido
- **H2 (Estacionalidad)**: CV <0.2 sin patrones
- **H3 (Horaria)**: Eficiencia uniforme (<20% variación)
- **H4 (Rentabilidad)**: Sin diferencias significativas por segmento
- **H5 (Retención)**: Fidelización <40% y ocupación <30%

---

## Conclusiones Estratégicas

### 1. Alineación Completa

**Todos los KPIs tienen relación clara con al menos una hipótesis**, lo que demuestra que el sistema de métricas está estratégicamente alineado con las suposiciones fundamentales del negocio.

### 2. Cobertura Integral

**Las 5 hipótesis están completamente cubiertas** por el sistema de KPIs:
- 3 hipótesis tienen 1 KPI directo
- 2 hipótesis tienen 2 KPIs (complementarios)

### 3. Capacidad de Toma de Decisiones

**Cada KPI permite acciones concretas** según confirma o refuta su hipótesis asociada, facilitando la toma de decisiones basada en evidencia.

### 4. Sistema de Validación Robusto

**Los 7 KPIs forman un sistema completo** para validar las 5 hipótesis del negocio de Uber NYC (2009-2015), permitiendo:

- Monitoreo continuo de suposiciones clave
- Detección temprana de cambios en el modelo de negocio
- Optimización de recursos según hipótesis confirmadas
- Pivote estratégico basado en hipótesis refutadas

### 5. Recomendaciones de Implementación

1. **Automatizar monitoreo**: Configurar alertas automáticas cuando KPIs crucen umbrales de decisión
2. **Dashboard ejecutivo**: Visualizar estado de validación de hipótesis en tiempo real
3. **Revisión periódica**: Evaluar trimestralmente si hipótesis siguen siendo válidas
4. **Experimentación**: Usar KPIs para diseñar experiments que validen/refuten hipótesis más rápido
5. **Cascada de objetivos**: Alinear objetivos de equipos con hipótesis que impactan directamente

---

## Referencias

- **Dataset**: Uber NYC (2009-2015) - 191,133 registros
- **Documentación**: `RESUMEN_KPIS.md`
- **Análisis**: `KPIs_Analysis_Uber_NYC.ipynb`
- **ETL**: `etl_uber.ipynb`
- **Dashboard**: `DashboardEntrega3.pbix`

---

**Documento preparado para:** Análisis de Datos - ITM 2026-1
**Fecha:** Abril 2026
**Autoría:** Basado en análisis de KPIs definidos para Uber NYC
