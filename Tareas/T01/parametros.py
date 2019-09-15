from os import path
# Valores máximos y mínimos de las partes y el peso de los vehículos

AUTOMOVIL = {
    'CHASIS': {
        'MIN': 180,
        'MAX': 220
    },
    'CARROCERIA': {
        'MIN': 165,
        'MAX': 175
    },
    'RUEDAS': {
        'MIN': 30,
        'MAX': 45
    },
    'MOTOR': {
        'MIN': 180,
        'MAX': 220
    },
    'ZAPATILLAS': {
        'MIN': 0,
        'MAX': 50
    },
    'PESO': {
        'MIN': 500,
        'MAX': 800
    }
}

TRONCOMOVIL = {
    'CHASIS': {
        'MIN': 80,
        'MAX': 100
    },
    'CARROCERIA': {
        'MIN': 90,
        'MAX': 110
    },
    'RUEDAS': {
        'MIN': 35,
        'MAX': 45
    },
    'MOTOR': {
        'MIN': 0,
        'MAX': 50
    },
    'ZAPATILLAS': {
        'MIN': 75,
        'MAX': 85
    },
    'PESO': {
        'MIN': 120,
        'MAX': 300
    }
}

MOTOCICLETA = {
    'CHASIS': {
        'MIN': 60,
        'MAX': 80
    },
    'CARROCERIA': {
        'MIN': 10,
        'MAX': 14
    },
    'RUEDAS': {
        'MIN': 15,
        'MAX': 30
    },
    'MOTOR': {
        'MIN': 30,
        'MAX': 35
    },
    'ZAPATILLAS': {
        'MIN': 0,
        'MAX': 50
    },
    'PESO': {
        'MIN': 130,
        'MAX': 180
    }
}

BICICLETA = {
    'CHASIS': {
        'MIN': 20,
        'MAX': 35
    },
    'CARROCERIA': {
        'MIN': 10,
        'MAX': 25
    },
    'RUEDAS': {
        'MIN': 5,
        'MAX': 10
    },
    'MOTOR': {
        'MIN': 0,
        'MAX': 50
    },
    'ZAPATILLAS': {
        'MIN': 10,
        'MAX': 25
    },
    'PESO': {
        'MIN': 30,
        'MAX': 55
    }
}


# Mejoras de las partes de los vehículos

MEJORAS = {
    'CHASIS': {
        'COSTO': 100,
        'EFECTO': 3
    },
    'CARROCERIA': {
        'COSTO': 50,
        'EFECTO': 2
    },
    'RUEDAS': {
        'COSTO': 120,
        'EFECTO': 4
    },
    'MOTOR': {
        'COSTO': 270,
        'EFECTO': 2
    },
    'ZAPATILLAS': {
        'COSTO': 200,
        'EFECTO': 6
    }
}


# Características de los pilotos de los diferentes equipos

EQUIPOS = {
    'TAREOS': {
        'CONTEXTURA': {
            'MIN': 35,
            'MAX': 45
        },
        'EQUILIBRIO': {
            'MIN': 40,
            'MAX': 50
        },
        'PERSONALIDAD': "precavido"
    },
    'HIBRIDOS': {
        'CONTEXTURA': {
            'MIN': 40,
            'MAX': 55
        },
        'EQUILIBRIO': {
            'MIN': 25,
            'MAX': 40
        },
        'PERSONALIDAD': "osado"
    },
    'DOCENCIOS': {
        'CONTEXTURA': {
            'MIN': 45,
            'MAX': 60
        },
        'EQUILIBRIO': {
            'MIN': 5,
            'MAX': 10
        },
        'PERSONALIDAD': "osado"
    }
}


# Las constantes de las formulas

# Numero de contrincantes por carrera
NUMERO_CONTRINCANTES = 8
# Velocidad real
VELOCIDAD_MINIMA = 1

# Velocidad intencional
EFECTO_OSADO = 4
EFECTO_PRECAVIDO = 2

# Dificultad de control del vehículo
PESO_MEDIO = 100
EQUILIBRIO_PRECAVIDO = 4

# Tiempo pits
TIEMPO_MINIMO_PITS = 20
VELOCIDAD_PITS = 12

# Experiencia por ganar
BONIFICACION_PRECAVIDO = 4
BONIFICACION_OSADO = 6

# Efectos hielo y roca
POND_EFECT_ROCAS = 1
POND_EFECT_DIFICULTAD = 2
POND_EFECT_HIELO = 3

# Paths de los archivos

PATHS = {
    'PISTAS': path.join(path.dirname(__file__), "pistas.csv"),
    'CONTRINCANTES': path.join(path.dirname(__file__), "contrincantes.csv"),
    'PILOTOS': path.join(path.dirname(__file__), "pilotos.csv"),
    'VEHICULOS': path.join(path.dirname(__file__), "vehículos.csv"),
}


# Power-ups

# Caparazon
DMG_CAPARAZON = None

# Relámpago
SPD_RELAMPAGO = None
