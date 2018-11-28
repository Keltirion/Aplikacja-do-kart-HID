from cx_Freeze import setup, Executable
additional_mods = ['numpy.core._methods', 'numpy.lib.format']

setup(name='HID creator',
      version='1.0',
      description='Face detection, HID preparation',
      options={'build_exe': {'includes': additional_mods}},
     executables= [Executable('App.py')])