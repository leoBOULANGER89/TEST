# Pull Request

<!--
⚠️ INSTRUCCIONES:
- Complete TODAS las secciones relevantes para su PR
- Elimine las secciones que NO se aplican a su cambio
- Reemplace los placeholders entre <...> con su informacion
- Marque [x] los items de la checklist a medida que avanza
-->

## Tipo de cambio

<!-- Marque todas las casillas que aplican -->

- [ ] 🐛 **Bug fix** (correccion de un problema existente)
- [ ] ✨ **Feature** (nueva funcionalidad)
- [ ] 🧠 **Model** (nuevo modelo ML o mejora de un modelo existente)
- [ ] 🔧 **Refactoring** (restructuracion del codigo sin cambio de funcionalidad)
- [ ] 📚 **Documentation** (actualizacion de la documentacion unicamente)
- [ ] 🚀 **Performance** (mejora del rendimiento)
- [ ] 🧪 **Tests** (agregado o correccion de tests)
- [ ] 🔐 **Security** (parche de seguridad)
- [ ] 🐳 **DevOps/Infrastructure** (CI/CD, Docker, configuracion)
- [ ] 📦 **Dependencies** (actualizacion de dependencias)

---

## Descripcion

<!--
Describa claramente y de manera concisa lo que hace este PR.
Incluya el contexto necesario para entender los cambios.
-->

**Resumen en una linea :**  
<Describa en una frase el cambio principal>

**Contexto detallado :**  
<Explique por que este cambio es necesario, que problema resuelve, o que funcionalidad agrega>

**Cambios principales :**
- <Cambio 1>
- <Cambio 2>
- <Cambio 3>

---

## Issues relacionadas

<!-- Vincule los issues de GitHub o tickets Jira correspondientes -->

Fixes #<numero_issue>  
Related to #<numero_issue>

---

## 🧠 Modelos ML

<!-- ⚠️ SECCION OBLIGATORIA si modifica archivos .pt, .pth, .onnx -->
<!-- Elimine esta seccion si no se modifica ningun modelo -->

### Modelo(s) modificado(s)

- [ ] `car_parts` (segmentacion)
- [ ] `car_damages/detector` (YOLOv10)
- [ ] `car_damages/segmentation`
- [ ] `car_damages/classificator`
- [ ] `car_angle` (clasificacion)
- [ ] Otro : <especifique>

### Metricas de rendimiento

<!-- El workflow Model Validation generara un informe automatico -->
<!-- Agregue aqui un resumen manual si tiene resultados preliminares -->

| Metrica | Modelo anterior | Nuevo modelo | Delta | Mejoria ? |
|--------|----------------|-------------|-------|-----------|
| mAP@0.5 | <0.XX> | <0.XX> | <+X.X%> | ✅ / ⚠️ / ❌ |
| Precision | <0.XX> | <0.XX> | <+X.X%> | ✅ / ⚠️ / ❌ |
| Recall | <0.XX> | <0.XX> | <+X.X%> | ✅ / ⚠️ / ❌ |
| F1-Score | <0.XX> | <0.XX> | <+X.X%> | ✅ / ⚠️ / ❌ |

**Tamano del modelo :** <XX MB>  
**Tiempo de inferencia (CPU) :** <XX ms>

### Justificacion de los cambios

<!-- Explique por que modifico el modelo -->
<!-- Ejemplos: nuevo dataset, nueva arquitectura, hiperparametros optimizados, etc. -->

<Describa las razones de la modificacion del modelo>

### Documento explicando el aprendizaje

<Enlace al documento que explica cómo aprender el modelo.>

---

## 🔌 API / Backend

<!-- Elimine esta seccion si no hay cambios API/Backend -->

### Endpoints modificados/agregados

| Metodo | Endpoint | Descripcion | Breaking change ? |
|--------|----------|-------------|-------------------|
| <GET/POST/PUT/DELETE> | `/api/v1/...` | <Descripcion> | ✅ Si / ❌ No |

### Cambios del esquema de datos

<!-- Si modifica los modelos de datos o el esquema de base de datos -->

**Antes :**
```json
{
  "field": "old_value"
}
```

**Despues :**
```json
{
  "field": "new_value",
  "new_field": "value"
}
```

### Migracion requerida ?

- [ ] ✅ Si, una migracion de base de datos es necesaria
  - Script de migracion : `<ruta/verso/migration.sql>`
  - Impacto : <Describa el impacto>
- [ ] ❌ No, no se requiere migracion

---

## 🖼️ Frontend / UI

<!-- Elimine esta seccion si no hay cambios de interfaz -->

### Capturas de pantalla

<!-- Agregue capturas de pantalla para mostrar los cambios visuales -->

**Antes :**  
<Inserte captura de pantalla>

**Despues :**  
<Inserte captura de pantalla>

### Diseno responsive

- [ ] Probado en desktop
- [ ] Probado en tablet
- [ ] Probado en movil

---

## 📊 OBD-II / Hardware

<!-- Elimine esta seccion si no hay cambios relacionados con hardware -->

### Hardware afectado

- [ ] OBDLink MX+
- [ ] Simulador OBD-II
- [ ] Otro : <especifique>

### PIDs utilizados

| PID | Descripcion | Formula | Unidad |
|-----|-------------|---------|-------|
| `0105` | Coolant Temperature | `A - 40` | °C |
| `010D` | Vehicle Speed | `A` | km/h |
| `0104` | Engine Load | `A * 100 / 255` | % |

### Interfaz de comunicacion

- **Puerto** : `/dev/rfcomm0`
- **Protocolo** : RFCOMM Bluetooth
- **Baud rate** : <si aplica>

---

## 🧪 Tests

### Tests unitarios

- [ ] He agregado tests para cubrir mis cambios
- [ ] Todos los tests unitarios existentes pasan
- [ ] Cobertura de codigo : <XX%>

**Comando para ejecutar los tests :**
```bash
pytest tests/
```

### Tests de integracion

- [ ] He probado la integracion con los otros componentes
- [ ] He probado los casos limite (edge cases)

### Tests manuales realizados

<!-- Describa los tests manuales que ha realizado -->

1. <Descripcion del test 1>
2. <Descripcion del test 2>
3. <Descripcion del test 3>

---

## 📝 Como probar este PR ?

<!--
SECCION OBLIGATORIA
Proporcione instrucciones CLARAS y DETALLADAS para probar sus cambios
-->

### Prerrequisitos

<!-- Liste todo lo que debe estar instalado/configurado antes de probar -->

- [ ] <Dependencia 1>
- [ ] <Dependencia 2>
- [ ] <Configuracion especifica>

### Paso 1 : Setup del entorno

```bash
# Ejemplo de comandos
git checkout <rama>
pip install -r requirements.txt
```

### Paso 2 : <Nombre del paso>

```bash
# Comandos o acciones a realizar
```

**Resultado esperado :**  
<Describa lo que deberia pasar>

### Paso 3 : <Nombre del paso>

```bash
# Comandos o acciones a realizar
```

**Resultado esperado :**  
<Describa lo que deberia pasar>

<!-- Agregue tantos pasos como sea necesario -->

---

## ✅ Checklist

<!-- Marque todas las casillas aplicables. Si una casilla no puede ser marcada, explique por que en los comentarios -->

<!-- Verifique los resultados de los GitAction antes de marcar -->

### Calidad del Codigo

- [ ] Mi codigo sigue las convenciones de estilo del proyecto (PEP 8, Black, isort) <!-- Verificar Code Linting -->
- [ ] He realizado una auto-revision de mi codigo
- [ ] Mi codigo es legible y comprensible <!-- Verificar Code Linting -->
- [ ] He comentado las partes complejas del codigo
- [ ] He eliminado los logs de debug y los comentarios inutiles

### Documentacion

- [ ] He actualizado la documentacion correspondiente
- [ ] He agregado docstrings a las nuevas funciones/clases
- [ ] He actualizado el README si es necesario
- [ ] He documentado los cambios de API en el changelog

### Tests

- [ ] He agregado tests que prueben que mi correccion funciona o que mi funcionalidad funciona
- [ ] Los nuevos tests y los tests existentes pasan en local <!-- Verificar Unit Tests -->
- [ ] He verificado la cobertura de codigo

### Seguridad

- [ ] No he introducido vulnerabilidades conocidas <!-- Verificar Dependency Vulnerability Scan -->
- [ ] No he expuesto secrets (API keys, passwords, tokens) <!-- Verificar Bandit Security Scan -->
- [ ] He validado todas las entradas de usuario
- [ ] He usado consultas parametrizadas para las queries SQL

### Rendimiento

- [ ] He verificado que mis cambios no tienen impacto negativo en el rendimiento
- [ ] He optimizado las consultas de base de datos si aplica
- [ ] He evitado los bucles N+1

### Git

- [ ] Mis commits son descriptivos y siguen la convencion de commit <!-- Verificar en pre-commit -->
- [ ] He hecho rebase de mi rama sobre la ultima version de `main`/`development`
- [ ] He resuelto todos los conflictos de merge

---

## 🔍 Resultados de las verificaciones automaticas

### Pre-commit Hooks

<!-- Los hooks se ejecutan automaticamente, documente aqui si tuvo que skip algunos -->

- [x] Black (formateo)
- [x] isort (imports)
- [x] Ruff (linting)
- [x] Bandit (seguridad)
- [x] nbstripout (notebooks)

### GitHub Actions

<!-- Estas verificaciones se ejecutan automaticamente al hacer push -->

#### Lint

<img width="698" alt="Pylint Results" src="<URL_de_su_captura>">

**Score Pylint :** <X.XX/10>

#### Tests

```
<Retorno del terminal al verificar los tests>
```

**Cobertura :** <XX%>

#### Security Scan

<!-- Verificar los logs de los git Actions -->
- **Bandit :** ✅ Ninguna falla detectada
- **Snyk :** ✅ Ninguna vulnerabilidad en las dependencias
- **Trivy :** ✅ Imagen Docker segurizada (si aplica)


---

## 🚨 Breaking Changes

<!-- ⚠️ SECCION CRITICA si su PR introduce breaking changes -->
<!-- Elimine esta seccion si no hay breaking change -->

### Cambios incompatibles

<Liste todos los cambios que rompen la compatibilidad con las versiones anteriores>

### Acciones requeridas para los usuarios

1. <Accion 1>
2. <Accion 2>

### Plan de migracion

<Describa como migrar desde la version anterior>

---

## 📌 Notas adicionales

<!-- Cualquier informacion adicional que los reviewers deberian conocer -->

<Informaciones adicionales>

---

## 🔗 Recursos

<!-- Enlaces a documentos, designs, discusiones, etc. -->

- Design : <URL>
- Discussion : <URL>
- Documentacion externa : <URL>

---

## 📸 Demostracion

<!-- (opcional) Si aplica, agregue una demo en video o GIF -->

<Inserte GIF o enlace de video>

---

## ⏱️ Estimacion de tiempo

**Tiempo estimado para la review :** <XX minutos>  
**Complejidad :** 🟢 Baja / 🟡 Media / 🔴 Alta

---

## 👥 Reviewers sugeridos

<!-- Mencione las personas que deberian revisar este PR -->

@<username1> @<username2>

---

<!--
══════════════════════════════════════════════════════════════════════
FIN DEL TEMPLATE
══════════════════════════════════════════════════════════════════════

Gracias por tomarse el tiempo de completar este template completamente.
Un PR bien documentado facilita la review y acelera el merge!
-->
