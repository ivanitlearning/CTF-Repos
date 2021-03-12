import os
import shutil


def main():
        for root, directories, files in os.walk("/var/www/dev.sneakycorp.htb"):
                for directory in directories:
                        try:
                                shutil.rmtree(os.path.join(root, directory))
                        except PermissionError:
                                pass
                for file in files:
                        try:
                                os.remove(os.path.join(root, file))
                        except PermissionError:
                                print(os.path.join(root, file))


if __name__ == "__main__":
        main()