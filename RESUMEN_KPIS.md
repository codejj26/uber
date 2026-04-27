# Análisis de KPIs - Uber NYC (2009-2015)

## Resumen Ejecutivo

Este documento define 7 KPIs clave para el análisis de negocio de Uber en Nueva York durante el periodo 2009-2015, alineados con las hipótesis fundamentales del negocio.

---

## Hipótesis del Negocio

1. H1: Expansión Acelerada - Uber está en fase de crecimiento agresivo (2009-2015)
2. H2: Patrones Estacionales - La demanda muestra variaciones predecibles por temporada
3. H3: Optimización Horaria - La eficiencia operativa depende de patrones horarios
4. H4: Rentabilidad Segmentada - La rentabilidad varía según distancia y ocupación
5. H5: Retención = Ingresos - La fidelización de usuarios impacta directamente en ingresos sostenibles

---

## KPI 1: Tasa de Crecimiento de Ingresos

### Definición
```
Tasa de Crecimiento = ((Ingresos_Periodo_Actual - Ingresos_Periodo_Anterior) / Ingresos_Periodo_Anterior) × 100
```

### Justificación desde el Negocio
**Hipótesis Relacionada:** H1 - Expansión Acelerada

Este KPI es critico porque:
- Valida el modelo de negocio y demuestra potencial de crecimiento
- Atrae inversionistas mediante evidencia de escalabilidad
- Justifica asignacion de recursos para marketing y tecnologia
- Permite benchmarking contra alternativas de transporte tradicional
- Facilita planificacion estrategica de infraestructura

### Interpretación
- Crecimiento > 20%: Expansion agresiva exitosa, invertir en escala
- Crecimiento 10-20%: Crecimiento saludable, mantener estrategia
- Crecimiento 0-10%: Maduracion del mercado, buscar nuevas oportunidades
- Crecimiento negativo: Alerta temprana de problemas, requiere intervencion inmediata

---

## KPI 2: Ticket Promedio

### Definición
```
Ticket Promedio = Total Ingresos / Total Viajes
```

### Justificación desde el Negocio
**Hipótesis Relacionada:** H4 - Rentabilidad Segmentada

Este KPI es fundamental porque:
- Mide el valor promedio que los clientes estan dispuestos a pagar
- Permite segmentacion de mercado (alto valor vs. comodidad)
- Optimiza pricing dinamico por zona/horario
- Base para proyeccion de ingresos y modelado de escenarios
- Benchmark contra taxis tradicionales y otros rideshare

### Interpretación
- Ticket > $15: Segmento premium, mayor margen por viaje
- Ticket $10-15: Rango optimo de equilibrio volumen-valor
- Ticket $5-10: Segmento alta frecuencia, bajo margen
- Ticket < $5: Alerta de posible subsidiacion excesiva

---

## KPI 3: Factor de Ocupación

### Definición
```
Factor de Ocupación = Pasajeros Promedio por Viaje / Capacidad Máxima (6 pasajeros)
Pasajeros Promedio = Total Pasajeros Transportados / Total Viajes
```

### Justificación desde el Negocio
**Hipótesis Relacionada:** H5 - Retención Impacta Ingresos

Este KPI es critico porque:
- Muestra eficiencia de utilizacion de la flota disponible
- Factor ESG clave (mas pasajeros = menor huella de carbono)
- Cada pasajero adicional es ingreso puro sin costo marginal significativo
- Patrones altos pueden indicar rutas consolidadas
- Disenar campanas para fomentar viajes compartidos

### Interpretación
- Ocupacion > 50%: Excelente uso de capacidad, alto impacto ambiental positivo
- Ocupacion 30-50%: Uso moderado, oportunidad para promover ridesharing
- Ocupacion < 30%: Alta dependencia de viajes individuales, margen de mejora

---

## KPI 4: Índice de Estacionalidad de la Demanda

### Definición
```
Índice de Estacionalidad = (Viajes en Período / Viajes Promedio Mensual) × 100
Coeficiente de Variación = (Desviación Estándar Viajes Mensuales / Media Viajes Mensuales)
```

### Justificación desde el Negocio
**Hipótesis Relacionada:** H2 - Patrones Estacionales

Este KPI es estratégico porque:
- Permite anticipar picos y valles de demanda
- Ajusta numero de conductores segun temporada
- Timing optimo para promociones y adquisicion de usuarios
- Prediccion mas precisa de ingresos futuros
- Optimizar gastos operativos segun demanda proyectada

### Interpretación
- CV > 0.3: Alta estacionalidad, requiere planificacion detallada por temporada
- CV 0.2-0.3: Estacionalidad moderada, planificacion por trimestres
- CV < 0.2: Baja estacionalidad, demanda relativamente estable

---

## KPI 5: Eficiencia por Hora

### Definición
```
Ingresos por Hora = Total Ingresos en Franja Horaria / Total Horas Operativas en Franja
Eficiencia Relativa = Ingresos por Hora de Franja / Ingresos por Hora Promedio × 100
```

### Justificación desde el Negocio
**Hipótesis Relacionada:** H3 - Optimización Horaria

Este KPI es operacionalmente critico porque:
- Permite optimizar turnos y horarios de mayor rentabilidad
- Disenar bonos por hora en periodos de alta demanda
- Implementar surge pricing en horas de alta presion
- Pautar publicidad en horas de menor eficiencia
- Identificar brechas entre disponibilidad de conductores y demanda

### Interpretación
- Eficiencia > 120%: Hora pico, priorizar disponibilidad de conductores
- Eficiencia 80-120%: Hora normal, operacion estandar
- Eficiencia < 80%: Hora valle, oportunidad para promociones

---

## KPI 6: Retorno por Kilómetro

### Definición
```
Retorno por KM = Total Ingresos / Total Kilómetros Recorridos
Retorno por KM por Segmento = Ingresos Segmento / Kilómetros Segmento
```

### Justificación desde el Negocio
**Hipótesis Relacionada:** H4 - Rentabilidad Segmentada

Este KPI es financieramente estratégico porque:
- Mide la eficiencia economica de cada kilometro operado
- Identifica viajes cortos vs. largos y su rentabilidad diferencial
- Permite disenar estrategias para maximizar retorno por distancia
- Benchmark contra costos operativos (combustible, mantenimiento)
- Estructurar bonificaciones a conductores por kilometro rentable

### Interpretación
- Retorno > $5/KM: Segmento premium de alta rentabilidad
- Retorno $3-5/KM: Rango optimo de equilibrio
- Retorno < $3/KM: Segmento de baja rentabilidad, revisar estructura de costos

---

## KPI 7: Índice de Fidelización de Usuarios

### Definición
```
Índice de Fidelización = (Usuarios con Múltiples Viajes / Total Usuarios Únicos) × 100
Frecuencia Promedio = Total Viajes / Total Usuarios Únicos
```

### Justificación desde el Negocio
**Hipótesis Relacionada:** H5 - Retención Impacta Ingresos

Este KPI es estratégico para crecimiento sostenible porque:
- Retener usuarios es 5x mas economico que adquirir nuevos
- Usuarios recurrentes generan mayor valor a lo largo del tiempo
- Alta fidelizacion crea barreras de entrada para competidores
- Base de usuarios leales permite forecast mas preciso
- Usuarios fieles recomiendan el servicio, reduciendo CAC

### Interpretación
- Fidelizacion > 60%: Base de usuarios muy leales, activar programas de referidos
- Fidelizacion 40-60%: Saludable, foco en aumentar frecuencia de uso
- Fidelizacion < 40%: Alta dependencia de adquisicion, revisar experiencia de usuario

Nota: Este KPI requiere tracking de usuarios unicos para medicion precisa. En este dataset se usan proxies.

---

## Resumen de Implementación

### Tabla de KPIs

| KPI | Fórmula | Unidad | Frecuencia | Dueño |
|-----|---------|--------|-------------|-------|
| 1. Tasa de Crecimiento | (Ingresos Actual - Ingresos Anterior) / Ingresos Anterior × 100 | % | Mensual | VP de Crecimiento |
| 2. Ticket Promedio | Total Ingresos / Total Viajes | USD | Semanal | Director de Pricing |
| 3. Factor de Ocupación | Pasajeros Promedio / Capacidad Máxima (6) | % | Diaria | Ops. de Flota |
| 4. Índice de Estacionalidad | Viajes Período / Viajes Promedio Mensual × 100 | Índice | Mensual | Planificación |
| 5. Eficiencia por Hora | Ingresos por Hora / Ingresos por Hora Promedio × 100 | % | Diaria | Gerente de Turnos |
| 6. Retorno por Kilómetro | Total Ingresos / Total Kilómetros | USD/KM | Semanal | Director Financiero |
| 7. Índice de Fidelización | Usuarios Múltiples Viajes / Total Usuarios × 100 | % | Mensual | Marketing |

### Alineación con Hipótesis

| Hipotesis | KPIs Relacionados | Validacion |
|-----------|-------------------|-------------|
| H1: Expansion Acelerada | KPI 1 (Tasa de Crecimiento) | Medicion directa |
| H2: Patrones Estacionales | KPI 4 (Estacionalidad) | Analisis temporal |
| H3: Optimizacion Horaria | KPI 5 (Eficiencia por Hora) | Gestion operativa |
| H4: Rentabilidad Segmentada | KPI 2 (Ticket), KPI 6 (Retorno/KM) | Analisis de segmentos |
| H5: Retencion = Ingresos | KPI 7 (Fidelizacion), KPI 3 (Ocupacion) | Metricas de lealtad |

---

## Proximos Pasos Recomendados

1. Automatizacion: Configurar dashboards en Power BI con alertas automaticas
2. Benchmarking: Comparar KPIs contra industria y competidores
3. Analisis Predictivo: Modelar tendencias futuras basado en datos historicos
4. Experimentacion: A/B testing para optimizar variables clave (pricing, incentivos)
5. Segmentacion Avanzada: Incorporar datos demograficos y geograficos para analisis mas granular

---

## Archivos del Proyecto

- `KPIs_Analysis_Uber_NYC.ipynb` - Notebook completo con análisis de 7 KPIs
- `etl_uber.ipynb` - Proceso ETL de datos
- `uber_clean.csv` - Dataset limpio para análisis
- `DashboardEntrega3.pbix` - Dashboard de Power BI

Curso: Analisis de Datos - ITM 2026-1
**Periodo:** Abril 2026
**Dataset:** Uber NYC (2009-2015) - 191,133 registros
