import math

# Diccionario con la radiación solar por zona (kWh/m²/mes)
RADIACION_ANUAL_POR_ZONA = {
    "Costa Caribe": 1643,
    "Región Andina": 1460,
    "Región Pacífica": 1278,
    "Llanos Orientales": 1643,
    "Amazonía": 1278,
    "Desierto de la Guajira": 2190
}

def radiacion_anual_zona (ubicacion):
    if ubicacion in RADIACION_ANUAL_POR_ZONA:
        return RADIACION_ANUAL_POR_ZONA[ubicacion] * 12
    else:
        raise ValueError(f"Ubicación {ubicacion} no encontrada en la base de datos.")


class CalculoNumeroPaneles:
    def __init__(self, ubicacion, potencia):
        self.radiacion_anual = radiacion_anual_zona(ubicacion)
        self.potencia = potencia

        # Potencia de diferentes tipos de paneles (kWp)
        self.potencia_panel_400 = 0.400
        self.potencia_panel_585 = 0.585
        self.potencia_panel_605 = 0.605

        # Área del panel en m²
        self.area_panel = 1.13  

    def energia_generada_por_panel(self):
        """
        Calcula la energía generada anualmente por cada tipo de panel y devuelve los tres valores.
        """
        energia_400 = round(self.potencia_panel_400 * self.radiacion_anual,2)
        energia_585 = round(self.potencia_panel_585 * self.radiacion_anual,2)
        energia_605 = round(self.potencia_panel_605 * self.radiacion_anual,2)
        
        """
        Consumo Anual del cliente
        """
        consumo_anual = self.potencia * 12  # Se usa self.potencia en vez de recibirlo como argumento
        
        """
        CALCULO DE PÁNELES
        """
        numeroPaneles_400 = math.ceil(consumo_anual / energia_400)
        numeroPaneles_585 = math.ceil(consumo_anual / energia_585)
        numeroPaneles_605 = math.ceil(consumo_anual / energia_605)

        return {
            "Consumo Anual (kWh)": consumo_anual,
            "Energía generada por panel de 400W": energia_400,
            "Energía generada por panel de 585W": energia_585,
            "Energía generada por panel de 605W": energia_605,
            "Número de paneles de 400W": numeroPaneles_400,
            "Número de paneles de 585W": numeroPaneles_585,
            "Número de paneles de 605W": numeroPaneles_605,
        }


# ✅ PRUEBA DEL CÓDIGO
ubicacion_seleccionada = "Región Andina"
potencia_cliente = 3000  # kWp/mes

calculo_paneles = CalculoNumeroPaneles(ubicacion_seleccionada, potencia_cliente)
resultados = calculo_paneles.energia_generada_por_panel()

# Imprimir los resultados de la simulación
for key, value in resultados.items():
    print(f"{key}: {value}")
    


# COSTO DEL PROYECTO
def beneficios_del_proyecto(numeroPaneles_400,potencia,costo):
    consumoAnual = potencia*12
    ahorroAnual = consumoAnual*costo
    costokWp = 375320
    costoProyecto = round(costokWp*numeroPaneles_400)
    disminucionRenta = round(costoProyecto/2)
    print("Consumo anual: ", consumoAnual)
    
    return consumoAnual,ahorroAnual,costokWp,costoProyecto,disminucionRenta


#AREA REQUERIDA
def area_requerida(numeroPaneles_400,numeroPaneles_585,numeroPaneles_605):
    areaRequerida_400 = math.ceil(numeroPaneles_400 * 1.13)
    areaRequerida_585 = math.ceil(numeroPaneles_585 * 1.13)
    areaRequerida_605 = math.ceil(numeroPaneles_605 * 1.13)
    return areaRequerida_400,areaRequerida_585,areaRequerida_605

#INVERSORES
def calculo_inversores(numeroPaneles_400,numeroPaneles_585,numeroPaneles_605):
    numeroInversores_3500 = math.ceil((numeroPaneles_400* 400)/3500)
    numeroInversores_6000 = math.ceil((numeroPaneles_585* 585)/6000)
    numeroInversores_12000 = math.ceil((numeroPaneles_605* 600)/12000)
    return numeroInversores_3500,numeroInversores_6000,numeroInversores_12000

def calcular_baterias_gel(consumo):
    """
    Calcula la cantidad de baterías de gel necesarias según la capacidad.
    """
    voltaje_baterias_gel = 12
    capacidad_bateria_gel = math.ceil((consumo / voltaje_baterias_gel) / 0.5)
    baterias_gel_100Ah = math.ceil(capacidad_bateria_gel / 100)
    baterias_gel_150Ah = math.ceil(capacidad_bateria_gel / 150),
    baterias_gel_200Ah = math.ceil(capacidad_bateria_gel / 200),
    baterias_gel_250Ah = math.ceil(capacidad_bateria_gel / 250)

    return baterias_gel_100Ah, baterias_gel_150Ah, baterias_gel_200Ah, baterias_gel_250Ah

def calcular_baterias_litio(consumo):
    """
    Calcula la cantidad de baterías de litio necesarias según la capacidad.
    """
    voltaje_baterias_litio = 24
    capacidad_bateria_litio = math.ceil(((consumo / voltaje_baterias_litio) * 0.9) * 12)
    baterias_litio_60Ah = math.ceil(capacidad_bateria_litio / 60),
    baterias_litio_100Ah = math.ceil(capacidad_bateria_litio / 100),
    baterias_litio_120Ah = math.ceil(capacidad_bateria_litio / 120),
    baterias_litio_150Ah = math.ceil(capacidad_bateria_litio / 150),
    baterias_litio_200Ah = math.ceil(capacidad_bateria_litio / 200)
    
    return baterias_litio_60Ah, baterias_litio_100Ah, baterias_litio_120Ah, baterias_litio_150Ah, baterias_litio_200Ah

def calcular_rieles(numero_paneles):
    """
    Calcula la cantidad de rieles necesarios según la longitud.
    """
    longitud_riel_47 = 4.7
    longitud_riel_48 = 4.8
    rieles_47m_paneles_400W = math.ceil(((numero_paneles["400"] * 1.15) / longitud_riel_47) * 2),
    rieles_47m_paneles_585W = math.ceil(((numero_paneles["585"] * 1.15) / longitud_riel_47) * 2),
    rieles_47m_paneles_605W = math.ceil(((numero_paneles["605"] * 1.15) / longitud_riel_47) * 2)
    rieles_48m_paneles_400W = math.ceil(((numero_paneles["400"] * 1.15) / longitud_riel_48) * 2),
    rieles_48m_paneles_585W = math.ceil(((numero_paneles["585"] * 1.15) / longitud_riel_48) * 2),
    rieles_48m_paneles_605W = math.ceil(((numero_paneles["605"] * 1.15) / longitud_riel_48) * 2)
    
    return rieles_47m_paneles_400W, rieles_47m_paneles_585W, rieles_47m_paneles_605W, rieles_48m_paneles_400W, rieles_48m_paneles_585W, rieles_48m_paneles_605W

def calcular_midcland(numero_paneles):
    """
    Calcula la cantidad de midcland necesarios.
    """
    midcland_400W = math.ceil(numero_paneles["400"] * 2) - 2
    midcland_585W = math.ceil(numero_paneles["585"] * 2) - 2
    midcland_605W = math.ceil(numero_paneles["605"] * 2) - 2

    return midcland_400W, midcland_585W, midcland_605W


def calcular_endcland(numero_paneles):
    """
    Calcula la cantidad de endcland necesarios.
    """
    endcland_400W = math.ceil(numero_paneles["400"] / 2)
    endcland_585W = math.ceil(numero_paneles["585"] / 2)
    endcland_605W = math.ceil(numero_paneles["605"] / 2)

    return endcland_400W, endcland_585W, endcland_605W
