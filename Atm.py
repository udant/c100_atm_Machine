class atm(object):
      def __init__(self, pin, atmcard):
            self.pin = pin
            self.atmcard = atmcard
      def start(self):
            print("started")
      def stop(self):
            print("stopped")
      "Withdrawl functionality here"
      def CashWithdrawl(self):
            print("$110 withdrawed")
      
      "Balance Enquiry functionality here"
      def BalanceEnquiry (self):
            print("$99999999999999999999 in bank")
      

audi = atm(input("atm number:"),input("bank:"))

audi.start()
audi.stop()
audi.CashWithdrawl()
audi.BalanceEnquiry()