import pandas as pd
import matplotlib.pyplot as plt
import csv

df = pd.read_csv("data.csv", encoding="ISO-8859-1")

str = '''
A
Afghanistan
Albania
Algeria
Andorra
Angola
Antigua and Barbuda
Argentina
Armenia
Australia
Austria
Azerbaijan
Bahamas
Bahrain
Bangladesh
Barbados
Belarus
Belgium
Belize
Benin
Bhutan
Bolivia
Bosnia and Herzegovina
Botswana
Brazil
Brunei
Bulgaria
Burkina Faso
Burundi
Cabo Verde
Cambodia
Cameroon
Canada
Central African Republic (CAR)
Chad
Chile
China
Colombia
Comoros
Democratic Republic of the Congo
Republic of the Congo
Costa Rica
Cote d'Ivoire
Croatia
Cuba
Cyprus
Czech Republic
Denmark
Djibouti
Dominica
Dominican Republic
Ecuador
Egypt
El Salvador
Equatorial Guinea
Eritrea
Estonia
Ethiopia
Fiji
Finland
France
Gabon
Gambia
Georgia
Germany
Ghana
Greece
Grenada
Guatemala
Guinea
Guinea-Bissau
Guyana
Haiti
Honduras
Hungary
Iceland
India
Indonesia
Iran
Iraq
Ireland
Israel
Italy
Jamaica
Japan
Jordan
Kazakhstan
Kenya
Kiribati
Kosovo
Kuwait
Kyrgyzstan
Laos
Latvia
Lebanon
Lesotho
Liberia
Libya
Liechtenstein
Lithuania
Luxembourg
Macedonia (FYROM)
Madagascar
Malawi
Malaysia
Maldives
Mali
Malta
Marshall Islands
Mauritania
Mauritius
Mexico
Micronesia
Moldova
Monaco
Mongolia
Montenegro
Morocco
Mozambique
Myanmar (formerly Burma)
Namibia
Nauru
Nepal
Netherlands
New Zealand
Nicaragua
Niger
Nigeria
North Korea
Norway
Oman
Pakistan
Palau
Palestine
Panama
Papua New Guinea
Paraguay
Peru
Philippines
Poland
Portugal
USA
UK
Russia
Greenland
Ukraine
Spain
Antarctica
Sweden
Venezuela
Suriname
Guyane
Uruguay
Uganda
South Sudan
Saudi Arabia
Tanzania
Somalia
South Africa
Zambia
Zimbabwe
Turkey
Turkmenistan
Romania
Uzbekistan
Tajikistan
Slovenia
Slovakia
Switzerland
Macedonia
Sudan
Central African Republic
Yemen
Myanmar
Thailand
Ivory Coast
Sierra Leone
Togo
Senegal
Tunisia
Vietnam
Guyana
Syria
Serbia
South Korea
'''
lst = str.split("\n")
lst = lst[2:-1]

country_dict = {}
for i in lst:
    count = df["location"].str.count(i).sum()
    country_dict[i] = count
country_dict

with open("data3.csv", 'w', encoding="ISO-8859-1") as outcsv:
        writer = csv.writer(outcsv, delimiter=',', lineterminator='\n')
        writer.writerow(["country", "count"])
        for key, value in country_dict.items():
            writer.writerow([key, value])
