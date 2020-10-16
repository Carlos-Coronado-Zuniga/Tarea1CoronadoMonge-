from setuptools import setup

setup(
    name='gitandpip',
    version='0.0.1',
    description='My package...ok fine',
    url='git@github.com/Carlos-Coronado-Zuniga/Tarea1CoronadoMonge_1erintento.git',
    author='Carlos_Adrian_Emanuel_Joseph',
    author_email='az36226@gmail.com',
    license='unlicense',
    packages=setuptools.find_packages(),
    install_requires=['sys','opencv-python','pillow','tabulate' , 'playsound','argparse', 'time','numpy'],
    python_requires='>=3.6',
    scripts=['gitandpip/funciones.py'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
