import numpy as np
import lightningchart as lc
import pandas as pd
from scipy.interpolate import griddata

lc.set_license('my-license-key')

file_path = 'data_train.npz'
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
        {"value": np.nanmin(slice_data), "color": lc.Color(0, 0, 255)},       # Blue for lower values
        {"value": np.nanpercentile(slice_data, 25), "color": lc.Color(0, 255, 255)},  # Cyan for lower mid values
        {"value": np.nanmedian(slice_data), "color": lc.Color(0, 255, 0)},   # Green for median values
        {"value": np.nanpercentile(slice_data, 75), "color": lc.Color(255, 255, 0)},  # Yellow for upper mid values
        {"value": np.nanmax(slice_data), "color": lc.Color(255, 0, 0)}       # Red for higher values
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

plot_slice_lc(array_3d, slice_index=50, axis=0)
plot_slice_lc(array_3d, slice_index=50, axis=1)
plot_slice_lc(array_3d, slice_index=50, axis=2)



