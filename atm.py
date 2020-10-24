class ATM(object):
      def __init__(self, pin, atmcard):
            self.pin = pin
            self.atmcard = atmcard
      def start(self):
            print("started")
      def stop(self):
            print("stopped")
      def CashWithdrawl(self):
            print("$110 withdrawed")
            "Withdrawl functionality here"
      def BalanceEnquiry (self):
            print("$99999999999999999999 in bank")
            "Balance Enquiry functionality here"


audi = ATM(1234,"hdfc")

print(audi.start())
print(audi.stop())
print(audi.CashWithdrawl())
print(audi.BalanceEnquiry())