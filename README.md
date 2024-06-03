# DutWrapper - Python

An unofficial wrapper for easier to use at [sv.dut.udn.vn - Da Nang University of Technology student page](http://sv.dut.udn.vn).

## Version

[![](https://img.shields.io/github/v/release/dutwrapper/dutwrapper-python?label=release)](https://github.com/dutwrapper/dutwrapper-python/releases)

[![](https://img.shields.io/github/v/tag/dutwrapper/dutwrapper-python?label=pre-release)](https://github.com/dutwrapper/dutwrapper-python/releases)

## Requirements
- Python 3.10 (3.8 still works, but need to modify if you got errors).
- [requirements.txt](requirements.txt) for get all libraries requirements.

## FAQ

### Which branch should I use?
- `stable`/`main`: Default branch and main release. This is **my recommend branch**.
- `draft`: Alpha branch. This branch is used for update my progress and it's very unstable. Use it at your own risk.

### I received error about login while running AccountTest?
- Did you mean `dut_account environment variable not found. Please, add or modify this environment in format "username|password"`?
- If so, you will need to add environment variable named `dut_account` with syntax `studentid|password`. You can add them in .env file.

### Wiki or manual for this package?
- In a plan, please be patient.

### I'm got issue with this library. Which place can I reproduce issue for you?
- You can report this via [issue tab](https://github.com/dutwrapper/dutwrapper-python/issues) on this repository.

## Changelog

### 1.8.0
- Added `fetch_account_training_status()` function in `Accounts`.
- Adjust and resolved issues in all functions in `Accounts`.
- Removed `GetCurrentWeek()` function in `Utils`. This will be back soon.
- Improved unittest.

### Older version
- To view log for all versions, [click here](CHANGELOG.md)

## Credits and license?
- License: [**MIT**](LICENSE)
- DISCLAIMER:
  - This project - dutwrapper - is not affiliated with [Da Nang University of Technology](http://sv.dut.udn.vn).
  - DUT, Da Nang University of Technology, web materials and web contents are trademarks and copyrights of [Da Nang University of Technology](http://sv.dut.udn.vn) school.
- Used third-party dependencies:
  - [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup): Licensed under the MIT license.
