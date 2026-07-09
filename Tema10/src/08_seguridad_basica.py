"""
Tema 10 - Biblioteca estándar
Laboratorio 10: seguridad básica con hashlib, hmac, secrets y random.

Objetivo:
    Diferenciar generación aleatoria segura, huellas criptográficas,
    comparación HMAC y uso pseudoaleatorio no crítico.
"""

import hashlib
import hmac
import secrets
import random


print("=== 1. Token temporal seguro con secrets ===")
token = secrets.token_urlsafe(12)
print("Token temporal seguro:", token)

print("\n=== 2. Huella SHA-256 con hashlib ===")
huella = hashlib.sha256(token.encode("utf-8")).hexdigest()
print("SHA-256:", huella)

print("\n=== 3. Firma HMAC de un mensaje ===")
clave = secrets.token_bytes(16)
mensaje = b"operacion=backup;host=srv-db-01"
firma = hmac.new(clave, mensaje, hashlib.sha256).hexdigest()
print("Firma HMAC:", firma)

print("\n=== 4. random para uso no crítico ===")
servidor = random.choice(["srv-web-01", "srv-web-02", "srv-web-03"])
print("Servidor elegido para prueba no crítica:", servidor)
