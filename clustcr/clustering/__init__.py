import warnings

# Suppress the multiprocessing fork warning in Python 3.12+
# This warning occurs when using multiprocessing.Pool with fork start method
# in a multi-threaded environment, which is common with numpy/scipy imports
warnings.filterwarnings(
    "ignore",
    message=".*multi-threaded.*fork.*",
    category=DeprecationWarning,
    module="multiprocessing.popen_fork"
)
