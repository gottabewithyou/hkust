# HKUST Virtual Courses Database Lookup

Navigating the approved mappings in the [credit transfer database](https://registry.hkust.edu.hk/useful-tools/credit-transfer/database-institution) for virtual courses can be challenging, especially when trying to fulfil requirements for your major, minor, extended major, or common core. This tool simplifies the process, giving all required courses of a chosen programme with approved virtual course mappings.

*Please be reminded that you are only allowed to transfer a maximum of 6 credits for each of the minor, extended major or common core.*

## Installation

Two packages are needed: [requests](https://requests.readthedocs.io/en/latest/user/install) and [pdfplumber](https://pypi.org/project/pdfplumber/0.1.2). Please use the package manager [pip](https://pip.pypa.io/en/stable) to install them.

```bash
pip install requests
```
```bash
pip install pdfplumber
```

## Acknowledgements

This project was made possible thanks to the efforts of @evnchn, who scraped the data for the `virtual_course.json` file.
