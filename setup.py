from setuptools import setup

setup(
    name='graphicone_models',
    url='https://github.com/trendvision/graphicone_models',
    packages=['graphicone_models'],
    install_requires=[
        'sqlalchemy',
        'graphicone_models @ git+https://github.com/trendvision/graphicone_models.git#egg=graphicone_models'
    ],
    version='0.1',
    license='TRV',
    description='all models',
)
