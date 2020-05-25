from setuptools import setup, find_packages



setup(
    name='iconator',
    version='0.0.1',
    description='icons package for django',
    license='MIT',
    author='MichailZh',
    author_email='michail.zhukov@gmail.com',
    url='https://github.com/MichailZh/Iconator.git',
    download_url = 'https://github.com/MichailZh/Iconator/archive/v_01.tar.gz',
    packages = find_packages(include=['templatetags','icons','iconator']),
    # package_data={'iconator':['LICENSE.txt']},
    # include_package_data=True,
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