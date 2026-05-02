from typing import Generator


def factorials(n: int) -> Generator[int]:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        yield factorial


def main() -> None:
    for i, factorial in enumerate(factorials(100)):
        print(f"{i + 1}! = {factorial}")


if __name__ == "__main__":
    main()
