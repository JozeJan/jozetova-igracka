import os

fileslist = []
fileslistaaaa = []
async def list_files(path='./audiofiles/'):
    for entry in os.scandir(path):
        if entry.is_file():
            fileslist.append(entry.path)
        elif entry.is_dir():
            await list_files(entry.path)
    return fileslist

