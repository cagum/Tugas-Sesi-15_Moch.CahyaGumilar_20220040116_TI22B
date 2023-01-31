import matplotlib as pyplot
import pandas


# Data Mahasiswa
mahasiswa = pandas.read_csv("./Data_siswa_unp.csv")
jurusan = mahasiswa['Jurusan']
jumlah = mahasiswa['Jumlah']

# in pie mode
pyplot.pie(jumlah, labels=jurusan)
pyplot.show()


# Data Mobil
carsData = pandas.read_csv("data_mobil.csv")

# update
carsData.loc[ (carsData['Transmisi'] == 1), 'Transmisi' ] = 'Automatic'
carsData.loc[ (carsData['Transmisi'] == 0), 'Transmisi' ] = 'Manual'
print(carsData)

# insert
carsData = carsData.assign( harga_1 = carsData['harga_juta'] * 0.98 )
carsData = carsData.assign( harga_2 = carsData['harga_1'] * 0.98 )
print(carsData)

# filter
filter_1 = carsData[ carsData['tahun'] > 2015 ]
filter_2 = carsData[ (carsData['harga_juta'] >= 200) & (carsData['harga_juta'] <= 250) ]

data_group = filter_2.groupby('tahun')[['harga_juta', 'harga_1', 'harga_2']].mean().astype(int)
data_group.plot(kind='bar')
pyplot.xlabel('Tahun')
pyplot.ylabel('Harga (dalam juta)')
pyplot.title('Rata-Rata Harga Mobil Bekas')

pyplot.show()