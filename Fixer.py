# gets all of .csv files and makes them comma seperated, only use if needed, plius keep in mind this changes "," to "_"
REPLACE = "	"

import os

DIRNAME = os.path.dirname(os.path.realpath(__file__))

List = os.listdir(DIRNAME)

os.mkdir(f'{DIRNAME}/Fixed')

for x in List:
    if x[-4:] == ".csv":
        print(f'Fixing [{x}]')
        file = open(f'{DIRNAME}/{x}', 'r')
        AllofData = file.read().replace(',','_')
        FixedData = AllofData.replace(REPLACE, ',')

        fixedfile = open(f'{DIRNAME}/Fixed/FIXED-{x}', 'w')

        fixedfile.write(FixedData)

        fixedfile.close()
        file.close()

