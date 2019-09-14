from os import path
# Valores máximos y mínimos de las partes y el peso de los vehículos

AUTOMOVIL = {
    'CHASIS': {
        'MIN': 12,
        'MAX': 20
    },
    'CARROCERIA': {
        'MIN': 10,
        'MAX': 18
    },
    'RUEDAS': {
        'MIN': 10,
        'MAX': 14
    },
    'MOTOR': {
        'MIN': 14,
        'MAX': 20
    },
    'ZAPATILLAS': {
        'MIN': 0,
        'MAX': 10
    },
    'PESO': {
        'MIN': 16,
        'MAX': 18
    }
}

TRONCOMOVIL = {
    'CHASIS': {
        'MIN': 12,
        'MAX': 18
    },
    'CARROCERIA': {
        'MIN': 14,
        'MAX': 16
    },
    'RUEDAS': {
        'MIN': 6,
        'MAX': 14
    },
    'MOTOR': {
        'MIN': 0,
        'MAX': 8
    },
    'ZAPATILLAS': {
        'MIN': 10,
        'MAX': 14
    },
    'PESO': {
        'MIN': 10,
        'MAX': 14
    }
}

MOTOCICLETA = {
    'CHASIS': {
        'MIN': 8,
        'MAX': 14
    },
    'CARROCERIA': {
        'MIN': 10,
        'MAX': 14
    },
    'RUEDAS': {
        'MIN': 14,
        'MAX': 18
    },
    'MOTOR': {
        'MIN': 12,
        'MAX': 18
    },
    'ZAPATILLAS': {
        'MIN': 0,
        'MAX': 10
    },
    'PESO': {
        'MIN': 8,
        'MAX': 10
    }
}

BICICLETA = {
    'CHASIS': {
        'MIN': 12,
        'MAX': 18
    },
    'CARROCERIA': {
        'MIN': 6,
        'MAX': 10
    },
    'RUEDAS': {
        'MIN': 10,
        'MAX': 16
    },
    'MOTOR': {
        'MIN': 0,
        'MAX': 10
    },
    'ZAPATILLAS': {
        'MIN': 12,
        'MAX': 20
    },
    'PESO': {
        'MIN': 4,
        'MAX': 8
    }
}


# Mejoras de las partes de los vehículos

MEJORAS = {
    'CHASIS': {
        'COSTO': 100,
        'EFECTO': 2
    },
    'CARROCERIA': {
        'COSTO': 200,
        'EFECTO': 2
    },
    'RUEDAS': {
        'COSTO': 500,
        'EFECTO': 6
    },
    'MOTOR': {
        'COSTO': 400,
        'EFECTO': 4
    },
    'ZAPATILLAS': {
        'COSTO': 200,
        'EFECTO': 4
    }
}


# Características de los pilotos de los diferentes equipos

EQUIPOS = {
    'TAREOS': {
        'CONTEXTURA': {
            'MIN': 12,
            'MAX': 18
        },
        'EQUILIBRIO': {
            'MIN': 16,
            'MAX': 20
        },
        'PERSONALIDAD': "osada"
    },
    'HIBRIDOS': {
        'CONTEXTURA': {
            'MIN': 12,
            'MAX': 18
        },
        'EQUILIBRIO': {
            'MIN': 14,
            'MAX': 20
        },
        'PERSONALIDAD': "precavido"
    },
    'DOCENCIOS': {
        'CONTEXTURA': {
            'MIN': 14,
            'MAX': 20
        },
        'EQUILIBRIO': {
            'MIN': 8,
            'MAX': 14
        },
        'PERSONALIDAD': "precavido"
    }
}


# Las constantes de las formulas

# Velocidad real
VELOCIDAD_MINIMA = 10

# Velocidad intencional
EFECTO_OSADO = 2
EFECTO_PRECAVIDO = 6

# Dificultad de control del vehículo
PESO_MEDIO = 22
EQUILIBRIO_PRECAVIDO = 14

# Tiempo pits
TIEMPO_MINIMO_PITS = 20
VELOCIDAD_PITS = 12

# Experiencia por ganar
BONIFICACION_PRECAVIDO = 16
BONIFICACION_OSADO = 20

# Efectos hielo y roca
POND_EFECT_ROCAS = 12
POND_EFECT_DIFICULTAD = 16
POND_EFECT_HIELO = 14

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
