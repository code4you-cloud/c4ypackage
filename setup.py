from setuptools import setup, find_packages

setup(name='Measurements',
      url='https://github.com/revego/package_demo',
      author='John Ladan',
      author_email='jladan@uwaterloo.ca',
      # Needed to actually package something
      #packages=['capitalize', 'capitalize.test'],
      packages=['measure'],
      # Needed for dependencies
      install_requires=['numpy'],
      # *strongly* suggested for sharing
      version='0.1',
      # The license can be anything you like
      license='MIT',
      description='An example of a python package from pre-existing code',
      # We will also need a readme eventually (there will be a warning)
      long_description=open('README.txt').read(),
      # if there are any scripts
      scripts=['scripts/hello.py'],
)
