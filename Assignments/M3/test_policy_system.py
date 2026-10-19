import unittest
from datetime import date
from product import Product
from policyholder import Policyholder
from payment import Payment


class PolicyTests(unittest.TestCase):
    def setUp(self):
        self.product = Product("P1", "Health", 100)
        self.member = Policyholder("M1", "Jane Doe")
        self.member.register(self.product)
        self.payment = Payment(self.member, date(2026, 10, 15))

    def test_payment_cannot_be_repeated(self):
        self.payment.process()
        with self.assertRaises(ValueError):
            self.payment.process()
        self.assertEqual(self.member.total_paid, 100)

    def test_penalty_only_once_and_after_due_date(self):
        self.payment.apply_penalty(date(2026, 10, 15))
        self.assertEqual(self.payment.penalty, 0)
        self.payment.apply_penalty(date(2026, 10, 16))
        self.payment.apply_penalty(date(2026, 10, 17))
        self.payment.process()
        self.assertEqual(self.member.total_paid, 110)

    def test_paid_bill_has_no_penalty(self):
        self.payment.process()
        self.payment.apply_penalty(date(2026, 10, 20))
        self.assertEqual(self.payment.penalty, 0)

    def test_member_suspension(self):
        self.member.suspend()
        with self.assertRaises(ValueError):
            self.payment.process()
        self.member.reactivate()
        self.payment.process()
        self.assertTrue(self.payment.paid)

    def test_product_suspension(self):
        self.product.suspend()
        with self.assertRaises(ValueError):
            Policyholder("M2", "John Doe").register(self.product)
        with self.assertRaises(ValueError):
            self.payment.process()

    def test_existing_bill_keeps_its_price(self):
        self.product.update("Family Health", 150)
        self.payment.process()
        self.assertEqual(self.member.total_paid, 100)
        self.assertEqual(Payment(self.member, date(2026, 11, 15)).amount, 150)


if __name__ == "__main__":
    unittest.main()
