import re


def parse_request(text):

    # Valores por defecto
    app_name = "nginx"
    image = "nginx:latest"
    replicas = 1
    port = 80

    namespace = "default"
    hostname = "example.local"

    app_env = "prod"
    log_level = "INFO"

    username = "admin"
    password = "changeme"

    # Imagen
    image_match = re.search(
        r"imagen\s+([^\s]+)",
        text,
        re.IGNORECASE
    )

    if image_match:
        image = image_match.group(1)

    # Replicas
    replicas_match = re.search(
        r"(\d+)\s*replicas",
        text,
        re.IGNORECASE
    )

    if replicas_match:
        replicas = int(
            replicas_match.group(1)
        )

    # Puerto
    port_match = re.search(
        r"puerto\s+(\d+)",
        text,
        re.IGNORECASE
    )

    if port_match:
        port = int(
            port_match.group(1)
        )

    # Aplicación
    app_match = re.search(
        r"aplicaci[oó]n\s+([a-zA-Z0-9\-]+)",
        text,
        re.IGNORECASE
    )

    if app_match:
        app_name = app_match.group(1)

    # Namespace
    namespace_match = re.search(
        r"namespace\s+([a-zA-Z0-9\-]+)",
        text,
        re.IGNORECASE
    )

    if namespace_match:
        namespace = namespace_match.group(1)

    # Host
    host_match = re.search(
        r"host\s+([^\s]+)",
        text,
        re.IGNORECASE
    )

    if host_match:
        hostname = host_match.group(1)

    # Usuario
    user_match = re.search(
        r"usuario\s+([^\s]+)",
        text,
        re.IGNORECASE
    )

    if user_match:
        username = user_match.group(1)

    # Password
    password_match = re.search(
        r"password\s+([^\s]+)",
        text,
        re.IGNORECASE
    )

    if password_match:
        password = password_match.group(1)

    # Ambiente
    env_match = re.search(
        r"ambiente\s+([^\s]+)",
        text,
        re.IGNORECASE
    )

    if env_match:
        app_env = env_match.group(1)

    # Log
    log_match = re.search(
        r"log\s+([^\s]+)",
        text,
        re.IGNORECASE
    )

    if log_match:
        log_level = log_match.group(1)

    return {
        "app_name": app_name,
        "image": image,
        "replicas": replicas,
        "port": port,
        "namespace": namespace,
        "hostname": hostname,
        "app_env": app_env,
        "log_level": log_level,
        "username": username,
        "password": password
    }