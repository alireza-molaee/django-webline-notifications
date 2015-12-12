from io import open
from distutils.core import setup

long_description = open('README.md', encoding="utf-8").read()

install_requires = [
    'django>=1.8'
]

setup(
    name='django_simple_notification',
    version='0.1',
    packages=['simple_notifications'],
    include_package_data=True,
    url='https://github.com/alireza-molaee/w_notifications',
    license='GNU General Public License (GPL)',
    author='alireza molaee',
    author_email='alirezamolaii@gmail.com',
    description='A simple Django app which allow you notify everything to user or users',
    long_description=long_description,
    install_requires=install_requires,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
)
