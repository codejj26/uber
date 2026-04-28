# Fase 6: Análisis, validación y storytelling

## Interpretación de resultados

El análisis de KPIs sobre Uber NYC (2009-2015) muestra un negocio con señales claras de crecimiento, alta sensibilidad a la hora del día y una demanda con comportamiento estacional. El ticket promedio observado en el dataset limpio es de aproximadamente 11.21 USD por viaje, lo que ubica la operación en un rango intermedio entre volumen y valor. Además, el análisis descriptivo evidencia que la mayor parte de los viajes se concentra en trayectos cortos, mientras que los viajes largos aportan un retorno por kilómetro más favorable para la empresa.

En términos operativos, la ocupación promedio por viaje es baja frente a la capacidad máxima teórica del vehículo, lo que sugiere que el modelo depende principalmente de viajes individuales y no de aprovechamiento intensivo de la capacidad. Esto es consistente con una operación urbana enfocada en rapidez y disponibilidad más que en ocupación compartida. Por otra parte, la demanda por hora y por mes confirma que existen franjas y periodos de mayor presión operativa, por lo que la asignación de conductores y el pricing dinámico son palancas clave.

## Validación de hipótesis mediante pruebas estadísticas

La validación de las hipótesis debe distinguir entre evidencia descriptiva y evidencia inferencial. En este proyecto, los KPIs permiten observar patrones, pero para confirmar diferencias de forma estadística se recomienda aplicar pruebas de hipótesis según el tipo de variable:

**H1: Expansión acelerada.**
Se valida comparando ingresos y volumen de viajes por año con una prueba de tendencia o con regresión temporal. Si la pendiente es positiva y el valor p es menor a 0.05, se rechaza la hipótesis nula de ausencia de crecimiento y se concluye que la expansión es estadísticamente significativa.

**H2: Patrones estacionales.**
Se valida con un ANOVA o una prueba no paramétrica entre meses. Si el valor p es menor a 0.05, se rechaza la hipótesis de igualdad entre meses y se confirma que la demanda cambia de forma significativa según la temporada.

**H3: Optimización horaria.**
Se puede validar comparando ingresos por hora con ANOVA o Kruskal-Wallis. Un valor p menor a 0.05 indicaría que no todas las horas generan el mismo nivel de ingreso y que existen franjas críticas para operación y pricing.

**H4: Rentabilidad segmentada.**
Se valida comparando ticket promedio y retorno por kilómetro entre segmentos de distancia. Si el valor p es menor a 0.05, se concluye que la rentabilidad no es uniforme y que el segmento sí afecta el desempeño económico.

**H5: Retención e ingresos sostenibles.**
En este dataset no existe un identificador de usuario real, por lo que esta hipótesis solo puede aproximarse mediante proxies de consistencia temporal. Para una validación estadística robusta se necesitaría un `user_id` o un identificador equivalente; sin ese dato, no es posible calcular una prueba concluyente de fidelización.

## Uso del valor p para la toma de decisiones

El valor p debe interpretarse como un criterio de evidencia, no como una verdad absoluta. Si p < 0.05, se rechaza la hipótesis nula y se adopta una decisión basada en evidencia estadística. Si p >= 0.05, no hay evidencia suficiente para afirmar que la diferencia observada sea real y no producto del azar.

Aplicado al negocio, esto significa lo siguiente: si la diferencia de ingresos entre horas pico y horas valle resulta significativa, Uber debe priorizar oferta de conductores y mecanismos de incentivo en esas horas. Si la estacionalidad mensual es significativa, se justifican planes de capacidad diferenciados por temporada. Si la rentabilidad por distancia difiere de forma significativa, el pricing y las estrategias de asignación de viajes deben ajustarse por segmento.

## Construcción de narrativa con los datos

La historia que cuentan los datos es la de una plataforma urbana que crece apoyada en una demanda masiva, pero cuya rentabilidad depende de optimizar momento, distancia y capacidad. El crecimiento anual respalda la fase de expansión; la concentración horaria muestra que la operación no es uniforme; y la rentabilidad por kilómetro evidencia que no todos los viajes aportan el mismo valor.

En otras palabras, Uber no gana únicamente por tener más viajes, sino por gestionar mejor qué viajes prioriza, cuándo los atiende y cómo distribuye su capacidad. El negocio se fortalece cuando convierte datos operativos en decisiones de asignación, pricing y retención.

## Propuesta de decisiones basadas en evidencia

1. Reforzar la oferta de conductores en las franjas de mayor eficiencia horaria y usar incentivos específicos en horas valle.
2. Ajustar la estrategia de pricing dinámico según la hora y el segmento de distancia para maximizar retorno por kilómetro.
3. Planificar capacidad y campañas de adquisición según los meses con mayor variación de demanda.
4. Priorizar trayectos y segmentos con mejor equilibrio entre ticket promedio y retorno por distancia.
5. Incorporar identificadores de usuario para medir fidelización real, frecuencia de uso y valor de vida del cliente.

## Discusión de limitaciones

El análisis presenta limitaciones importantes. La principal es la ausencia de un identificador de usuario, lo que impide medir fidelización de manera exacta. También hay una dependencia fuerte de métricas agregadas, por lo que no se observan diferencias individuales ni comportamientos microsegmentados. Adicionalmente, el dataset cubre un periodo histórico específico y no necesariamente representa el comportamiento actual de la plataforma.

Otra limitación es que varias conclusiones son descriptivas y requieren pruebas inferenciales adicionales para afirmarse con rigor estadístico. Sin esas pruebas, se puede hablar de patrones observados, pero no de causalidad. Finalmente, variables como clima, eventos especiales, congestión vial, competencia local o cambios regulatorios no están incluidas y podrían explicar parte de las variaciones detectadas.

## Conclusión

La evidencia disponible sugiere que Uber operó en Nueva York con un patrón de expansión fuerte, alta sensibilidad temporal y rentabilidad desigual entre segmentos. La lectura estratégica es clara: crecer no basta; hay que crecer con inteligencia operativa, enfocando recursos en las horas, periodos y segmentos con mayor retorno.