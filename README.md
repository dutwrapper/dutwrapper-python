# DutWrapper

An unofficial wrapper for easier to use at [sv.dut.udn.vn - Da Nang University of Technology student page](http://sv.dut.udn.vn).

## Version

[![](https://img.shields.io/github/v/release/dutwrapper/dutwrapper-python?label=release)](https://github.com/dutwrapper/dutwrapper-python/releases)

[![](https://img.shields.io/github/v/tag/dutwrapper/dutwrapper-python?label=pre-release)](https://github.com/dutwrapper/dutwrapper-python/releases)

## Requirements
- Python 3.10 (3.8 still works, but need to modify if you got errors).

## FAQ

## Where can I found library changelog?
If you want to:
- View major changes: [Click here](CHANGELOG.md).
- View entire source code changes: [Click here](https://github.com/dutwrapper/dutwrapper-python/commits).
  - You will need to change branch if you want to view changelog for stable/draft version.

## Branch in dutwrapper?
- `stable`/`main`: Default branch and main release.
- `draft`: Alpha branch. This branch is used for update my progress and it's very unstable. Use it at your own risk.

### I received error about login while running AccountTest?
- Did you mean `dut_account environment variable not found. Please, add or modify this environment in format "username|password"`?
- If so, you will need to add environment variable named `dut_account` with syntax `studentid|password`. You can add them in `.env` file.

### Wiki or manual for this package?
- In a plan, please be patient.

### I'm got issue with this library. Which place can I reproduce issue for you?
- If you found a issue, you can report this via [issue tab](https://github.com/dutwrapper/dutwrapper-python/issues) on this repository.

## Credits and license?
- License: [**MIT**](LICENSE)
- DISCLAIMER:
  - This project - dutwrapper - is not affiliated with [Da Nang University of Technology](http://sv.dut.udn.vn).
  - DUT, Da Nang University of Technology, web materials and web contents are trademarks and copyrights of [Da Nang University of Technology](http://sv.dut.udn.vn) school.
- Used third-party dependencies:
  - [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup): Licensed under the MIT license
  - [certifi](https://github.com/certifi/python-certifi): Licensed under the [Mozilla Public License 2.0 (MPL 2.0) license](https://github.com/certifi/python-certifi/blob/master/LICENSE)
  - [charset_normalizer](https://github.com/jawah/charset_normalizer): Licensed under the [MIT license](https://github.com/jawah/charset_normalizer/blob/master/LICENSE)
  - [idna](https://github.com/kjd/idna): Licensed under the [BSD 3-Clause license](https://github.com/kjd/idna/blob/master/LICENSE.md)
  - [lxml](https://github.com/lxml/lxml): Licensed under the [BSD-3-Clause license](https://github.com/lxml/lxml/blob/master/LICENSE.txt)
  - [requests](https://github.com/psf/requests): Licensed under the [Apache-2.0 license](https://github.com/psf/requests/blob/main/LICENSE)
  - [soupsieve](https://github.com/facelessuser/soupsieve): Licensed under the [MIT license](https://github.com/facelessuser/soupsieve/blob/main/LICENSE.md)
  - [urllib3](https://github.com/urllib3/urllib3): Licensed under the [MIT license](https://github.com/urllib3/urllib3/blob/main/LICENSE.txt)
