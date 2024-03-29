from Sala import sala


sala = sala.Sala("porky123", 2, False, 30, ["porky 123", "joacocucho 45"] )


cartas_porky = sala.ronda.repartir_cartas()
cartas_guijaj = sala.ronda.repartir_cartas()

print("Mis Cartas:", cartas_porky ,"\n")
print("Cartas Guijaa:", cartas_guijaj ,"\n")
print("Cartas baneadas: ", sala.ronda.banned_cards ,"\n") 