## Consigna: Sistema de Descuentos para Estación de Servicio ⛽

### Objetivo:
Crea un programa en Python que calcule el monto final a pagar en una estación de servicio, aplicando descuentos según el tipo de usuario y el combustible que compren.

### Requisitos:
1.  El programa debe **solicitar al usuario** tres datos de entrada:
    * El **total de la compra** (un valor numérico).
    * El **tipo de combustible** (que puede ser `nafta`, `gasoil` o `gnc`).
    * El **tipo de usuario** (que puede ser `regular`, `socio` o `vip`).

2.  Aplica la siguiente **lógica de descuentos**:
    * Los clientes **VIP** obtienen un descuento fijo del **10%** en su compra, independientemente del tipo de combustible.
    * Los **socios** obtienen un descuento fijo del **5%** en su compra, sin importar el tipo de combustible.
    * Los usuarios **regulares** solo obtienen un descuento si compran **nafta**, y este descuento es del **2%**. Si compran gasoil o gnc, no tienen descuento.

3.  El programa debe **calcular** el monto del descuento y el total final a pagar.

4.  Finalmente, el programa debe **imprimir un resumen de la compra**, mostrando el total sin descuento, el monto del descuento aplicado y el total final a pagar. Los valores monetarios deben mostrarse con dos decimales.

5.  Considera la **gestión de errores**: Si el usuario ingresa un valor no numérico para el total de la compra, el programa debe mostrar un mensaje de error claro y amigable.

---

Este programa ayuda a una estación de servicio a automatizar el cálculo de los precios finales, aplicando diferentes reglas de descuento.