from pathlib import Path

# Directorio base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Directorios
TEMPLATE_DIR = BASE_DIR / "templates"
GENERATED_DIR = BASE_DIR / "generated"

# Crear generated si no existe
GENERATED_DIR.mkdir(parents=True, exist_ok=True)


def generate_namespace(namespace):

    template = (
        TEMPLATE_DIR / "namespace.yaml"
    ).read_text()

    content = (
        template
        .replace("NAMESPACE", namespace)
    )

    output_file = (
        GENERATED_DIR /
        f"{namespace}-namespace.yaml"
    )

    print(f"Creando: {output_file}")

    output_file.write_text(
    content + "\n",
    encoding="utf-8"
)

    return content


def generate_ingress(
    app_name,
    hostname,
    port
):

    template = (
        TEMPLATE_DIR / "ingress.yaml"
    ).read_text()

    content = (
        template
        .replace("APP_NAME", app_name)
        .replace("HOSTNAME", hostname)
        .replace("PORT", str(port))
    )

    output_file = (
        GENERATED_DIR /
        f"{app_name}-ingress.yaml"
    )

    print(f"Creando: {output_file}")

    output_file.write_text(
    content + "\n",
    encoding="utf-8"
)

    return content


def generate_deployment(
    app_name,
    image,
    replicas,
    port
):

    template = (
        TEMPLATE_DIR / "deployment.yaml"
    ).read_text()

    content = (
        template
        .replace("APP_NAME", app_name)
        .replace("IMAGE", image)
        .replace("REPLICAS", str(replicas))
        .replace("PORT", str(port))
    )

    output_file = (
        GENERATED_DIR /
        f"{app_name}-deployment.yaml"
    )

    print(f"Creando: {output_file}")

    output_file.write_text(
    content + "\n",
    encoding="utf-8"
)

    return content


def generate_service(
    app_name,
    port
):

    template = (
        TEMPLATE_DIR / "service.yaml"
    ).read_text()

    content = (
        template
        .replace("APP_NAME", app_name)
        .replace("PORT", str(port))
    )

    output_file = (
        GENERATED_DIR /
        f"{app_name}-service.yaml"
    )

    print(f"Creando: {output_file}")

    output_file.write_text(
    content + "\n",
    encoding="utf-8"
)
    
    return content
def generate_configmap(
    app_name,
    app_env,
    log_level
):

    template = (
        TEMPLATE_DIR / "configmap.yaml"
    ).read_text()

    content = (
        template
        .replace("APP_NAME", app_name)
        .replace("APP_ENV", app_env)
        .replace("LOG_LEVEL", log_level)
    )

    output_file = (
        GENERATED_DIR /
        f"{app_name}-configmap.yaml"
    )

    print(f"Creando: {output_file}")

    output_file.write_text(
        content + "\n",
        encoding="utf-8"
    )

    return content

def generate_secret(
    app_name,
    username,
    password
):

    template = (
        TEMPLATE_DIR / "secret.yaml"
    ).read_text()

    content = (
        template
        .replace("APP_NAME", app_name)
        .replace("USERNAME", username)
        .replace("PASSWORD", password)
    )

    output_file = (
        GENERATED_DIR /
        f"{app_name}-secret.yaml"
    )

    print(f"Creando: {output_file}")

    output_file.write_text(
        content + "\n",
        encoding="utf-8"
    )

    return content

def generate_route(
    app_name,
    hostname
):

    template = (
        TEMPLATE_DIR / "route.yaml"
    ).read_text()

    content = (
        template
        .replace("APP_NAME", app_name)
        .replace("HOSTNAME", hostname)
    )

    output_file = (
        GENERATED_DIR /
        f"{app_name}-route.yaml"
    )

    print(f"Creando: {output_file}")

    output_file.write_text(
        content + "\n",
        encoding="utf-8"
    )

    return content