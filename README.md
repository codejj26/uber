# Proyecto BI - Uber NYC (2009-2015)

Este repositorio contiene el proyecto de Analisis de Datos sobre viajes de Uber en Nueva York (2009-2015). Incluye el proceso ETL, el analisis de KPIs, la documentacion y el dashboard en Power BI.

## Contenido

- Notebooks
  - etl_uber.ipynb: limpieza, transformaciones y generacion del dataset limpio.
  - KPIs_Analysis_Uber_NYC.ipynb: analisis exploratorio y calculo de KPIs.
- Datos
  - uber.csv: dataset original.
  - uber_clean.csv: dataset limpio para analisis.
- Documentacion
  - fase1y2.md: fases 1 y 2 del proyecto (problema e hipotesis).
  - RESUMEN_KPIS.md: relacion entre KPIs e hipotesis con redaccion academica.
  - Analisis_DashBoard.md: fase 6 (analisis, validacion y storytelling).
- Visualizacion
  - DashboardEntrega3.pbix: dashboard de Power BI.

## Requisitos

- Python 3.x
- Paquetes en requirements.txt

## Configuracion rapida

1. Crear entorno virtual (opcional) y activar.
2. Instalar dependencias:

```
pip install -r requirements.txt
```

## Ejecucion

- Ejecutar etl_uber.ipynb para generar uber_clean.csv.
- Ejecutar KPIs_Analysis_Uber_NYC.ipynb para el analisis y KPIs.
- Abrir DashboardEntrega3.pbix en Power BI para visualizar el dashboard.

## Notas

- El dataset cubre el periodo 2009-2015.
- Algunas metricas requieren proxies por ausencia de identificadores de usuario.
