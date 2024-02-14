from importlib.metadata import version, PackageNotFoundError
from os.path import join, exists
from .configuration import loadDeviceConfig

try:
    __version__ = version("sst_funcs")
except PackageNotFoundError:
    # package is not installed
    pass


ip = get_ipython()
startup_dir = join(f"{ip.ipython_dir}", f"profile_{ip.profile}", "startup")
config_file = join(startup_dir, "device_config.yaml")
if exists(config_file):
    print(f"Attempting to load objects in {config_file}")
    device_dict = loadDeviceConfig(config_file, ip.user_ns)
else:
    print(f"{config_file} does not exist!")

for key, dev in device_dict.items():
    globals()[key] = dev

# ip.user_ns['RE'] = RE
