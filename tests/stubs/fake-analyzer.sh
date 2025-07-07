#!/bin/bash

# Simula un analizador externo con diferentes códigos de salida
case "$1" in
    success)
        echo "Análisis exitoso"
        exit 0
        ;;
    failure)
        echo "Error en el análisis"
        exit 1
        ;;
    timeout)
        echo "Tiempo de espera agotado"
        exit 124
        ;;
    *)
        echo "Uso: $0 {success|failure|timeout}"
        exit 2
        ;;
esac