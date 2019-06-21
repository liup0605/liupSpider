from setuptools import setup, find_packages

setup(
    name = "liupSpider",
    version = "1.0.0",
    keywords = ("pip", "requests","aiohttp", "spider"), 
    description = "liupSpider",
    long_description = "Aiohttp is encapsulated to keep the speed of asynchronism, and it can be used as simple and convenient as requests.",
    url = "https://github.com/liup0605/liupSpider",
    author = "liup",
    author_email = "peng_l666@126.com",
    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ['aiohttp','lxml']
)
