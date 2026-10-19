from datetime import date
from product import Product
from policyholder import Policyholder
from payment import Payment


def main():
    # Creating the product and changing its premium.
    health = Product("P01", "Health Cover", 100)
    health.update("Family Health", 120)

    amina = Policyholder("M01", "Amina Hassan")
    david = Policyholder("M02", "David Mushi")
    amina.register(health)
    david.register(health)

    # Amina pays on time; David pays after a late fee is added.
    payment1 = Payment(amina, date(2026, 10, 15))
    payment1.reminder()
    payment1.process()

    payment2 = Payment(david, date(2026, 10, 15))
    payment2.reminder()
    payment2.apply_penalty(date(2026, 10, 19))
    payment2.process()

    amina.suspend()
    print("Amina's status:", amina.status)
    amina.reactivate()

    amina.display_details()
    david.display_details()

    health.suspend()
    print("\nProduct status:", health.status)
    try:
        grace = Policyholder("M03", "Grace John")
        grace.register(health)
    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()
