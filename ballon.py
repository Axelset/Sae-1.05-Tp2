import csv

donnees=[]
altitude=[]
temperature_interne=[]
temperature_externe=[]



with open('Donnees.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=';')
    for row in reader:
        donnees.append(row)





altitude=[float(donnees[i+1][3]) for i in range(len(donnees)-1)]
print(altitude)
temperature_interne=[float(donnees[i+1][5]) for i in range(len(donnees)-1)]
print(temperature_interne)
temperature_externe=[float(donnees[i+1][6]) for i in range(len(donnees)-1)]
print(temperature_externe)

from matplotlib import pyplot as plt

plt.plot(temperature_interne,altitude,color='b')
plt.plot(temperature_externe,altitude,color='r')

plt.title("Température sur l'altitude")
plt.ylabel('Altitude')
plt.xlabel('Température interne en bleu et tempéraure externe en rouge')

plt.show()