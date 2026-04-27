"""
Análisis de KPIs - Uber NYC (2009-2015)
=======================================
Este script define, calcula e interpreta KPIs clave para el negocio de Uber
basados en el dataset de viajes en Nueva York (2009-2015).
"""

import pandas as pd
import numpy as np

def print_section(title: str):
    print("\n" + "=" * 80)
    print(f" {title}")
    print("=" * 80)

def load_and_clean_data():
    """Carga y limpia el dataset aplicando el mismo proceso ETL del notebook."""
    print_section("1. CARGA Y LIMPIEZA DE DATOS")

    df = pd.read_csv("uber.csv")

    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])

    print(f"Registros originales: {len(df):,}")

    # Eliminar duplicados y nulos
    df.drop_duplicates(inplace=True)

    numeric_columns = ["fare_amount", "pickup_longitude", "pickup_latitude",
                      "dropoff_longitude", "dropoff_latitude", "passenger_count"]
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    critical_columns = ["pickup_datetime"] + numeric_columns
    df.dropna(subset=critical_columns, inplace=True)

    # Convertir datetime
    df["pickup_datetime"] = pd.to_datetime(df["pickup_datetime"], utc=True, errors="coerce")
    df.dropna(subset=["pickup_datetime"], inplace=True)

    # Filtros de calidad
    mask_fare = (df["fare_amount"] > 0) & (df["fare_amount"] <= 200)
    df = df[mask_fare]

    def coordenadas_validas_nyc(lat, lon):
        lat_min, lat_max = 40.4774, 40.9176
        lon_min, lon_max = -74.2591, -73.7004
        return (lat >= lat_min) & (lat <= lat_max) & (lon >= lon_min) & (lon <= lon_max)

    mask_pickup = coordenadas_validas_nyc(df["pickup_latitude"], df["pickup_longitude"])
    mask_dropoff = coordenadas_validas_nyc(df["dropoff_latitude"], df["dropoff_longitude"])
    df = df[mask_pickup & mask_dropoff].copy()

    mask_pax = (df["passenger_count"] >= 1) & (df["passenger_count"] <= 6)
    df = df[mask_pax].copy()

    print(f"Registros tras limpieza: {len(df):,}")
    print(f"Retención: {len(df) / 200000 * 100:.2f}%")

    return df

def transform_data(df):
    """Aplica transformaciones necesarias para cálculo de KPIs."""
    print_section("2. TRANSFORMACIÓN DE DATOS PARA KPIs")

    # Variables temporales
    df["year"] = df["pickup_datetime"].dt.year
    df["month"] = df["pickup_datetime"].dt.month
    df["day_of_week"] = df["pickup_datetime"].dt.dayofweek
    df["hour"] = df["pickup_datetime"].dt.hour

    # Calcular distancia con Haversine
    def haversine(lat1, lon1, lat2, lon2):
        R = 6371
        lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = np.sin(dlat / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2) ** 2
        c = 2 * np.arcsin(np.sqrt(a))
        return R * c

    df["distance_km"] = haversine(
        df["pickup_latitude"].values,
        df["pickup_longitude"].values,
        df["dropoff_latitude"].values,
        df["dropoff_longitude"].values,
    )

    # Filtros de calidad adicionales
    df = df[df["distance_km"] >= 0.1].copy()
    df["fare_per_km"] = df["fare_amount"] / df["distance_km"]
    df = df[df["fare_per_km"] <= 30].copy()

    print(f"Registros finales para KPIs: {len(df):,}")

    return df

def calcular_kpis(df):
    """Calcula los KPIs principales del negocio."""
    print_section("3. CÁLCULO DE KPIS")

    kpis = {}

    # KPI 1: Ingreso Promedio por Viaje (APV - Average Fare per Ride)
    kpis["ingreso_promedio_por_viaje"] = {
        "valor": df["fare_amount"].mean(),
        "descripcion": "Ingreso promedio generado por cada viaje",
        "unidad": "USD"
    }

    # KPI 2: Tasa de Ocupación Promedio (Average Occupancy Rate)
    kpis["tasa_ocupacion_promedio"] = {
        "valor": df["passenger_count"].mean(),
        "descripcion": "Promedio de pasajeros por viaje (ocupación del vehículo)",
        "unidad": "pasajeros"
    }

    # KPI 3: Ingreso por Kilómetro (Revenue per KM)
    kpis["ingreso_por_km"] = {
        "valor": (df["fare_amount"].sum() / df["distance_km"].sum()),
        "descripcion": "Ingreso total generado por cada kilómetro recorrido",
        "unidad": "USD/km"
    }

    # KPI 4: Distancia Promedio por Viaje (Average Trip Distance)
    kpis["distancia_promedio_viaje"] = {
        "valor": df["distance_km"].mean(),
        "descripcion": "Distancia promedio recorrida por viaje",
        "unidad": "km"
    }

    # KPI 5: Eficiencia de Ingreso por Pasajero (Revenue per Passenger)
    kpis["ingreso_por_pasajero"] = {
        "valor": (df["fare_amount"].sum() / df["passenger_count"].sum()),
        "descripcion": "Ingreso generado por cada pasajero transportado",
        "unidad": "USD/pasajero"
    }

    # KPI 6: Tasa de Crecimiento Anual (Year-over-Year Growth Rate)
    yearly_revenue = df.groupby("year")["fare_amount"].sum()
    if len(yearly_revenue) > 1:
        growth_rates = yearly_revenue.pct_change() * 100
        kpis["tasa_crecimiento_anual"] = {
            "valor": growth_rates.mean(),
            "descripcion": "Tasa promedio de crecimiento anual de ingresos",
            "unidad": "%"
        }

    # KPI 7: Precio por Kilómetro Promedio (Average Price per KM)
    kpis["precio_por_km_promedio"] = {
        "valor": df["fare_per_km"].mean(),
        "descripcion": "Precio promedio cobrado por kilómetro recorrido",
        "unidad": "USD/km"
    }

    return kpis

def analizar_kpis_por_dimension(df):
    """Analiza los KPIs desglosados por dimensiones clave."""
    print_section("4. ANÁLISIS DE KPIS POR DIMENSIÓN")

    analisis = {}

    # Por año
    analisis["por_año"] = df.groupby("year").agg({
        "fare_amount": ["sum", "mean", "count"],
        "distance_km": "mean",
        "passenger_count": "mean"
    }).round(2)

    # Por franja horaria
    df["time_of_day"] = df["hour"].apply(lambda h:
        "Madrugada" if 0 <= h < 6 else
        "Mañana" if 6 <= h < 12 else
        "Tarde" if 12 <= h < 18 else "Noche"
    )

    analisis["por_franja_horaria"] = df.groupby("time_of_day").agg({
        "fare_amount": ["mean", "count"],
        "distance_km": "mean",
        "passenger_count": "mean"
    }).round(2)

    # Por día de la semana
    dias = {0: "Lunes", 1: "Martes", 2: "Miércoles", 3: "Jueves",
            4: "Viernes", 5: "Sábado", 6: "Domingo"}
    df["day_name"] = df["day_of_week"].map(dias)

    analisis["por_dia_semana"] = df.groupby("day_name").agg({
        "fare_amount": ["mean", "count"],
        "distance_km": "mean"
    }).round(2)

    return analisis

def interpretar_kpis(kpis, analisis):
    """Interpreta los KPIs y genera insights de negocio."""
    print_section("5. INTERPRETACIÓN DE KPIS E INSIGHTS DE NEGOCIO")

    print("\n📊 KPI 1: INGRESO PROMEDIO POR VIAJE")
    print(f"   Valor: ${kpis['ingreso_promedio_por_viaje']['valor']:.2f}")
    print("   💼 Justificación de Negocio:")
    print("   - Indica cuánto gana en promedio Uber por cada viaje realizado")
    print("   - Fundamental para proyectar ingresos y evaluar rentabilidad")
    print("   - Permite comparar con competidores y benchmark de mercado")
    print("   🎯 Hipótesis Relacionada:")
    print("   - H1: Las tarifas varían según hora del día y ubicación")

    print("\n📊 KPI 2: EFICIENCIA DE OCUPACIÓN")
    print(f"   Valor: {kpis['tasa_ocupacion_promedio']['valor']:.2f} pasajeros/viaje")
    print("   💼 Justificación de Negocio:")
    print("   - Maximizar la ocupación es clave para la rentabilidad de Uber")
    print("   - Mayor ocupación = mejor uso del activo (vehículo)")
    print("   - Influye directamente en el ingreso por viaje")
    print("   🎯 Hipótesis Relacionada:")
    print("   - H2: La ocupación varía según franja horaria (compartidos vs individuales)")

    print("\n📊 KPI 3: INGRESO POR KILÓMETRO")
    print(f"   Valor: ${kpis['ingreso_por_km']['valor']:.2f} por km")
    print("   💼 Justificación de Negocio:")
    print("   - Mide la eficiencia generadora de ingresos por distancia recorrida")
    print("   - Permite optimizar rutas y estrategias de定价")
    print("   - Indica qué tan rentables son los viajes según distancia")
    print("   🎯 Hipótesis Relacionada:")
    print("   - H3: Los viajes cortos tienen mayor ingreso por km que los largos")

    print("\n📊 KPI 4: DISTANCIA PROMEDIO POR VIAJE")
    print(f"   Valor: {kpis['distancia_promedio_viaje']['valor']:.2f} km")
    print("   💼 Justificación de Negocio:")
    print("   - Define el perfil típico de viaje en NYC")
    print("   - Impacta tiempos de viaje y disponibilidad de conductores")
    print("   - Ayuda a planificar cobertura geográfica del servicio")
    print("   🎯 Hipótesis Relacionada:")
    print("   - H4: Las distancias varían según zonas de NYC y hora del día")

    print("\n📊 KPI 5: INGRESO POR PASAJERO")
    print(f"   Valor: ${kpis['ingreso_por_pasajero']['valor']:.2f} por pasajero")
    print("   💼 Justificación de Negocio:")
    print("   - Mide el valor generado por cada usuario del servicio")
    print("   - Fundamental para calcular LTV (Lifetime Value) del cliente")
    print("   - Permite evaluar el retorno de inversión en adquisición de clientes")
    print("   🎯 Hipótesis Relacionada:")
    print("   - H5: El ingreso por pasajero es mayor en horas pico")

    if "tasa_crecimiento_anual" in kpis:
        print("\n📊 KPI 6: TASA DE CRECIMIENTO ANUAL")
        print(f"   Valor: {kpis['tasa_crecimiento_anual']['valor']:.1f}%")
        print("   💼 Justificación de Negocio:")
        print("   - Mide la velocidad de expansión del negocio")
        print("   - Indica salud del crecimiento y penetración de mercado")
        print("   - Clave para inversores y planificación estratégica")
        print("   🎯 Hipótesis Relacionada:")
        print("   - H6: El crecimiento se acelera con la adopción masiva de smartphones")

    print("\n📊 KPI 7: PRECIO POR KILÓMETRO PROMEDIO")
    print(f"   Valor: ${kpis['precio_por_km_promedio']['valor']:.2f} por km")
    print("   💼 Justificación de Negocio:")
    print("   - Indica el precio base del servicio por unidad de distancia")
    print("   - Permite comparar competitividad en precios")
    print("   - Base para cálculos de tarifas dinámicas y promociones")
    print("   🎯 Hipótesis Relacionada:")
    print("   - H7: El precio por km varía según demanda (dinámica de precios)")

    print_section("6. ANÁLISIS TEMPORAL DE KPIS")
    print("\n📈 EVOLUCIÓN POR AÑO:")
    print(analisis["por_año"])

    print("\n⏰ COMPORTAMIENTO POR FRANJA HORARIA:")
    print(analisis["por_franja_horaria"])

    print("\n📅 PATRONES POR DÍA DE LA SEMANA:")
    print(analisis["por_dia_semana"])

def main():
    """Función principal del análisis de KPIs."""
    print("🚖 ANÁLISIS DE KPIS - UBER NYC (2009-2015)")
    print("=" * 80)

    # Cargar y limpiar datos
    df = load_and_clean_data()

    # Transformar datos
    df = transform_data(df)

    # Calcular KPIs
    kpis = calcular_kpis(df)

    # Analizar por dimensiones
    analisis = analizar_kpis_por_dimension(df)

    # Interpretar resultados
    interpretar_kpis(kpis, analisis)

    print_section("7. GUARDAR RESULTADOS")

    # Crear DataFrame con KPIs
    kpi_df = pd.DataFrame([
        {
            "KPI": k,
            "Valor": f"{v['valor']:.2f} {v['unidad']}",
            "Descripción": v['descripcion']
        }
        for k, v in kpis.items()
    ])

    kpi_df.to_csv("kpis_resumen.csv", index=False)
    print("✅ KPIs guardados en 'kpis_resumen.csv'")

    # Guardar análisis detallado
    with open("kpis_interpretacion.txt", "w", encoding="utf-8") as f:
        f.write("ANÁLISIS DETALLADO DE KPIS - UBER NYC (2009-2015)\n")
        f.write("=" * 80 + "\n\n")

        for kpi_name, kpi_data in kpis.items():
            f.write(f"\n{kpi_name.upper()}\n")
            f.write(f"Valor: {kpi_data['valor']:.2f} {kpi_data['unidad']}\n")
            f.write(f"Descripción: {kpi_data['descripcion']}\n")

    print("✅ Interpretación detallada guardada en 'kpis_interpretacion.txt'")

    print_section("✅ ANÁLISIS COMPLETADO")
    print("Se han definido, calculado e interpretado 7 KPIs clave para el negocio.")
    print("Cada KPI incluye justificación de negocio y relación con hipótesis.")

if __name__ == "__main__":
    main()