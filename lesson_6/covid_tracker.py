from covid import Covid

country = input()
info = Covid().get_status_by_country_name(country)

print("Заболело - "+str(info['active']))
print("Выздоровело - "+str(info['recovered']))
print("Умерло - "+str(info['deaths']))