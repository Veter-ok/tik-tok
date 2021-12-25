from colorama import Back, Fore, Style

print(Fore.RED + "красный текст")
print(Back.GREEN + "текст с зелёным фоном")
print(Style.DIM + Back.RESET + Fore.YELLOW + "бледно-жёлтый текст")
print(Style.RESET_ALL)
print("нормальный текст")