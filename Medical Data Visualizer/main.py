# This entrypoint file to be used in development. Start by reading README.md
import medical_data_visualizer
from unittest import main
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Test your function by calling it here
medical_data_visualizer.draw_cat_plot()
medical_data_visualizer.draw_heat_map()

# Run unit tests automatically
main(module='test_module', exit=False)