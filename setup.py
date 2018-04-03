from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ansible-tools-pass',
    version='0.0.8',
    description='Keyring integration and local execution wrappers for Ansible (PASS FORK)',
    long_description=long_description,
    url='https://github.com/toke/ansible-tools',
    author='Thomas Kerpe',
    author_email='toke@toke.de',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: System :: Systems Administration',
    ],
    keywords='ansible local pass tools wrapper',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=['passlib'],
    entry_points={
        'console_scripts': [
            'ansible-local=ansibletools.cli.ansible_local:main',
            'ansible-mkpasswd=ansibletools.cli.ansible_mkpasswd:main',
            'ansible-vault-helper=ansibletools.cli.ansible_vault_helper:main',
            'vaultify=ansibletools.cli.vaultify:main',
        ],
    },
)
