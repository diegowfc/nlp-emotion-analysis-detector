from setuptools import setup, find_packages

setup(
    name='emotion-analysis-detector',
    version='0.1',
    packages=find_packages(include=['EmotionDetection', 'EmotionDetection.*']),
    install_requires=[
        'Flask>=2.0.0',  # Especifica a versão mínima do Flask
        'requests>=2.25.0',  # Especifica a versão mínima do requests
    ],
    description='An emotion analysis detector application developed while learning Flask and Python for AI in Coursera/IBM',
    author='Diego William Fernandes',
    author_email='',
    url='https://github.com/diegowfc/nlp-emotion-analysis-detector',
    include_package_data=True,
    package_data={
        '': ['static/*.css', 'static/*.js', 'templates/*.html'],
    },
)
