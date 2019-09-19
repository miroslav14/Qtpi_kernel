from ipykernel.kernelapp import IPKernelApp
from . import QtpiKernel

IPKernelApp.launch_instance(kernel_class=QtpiKernel)
