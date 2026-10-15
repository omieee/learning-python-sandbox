class Tx:
    def __init__(self, dbname: str) -> None:
        self.dbname = dbname

    def __enter__(self):
        print("Came inside ... Some real thing will happen here ...")
        return self.dbname + " is enabled"

    def __exit__(self, exc_type, exc, tb):
        if exc:
            print(f"Bro Some error happened, {self.dbname} not enabled")
            print(f"{exc_type}")
            print(f"{exc}")
            print(f"{tb}")
            return False  # Propagates the error program will crsh in this case
            # return True This wil makle program continue and will just print the error
            # and not crash the program also which file and line error came will also
            # not get printed
        else:
            print(
                f"You are done with your awesome work with {self.dbname}, closing off"
            )


class NewTx:
    def __init__(self, swallow: bool = False) -> None:
        self.events = []
        self.swallow = swallow

    def __enter__(self):
        self.events.append("BEGIN")
        print("We started..")
        return self.events

    def __exit__(self, exc_type, exc, tb):
        if exc:
            self.events.append("ROLLBACK")
        else:
            self.events.append("COMMIT")
        return self.swallow


if __name__ == "__main__":
    with Tx("some-awesome-db") as tix:
        print(tix)  # will print the line as well as some-awesome-db is enabled
        print("-" * 40)  # will print this line
        tix[100]  # this will throw error as that string is not 100 character long

    print(
        "Hello World"
    )  # beacuse set to false it will never run, program will crash early
