def lambda_handler(event, context):
    """
    Handler básico para probar el flujo CI/CD.
    Solo retorna un mensaje fijo.

    Cambiando algo!!
    """
    return {
        "statusCode": 200,
        "body": "Modelo cargado OK. Predicción = 1. Updating functionn"
    }
