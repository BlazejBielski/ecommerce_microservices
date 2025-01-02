import docker
import requests


CONSUL_URL = "http://consul:8500/v1/agent/service/egister"

def get_running_services():
    client = docker.from_env()
    services = []

    for container in client.containers.list():
        container_info = container.attrs
        service_name = container.name
        ip = container_info['NetworkSettings']['IPAddress']
        ports = container_info['NetworkSettings']['Ports']
        if ports:
            for port, bindings in ports.items():
                if bindings:
                    services.append({
                        'service_name': service_name,
                        'ip': ip,
                        'port': port,
                    })
    return services

def register_service_in_consul(service):
    response = requests.put(CONSUL_URL, json=service)
    if response.status_code == 200:
        print(f"Successfully registered service {service['Name']} in Consul")
    else:
        print(f"Failed to register service {service['Name']} in Consul with error {response.text}")


if __name__ == '__main__':
    services = get_running_services()
    for service in services:
        register_service_in_consul(service)
