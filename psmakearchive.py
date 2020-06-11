from abc import ABC, abstractmethod
from zipfile import ZipFile
from tarfile import TarFile
from glob import glob


class UnSupportedArchiveError(Exception):
    """custom/user defined exception"""


class ArchiveManager(ABC):
    """abstract class"""

    @abstractmethod
    def save(self):
        """abstract method"""


class ZipArchive(ArchiveManager):
    """concrete class"""

    def __init__(self, name):
        self.name = name

    def save(self, *args):
        with ZipFile(self.name, mode='w') as zf:
            for filename in args:
                zf.write(filename)
                print(f'{filename}: added into {self.name}')


class TarArchive(ArchiveManager):
    def __init__(self, name):
        self.name = name

    def save(self, *args):
        with TarFile(self.name, mode='w') as tf:
            for filename in args:
                tf.add(filename)
                print(f'{filename}: added into {self.name}')


def make_archive(archive_name, archive_type='zip'):
    """factory method"""

    if archive_type == 'zip':
        return ZipArchive(archive_name)
    elif archive_type == 'tar':
        return TarArchive(archive_name)
    else:
        raise UnSupportedArchiveError(f'unsupport archive format : {archive_type}')


if __name__ == '__main__':
    try:
        archive = make_archive('source.zip')
        archive.save(*glob('*.py'))
        print()
        archive = make_archive('source.tar', archive_type='tar')
        archive.save(*glob('*.py'))

    except UnSupportedArchiveError as error:
        print(error)
