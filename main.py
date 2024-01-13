# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main


print(add_time("11:59 PM", "24:05"))
print(add_time("3:30 PM", "2:12"))
print(add_time("9:15 PM", "5:30"))
print(add_time("5:01 AM", "0:00"))
print(add_time("2:59 AM", "24:00", "saturDay"))


# Run unit tests automatically
main(module='test_module', exit=False)