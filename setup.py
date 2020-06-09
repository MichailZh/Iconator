from setuptools import setup

setup(
    name='iconatron',
    version='0.1.3',
    description='icons package for django',
    license='MIT',
    author='MichailZh',
    author_email='michail.zhukov@gmail.com',
    url='https://github.com/MichailZh/Iconatron.git',
    download_url = 'https://github.com/MichailZh/Iconatron/archive/V_02.tar.gz',
    packages = ['iconatron', 'iconatron.templatetags'],
    include_package_data=True,
    keywords = ['ICONS', 'DJANGO'],
    zip_safe=False,
    classifiers=[
                    'Development Status :: 3 - Alpha',
                    'Intended Audience :: Developers',
                    'Topic :: Software Development :: Build Tools',
                    'License :: OSI Approved :: MIT License',
                    'Programming Language :: Python :: 3.8',
                ],
)