import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cicc_colors",
    version="0.2.0",
    author="Pengcheng Song",
    author_email="smth_spc@hotmail.com",
    description="Library of color palettes for CICC WM slides, reports and tables.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nyuspc/cicc_colors",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "Intended Audience :: Financial and Insurance Industry",
        "Topic :: Multimedia :: Graphics",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
