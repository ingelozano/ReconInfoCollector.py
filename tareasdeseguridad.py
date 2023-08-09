import subprocess

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout, result.stderr
    except Exception as e:
        return None, str(e)

def main():
    domain = input("Ingrese el dominio a analizar: ")

    print("\n** ADVERTENCIA **")
    print("Este script se proporciona con fines educativos y para demostrar habilidades técnicas.")
    print("El mal uso de esta herramienta para actividades ilegales o no autorizadas está estrictamente prohibido.")
    print("NO me hago responsable del uso indebido de esta herramienta.")
    print("\nRealizando análisis de información para el dominio:", domain)

    # Realizar nslookup para obtener información del DNS
    nslookup_command = f"nslookup {domain}"
    nslookup_stdout, nslookup_stderr = run_command(nslookup_command)

    # Realizar whois para obtener información sobre el dominio
    whois_command = f"whois {domain}"
    whois_stdout, whois_stderr = run_command(whois_command)

    # Realizar traceroute para obtener la ruta de red al dominio
    traceroute_command = f"tracert {domain}"
    traceroute_stdout, traceroute_stderr = run_command(traceroute_command)

    print("\nResultados de nslookup:")
    print(nslookup_stdout)

    print("\nResultados de whois:")
    print(whois_stdout)

    print("\nResultados de traceroute:")
    print(traceroute_stdout)

if __name__ == "__main__":
    main()
