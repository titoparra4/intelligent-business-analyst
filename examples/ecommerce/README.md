# Example A — E-commerce checkout coupons (Spanish)

> Synthetic example. It shows the expected *shape and behaviour* of a `/full-business-analysis`
> response to a one-line request in Spanish. It is a hand-written reference output, not a recorded
> model run. All names and data are fictitious.

## Input

```text
/full-business-analysis
Necesitamos que los clientes puedan aplicar cupones de descuento durante el checkout.
```

## Expected output

### 1. Resumen

**Objetivo (Inferred):** permitir que el cliente reduzca el importe de su pedido mediante un código
promocional en el checkout, para apoyar campañas comerciales.
**Fuente:** S1 = la solicitud anterior (una frase). Casi todas las reglas de negocio son desconocidas,
por lo que los artefactos se entregan como **Draft** y dependen de las preguntas Q-001…Q-008.

### 2. Conocido / Inferido / Desconocido

| Tipo | Contenido |
|---|---|
| Confirmed | Actor: cliente. Momento: checkout. Capacidad: aplicar un cupón de descuento (S1). |
| Inferred | Existe (o hará falta) un mecanismo para crear/gestionar cupones; el descuento se refleja en el total; marketing es el probable dueño de las campañas. |
| Unknown | Tipo de descuento, acumulabilidad, caducidad, límites de uso, alcance (productos/envío), quién crea cupones, impacto en devoluciones, canales. |

### 3. Stakeholders y sistemas

| ID | Stakeholder / sistema | Interés | Fuente | Conocimiento |
|---|---|---|---|---|
| STK-001 | Cliente | Pagar menos con un cupón válido | S1 | Confirmed |
| STK-002 | Marketing / gestor de campañas | Crear y medir promociones | — | Inferred |
| STK-003 | Finanzas | Contabilizar descuentos | — | Inferred |
| STK-004 | Atención al cliente | Resolver incidencias con cupones | — | Inferred |
| SYS-001 | Checkout / carrito | Aplicar y mostrar el descuento | S1 | Confirmed |
| SYS-002 | Gestión de cupones (existente o nueva) | Fuente de verdad de cupones | — | Unknown (Q-007) |
| SYS-003 | Pedidos / facturación | Registrar el descuento en el pedido | — | Inferred |

### 4. Requisitos

| ID | Requisito | Tipo | Fuente | Estado |
|---|---|---|---|---|
| BRQ-001 | Los clientes podrán reducir el importe de un pedido aplicando un cupón de descuento en el checkout. | Business | S1 | Proposed |
| FR-001 | El sistema permitirá al cliente introducir un código de cupón en el checkout antes de confirmar el pago. | Functional | S1 | Proposed |
| FR-002 | El sistema validará el código frente a las reglas BR-001…BR-005 al aplicarlo. | Functional | Inferred | Proposed |
| FR-003 | Si el cupón es válido, el sistema recalculará y mostrará el descuento y el nuevo total antes del pago. | Functional | Inferred | Proposed |
| FR-004 | Si el cupón no es válido, el sistema mostrará el motivo del rechazo sin modificar el total. | Functional | Inferred | Proposed |
| FR-005 | El cliente podrá retirar un cupón aplicado antes de pagar. | Functional | Inferred | Pending Validation |
| FR-006 | El pedido confirmado registrará el cupón usado y el importe descontado. | Functional | Inferred | Proposed |
| FR-007 | Un usuario autorizado podrá crear, configurar y desactivar cupones. | Functional | Inferred | Pending Validation (Q-007) |
| NFR-001 | La validación del cupón responderá dentro de `TBD` en condiciones de carga `TBD`. | Performance | — | Pending Validation (Q-008) |
| NFR-002 | Los intentos de aplicación de cupones quedarán registrados para auditoría y análisis. | Auditability | Inferred | Proposed |
| NFR-003 | El sistema limitará intentos repetidos de códigos inválidos para mitigar la enumeración de cupones (umbral `TBD`). | Security | Inferred | Proposed |

### 5. Reglas de negocio

Ninguna regla fue indicada por el negocio. Se listan las reglas **necesarias** para especificar el
comportamiento, sin decidir su valor.

| Rule ID | Nombre | Condición | Acción esperada | Fuente | Estado |
|---|---|---|---|---|---|
| BR-001 | Existencia y estado del cupón | El código no existe o está desactivado | Rechazar con motivo "código no válido" | Inferred | Proposed |
| BR-002 | Vigencia | La fecha actual está fuera del periodo de validez | Rechazar con motivo "caducado / no vigente" | Inferred | Pending Validation (Q-003: ¿tienen caducidad? ¿zona horaria?) |
| BR-003 | Cupones por pedido | Ya hay un cupón aplicado | `TBD` (Q-002) | — | Pending Validation |
| BR-004 | Importe mínimo | Subtotal < mínimo del cupón | Rechazar indicando el mínimo | — | Pending Validation (Q-004: ¿existe mínimo?) |
| BR-005 | Límite de usos | Usos del cupón o del cliente ≥ límite | Rechazar | — | Pending Validation (Q-005) |
| BR-006 | Cálculo del descuento | Cupón válido | Descuento según tipo (`TBD`: % / importe fijo / envío) sobre base `TBD`; el total no puede ser negativo | Inferred (total ≥ 0) | Pending Validation (Q-001) |

**DT-01 — Aceptación de cupón** (hit policy: first)

| # | Existe y activo | Vigente | Mínimo cumplido | Límite de uso no alcanzado | → Acción |
|---|---|---|---|---|---|
| 1 | No | – | – | – | Rechazar: no válido (BR-001) |
| 2 | Sí | No | – | – | Rechazar: no vigente (BR-002) |
| 3 | Sí | Sí | No | – | Rechazar: mínimo (BR-004) |
| 4 | Sí | Sí | Sí | No | Rechazar: límite (BR-005) |
| 5 | Sí | Sí | Sí | Sí | Aceptar y calcular (BR-006) |

Combinación no cubierta: interacción con un cupón ya aplicado (BR-003) → depende de Q-002.

### 6. Gaps

| Gap ID | Estado actual | Estado objetivo | Gap | Impacto | Prioridad | Recomendación |
|---|---|---|---|---|---|---|
| GAP-001 | Sin campo de cupón en checkout (Inferred de S1) | Cupón aplicable en checkout | Entrada y validación de cupones | Alto — requisito central | Must (Proposed) | FR-001…FR-004 |
| GAP-002 | Desconocido (Q-007) | Cupones gestionables por negocio | Posible ausencia de gestión de cupones | Alto si no existe | TBD | Confirmar si existe SYS-002 |

### 7. Épica e historias

**EP-01 — Cupones de descuento en checkout** (OBJ-001)

#### US-001 — Aplicar un cupón válido
**Epic:** EP-01 · **Business Value:** el cliente obtiene el descuento de la campaña (OBJ-001)
**As a** cliente **I want** introducir un código de cupón en el checkout **So that** pague el precio con descuento
**Preconditions:** carrito con al menos un producto; cliente en el paso de checkout.
**Acceptance Criteria:**
- **US-001-AC01 (positive)** Given un cupón activo y vigente que cumple BR-001…BR-005, When el cliente lo aplica, Then se muestran el descuento y el nuevo total antes del pago.
- **US-001-AC02 (positive)** Given un cupón aplicado, When el cliente confirma el pedido, Then el pedido registra el código y el importe descontado (FR-006).
- **US-001-AC03 (edge)** Given un descuento mayor que el importe sujeto a descuento, When se aplica, Then el total no es negativo (BR-006).
- **US-001-AC04 (edge)** Given un código con distinta capitalización o espacios, When se aplica, Then el resultado sigue la regla `TBD (Q-006)`.
**Business Rules:** BR-001, BR-002, BR-006 · **Traces to:** FR-001, FR-002, FR-003, FR-006
**Dependencies:** DEP-001 fuente de cupones (Q-007) · **Priority:** Must (Proposed: núcleo de la solicitud)
**Open Questions:** Q-001, Q-006 · **INVEST:** I✔ N✔ V✔ E✖(Q-001) S✔ T✔
**Definition of Ready Status:** Not Ready — falta el tipo de descuento (Q-001) y la fuente de cupones (Q-007).

#### US-002 — Ver por qué se rechaza un cupón
**As a** cliente **I want** saber por qué mi cupón no se aplica **So that** pueda corregirlo o continuar sin él
**Acceptance Criteria:**
- **US-002-AC01 (negative)** Given un código inexistente, When lo aplico, Then veo un mensaje de código no válido y el total no cambia.
- **US-002-AC02 (negative)** Given un cupón fuera de vigencia, When lo aplico, Then veo un mensaje de cupón no vigente y el total no cambia.
- **US-002-AC03 (negative)** Given un subtotal inferior al mínimo del cupón, When lo aplico, Then veo el mínimo requerido y el total no cambia.
- **US-002-AC04 (negative)** Given que he superado el número de intentos inválidos `TBD`, When intento otro código, Then el sistema bloquea temporalmente nuevos intentos (NFR-003).
**Business Rules:** BR-001, BR-002, BR-004, BR-005 · **Traces to:** FR-004, NFR-003
**Priority:** Must (Proposed) · **Open Questions:** Q-003, Q-004, Q-005
**Definition of Ready Status:** Not Ready — dependen de Q-003…Q-005.

#### US-003 — Retirar un cupón aplicado
**As a** cliente **I want** quitar un cupón aplicado **So that** pueda usar otro o guardarlo
**Acceptance Criteria:**
- **US-003-AC01 (positive)** Given un cupón aplicado, When lo retiro, Then el total vuelve al importe sin descuento.
**Traces to:** FR-005 · **Priority:** Should (Proposed) · **Definition of Ready Status:** Not Ready — FR-005 Pending Validation.

#### US-004 — Gestionar cupones (Enabler)
**As a** gestor de campañas **I want** crear, configurar y desactivar cupones **So that** pueda lanzar promociones sin desarrollo
**Traces to:** FR-007 · **Priority:** TBD · **Definition of Ready Status:** Not Ready — confirmar si ya existe (Q-007); si existe, la historia se descarta.

**Dependencias:** US-001 → DEP-001 (US-004 o sistema existente); US-002 → US-001; US-003 → US-001.

### 8. Impactos y dependencias

| IMP ID | Área | Descripción | Severidad | Confianza |
|---|---|---|---|---|
| IMP-001 | Pagos | El importe enviado a la pasarela debe ser el total con descuento | High | Medium |
| IMP-002 | Devoluciones | Reembolso parcial de un pedido con cupón (¿prorrateo?) | High | Low — Q-009 |
| IMP-003 | Finanzas / informes | Registro contable del descuento | Medium | Low |
| IMP-004 | Pruebas de regresión | Cálculo de totales, impuestos, envío | High | Medium |

### 9. Revisión de calidad (requisitos de este análisis)

Rúbrica v1.0, pesos por defecto, 11 ítems (BRQ-001, FR-001…FR-007, NFR-001…NFR-003), máximo 44 puntos por dimensión:

| Dimensión | Suma ítems / 44 | D | Peso | Aporte |
|---|---|---|---|---|
| Clarity | 38 | 86.4 | 20 | 17.27 |
| Completeness | 24 | 54.5 | 15 | 8.18 |
| Consistency | 44 | 100 | 15 | 15.00 |
| Testability | 25 | 56.8 | 20 | 11.36 |
| Traceability | 26 | 59.1 | 10 | 5.91 |
| Feasibility | 40 | 90.9 | 10 | 9.09 |
| Atomicity | 42 | 95.5 | 10 | 9.55 |
| **Total** | | | 100 | **76.36 → 76** |

Sin hallazgos Critical → sin tope. **76 / 100 — Minor rework**. Principales hallazgos:
QF-001 (High, Testability) NFR-001 sin objetivo; QF-002 (High, Completeness) BR-003…BR-006 sin decidir;
QF-003 (Medium, Traceability) OBJ-001 inferido. La puntuación sube al resolver Q-001…Q-005.
*Heurística, no certificación.*

### 10. Preguntas abiertas (priorizadas)

| ID | Prioridad | Pregunta | Por qué importa |
|---|---|---|---|
| Q-001 | Blocking | ¿Qué tipos de descuento existen (porcentaje, importe fijo, envío gratis) y sobre qué base (subtotal, con/sin impuestos, envío)? | Define el cálculo BR-006 |
| Q-002 | Blocking | ¿Se pueden combinar varios cupones o un cupón con otras promociones? | Define BR-003 y la UI |
| Q-007 | Blocking | ¿Existe ya un sistema donde se crean los cupones? | Determina si US-004 entra en alcance |
| Q-003 | Important | ¿Los cupones caducan? ¿En qué zona horaria se evalúa la vigencia? | BR-002 |
| Q-004 | Important | ¿Existen importes mínimos de pedido? | BR-004 |
| Q-005 | Important | ¿Hay límites de uso por cupón o por cliente? ¿Requiere estar registrado? | BR-005 |
| Q-009 | Important | ¿Cómo se tratan las devoluciones parciales de pedidos con cupón? | IMP-002 |
| Q-006 | Minor | ¿Los códigos distinguen mayúsculas/minúsculas? | US-001-AC04 |
| Q-008 | Minor | ¿Qué tiempo de respuesta se espera para la validación? | NFR-001 |

### 11. Supuestos y limitaciones

- AS-001: el cupón se aplica a pedidos web; otros canales (app, tienda) fuera de alcance hasta confirmar.
- Análisis basado en una sola frase; ninguna regla está confirmada. No se han estimado esfuerzos.

### 12. Siguientes pasos

1. Responder Q-001, Q-002 y Q-007. 2. `/analyze-business-rules` para cerrar BR-003…BR-006.
3. `/generate-documentation` (FRD + RTM) cuando las historias estén Ready.
