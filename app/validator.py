import subprocess
import subprocess


def validate_yaml_syntax(path):

    print(f"\nValidando sintaxis YAML en {path}\n")

    result = subprocess.run(
        [
            "yamllint",
            path
        ],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print("✓ YAML válido")
        return True

    print("✗ Error de sintaxis YAML")
    print(result.stdout)
    print(result.stderr)

    return False


def validate_all(path):

    return validate_yaml_syntax(path)

# def validate_kubernetes(path):

#     result = subprocess.run(
#         [
#             "kubectl",
#             "apply",
#             "--dry-run=client",
#             "--validate=false",
#             "-f",
#             path
#         ],
#         capture_output=True,
#         text=True
#     )

#     if result.returncode == 0:
#         print("✓ Kubernetes válido")
#         print(result.stdout)
#         return True

#     print("✗ Error de validación Kubernetes")
#     print(result.stderr)

#     return False


# def validate_all(path):

#     yaml_ok = validate_yaml_syntax(path)

#     k8s_ok = validate_kubernetes(path)

#     return yaml_ok and k8s_ok