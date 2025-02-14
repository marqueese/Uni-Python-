class StreamingAccount:
    def __init__(self):
        self._account_name = "guest"
        self._mem_type = "basic"
        self.stream_limit = 0


    def view_details(self):
        print(f"The current account belongs to {self.account_name}\n"
                  f"The member type of this account is {self.mem_type}\n"
                  f"The stream count is {self.stream_limit}\n")

    def upgrade_account(self):
        print(f"Current account type is {self.mem_type}")
        if self.mem_type == "Premium":
            print("You are already on a premium plan you cannot upgrade again\n")
        elif self.mem_type != "Premium":
            self.mem_type = "Premium"
            print(f"Upgrading account to {self.mem_type}\n")

    def stream_movie(self):
        if self.stream_limit > 5:
            print("You have reached your streaming limit")
        else:
            print("Streaming movie")
            self.stream_limit = self.stream_limit + 1

    @property #accesses private variables
    def account_name(self):
        return self._account_name

    @account_name.setter # use setter to alter the current stored variable in the function
    def account_name(self, name):
        self._account_name = name

    @property
    def mem_type(self):
        return self._mem_type

    @mem_type.setter
    def mem_type(self, mem_type):
        self._mem_type = mem_type

def main():
    account = StreamingAccount()

    account.account_name = "Alice"
    print(account.account_name)
    account.view_details()

    account.stream_movie()
    account.stream_movie()

    account.view_details()

    account.upgrade_account()

    account.view_details()

main()