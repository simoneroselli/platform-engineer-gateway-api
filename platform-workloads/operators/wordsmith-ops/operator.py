import kopf
import kubernetes

@kopf.on.create('padre.maronno', 'v1', 'wordsmithapps')
def create_fn(spec, name, namespace, logger, **kwargs):
    # This function triggers when you create a new "MyApp" CR
    logger.info(f"A new wordsmithapps {name} was created with spec: {spec}")

    # You can add logic here to create Deployments, Services, etc.
    # Kopf makes this feel like writing simple Python functions!
    return {'message': 'Hello from your Operator!'}