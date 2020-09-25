from setuptools import setup

setup(
    name='graphicone_monitors',
    url='https://github.com/trendvision/graphicone_monitors',
    packages=['graphicone_monitors'],
    install_requires=[
        'sqlalchemy',
        'graphicone_models @ git+https://github.com/trendvision/graphicone_models.git#egg=graphicone_models'
    ],
    version='0.1',
    license='TRV',
    description='Common methods for monitors',
)
