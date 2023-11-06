from varasto import Varasto

def print_varasto_info(varasto, nimi):
    print(f"{nimi} getterit:")
    print(f"saldo = {varasto.saldo}")
    print(f"tilavuus = {varasto.tilavuus}")
    print(f"paljonko_mahtuu = {varasto.paljonko_mahtuu()}")

def test_varasto_operations():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehua}")
    print(f"Olutvarasto: {olutta}")

    print_varasto_info(olutta, "Olut")
    print_varasto_info(mehua, "Mehu")

    print("Mehu setterit:")
    print("Lisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}")
    print("Otetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}")

def test_error_cases():
    print("Virhetilanteita:")
    virhe_varasto = Varasto(-100.0)
    print(virhe_varasto)

    virhe_olutta = Varasto(100.0, -50.7)
    print(virhe_olutta)

def main():
    test_varasto_operations()
    test_error_cases()

if __name__ == "__main__":
    main()
