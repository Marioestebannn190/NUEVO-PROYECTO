
productos = {
    "jeans": 125000,
    "camisa": 45000,
    "polo": 30000
}
total = 0

cantidad_jeans = 2
total += productos["jeans"] * cantidad_jeans

cantidad_camisas = 2
total += productos["camisa"] * cantidad_camisas

cantidad_polos = 1
total += productos["polo"] * cantidad_polos

descuento_polo = 0
if cantidad_polos > 0:
    descuento_polo = total * 0.05
    total -= descuento_polo

descuento_monto = 0
if total > 200000:
    descuento_monto = total * 0.30
    total -= descuento_monto

print("          FACTURA               ")
print("Cliente: Pedro Ramirez")
print(f"Jeans ({cantidad_jeans} unidades): ${productos['jeans'] * cantidad_jeans:,}")
print(f"Camisas ({cantidad_camisas} unidades): ${productos['camisa'] * cantidad_camisas:,}")
print(f"Polo ({cantidad_polos} unidades): ${productos['polo'] * cantidad_polos:,}")
if descuento_polo > 0:
    print(f"Descuento por polo: ${descuento_polo:,.2f}")
if descuento_monto > 0:
    print(f"Descuento por monto: ${descuento_monto:,.2f}")
print(f"Total a pagar: ${total:,.2f}")


