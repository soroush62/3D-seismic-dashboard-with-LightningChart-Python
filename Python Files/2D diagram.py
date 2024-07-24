# import numpy as np
# import lightningchart as lc
# from scipy.interpolate import griddata

# with open('D:/Computer Aplication/WorkPlacement/Projects/shared_variable.txt', 'r') as f:
#     mylicensekey = f.read().strip()
# lc.set_license(mylicensekey)

# # Load the data
# file_path = 'D:/Computer Aplication/WorkPlacement/Projects/Project6/Dataset/data_train.npz'
# data = np.load(file_path)

# array_3d = data['data']

# # Print the shape of the array
# print("Shape of the array:", array_3d.shape)

# # Function to plot a 2D slice using LightningChart
# def plot_slice_lc(data, slice_index, axis=0):
#     if axis == 0:
#         slice_data = data[slice_index, :, :]
#     elif axis == 1:
#         slice_data = data[:, slice_index, :]
#     elif axis == 2:
#         slice_data = data[:, :, slice_index]

#     # Create interpolated grid
#     grid_size = 1000  # Reduced grid size for faster processing
#     x_values = np.linspace(0, slice_data.shape[1], slice_data.shape[1])
#     y_values = np.linspace(0, slice_data.shape[0], slice_data.shape[0])
#     grid_x, grid_y = np.mgrid[min(x_values):max(x_values):complex(grid_size), min(y_values):max(y_values):complex(grid_size)]
#     grid_z = griddata((np.repeat(x_values, slice_data.shape[0]), np.tile(y_values, slice_data.shape[1])), slice_data.ravel(), (grid_x, grid_y), method='linear')

#     # Convert numpy int to Python int
#     grid_z = grid_z.astype(float)

#     # Initialize a chart
#     chart = lc.ChartXY(theme=lc.Themes.Dark, title=f'2D Slice along axis {axis} at index {slice_index}')

#     # Create HeatmapGridSeries
#     heatmap = chart.add_heatmap_grid_series(
#         columns=grid_size,
#         rows=grid_size,
#     )

#     # Set start and end coordinates
#     heatmap.set_start(x=min(x_values), y=min(y_values))
#     heatmap.set_end(x=max(x_values), y=max(y_values))

#     # Set step size
#     heatmap.set_step(x=(max(x_values) - min(x_values)) / grid_size, y=(max(y_values) - min(y_values)) / grid_size)

#     # Enable intensity interpolation
#     heatmap.set_intensity_interpolation(True)

#     # Invalidate intensity values
#     heatmap.invalidate_intensity_values(grid_z)

#     # Hide wireframe
#     heatmap.hide_wireframe()

#     # Define custom palette to match the second image
#     custom_palette = [
#         {"value": np.nanmin(grid_z), "color": lc.Color(255, 0, 0)},     # Black  
#         {"value": np.nanmax(grid_z), "color": lc.Color(255, 255, 255)}  # White  
#     ]

#     heatmap.set_palette_colors(
#         steps=custom_palette,
#         look_up_property='value',
#         interpolate=True
#     )

#     # Set axis titles
#     chart.get_default_x_axis().set_title('X-axis')
#     chart.get_default_y_axis().set_title('Y-axis')

#     # Set axis limits based on the actual data ranges
#     chart.get_default_x_axis().set_interval(min(x_values), max(x_values))
#     chart.get_default_y_axis().set_interval(min(y_values), max(y_values))
#     chart.add_legend(data=heatmap)

#     chart.open()

# # Plot a slice from each axis
# plot_slice_lc(array_3d, slice_index=50, axis=0)
# plot_slice_lc(array_3d, slice_index=50, axis=1)
# plot_slice_lc(array_3d, slice_index=50, axis=2)




# import numpy as np
# import lightningchart as lc

# # Read the license key from a file
# with open('D:/Computer Aplication/WorkPlacement/Projects/shared_variable.txt', 'r') as f:
#     mylicensekey = f.read().strip()
# lc.set_license(mylicensekey)

# file_path = 'D:/Computer Aplication/WorkPlacement/Projects/Project6/Dataset/data_train.npz'
# data = np.load(file_path)
# array_3d = data['data']

# # Function to plot a 2D slice using LightningChart
# def plot_slice_lc(data, slice_index, axis=0):
#     if axis == 0:
#         slice_data = data[slice_index, :, :]
#     elif axis == 1:
#         slice_data = data[:, slice_index, :]
#     elif axis == 2:
#         slice_data = data[:, :, slice_index]
    
#     # Convert slice_data to a JSON serializable format
#     slice_data = slice_data.astype(np.float64)
    
#     # Initialize a chart
#     chart = lc.ChartXY(
#         title=f'2D Slice along axis {axis} at index {slice_index}',
#         theme=lc.Themes.Dark
#     )
    
#     # Create HeatmapGridSeries
#     heatmap = chart.add_heatmap_grid_series(
#         columns=slice_data.shape[1],
#         rows=slice_data.shape[0],
#     )
    
#     # Set start and end coordinates
#     heatmap.set_start(x=0, y=0)
#     heatmap.set_end(x=slice_data.shape[1], y=slice_data.shape[0])
    
#     # Set step size
#     heatmap.set_step(x=1, y=1)
    
#     # Enable intensity interpolation
#     heatmap.set_intensity_interpolation(True)
    
#     # Invalidate intensity values
#     heatmap.invalidate_intensity_values(slice_data.tolist())
    
#     # Hide wireframe
#     heatmap.hide_wireframe()
    
#     # Define custom palette to match Matplotlib's 'viridis'
#     custom_palette = [
#         {"value": np.nanmin(slice_data), "color": lc.Color(68, 1, 84)},
#         {"value": np.percentile(slice_data, 25), "color": lc.Color(58, 82, 139)},
#         {"value": np.percentile(slice_data, 50), "color": lc.Color(32, 144, 140)},
#         {"value": np.percentile(slice_data, 75), "color": lc.Color(94, 201, 98)},
#         {"value": np.nanmax(slice_data), "color": lc.Color(253, 231, 37)}
#     ]
    
#     heatmap.set_palette_colors(
#         steps=custom_palette,
#         look_up_property='value',
#         interpolate=True
#     )
    
#     # Set axis titles
#     chart.get_default_x_axis().set_title('X-axis')
#     chart.get_default_y_axis().set_title('Y-axis')
    
#     # Open the chart
#     chart.open()

# # Plot a slice from each axis
# plot_slice_lc(array_3d, slice_index=50, axis=0)
# plot_slice_lc(array_3d, slice_index=50, axis=1)
# plot_slice_lc(array_3d, slice_index=50, axis=2)




import numpy as np
import lightningchart as lc
import pandas as pd
from scipy.interpolate import griddata

with open('D:/Computer Aplication/WorkPlacement/Projects/shared_variable.txt', 'r') as f:
    mylicensekey = f.read().strip()
lc.set_license(mylicensekey)

file_path = 'D:/Computer Aplication/WorkPlacement/Projects/Project6/Dataset/data_train.npz'
data = np.load(file_path)

array_3d = data['data']

# Print the shape of the array
print("Shape of the array:", array_3d.shape)

# Function to plot a 2D slice with LightningChart
def plot_slice_lc(data, slice_index, axis=0):
    if axis == 0:
        slice_data = data[slice_index, :, :]
    elif axis == 1:
        slice_data = data[:, slice_index, :]
    elif axis == 2:
        slice_data = data[:, :, slice_index]
    
    # Filter out the zero intensity areas
    slice_data = slice_data.astype(float)  # Convert to float to handle NaN properly
    slice_data[slice_data == 0] = np.nan
    
    chart = lc.ChartXY(
        title=f'2D Slice along axis {axis} at index {slice_index}',
        theme=lc.Themes.Dark
    )

    grid_size_x, grid_size_y = slice_data.shape
    heatmap = chart.add_heatmap_grid_series(
        columns=grid_size_x,
        rows=grid_size_y,
    )

    heatmap.set_start(x=0, y=0)
    heatmap.set_end(x=grid_size_x, y=grid_size_y)

    heatmap.set_step(x=1, y=1)
    heatmap.set_intensity_interpolation(True)
    heatmap.invalidate_intensity_values(slice_data.tolist())

    heatmap.hide_wireframe()

    custom_palette = [
        {"value": np.nanmin(slice_data), "color": lc.Color(68, 1, 84)},
        {"value": np.percentile(slice_data, 25), "color": lc.Color(58, 82, 139)},
        {"value": np.percentile(slice_data, 50), "color": lc.Color(32, 144, 140)},
        {"value": np.percentile(slice_data, 75), "color": lc.Color(94, 201, 98)},
        {"value": np.nanmax(slice_data), "color": lc.Color(253, 231, 37)}
    ]

    heatmap.set_palette_colors(
        steps=custom_palette,
        look_up_property='value',
        interpolate=True
    )

    chart.get_default_x_axis().set_title('X-axis')
    chart.get_default_y_axis().set_title('Y-axis')
    chart.add_legend(data=heatmap)

    chart.open()

# Plot a slice from each axis
plot_slice_lc(array_3d, slice_index=50, axis=0)
plot_slice_lc(array_3d, slice_index=50, axis=1)
plot_slice_lc(array_3d, slice_index=50, axis=2)
