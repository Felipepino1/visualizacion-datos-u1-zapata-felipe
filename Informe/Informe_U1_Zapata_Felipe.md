# Informe: Análisis Crítico, Ensayo y Reflexión

## Introducción

Este informe reúne las Partes II, III y IV de la Evaluación Sumativa de la Unidad 1. La Parte II analiza tres visualizaciones reales publicadas por un organismo gubernamental (INE), un observatorio de datos internacional (Our World in Data) y un informe institucional (Banco Central de Chile). La Parte III es un ensayo sobre cómo la visualización transforma datos en conocimiento útil para decidir, y la Parte IV reflexiona sobre el aporte de Obsidian y GitHub a la gestión del conocimiento. Todo el análisis se apoya en los conceptos desarrollados en la bóveda de Obsidian, construida a partir del libro *Visualización de la información: De los datos al conocimiento* de Ignasi Alcalde.

---

# PARTE II: Análisis Crítico de Visualizaciones Reales

Criterios usados en las tres evaluaciones (ver notas [Buenas Prácticas], [Tipos de Gráficos] y [Usuarios] de la bóveda):

- **Claridad:** ¿el mensaje principal se entiende en pocos segundos?
- **Buenas prácticas:** título, ejes, escalas, fuente, uso de color, relación datos-tinta (Tufte).
- **Interpretación:** ¿qué podría entender mal un lector no experto?
- **Sesgos:** ¿qué decisiones de diseño o de datos inclinan la lectura?

## Visualización 1: Evolución de la tasa de desocupación según sexo (INE)

[[FIGURA:1]]

### 1. Descripción

| Elemento | Detalle |
|---|---|
| **Fuente** | Instituto Nacional de Estadísticas (INE). *Boletín Estadístico: Empleo Trimestral*, edición N.º 331, 29 de mayo de 2026. Gráfico 1: «Evolución tasa de desocupación, según sexo, total país, trimestres móviles». |
| **Contexto** | La Encuesta Nacional de Empleo (ENE) publica todos los meses la situación del mercado laboral. En el trimestre febrero-abril 2026 la desocupación llegó a 9,1 % (mujeres 10,5 %, hombres 8,0 %), dentro de un período de desempleo persistentemente sobre el 8 %. |
| **Audiencia objetivo** | Autoridades, economistas, prensa y ciudadanía interesada. El boletín es un documento técnico, pero su gráfico se reproduce mucho en los medios. |

### 2. Evaluación técnica

| Aspecto | Evaluación |
|---|---|
| **Tipo de gráfico** | Gráfico de líneas múltiples (serie temporal). |
| **Variables** | Eje X: 13 trimestres móviles (feb-abr 2025 a feb-abr 2026), variable temporal ordinal. Eje Y: tasa de desocupación (%), variable cuantitativa continua. Series: total país, mujeres y hombres (variable categórica nominal). |
| **Calidad de representación** | Adecuada: la línea es la forma correcta para mostrar evolución en el tiempo ([Tipos de Gráficos]) y permite comparar la brecha entre sexos. |
| **Nivel de complejidad** | Bajo a medio. Se lee sin formación técnica, aunque el concepto de «trimestre móvil» exige conocimiento previo. |

### 3. Evaluación crítica

- **Claridad visual:** el gráfico es limpio y cumple la idea de Tufte de máxima simplicidad. Con tres series y un solo indicador no hay sobrecarga, lo que evita la [Infoxicación].
- **Buenas prácticas:** cita la fuente y define el indicador. En un gráfico de líneas, que el eje Y no parta en cero es aceptable, pero amplifica visualmente variaciones de pocas décimas.
- **Problemas de interpretación:**
  1. *Trimestres móviles superpuestos:* dos puntos consecutivos comparten dos de sus tres meses. Un lector común puede leer cada punto como un dato independiente y sobrestimar la velocidad del cambio.
  2. *Error muestral:* la ENE es una encuesta y sus cifras tienen margen de error. El gráfico muestra líneas «exactas», sin bandas de confianza. El texto del boletín sí indica qué variaciones son estadísticamente significativas, pero el gráfico no lo refleja ([Calidad de Datos]).
- **Posibles sesgos:** la ventana de solo 12 meses impide ver si el nivel actual es alto o bajo en perspectiva histórica (sesgo de encuadre temporal). La elección del período puede hacer parecer un alza puntual algo que es una tendencia, o al revés.

### 4. Propuesta de mejora

- **Modificaría** el título por uno declarativo que comunique la conclusión, por ejemplo: «La desocupación femenina sube a 10,5 % y amplía la brecha con los hombres». Esto aplica el principio de un solo mensaje simple y concreto ([Paradoja del Conocimiento], [Storytelling]).
- **Eliminaría** la leyenda separada y la reemplazaría por etiquetas directas al final de cada línea, para que el ojo no tenga que ir y volver ([Percepción Visual]).
- **Agregaría** bandas sombreadas de intervalo de confianza, una anotación sobre los trimestres con variación significativa y una línea de referencia del promedio de los últimos 5 años.
- **Visualización propuesta:** un gráfico de líneas con período extendido (por ejemplo, desde 2018) y un segundo panel pequeño con la **brecha** mujeres–hombres en puntos porcentuales. En la versión web, un selector de período para explorar ([Interactividad]).

## Visualización 2: Emisiones de CO₂ per cápita (Our World in Data)

[[FIGURA:2]]

### 1. Descripción

| Elemento | Detalle |
|---|---|
| **Fuente** | Our World in Data (Universidad de Oxford / Global Change Data Lab). Gráfico interactivo «CO₂ emissions per capita», con datos del *Global Carbon Budget* (2025) y estimaciones de población. Última actualización: 13 de noviembre de 2025. |
| **Contexto** | Las emisiones globales se mantienen cerca de 5 toneladas por persona desde hace más de una década, con grandes diferencias entre países. Es un insumo frecuente en la discusión sobre cambio climático. |
| **Audiencia objetivo** | Público general, periodistas, docentes, estudiantes e investigadores. Es un ejemplo de [Datos Abiertos]: los datos se pueden descargar en CSV y consultar por API. |

### 2. Evaluación técnica

| Aspecto | Evaluación |
|---|---|
| **Tipo de gráfico** | Gráfico de líneas interactivo con pestañas para cambiar a mapa coroplético y tabla. |
| **Variables** | Eje X: año (1750-2024). Eje Y: toneladas de CO₂ por persona (cuantitativa continua, razón). Países y regiones como series (nominal). En el mapa, el país es una variable geográfica y el color codifica la magnitud. |
| **Calidad de representación** | Alta. Las vistas de línea y mapa responden a preguntas distintas (evolución y distribución geográfica). La metodología está documentada. |
| **Nivel de complejidad** | Medio. La lectura básica es simple, pero las notas metodológicas (emisiones territoriales, exclusiones) requieren conocimiento previo. |

### 3. Evaluación crítica

- **Claridad visual:** muy buena. Diseño minimalista, etiquetas directas en las líneas y fuente visible en el pie. Cumple la estructura introducción, cuerpo y pie que Alcalde describe ([Estructura de la Infografía]).
- **Buenas prácticas:** cita la fuente, permite descargar los datos y explica la metodología. Es un caso ejemplar de visualización exploratoria en el sentido de Cairo ([Visualización de Datos], [Interactividad]).
- **Problemas de interpretación:**
  1. *Per cápita vs. total:* un país pequeño con alto consumo puede aparecer como «gran emisor» aunque su aporte al total mundial sea mínimo, y al revés.
  2. *Escala de colores del mapa:* los cortes de las categorías influyen en qué países parecen «iguales». Diferencias grandes dentro de un mismo color quedan ocultas.
- **Posibles sesgos:** el indicador mide **emisiones territoriales**, es decir, producidas dentro de las fronteras. Los países que importan bienes manufacturados (principalmente economías desarrolladas) aparecen con menos emisiones que si se midiera el consumo. Además, excluye el cambio de uso de suelo, relevante para países con deforestación. No es un error, pero el enfoque elegido favorece cierta lectura.

### 4. Propuesta de mejora

- **Modificaría** la vista por defecto para mostrar juntas la serie territorial y la basada en consumo (OWID tiene ambas por separado), haciendo visible el sesgo en vez de dejarlo en una nota.
- **Eliminaría** de la vista inicial los años anteriores a 1850, donde casi todos los países están en cero y la escala comprime el período relevante.
- **Agregaría** una línea de referencia con el promedio mundial y una anotación destacando a Chile frente a América Latina, para orientar a un usuario local ([Usuarios]).
- **Visualización propuesta:** *small multiples* (pequeños múltiplos) con dos paneles por país, uno de emisiones totales y otro per cápita. Así el lector ve la responsabilidad absoluta y la relativa sin confundirlas.

## Visualización 3: Proyección de inflación (Banco Central de Chile, IPoM septiembre 2026)

[[FIGURA:3]]

### 1. Descripción

| Elemento | Detalle |
|---|---|
| **Fuente** | Banco Central de Chile. *Informe de Política Monetaria (IPoM)*, septiembre 2026, capítulo II, Gráfico II.9 «Proyección de inflación». |
| **Contexto** | El IPoM explica las decisiones de tasa de política monetaria. En septiembre de 2026 se proyecta una inflación IPC de 4,3 % a diciembre de 2026, 2,8 % a diciembre de 2027 y 3,0 % en el horizonte de dos años (Tabla II.4). |
| **Audiencia objetivo** | Mercados financieros, economistas, prensa especializada y autoridades. Audiencia experta. |

### 2. Evaluación técnica

| Aspecto | Evaluación |
|---|---|
| **Tipo de gráfico** | Gráfico de líneas en dos paneles: inflación total (IPC) e inflación subyacente (sin volátiles). |
| **Variables** | Eje X: tiempo (2021-2028). Eje Y: variación anual (%). Series: dato efectivo, proyección del IPoM de septiembre 2026 y proyección del IPoM de junio 2026 (comparación entre informes). |
| **Calidad de representación** | Correcta para la audiencia experta: la comparación entre la proyección actual y la anterior muestra cómo cambió la evaluación del Banco. |
| **Nivel de complejidad** | Alto. Supone conocer conceptos como inflación subyacente, horizonte de política y meta de 3 %. |

### 3. Evaluación crítica

- **Claridad visual:** los dos paneles con el mismo eje temporal facilitan la comparación. Sin embargo, distinguir el dato observado de la proyección depende del estilo de línea, y eso no siempre se percibe con rapidez.
- **Buenas prácticas:** cumple con título, fuente y unidades. No incluye bandas de incertidumbre, que muchos bancos centrales publican como *fan charts*.
- **Problemas de interpretación:** al mostrar la proyección como una sola línea, un lector no experto (por ejemplo, alguien que ve el gráfico en un noticiero) puede entenderla como un pronóstico seguro y no como un escenario central con incertidumbre. Esto da una **falsa precisión**.
- **Posibles sesgos:** el mensaje de convergencia a la meta queda reforzado visualmente sin la dispersión de escenarios posibles. El propio informe describe un «corredor» con escenarios alternativos de tasa, pero el gráfico de inflación no lo traduce en una representación visual de riesgo.

### 4. Propuesta de mejora

- **Modificaría** la separación entre dato efectivo y proyección: fondo sombreado para el período proyectado y una línea vertical rotulada «hoy».
- **Eliminaría** la serie del IPoM anterior de la vista principal y la pasaría a un gráfico complementario. Para un público no experto, tres líneas que se cruzan añaden carga cognitiva.
- **Agregaría** bandas de confianza (10 %-90 %) alrededor del escenario central y una franja horizontal que marque la meta de 3 % y el rango de tolerancia de 2 % a 4 %.
- **Visualización propuesta:** un *fan chart* con meta y rango sombreados, además de una versión simplificada para comunicados de prensa con un título declarativo («La inflación volvería al 3 % a mediados de 2027»). Así se adapta el estilo según el usuario ([Estilos de Visualización], [Usuarios]).

## Síntesis comparativa

| Criterio | INE | Our World in Data | Banco Central |
|---|---|---|---|
| Tipo de organismo | Gubernamental | Observatorio internacional | Informe institucional |
| Tipo de gráfico | Líneas | Líneas + mapa + tabla | Líneas (2 paneles) |
| Interactividad | No | Alta | No |
| Muestra la incertidumbre | No (solo en el texto) | No aplica (datos de inventario) | No |
| Principal riesgo | Encuadre temporal corto | Indicador territorial vs. consumo | Falsa precisión |
| Complejidad | Baja-media | Media | Alta |

La conclusión común es que **las tres visualizaciones son técnicamente correctas, pero ninguna es neutral**. Las decisiones sobre el período, el indicador y la forma de representar la incertidumbre orientan la interpretación. Esto confirma la idea del libro de que la visualización combina contenido y forma, y que ambas dimensiones deben diseñarse con responsabilidad.

---

# PARTE III: Ensayo Reflexivo

## ¿Cómo contribuye la visualización de datos a transformar datos en conocimiento útil para la toma de decisiones en una organización?

Toda organización produce datos todos los días: ventas, reclamos, horarios, inventario, tiempos de respuesta. Producir datos no es el problema. Lo difícil es que esos datos lleguen a convertirse en algo que permita decidir mejor. En este ensayo sostengo que la visualización de datos cumple justamente esa función de puente: toma datos sin significado, los organiza como información y facilita que las personas los conviertan en conocimiento útil. Para argumentarlo me apoyo en las ideas de Ignasi Alcalde, en las relaciones que construí en mi bóveda de Obsidian y en mi experiencia de trabajo en soporte técnico de post venta.

El primer punto es entender qué se transforma. Alcalde define la información como «un conjunto organizado de datos capaz de cambiar el estado de conocimiento del receptor». La definición tiene dos condiciones: que los datos estén **organizados** y que **cambien algo** en quien los recibe. Un dato suelto, como «47 equipos ingresados», no cumple ninguna de las dos. Si lo pongo en contexto (47 equipos ingresados esta semana, el doble que el promedio, la mayoría por la misma falla), ya es información. Y si con eso el encargado de tienda decide pedir más repuestos o escalar el problema al proveedor, se transformó en conocimiento aplicado. Este recorrido es el que resume la pirámide DIKW (datos, información, conocimiento, sabiduría), una de las notas centrales de mi bóveda. Al conectarla con las notas de [Toma de Decisiones] y [Visualización de Información] entendí que la visualización no es un adorno al final del proceso, sino el mecanismo que acelera el paso de un nivel al siguiente.

El segundo punto es por qué ese paso necesita lo visual. Alcalde parte de un diagnóstico: vivimos en un estado de **infoxicación**, término de Alfons Cornella que une información e intoxicación. Recibimos cinco veces más información que hace 30 años, el 99,9 % de lo que se genera es digital y de los miles de estímulos visuales del día recordamos apenas un 10 %. En una organización esto se traduce en reportes extensos que nadie lee completos, planillas con cientos de filas y correos con datos adjuntos que se acumulan. El libro advierte que la infoxicación provoca parálisis en la toma de decisiones, decisiones equivocadas y ansiedad. La visualización responde a este problema porque **filtra y jerarquiza**: obliga a elegir qué mostrar y qué dejar fuera. En mi bóveda, la nota [Infoxicación] enlaza directamente con [Beneficios de la Visualización], y esa relación resume el argumento: visualizar es, antes que todo, seleccionar.

Además, el ser humano procesa mejor las imágenes que el texto. El libro cita el experimento de John Medina: solo el 10 % de las personas recordaba una información presentada de forma oral, frente al 65 % cuando se acompañaba de una imagen. También señala que en internet no leemos, escaneamos. Para una organización esto tiene consecuencias prácticas. Un gerente que revisa un dashboard durante dos minutos entre reuniones necesita que el patrón se vea, no que se lea. Un gráfico de líneas que muestra el aumento sostenido de reclamos por una misma falla comunica en segundos lo que una tabla tardaría minutos en revelar, si es que alguien llega a notarlo.

El tercer punto es que la visualización no solo presenta conocimiento, también lo **produce**. Alcalde, siguiendo a Alberto Cairo, distingue entre la infografía, orientada a presentar un mensaje de forma estática, y la visualización de datos, cuyo eje es la exploración e interacción. Ambas pertenecen a un mismo continuo. En una organización ambas son necesarias: la visualización exploratoria permite que un analista descubra algo que no buscaba, como que los equipos de cierta marca fallan más en verano; la presentación permite comunicar ese hallazgo al resto. El caso histórico de John Snow, que revisé para la nota [Historia de la Visualización], lo muestra bien: al mapear los casos de cólera en Londres en 1854 descubrió que se concentraban alrededor de un pozo de agua, y esa evidencia visual permitió tomar una decisión concreta que detuvo la epidemia. Ahí la visualización fue a la vez exploración, descubrimiento y argumento para decidir.

Sin embargo, la visualización también puede llevar a malas decisiones, y esto es algo que comprobé en la Parte II. Las tres visualizaciones que analicé (INE, Our World in Data y Banco Central) son técnicamente correctas, pero en las tres hay decisiones de diseño que orientan la lectura: un período corto que no da perspectiva, un indicador territorial que favorece a ciertos países, una proyección sin bandas de incertidumbre que transmite falsa precisión. Si una organización decide con gráficos que esconden la incertidumbre o que eligen el período más conveniente, el resultado puede ser peor que no visualizar. Por eso en mi bóveda la nota [Calidad de Datos] está enlazada con [Toma de Decisiones]: un gráfico solo es tan confiable como los datos y las decisiones de diseño que lo sostienen. Para que la visualización genere conocimiento útil, la organización necesita también **buenas prácticas**: citar fuentes, usar escalas honestas, mostrar la incertidumbre y elegir el tipo de gráfico según el tipo de dato.

Otro aspecto que me parece clave es la audiencia. Alcalde describe la «paradoja del conocimiento»: cuando sabemos algo, nos cuesta imaginar cómo era no saberlo, y por eso explicamos mal. Me pasa a diario en el mesón de post venta cuando explico a un cliente por qué su equipo no tiene garantía: lo que para mí es obvio, para él no lo es. En una organización ocurre lo mismo entre el analista que construye el dashboard y el gerente que lo usa. La solución que propone el libro es centrarse en un solo mensaje simple, relevante, concreto y creíble. Esto conecta con el **storytelling** y con la estructura de la infografía (introducción, cuerpo y una conclusión o «moraleja»). Para que la visualización sirva para decidir, debe estar diseñada pensando en quién decide, no en quien la construye. En mi bóveda, las notas [Usuarios], [Paradoja del Conocimiento] y [Storytelling] forman un triángulo que representa exactamente esta idea.

Finalmente, la construcción de la propia bóveda me dejó una lección sobre el tema del ensayo. Al principio tenía 36 notas que eran solo resúmenes. Se convirtieron en conocimiento recién cuando tuve que decidir cómo se relacionaban: qué enlazar con qué y por qué. El grafo de Obsidian me mostró agrupaciones que no había notado en la lectura, como lo cerca que están [Infoxicación] y [Big Data] de [Toma de Decisiones]. Es decir, visualizar mis propias notas me ayudó a entenderlas mejor, que es exactamente lo que la visualización hace por una organización a mayor escala.

En conclusión, la visualización de datos contribuye a transformar datos en conocimiento útil porque organiza y da contexto a los datos, filtra el exceso de información, aprovecha nuestra capacidad de procesar imágenes, permite explorar y descubrir patrones y comunica hallazgos de forma que lleven a la acción. Pero su valor depende de dos condiciones: datos de calidad y un diseño honesto pensado en el usuario. Como resume el subtítulo del libro de Alcalde, el objetivo es ir *de los datos al conocimiento*, y en una organización ese recorrido solo termina cuando alguien toma una mejor decisión gracias a lo que vio.

---

# PARTE IV: Reflexión sobre Gestión del Conocimiento Digital

## ¿Cómo aportan Obsidian y GitHub a la construcción y gestión del conocimiento en proyectos de Ciencia de Datos?

Durante esta actividad usé Obsidian para construir una red de 36 notas conceptuales y GitHub para versionar el trabajo. Mi conclusión es que se complementan: Obsidian organiza el **qué** sé y GitHub registra **cómo y cuándo** lo construí.

**Organización del conocimiento.** Obsidian trabaja con archivos Markdown enlazados entre sí. A diferencia de una carpeta de documentos, obliga a pensar relaciones: cada `[[enlace]]` es una decisión sobre cómo se conectan dos ideas. El MOC «Mapa General de Visualización de Datos» funciona como índice, y el Graph View muestra agrupaciones temáticas (fundamentos, gestión de datos, visualización, comunicación y práctica) que no eran evidentes al leer el libro de forma lineal. El Canvas permitió llevar esas relaciones a un mapa conceptual con conexiones etiquetadas.

**Trazabilidad del aprendizaje.** Cada commit de GitHub registra qué cambió y por qué: primero la estructura, luego los conceptos de datos, después los de visualización, el MOC, las relaciones cruzadas, el mapa y el informe. El historial muestra la evolución del razonamiento. En ciencia de datos esto permite saber, por ejemplo, en qué momento se cambió una definición o una métrica.

**Documentación técnica.** Markdown es texto plano, legible por personas y por máquinas, y el README explica el proyecto a quien llegue por primera vez. En un proyecto real, las notas de Obsidian pueden documentar fuentes de datos, diccionarios de variables y decisiones de limpieza junto al código.

**Trabajo colaborativo.** GitHub permite que varias personas trabajen sobre el mismo repositorio mediante ramas, *pull requests* y revisiones. Una bóveda de Obsidian versionada en GitHub puede convertirse en la base de conocimiento compartida de un equipo de datos.

**Reproducibilidad.** Como todo queda en archivos abiertos y versionados, cualquier persona puede clonar el repositorio y obtener exactamente la misma bóveda, el mismo mapa y el mismo informe. Esto es fundamental en ciencia de datos, donde un resultado que no se puede reproducir pierde credibilidad.

**Gestión de versiones.** Git permite volver a cualquier estado anterior, comparar versiones y recuperar trabajo. Cometer un error deja de ser grave porque siempre hay un punto de retorno.

Como aprendizaje personal, reconozco que no distribuí el trabajo durante la semana como pedía la actividad y lo concentré al final. Aun así, los commits por etapa reflejan el orden real en que construí la bóveda. La lección para el próximo proyecto es hacer commits pequeños y frecuentes desde el primer día, que es justamente lo que permite aprovechar la trazabilidad que ofrece GitHub.

---

# Referencias

- Alcalde Perea, I. (2015). *Visualización de la información: De los datos al conocimiento*. Editorial UOC.
- Banco Central de Chile. (2026). *Informe de Política Monetaria, septiembre 2026*. https://www.bcentral.cl/web/banco-central/areas/politica-monetaria/informe-de-politica-monetaria
- Cairo, A. (2011). *El arte funcional: Infografía y visualización de información*. Alamut.
- Instituto Nacional de Estadísticas. (2026). *Boletín estadístico: Empleo trimestral* (Edición N.º 331). https://www.ine.gob.cl/docs/default-source/ocupacion-y-desocupacion/boletines/2026/nacional/ene-nacional-331.pdf
- Knaflic, C. N. (2015). *Storytelling with data*. Wiley.
- Our World in Data. (2025). *CO₂ emissions per capita* [Gráfico interactivo]. Global Carbon Budget (2025). https://ourworldindata.org/grapher/co-emissions-per-capita
- Tufte, E. (2001). *The visual display of quantitative information* (2.ª ed.). Graphics Press.
