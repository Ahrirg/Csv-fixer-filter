import csv
import os
import asyncio
ViableFFList = []
DIRNAME = os.getcwd()

# async def print(StartingFolder):
#     print(f'Some thread is Starting folder - {StartingFolder}')


# Open file
def ReadData(Name):
    file = open(Name)
    type(file)
    csvreader = csv.reader(file)

    # Opening file
    header = []
    header = next(csvreader)

    for row in csvreader:
        if row[6] == "English" and int(row[11]) > 40:
            x = { "link": row[2], "category": row[7], "description": row[16] }
            ViableFFList.append(x)
    file.close()


def ReadFolder(FolderName):
    FolderDir = f'{DIRNAME}/folder/{FolderName}'
    ListofFiles = os.listdir(FolderDir)

    for x in ListofFiles:
        print(x)
        ReadData(f'{FolderDir}/{x}')


folderiai = os.listdir(f'{DIRNAME}/folder')


# create new file
def irasomifaila(name):
    with open(f'{name}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['link', 'category', 'description'])

        for x in ViableFFList:
            writer.writerow([x['link'], x['category'], x['description']])


for x in folderiai:
    print('FOLDERIS' + x)
    ReadFolder(x)
    
    irasomifaila(x)

    ViableFFList = []

print("BAIGEM DARBA!")