from kubernetes import client, config
import os

def main():
    # Load in-cluster config
    config.load_incluster_config()
    
    namespace = open("/var/run/secrets/kubernetes.io/serviceaccount/namespace").read()
    v1 = client.CoreV1Api()
    
    secrets = v1.list_namespaced_secret(namespace)
    
    print(f"Secrets in namespace '{namespace}':")
    for secret in secrets.items:
        print(f"- {secret.metadata.name}")

if __name__ == "__main__":
    main()
