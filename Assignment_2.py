foot = float (input('Enter Length in foot : '))
km = foot / 3281
meter = foot * 0.3048
centimeter = foot * 30.48
millimeter = foot * 304.4
micrometer = foot * 304800
nanometer = foot * 3.04800000
mile = foot * 0.000189394
yard = foot / 3
inch = foot * 12
print(f'{round(foot)} foots are = {km} KM')
print(f'{round(foot)} foots are = {meter} Meter')
print(f'{round(foot)} foots are = {centimeter} Centimeter')
print(f'{round(foot)} foots are = {millimeter} Millimeter')
print(f'{round(foot)} foots are - {micrometer} Micrometer')
print(f'{round(foot)} foots are = {nanometer} Nanometer')
print(f'{round(foot)} foots are = {mile} Mile')
print(f'{round(foot)} foots are = {yard} Yard')
print(f'{round(foot)} foots are = {inch} Inch')