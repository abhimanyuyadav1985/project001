from setuptools import setup, find_packages

setup(
    name='project001',
    version='0.0.1',
    description='Test package',
    long_description='for PyPI project',
    url='https://github.com/abhimanyuyadav1985/project001/',
    author='Abhimanyu Yadav',
    authoer_email='yadav.manyu@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Programming Language :: python :: 3.6'
    ],
    keywords='project1 cirrus',
    packages=find_packages(exclude=['docs', 'tests*']),
    install_requires=['numpy'],
    package_data={
        'sample': ['dfsd.dat']
    },
    data_files=None,
    entry_points={
        'console_scripts': [
            'hello=fsdfs:fafd'
        ]
    }
)
