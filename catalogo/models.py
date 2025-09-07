from django.db import models

# Create your models here.
catalogo1 = {
    1: {'nombre': 'Alimentación transportada', 'imagen': 'transporte.jpg', 'servicio': 'servicio_transportado'},
    2: {'nombre': 'Alimentación tradicional (presencial)', 'imagen': 'presencial.jpg', 'servicio': 'servicio_tradicional'},
    3: {'nombre': 'Concesión de Casinos', 'imagen': 'casino.jpg', 'servicio': 'servicio_concesion'},
    4: {'nombre': 'Coffee break y eventos', 'imagen': 'cafeb.jpg', 'servicio': 'servicio_coffe'},
    5: {'nombre': 'Repostería y snack con tickets', 'imagen': 'snack.jpg', 'servicio': 'servicio_reposteria'},
}

catalogo_transportado = {
    1: {'nombre': 'Almuerzo tradicional', 'imagen': 'pollo a la chilena.png'},
    2: {'nombre': 'Vegetariano', 'imagen': 'lasagna de verduras.png'},
    3: {'nombre': 'Vegano', 'imagen': 'bowl de quinoa.png'},
    4: {'nombre': 'Hipocalórico', 'imagen': 'filete de pescado.png'},
    5: {'nombre': 'Menú especial del día', 'imagen': 'especial.jpg'},
}

catalogo_coffee = {
    1: {'nombre': 'Sándwiches', 'imagen': 'sandwiches.jpg'},
    2: {'nombre': 'Jugos naturales', 'imagen': 'jugos.jpg'},
    3: {'nombre': 'Repostería', 'imagen': 'reposteria.jpg'},
    4: {'nombre': 'Colaciones dulces', 'imagen': 'colacion.jpg'},
    5: {'nombre': 'Colaciones saladas', 'imagen': 'colacion2.jpg'},
}

catalogo_tradicional = {
    1: {'nombre': 'Menú Ejecutivo', 'imagen': 'ejecutivo.jpg'},
    2: {'nombre': 'Menú Saludable', 'imagen': 'saludable.jpg'},
    3: {'nombre': 'Desayuno Completo', 'imagen': 'desayuno.jpg'},
    4: {'nombre': 'Cena Ligera', 'imagen': 'cena.jpg'},
    5: {'nombre': 'Menú Regional', 'imagen': 'regional.jpg'},
}

catalogo_reposteria = {
    1: {'nombre': 'Queques', 'imagen': 'queques.jpg'},
    2: {'nombre': 'Tortas', 'imagen': 'tortas.jpg'},
    3: {'nombre': 'Galletas', 'imagen': 'galletas.jpg'},
    4: {'nombre': 'Brownies', 'imagen': 'brownies.jpg'},
    5: {'nombre': 'Muffins', 'imagen': 'muffins.jpg'},
}

catalogo_concesion = {
    1: {'nombre': 'Personal de aseo', 'imagen': 'aseo.jpg'},
    2: {'nombre': 'Personal de alimentación', 'imagen': 'alimentacion.jpg'},
    3: {'nombre': 'Personal de montaje', 'imagen': 'montaje.jpg'},
    4: {'nombre': 'Personal administrativo', 'imagen': 'administrativo.jpg'},
    5: {'nombre': 'Personal de mantención', 'imagen': 'mantencion.jpg'},
}

#Agregar imagenes a los menús
menu_transportado = {
    1: {'nombre':'Pollo a la chilena con arroz y ensalada',
        'descripcion':'Plato casero clásico, nutritivo y balanceado.',
        'ingredientes':'Pollo al horno con especias, arroz blanco, ensalada de lechuga y tomate',
        'tiempo_entrega':'30 - 40 Minutos',
        'condiciones_consumo':'Consumir caliente, mantener a una temperatura superior a 65°C hasta servir. No recomendado recalentar más de una vez.','imagen':'pollo a la chilena.png'},
    2: {'nombre':'Lasagna de verduras gratinada',
        'descripcion':'Opción sin carne con variedad de vegetales frescos.',
        'ingredientes':'Berenjena, zapallo italiano, champiñones, espinaca, salsa bechamel, queso mozzarella',
        'tiempo_entrega':'35 - 45 Minutos',
        'condiciones_consumo':'Mantener en envase térmico; consumir antes de 2 horas tras la entrega. Recalentar en horno o microondas si es necesario.','imagen':'lasagna de verduras.png'},

    3: {'nombre':'Bowl de quinoa mediterráneo',
        'descripcion':'Plato ligero, 100% vegetal, ideal para energía y frescura.',
        'ingredientes':'Quinoa cocida, garbanzos, pepino, tomate cherry, aceitunas, palta, aderezo de limón y aceite de oliva',
        'tiempo_entrega':'25 - 35 Minutos',
        'condiciones_consumo':'Mantener refrigerado si no se consume de inmediato; apto para consumirse frío o a temperatura ambiente.','imagen':'bowl de quinoa.png'},

    4: {'nombre':'Filete de pescado con ensalada fresca',
        'descripcion':'Preparación baja en calorías, rica en proteínas y omega-3.',
        'ingredientes':'Filete de merluza a la plancha, ensalada de rúcula con zanahoria y pepino, rodaja de limón',
        'tiempo_entrega':'25 - 30 Minutos',
        'condiciones_consumo':'Servir inmediatamente tras la entrega o mantener en envase térmico; no dejar más de 1 hora sin refrigeración.','imagen':'filete de pescado.png'},

    5: {'nombre':'Pastel de choclo tradicional',
        'descripcion':'Receta típica chilena, especial para el menú del día.',
        'ingredientes':'Pino de carne, huevo duro, aceitunas, pollo desmenuzado, masa de choclo molido gratinada',
        'tiempo_entrega':'40 - 50 Minutos',
        'condiciones_consumo':'Mantener en envase térmico cerrado; consumir caliente, idealmente dentro de los 30 minutos posteriores a la entrega.','imagen':'pastel de choclo.png'}
}

menu_coffe = {
    1: {'nombre':'Sándwich de pollo a la plancha',
        'descripcion':'Sándwich nutritivo y clásico en pan frica.',
        'ingredientes':'Pechuga de pollo a la plancha, lechuga, tomate, palta, mayonesa, pan frica',
        'tiempo_entrega':'15 - 20 Minutos',
        'condiciones_consumo':'Consumir fresco, mantener a temperatura ambiente máxima de 25°C. No recomendable refrigerar más de 24 horas.'},

    2: {'nombre':'Jugo natural de naranja',
        'descripcion':'Bebida refrescante y rica en vitamina C.',
        'ingredientes':'Naranjas frescas exprimidas, sin aditivos',
        'tiempo_entrega':'10 - 15 Minutos',
        'condiciones_consumo':'Mantener refrigerado a 4°C. Consumir dentro de las 2 horas posteriores a la preparación.'},

    3: {'nombre':'Queque casero de zanahoria',
        'descripcion':'Repostería suave y dulce con toques caseros.',
        'ingredientes':'Harina, zanahoria rallada, azúcar, huevos, aceite vegetal, polvos de hornear',
        'tiempo_entrega':'20 - 30 Minutos',
        'condiciones_consumo':'Mantener en envase cerrado a temperatura ambiente hasta 24 horas o refrigerado hasta 48 horas.'},

    4: {'nombre':'Barrita energética de avena y miel',
        'descripcion':'Colación dulce práctica y saludable.',
        'ingredientes':'Avena, miel, frutos secos, semillas de chía',
        'tiempo_entrega':'15 - 20 Minutos',
        'condiciones_consumo':'Conservar en envase sellado, en lugar fresco y seco. Consumir en un máximo de 3 días.'},

    5: {'nombre':'Empanada de queso',
        'descripcion':'Colación salada tradicional y sabrosa.',
        'ingredientes':'Masa de empanada, queso mantecoso',
        'tiempo_entrega':'20 - 25 Minutos',
        'condiciones_consumo':'Consumir caliente, mantener en envase térmico hasta 1 hora después de la entrega. Recalentar en horno si es necesario.'}
}

menu_reposteria = {
    1: {'nombre':'Queque de plátano',
        'descripcion':'Bizcocho casero suave y húmedo, ideal para acompañar con té o café.',
        'ingredientes':'Harina, plátano maduro, azúcar, huevos, leche, mantequilla',
        'tiempo_entrega':'20 - 30 Minutos',
        'condiciones_consumo':'Mantener en envase cerrado a temperatura ambiente hasta 24 horas o refrigerado hasta 48 horas.'},

    2: {'nombre':'Torta de tres leches',
        'descripcion':'Postre clásico y cremoso, empapado en mezcla de leches.',
        'ingredientes':'Bizcocho de vainilla, leche condensada, leche evaporada, crema de leche, merengue',
        'tiempo_entrega':'30 - 40 Minutos',
        'condiciones_consumo':'Conservar refrigerada a 4°C y consumir en un máximo de 48 horas.'},

    3: {'nombre':'Galletas de avena y pasas',
        'descripcion':'Galletas crujientes y nutritivas, perfectas como snack.',
        'ingredientes':'Harina, avena, pasas, azúcar morena, mantequilla, huevo',
        'tiempo_entrega':'15 - 20 Minutos',
        'condiciones_consumo':'Guardar en frasco o envase hermético. Consumir dentro de 5 días.'},

    4: {'nombre':'Brownie de chocolate',
        'descripcion':'Bizcocho húmedo de chocolate intenso, estilo americano.',
        'ingredientes':'Chocolate amargo, mantequilla, azúcar, huevos, harina',
        'tiempo_entrega':'20 - 30 Minutos',
        'condiciones_consumo':'Mantener en envase cerrado a temperatura ambiente hasta 48 horas o refrigerado hasta 4 días.'},

    5: {'nombre':'Muffin de arándanos',
        'descripcion':'Pastelito individual esponjoso con frutas naturales.',
        'ingredientes':'Harina, azúcar, leche, huevo, mantequilla, arándanos frescos',
        'tiempo_entrega':'15 - 25 Minutos',
        'condiciones_consumo':'Consumir en un máximo de 2 días. Guardar en envase cerrado a temperatura ambiente.'}
}

menu_tradicional = {
    1: {'nombre':'Lomo saltado con arroz',
        'descripcion':'Plato ejecutivo inspirado en la cocina peruana, mezcla de carne y verduras salteadas con arroz.',
        'ingredientes':'Lomo de res, cebolla morada, tomate, pimentón, salsa de soya, arroz blanco',
        'tiempo_entrega':'30 - 40 Minutos',
        'condiciones_consumo':'Consumir caliente, mantener en envase térmico y no recalentar más de una vez.'},

    2: {'nombre':'Ensalada César con pollo grillado',
        'descripcion':'Opción saludable y fresca, alta en proteínas y baja en grasas.',
        'ingredientes':'Lechuga romana, pollo grillado, crutones, queso parmesano, aderezo César ligero',
        'tiempo_entrega':'20 - 30 Minutos',
        'condiciones_consumo':'Mantener refrigerada a 4°C si no se consume de inmediato. Consumir en un máximo de 2 horas tras la entrega.'},

    3: {'nombre':'Desayuno americano',
        'descripcion':'Desayuno completo con variedad de sabores dulces y salados.',
        'ingredientes':'Huevos revueltos, tocino, pan tostado, jugo de naranja natural, café',
        'tiempo_entrega':'15 - 25 Minutos',
        'condiciones_consumo':'Consumir inmediatamente tras la entrega. Mantener bebidas refrigeradas y alimentos calientes en envase térmico.'},

    4: {'nombre':'Crema de zapallo con tostadas integrales',
        'descripcion':'Cena ligera, cálida y de fácil digestión.',
        'ingredientes':'Zapallo, cebolla, zanahoria, caldo de verduras, tostadas de pan integral',
        'tiempo_entrega':'20 - 30 Minutos',
        'condiciones_consumo':'Consumir caliente. Mantener en envase térmico y no dejar reposar más de 1 hora sin refrigerar.'},

    5: {'nombre':'Cazuela de vacuno',
        'descripcion':'Menú regional típico chileno, abundante y nutritivo.',
        'ingredientes':'Carne de vacuno, papa, zapallo, choclo, arroz, zanahoria, porotos verdes',
        'tiempo_entrega':'40 - 50 Minutos',
        'condiciones_consumo':'Consumir caliente, mantener en envase térmico cerrado. Recalentar solo una vez antes de servir.'}
}

menu_concesion = {
    1: {'nombre':'Personal de aseo',
        'descripcion':'Encargado de limpiar y mantener higiénico el espacio donde se ofrece el servicio.',
        'componentes':'Escobas, traperos, productos de limpieza, desinfectantes, guantes, bolsas de basura'},

    2: {'nombre':'Personal de alimentación',
        'descripcion':'Responsable de preparar y manipular los alimentos de manera segura y eficiente.',
        'componentes':'Utensilios de cocina, ollas, sartenes, cuchillos, tablas de picar, uniforme de cocina, guantes'},

    3: {'nombre':'Personal de montaje',
        'descripcion':'Encargado de montar y alistar todo el lugar: mesas, sillas, decoración y logística básica.',
        'componentes':'Mesas, sillas, manteles, decoración, vajilla, cubiertos, cristalería'},

    4: {'nombre':'Personal administrativo',
        'descripcion':'Se asegura de la correcta organización y gestión del servicio, coordinando todas las áreas.',
        'componentes':'Computador, documentos de control, planillas de gestión, software administrativo, teléfono de contacto'},

    5: {'nombre':'Personal de mantención',
        'descripcion':'Atiende reparaciones y resuelve imprevistos técnicos o de infraestructura durante el servicio.',
        'componentes':'Herramientas básicas, kit de electricidad, kit de fontanería, repuestos menores'}
}