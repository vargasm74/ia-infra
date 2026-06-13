from parser import parse_request

from validator import validate_all

from generator import (
    generate_deployment,
    generate_service,
    generate_namespace,
    generate_ingress,
    generate_configmap,
    generate_secret,
    generate_route
)

print("\n¿Qué infraestructura querés crear?")
print("(finalizá con una línea vacía)\n")

lines = []

while True:
    line = input()

    if line.strip() == "":
        break

    lines.append(line)

request = "\n".join(lines)

print("\nTEXTO RECIBIDO:")
print(repr(request))

data = parse_request(request)

print("\nDATA PARSEADA:")
print(data)

generate_deployment(
    data["app_name"],
    data["image"],
    data["replicas"],
    data["port"]
)

generate_service(
    data["app_name"],
    data["port"]
)

generate_namespace(
    data["namespace"]
)

generate_ingress(
    data["app_name"],
    data["hostname"],
    data["port"]
)

generate_configmap(
    data["app_name"],
    data["app_env"],
    data["log_level"]
)

generate_secret(
    data["app_name"],
    data["username"],
    data["password"]
)

generate_route(
    data["app_name"],
    data["hostname"]
)

is_valid = validate_all(
    "/app/generated"
)

if is_valid:
    print(
        "\n✓ Archivos generados y validados correctamente."
    )
else:
    print(
        "\n✗ La validación falló."
    )