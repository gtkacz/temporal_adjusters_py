import setuptools

with open('README.md') as fh:
	long_description = fh.read()

with open('requirements.txt') as fh:
	requirements = fh.readlines()

setuptools.setup(
	long_description=long_description,
	long_description_content_type='text/markdown',
	packages=setuptools.find_packages(),
	py_modules=['temporal_adjuster', 'temporal_adjuster.common'],
	install_requires=requirements,
)
