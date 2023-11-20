import nmap

class NetworkScanner:
    def __init__(self, target_network):
        self.target_network = target_network
        self.nm = nmap.PortScanner()

    def scan_devices(self):
        self.nm.scan(hosts=self.target_network, arguments='-sS -F -T4 -n --max-hostgroup 10')

        for host in self.nm.all_hosts():
            print(f"Dispositivo: {host}")
            try:
                host_info = self.nm[host]
            
                state = host_info.get('status', {}).get('state', 'No disponible')
                print(f"    Estado: {state}")

                if 'tcp' in host_info:
                    open_ports = host_info['tcp'].keys()
                    print(f"    Puertos abiertos: {', '.join(str(port) for port in open_ports)}")
                    self.scan_vulnerabilities(host, open_ports)
                else:
                    print("    No se encontraron puertos abiertos")
                    
                print("-----------------------------------------------")
            except:
                pass

    def scan_vulnerabilities(self, host, open_ports):
        ports_to_scan = ','.join(str(port) for port in open_ports)
        if ports_to_scan:
            print(f"Ejecutando Nmap scripts de vulnerabilidad para todos los puertos abiertos en {host}")
            self.nm.scan(hosts=host, ports=ports_to_scan, arguments='--script vuln')
            
            for port in open_ports:
                try:
                    script_output = self.nm[host]['tcp'][port]['script']
                    print(f"Resultados del escaneo de vulnerabilidad en el puerto {port}:\n{script_output}\n")
                except KeyError:
                    print(f"No se encontraron vulnerabilidades en el puerto {port} en {host}\n")
        else:
            print(f"No se encontraron puertos abiertos en {host}")

if __name__ == "__main__":
    # Poner tu IP o red a escanear (x.x.x.x o x.x.x.x/yy)
    # Si tarda mucho, poner la IP objetivo para agilizarlo
    target_network = '192.168.0.70'
    scanner = NetworkScanner(target_network)
    print("Iniciando escaneo de red...")
    scanner.scan_devices()
