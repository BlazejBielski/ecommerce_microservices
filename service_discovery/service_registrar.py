import docker
import requests


CONSUL_URL = "http://consul:8500//v1/agent/service/register"

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
                    numeric_port = int(port.split('/')[0])
                    services.append({
                        'service_name': service_name,
                        'ip': ip,
                        'port': numeric_port,
                    })
    return services

def register_service(service_name, service_id, address, port):
    payload = {
        "Name": service_name,
        "ID": service_id,
        "Address": address,
        "Port": port
    }
    try:
        response = requests.put(CONSUL_URL, json=payload)
        response.raise_for_status()
        print(f"Service {service_name} registered successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to register service {service_name} with error: {e}")


if __name__ == '__main__':
    services = get_running_services()
    for service in services:
        service_name = service['service_name']
        ip = service['ip']
        port = service['port']
        service_id = f"{service_name}-{port}"
        register_service(service_name, service_id, ip, port)
