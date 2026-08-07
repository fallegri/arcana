# Sistema de Gestión de Inventario — Requerimientos Completos

## Contexto del Negocio
Empresa distribuidora de productos de consumo masivo con 3 bodegas.
Maneja ~2000 SKUs (productos), 150 proveedores y 500 clientes.
Necesita control en tiempo real de stock, alertas de reabastecimiento,
y trazabilidad completa de movimientos.

## Historias de Usuario

### Gestión de Productos
- Como almacenero quiero registrar productos nuevos con código SKU, nombre, descripción, categoría, unidad de medida y precio unitario para mantener el catálogo actualizado
- Como almacenero quiero asignar stock mínimo y stock máximo a cada producto para que el sistema me alerte cuando deba reabastecer
- Como administrador quiero categorizar productos (electrónica, alimentos, limpieza, etc.) para generar reportes por categoría
- Como almacenero quiero registrar la ubicación física de cada producto (bodega, pasillo, estante) para facilitar la búsqueda

### Gestión de Bodegas
- Como administrador quiero registrar múltiples bodegas con nombre, dirección y capacidad máxima para gestionar el espacio
- Como almacenero quiero ver el porcentaje de ocupación de cada bodega para planificar almacenamiento
- Como administrador quiero transferir productos entre bodegas registrando el movimiento

### Movimientos de Inventario
- Como almacenero quiero registrar entradas de mercadería (compras a proveedores) indicando producto, cantidad, proveedor, número de factura y fecha
- Como almacenero quiero registrar salidas de mercadería (ventas o despachos) indicando producto, cantidad, cliente destino y referencia de orden
- Como almacenero quiero registrar ajustes de inventario (merma, rotura, vencimiento) con motivo obligatorio
- Como administrador quiero ver el historial completo de movimientos de un producto con fecha, tipo, cantidad, responsable y referencia
- Como sistema debo actualizar el stock automáticamente después de cada movimiento

### Alertas y Notificaciones
- Como administrador quiero recibir alerta cuando un producto llegue a stock mínimo para iniciar reabastecimiento
- Como administrador quiero recibir alerta cuando un producto supere stock máximo para detener compras
- Como sistema debo alertar cuando un producto tiene fecha de vencimiento próxima (30 días)

### Proveedores
- Como comprador quiero registrar proveedores con nombre, RUC/NIT, contacto, email, teléfono y condiciones de pago
- Como comprador quiero asociar productos con sus proveedores (un producto puede tener múltiples proveedores)
- Como comprador quiero ver el historial de compras a cada proveedor

### Clientes
- Como vendedor quiero registrar clientes con nombre, documento, dirección, email y teléfono
- Como vendedor quiero ver el historial de despachos a cada cliente

### Reportes
- Como gerente quiero un reporte de stock actual con valorización (cantidad × precio unitario)
- Como gerente quiero un reporte de movimientos por período (diario, semanal, mensual)
- Como gerente quiero un reporte de productos con stock bajo mínimo
- Como gerente quiero un reporte de rotación de inventario (productos más y menos movidos)
- Como auditor quiero un reporte de ajustes con motivos para verificar mermas

### Seguridad y Auditoría
- Como administrador quiero que cada usuario tenga un rol (admin, almacenero, comprador, vendedor, gerente, auditor) con permisos específicos
- Como auditor quiero que toda operación registre quién la hizo, cuándo, y desde qué IP
- Como administrador quiero que las eliminaciones sean lógicas (soft delete) y recuperables
- Como sistema debo bloquear la cuenta después de 5 intentos fallidos de login

## Reglas de Negocio

### Stock
- El stock nunca puede ser negativo (no permitir salida si no hay suficiente)
- Toda salida debe tener referencia de orden o autorización
- Los ajustes negativos requieren motivo obligatorio (merma, rotura, vencimiento, error)
- Las transferencias entre bodegas no alteran el stock total (solo redistribuyen)

### Productos
- El código SKU debe ser único en todo el sistema
- El precio unitario no puede ser negativo ni cero
- Un producto no puede eliminarse si tiene stock > 0 (debe vaciarse primero)
- La categoría es obligatoria

### Movimientos
- Toda entrada debe tener proveedor y número de factura
- Toda salida debe tener cliente y referencia de orden
- Los movimientos no se pueden editar ni eliminar (inmutables para auditoría)
- La fecha del movimiento no puede ser futura

### Proveedores/Clientes
- El RUC/NIT debe ser único
- El email debe tener formato válido
- No se puede eliminar un proveedor con compras registradas (soft delete)

### Seguridad
- Solo admin puede crear usuarios y asignar roles
- Solo almacenero y admin pueden registrar movimientos
- Solo gerente y admin pueden ver reportes de valorización
- Solo auditor y admin pueden ver el log de auditoría
- El password debe tener mínimo 8 caracteres, mayúscula, número y especial
- Tokens JWT expiran en 8 horas (jornada laboral)
- Toda acción se registra en audit_log (user_id, acción, timestamp, ip, detalle)
