import kopf
import kubernetes

@kopf.on.create('padre.maronno', 'v1', 'wordsmithapps')
def create_fn(spec, name, namespace, logger, **kwargs):
    replicas = spec.get('replicas', 1)

    # Define the Deployment
    deployment = {
        'apiVersion': 'apps/v1',
        'kind': 'Deployment',
        'metadata': {'name': f'{name}-api', 'namespace': namespace},
        'spec': {
            'replicas': replicas,
            'selector': {'matchLabels': {'app': name}},
            'template': {
                'metadata': {'labels': {'app': name}},
                'spec': {'containers': [{'name': 'api', 'image': 'nginx'}]} # Replace with your real image
            }
        }
    }

    # Use Kopf's built-in 'adopt' to make the deployment child of the CR
    kopf.adopt(deployment)
    
    api = kubernetes.client.AppsV1Api()
    api.create_namespaced_deployment(namespace=namespace, body=deployment)
    
    logger.info(f"Deployment {name}-api created with {replicas} replicas")

@kopf.on.update('padre.maronno', 'v1', 'wordsmithapps')
def update_fn(spec, name, namespace, logger, **kwargs):
    replicas = spec.get('replicas', 1)
    
    # Define the update
    api = kubernetes.client.AppsV1Api()
    deployment = api.read_namespaced_deployment(f'{name}-api', namespace)
    deployment.spec.replicas = replicas
    
    api.patch_namespaced_deployment(name=f'{name}-api', namespace=namespace, body=deployment)
    
    logger.info(f"Deployment {name}-api scaled to {replicas} replicas")