# DutWrapper

This library provides wrapper (for this repository - crawl data from a page) for access for some features in [DUT Student page - Da Nang University of Technology](http://sv.dut.udn.vn).

## Versions

- Dart: 0.3.1
- .NET: 1.6.1
- Python: 1.7.0
- Java: 1.7.5

## Building requirements

- Dart:
  - Follow [this document](https://docs.flutter.dev/) for building or using this library.
- .NET:
  - One of following application:
    - Visual Studio 2017 or later (for .NET Core/.NET Framework support) (recommend).
    - Visual Studio Code with C# extension (you will still need .NET SDK).
  - .NET 6 SDK (you can edit .csproj for using .NET Core 3.1, but you may need to change something in this project).
    - **Remember:** Download .NET SDK (not .NET Runtime) for building library and application.
- Java:
  - JDK (tested with Eclipse Temurin JDK with Hotspot v17.0.2 and v8).
  - [Jsoup](https://jsoup.org/) (included in library)
  - [OkHttp3](https://square.github.io/okhttp/) (included in library)
- Python:
  - Python 3.10 (3.8 still works, but need to modify if got errors).
  - [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)
  - [View here](src/python/requirements.txt) for get all libraries requirements.

## License and credits

[MIT](LICENSE) (click to view licenses)

Click links below for view which this repository used:
- ~~Dart~~ (no third-party library used)
- [.NET](CREDIT.md#dotnet)
- [Java](CREDIT.md#java)
- [Python](CREDIT.md#python)

## FAQ

### Can I port back .NET project to .NET Framework?
- Yes, you can port back, but you need to do it manually. I don't provide .NET Framework version anymore.

### Branch in dutwrapper?
- "main": Default branch and main release.
- "nightly": Nightly branch. This code isn't tested and use it at your own risk.

### Wiki, or manual for how-to-use?
- In a plan, please be patient.

### Latest change log?

- To view log for all versions, click for:
  - [Dart](docs/CHANGELOG-DART.md)
  - [.NET](docs/CHANGELOG-DOTNET.md)
  - [Python](docs/CHANGELOG-PYTHON.md)
  - [Java](docs/CHANGELOG-JAVA.md)

## Copyright?

- This project - dutwrapper - is not affiliated with [Da Nang University of Technology](http://sv.dut.udn.vn).
- DUT, Da Nang University of Technology, web materials and web contents are trademarks and copyrights of [Da Nang University of Technology](http://sv.dut.udn.vn) school.
