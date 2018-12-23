from setuptools import setup

setup(name='monitorPower',
      version='0.1',
      description='Monitors power status',
      url='http://github.com/luiarthur/monitorPower',
      author='Arthur Lui',
      author_email='luiarthur@gmail.com',
      license='MIT',
      packages=['monitorPower'],
      install_requires=['psutil']
      zip_safe=False)
