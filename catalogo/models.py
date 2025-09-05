from django.db import models

# Create your models here.
catalogo1 = {
    'Alimentación transportada': ['transporte.jpg', 'servicio_transportado'],
    'Alimentación tradicional (presencial)': ['presencial.jpg', 'servicio_tradicional'],
    'Concesión de Casinos': ['casino.jpg', 'servicio_concesion'],
    'Coffee break y eventos': ['cafeb.jpg', 'servicio_coffe'],
    'Repostería y snack con tickets': ['snack.jpg', 'servicio_reposteria'],
}

catalogo_transportado = {
    'Almuerzo tradicional': ['almuerzo.jpg', 'menu_transportado'],
    'Vegetariano': ['vegetariano.jpg', 'menu_transportado'],
    'Vegano': ['vegano.jpg', 'menu_transportado'],
    'Hipocalórico': ['hipocalorico.jpg', 'menu_transportado'],
    'Menú especial del día' : ['especial.jpg', 'menu_transportado'],
}

catalogo_coffee = {
    'Sándwiches': ['sandwiches.jpg', 'menu_coffe'],
    'Jugos naturales': ['jugos.jpg', 'menu_coffe'],
    'Repostería': ['reposteria.jpg', 'menu_coffe'],
    'Colaciones dulces': ['colacion.jpg', 'menu_coffe'],
    'Colaciones saladas': ['colacion2.jpg', 'menu_coffe'],
}

catalogo_tradicional = {
    'Menú Ejecutivo': ['ejecutivo.jpg', 'menu_especial'],
    'Menú Saludable': ['saludable.jpg', 'menu_especial'],
    'Desayuno Completo': ['desayuno.jpg', 'menu_especial'],
    'Cena Ligera': ['cena.jpg', 'menu_especial'],
    'Menú Regional': ['regional.jpg', 'menu_especial'],
}

catalogo_reposteria = {
    'Queques': ['queques.jpg', 'menu_reposteria'],
    'Tortas': ['tortas.jpg', 'menu_reposteria'],
    'Galletas': ['galletas.jpg', 'menu_reposteria'],
    'Brownies': ['brownies.jpg', 'menu_reposteria'],
    'Muffins': ['muffins.jpg', 'menu_reposteria'],
}

catalogo_concesion = {
    'personal de aseo ': ['aseo.jpg', 'menu_concesion'],
    'personal de alimentación': ['alimentacion.jpg', 'menu_concesion'],
    'personal de montaje': ['montaje.jpg', 'menu_concesion'],
    'personal administrativo': ['administrativo.jpg', 'menu_concesion'],
    'personal de mantención': ['mantencion.jpg', 'menu_concesion']

}





menu_transportado = [
    {'Nombre':'Pollo a la chilena con arroz y ensalada',
     'Descripcion':'Plato casero clásico, nutritivo y balanceado.',
     'Ingredientes':'Pollo al horno con especias, arroz blanco, ensalada de lechuga y tomate',
     'Tiempo de entrega':'30 - 40 Minutos',
     'Condiciones de consumo':'Consumir caliente, mantener a una temperatura superior a 65°C hasta servir. No recomendado recalentar más de una vez.'},

    {'Nombre':'Lasagna de verduras gratinada',
     'Descripcion':'Opción sin carne con variedad de vegetales frescos.',
     'Ingredientes':'Berenjena, zapallo italiano, champiñones, espinaca, salsa bechamel, queso mozzarella',
     'Tiempo de entrega':'35 - 45 Minutos',
     'Condiciones de consumo':'Mantener en envase térmico; consumir antes de 2 horas tras la entrega. Recalentar en horno o microondas si es necesario.'},

    {'Nombre':'Bowl de quinoa mediterráneo',
     'Descripcion':'Plato ligero, 100% vegetal, ideal para energía y frescura.',
     'Ingredientes':'Quinoa cocida, garbanzos, pepino, tomate cherry, aceitunas, palta, aderezo de limón y aceite de oliva',
     'Tiempo de entrega':'25 - 35 Minutos',
     'Condiciones de consumo':'Mantener refrigerado si no se consume de inmediato; apto para consumirse frío o a temperatura ambiente.'},

    {'Nombre':'Filete de pescado con ensalada fresca',
     'Descripcion':'Preparación baja en calorías, rica en proteínas y omega-3.',
     'Ingredientes':'Filete de merluza a la plancha, ensalada de rúcula con zanahoria y pepino, rodaja de limón',
     'Tiempo de entrega':'25 - 30 Minutos',
     'Condiciones de consumo':'Servir inmediatamente tras la entrega o mantener en envase térmico; no dejar más de 1 hora sin refrigeración.'},

    {'Nombre':'Pastel de choclo tradicional',
     'Descripcion':'Receta típica chilena, especial para el menú del día.',
     'Ingredientes':'Pino de carne, huevo duro, aceitunas, pollo desmenuzado, masa de choclo molido gratinada',
     'Tiempo de entrega':'40 - 50 Minutos',
     'Condiciones de consumo':'Mantener en envase térmico cerrado; consumir caliente, idealmente dentro de los 30 minutos posteriores a la entrega.'}
]
menu_coffe = [
    {'Nombre':'Sándwich de pollo a la plancha',
     'Descripcion':'Sándwich nutritivo y clásico en pan frica.',
     'Ingredientes':'Pechuga de pollo a la plancha, lechuga, tomate, palta, mayonesa, pan frica',
     'Tiempo de entrega':'15 - 20 Minutos',
     'Condiciones de consumo':'Consumir fresco, mantener a temperatura ambiente máxima de 25°C. No recomendable refrigerar más de 24 horas.'},

    {'Nombre':'Jugo natural de naranja',
     'Descripcion':'Bebida refrescante y rica en vitamina C.',
     'Ingredientes':'Naranjas frescas exprimidas, sin aditivos',
     'Tiempo de entrega':'10 - 15 Minutos',
     'Condiciones de consumo':'Mantener refrigerado a 4°C. Consumir dentro de las 2 horas posteriores a la preparación.'},

    {'Nombre':'Queque casero de zanahoria',
     'Descripcion':'Repostería suave y dulce con toques caseros.',
     'Ingredientes':'Harina, zanahoria rallada, azúcar, huevos, aceite vegetal, polvos de hornear',
     'Tiempo de entrega':'20 - 30 Minutos',
     'Condiciones de consumo':'Mantener en envase cerrado a temperatura ambiente hasta 24 horas o refrigerado hasta 48 horas.'},

    {'Nombre':'Barrita energética de avena y miel',
     'Descripcion':'Colación dulce práctica y saludable.',
     'Ingredientes':'Avena, miel, frutos secos, semillas de chía',
     'Tiempo de entrega':'15 - 20 Minutos',
     'Condiciones de consumo':'Conservar en envase sellado, en lugar fresco y seco. Consumir en un máximo de 3 días.'},

    {'Nombre':'Empanada de queso',
     'Descripcion':'Colación salada tradicional y sabrosa.',
     'Ingredientes':'Masa de empanada, queso mantecoso',
     'Tiempo de entrega':'20 - 25 Minutos',
     'Condiciones de consumo':'Consumir caliente, mantener en envase térmico hasta 1 hora después de la entrega. Recalentar en horno si es necesario.'}
]

menu_reposteria = [
    {'Nombre':'Queque de plátano',
     'Descripcion':'Bizcocho casero suave y húmedo, ideal para acompañar con té o café.',
     'Ingredientes':'Harina, plátano maduro, azúcar, huevos, leche, mantequilla',
     'Tiempo de entrega':'20 - 30 Minutos',
     'Condiciones de consumo':'Mantener en envase cerrado a temperatura ambiente hasta 24 horas o refrigerado hasta 48 horas.'},

    {'Nombre':'Torta de tres leches',
     'Descripcion':'Postre clásico y cremoso, empapado en mezcla de leches.',
     'Ingredientes':'Bizcocho de vainilla, leche condensada, leche evaporada, crema de leche, merengue',
     'Tiempo de entrega':'30 - 40 Minutos',
     'Condiciones de consumo':'Conservar refrigerada a 4°C y consumir en un máximo de 48 horas.'},

    {'Nombre':'Galletas de avena y pasas',
     'Descripcion':'Galletas crujientes y nutritivas, perfectas como snack.',
     'Ingredientes':'Harina, avena, pasas, azúcar morena, mantequilla, huevo',
     'Tiempo de entrega':'15 - 20 Minutos',
     'Condiciones de consumo':'Guardar en frasco o envase hermético. Consumir dentro de 5 días.'},

    {'Nombre':'Brownie de chocolate',
     'Descripcion':'Bizcocho húmedo de chocolate intenso, estilo americano.',
     'Ingredientes':'Chocolate amargo, mantequilla, azúcar, huevos, harina',
     'Tiempo de entrega':'20 - 30 Minutos',
     'Condiciones de consumo':'Mantener en envase cerrado a temperatura ambiente hasta 48 horas o refrigerado hasta 4 días.'},

    {'Nombre':'Muffin de arándanos',
     'Descripcion':'Pastelito individual esponjoso con frutas naturales.',
     'Ingredientes':'Harina, azúcar, leche, huevo, mantequilla, arándanos frescos',
     'Tiempo de entrega':'15 - 25 Minutos',
     'Condiciones de consumo':'Consumir en un máximo de 2 días. Guardar en envase cerrado a temperatura ambiente.'}
]

menu_especial = [
    {'Nombre':'Lomo saltado con arroz',
     'Descripcion':'Plato ejecutivo inspirado en la cocina peruana, mezcla de carne y verduras salteadas con arroz.',
     'Ingredientes':'Lomo de res, cebolla morada, tomate, pimentón, salsa de soya, arroz blanco',
     'Tiempo de entrega':'30 - 40 Minutos',
     'Condiciones de consumo':'Consumir caliente, mantener en envase térmico y no recalentar más de una vez.'},

    {'Nombre':'Ensalada César con pollo grillado',
     'Descripcion':'Opción saludable y fresca, alta en proteínas y baja en grasas.',
     'Ingredientes':'Lechuga romana, pollo grillado, crutones, queso parmesano, aderezo César ligero',
     'Tiempo de entrega':'20 - 30 Minutos',
     'Condiciones de consumo':'Mantener refrigerada a 4°C si no se consume de inmediato. Consumir en un máximo de 2 horas tras la entrega.'},

    {'Nombre':'Desayuno americano',
     'Descripcion':'Desayuno completo con variedad de sabores dulces y salados.',
     'Ingredientes':'Huevos revueltos, tocino, pan tostado, jugo de naranja natural, café',
     'Tiempo de entrega':'15 - 25 Minutos',
     'Condiciones de consumo':'Consumir inmediatamente tras la entrega. Mantener bebidas refrigeradas y alimentos calientes en envase térmico.'},

    {'Nombre':'Crema de zapallo con tostadas integrales',
     'Descripcion':'Cena ligera, cálida y de fácil digestión.',
     'Ingredientes':'Zapallo, cebolla, zanahoria, caldo de verduras, tostadas de pan integral',
     'Tiempo de entrega':'20 - 30 Minutos',
     'Condiciones de consumo':'Consumir caliente. Mantener en envase térmico y no dejar reposar más de 1 hora sin refrigerar.'},

    {'Nombre':'Cazuela de vacuno',
     'Descripcion':'Menú regional típico chileno, abundante y nutritivo.',
     'Ingredientes':'Carne de vacuno, papa, zapallo, choclo, arroz, zanahoria, porotos verdes',
     'Tiempo de entrega':'40 - 50 Minutos',
     'Condiciones de consumo':'Consumir caliente, mantener en envase térmico cerrado. Recalentar solo una vez antes de servir.'}
]

menu_concesion = [
    {'Nombre':'Personal de aseo',
     'Descripcion':'Encargado de limpiar y mantener higiénico el espacio donde se ofrece el servicio.',
     'Componentes principales':'Escobas, traperos, productos de limpieza, desinfectantes, guantes, bolsas de basura'},

    {'Nombre':'Personal de alimentación',
     'Descripcion':'Responsable de preparar y manipular los alimentos de manera segura y eficiente.',
     'Componentes principales':'Utensilios de cocina, ollas, sartenes, cuchillos, tablas de picar, uniforme de cocina, guantes'},

    {'Nombre':'Personal de equipación',
     'Descripcion':'Encargado de montar y alistar todo el lugar: mesas, sillas, decoración y logística básica.',
     'Componentes principales':'Mesas, sillas, manteles, decoración, vajilla, cubiertos, cristalería'},

    {'Nombre':'Personal administrativo',
     'Descripcion':'Se asegura de la correcta organización y gestión del servicio, coordinando todas las áreas.',
     'Componentes principales':'Computador, documentos de control, planillas de gestión, software administrativo, teléfono de contacto'},

    {'Nombre':'Personal de mantención',
     'Descripcion':'Atiende reparaciones y resuelve imprevistos técnicos o de infraestructura durante el servicio.',
     'Componentes principales':'Herramientas básicas, kit de electricidad, kit de fontanería, repuestos menores'}
]




