import zipfile


def extract_archive(archivepath, directory):
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(directory)


if __name__ == "__main__":
    extract_archive(archivepath=r'C:\Users\ARAVIND\PycharmProjects\Task\bonus\compressed.zip',
                    directory=r'C:\Users\ARAVIND\PycharmProjects\Task\bonus\Extract')
