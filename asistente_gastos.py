
# Pedimos el dinero inicial
saldo_inicial = float(input("¿Cuánto dinero tenés disponible al empezar? "))
saldo_actual = saldo_inicial

# Inicializamos los gastos en cero
alquiler = 0
comida = 0
servicios = 0
tarjeta = 0

# Saludo una sola vez
print("Hola, soy tu asistente de gastos.")
print("Cargá tus gastos y yo te hago las cuentas.")
print()

# Bucle del menú
while True:
    print("==== MENÚ ====")
    print("1 - Cargar gasto de ALQUILER")
    print("2 - Cargar gasto de COMIDA")
    print("3 - Cargar gasto de SERVICIOS")
    print("4 - Ver resumen completo")
    print("5 - cuota de TARJETA")
    print("0 - Salir")
    print()

    opcion = input("Elegí una opción escribiendo el número: ")

    # Opción 1 - Alquiler
    if opcion == "1":
        print("Vamos a cargar ALQUILER")
        monto = float(input("¿Cuánto pagaste de alquiler? "))
        alquiler = alquiler + monto
        saldo_actual = saldo_actual - monto
        print("✅ Gastaste: $", monto)
        print("💰 Te queda: $", saldo_actual)
        print()

    # Opción 2 - Comida
    elif opcion == "2":
        print("Vamos a cargar COMIDA")
        monto = float(input("¿Cuánto gastaste en comida? "))
        comida = comida + monto
        saldo_actual = saldo_actual - monto
        print("✅ Gastaste: $", monto)
        print("💰 Te queda: $", saldo_actual)
        print()

    # Opción 3 - Servicios
    elif opcion == "3":
        print("Vamos a cargar SERVICIOS")
        monto = float(input("¿Cuánto gastaste en servicios? "))
        servicios = servicios + monto
        saldo_actual = saldo_actual - monto
        print("✅ Gastaste: $", monto)
        print("💰 Te queda: $", saldo_actual)
        print()

    # Opción 4 - Resumen
    elif opcion == "4":
        print("\n=== RESUMEN COMPLETO ===")
        print("💵 Saldo inicial:   $", saldo_inicial)
        print("🏠 Alquiler:        $", alquiler)
        print("🍔 Comida:          $", comida)
        print("🔌 Servicios:       $", servicios)
        print("💳 □Tarjeta:       $", tarjeta)
        total_gastado = alquiler + comida + servicios + tarjeta
        print("--------------------------")
        print("💸 TOTAL GASTADO:   $", total_gastado)
        print("💰 SALDO ACTUAL:    $", saldo_actual)
        print()


    elif opcion =="5":
        print("Vamos a pagar tarjeta")
        monto = float(input("cuota de tatjeta"))
        tarjeta = tarjeta + monto
        saldo_actual = saldo_actual - monto
        print("✅ Gastaste: $", monto)
        print("💰 Te queda: $", saldo_actual)
        print()
        
    # Opción 0 - Salir
    elif opcion == "0":
        print("¡Chau! Vuelve pronto.")
        break

    # Opción inválida
    else:
        print("Esa opción no existe. Intentá de nuevo.")
        print()
