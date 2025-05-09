# 3.8_ProyectoIntegrador

## Descripción
Este proyecto consiste en una empresa que permite a sus clientes crear autos personalizados. Entre más características escojan más se eleva el precio. Aquí se muestra la creación de autos de un cliente, su orden desglosada y el pago de la misma.

### Uso de patrón de diseño creacional: Builder
- __Problema__: La creación de un auto es complicada, pues debe de tener sus características personalizadas, un precio base de acuerdo al tipo de auto a personalizar y un nombre. A pesar de ser una empresa de autos personalizados, hay algunos modelos que se venden más comúnmenete. No es eficiente crear de nuevo cada uno de los carros ni hacer que el usuario interactue directamente con la clase de Car, especialmente para "ocultar" sus atributos.
- __Razón por la cual se escogió__: El patrón builder permite a un usuario crear un objeto, en este caso un carro, al ir asignandole cada una de sus características sin tener que interactuar directamente con este. Por medio del builder y el director que permite crear plantillas, la creación de objetos personalizados pero con atributos definidos me pareció un buen lugar para utilizarlo.
- __Cómo se solucionó el problema__: El carro personalizado se crea mediante el CarBuilder al darle primero su nombre, el precio base del modelo escogido, su grupo de características personalizadas. El builder permite la creación de varios carros distintos, por lo que un mismo cliente en una misma orden puede crear los carros de una manera más sencilla. De igual manera, los autos más pedidos se pueden crear por medio del CarDirector, así evitando incluso tener que definir cada uno de los atributos de un carro manualmente.

### Uso de patrón de diseño estructural: Composite
- __Problema__: Los autos pueden tener muchas características y cada una de estas tiene que agregar su precio al costo total del carro. De igual manera, al mostrarlo en el ticket, se deben ver cada una de las características seleccionadas de manera desglosada, pero agrupadas de acuerdo a su función, las cuales varían entre carros.
- __Razón por la cual se escogió__: El patrón composite permite crear estructuras tipo folder en donde dentro de un grupo puede haber grupos pero también items individuales. Esta es exactamente la estructura que los grupos de características deben tener en el ticket de la empresa.
- __Cómo se solucionó el problema__: Se crean características personalizadas individuales como leaves del patrón estructural y estas se pueden ordenar en Tech Features, Paint Jobs, etc. Cada una de las características tiene su precio, y al ponerlas dentro de un grupo, se puede obtener el precio total del grupo para el cálculo del costo total de un carro. De igual manera, de acuerdo al nivel de anidación, la identación va aumentando, haciendo el desglose de características mucho más legible, pues también se incluye el precio junto a su característica.

### Uso de patrón de diseño de comportamiento: Iterator
- __Problema__: Al momento de guardar y mostrar la orden debía existir una especie de colección en la que almacenar los carros a comprar y una manera de recorrerlo. Esta empresa guarda los carros a comprar en su sitema de acuerdo al momento en que fueron marcados, pero quiere que se muestren en su ticket en orden alfabético sin que se conozca el orden guardado en el sistema.
- __Razón por la cual se escogió__: El patrón iterator permite recorrer una colección sin exponer la manera en que está organizada originalmente, que es lo que se quiere. De igual manera, al definir el iterator se especifica la manera en la que se quiere recorrer, por lo que se puede hacer que se recorra en la manera personalizada que se solicita.
- __Cómo se solucionó el problema__: Se creó una colección de carros llamada CarOrder en la que se guardan los carros conforme se van agregando para el uso que la empresa quiera darle. Esta misma clase crea un OrderIterator que recorre la lista alfabéticamente y es el que se usa al momento de imprimir la orden.

### Uso de patrón de diseño estructural: Adapter
- __Problema__: Para realizar los pagos en la empresa siempre habían utilizado el servicio de pago de LowPayment, pero ahora que su empresa va creciendo y los clientes piden más autos en una misma orden, quieren adoptar el servicio de AnyPayment, pero su sistema actual no coincide con el servicio proporcionado por AnyPayment.
- __Razón por la cual se escogió__: El patrón de adapter permite, como su nombre lo dice, crear un adaptador para poder "estandarizar" el uso de una clase en un sistema ya existente sin tener que modificarlo a estas nuevas características o funciones.
- __Cómo se solucionó el problema__: Se creó una clase AnyPaymentAdapter que pasa la petición de pago del sistema actual al servicio de AnyPayment. Es en esta clase adaptador que se llama a la función equivalente para que realice el proceso de pago y se le pasan sus parámetros que no coinciden con los proporcionados por el sistema actual. De esta manera, no se cambia el sistema y se puede seguir usando el servicio anterior y ahora también el nuevo servicio.

### Diagrama de Clases
![3 8_DiagramaClases_ProyectoIntegrador](https://github.com/user-attachments/assets/147ca75b-9642-4aca-81e9-7b51506efcc8)

