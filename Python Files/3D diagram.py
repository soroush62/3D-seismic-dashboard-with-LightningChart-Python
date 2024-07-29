import numpy as np
import lightningchart as lc
from scipy.interpolate import griddata

# Read the license key from a file
lc.set_license('my-license-key')

file_path = 'data_train.npz'
data = np.load(file_path)
array_3d = data['data']

def plot_slice_lc(data, slice_index, axis=0):
    if axis == 0:
        slice_data = data[slice_index, :, :]
    elif axis == 1:
        slice_data = data[:, slice_index, :]
    elif axis == 2:
        slice_data = data[:, :, slice_index]

    # Replace zero intensity areas with NaN to avoid displaying them
    slice_data[slice_data == 0] = np.nan
    slice_data = slice_data.astype(float)

    # Initialize a 3D chart
    chart = lc.Chart3D(
        theme=lc.Themes.Dark,
        title=f'3D Surface Plot of Slice along axis {axis} at index {slice_index}'
    )
    grid_size_x, grid_size_y = slice_data.shape
    surface_series = chart.add_surface_grid_series(
        columns=grid_size_x,
        rows=grid_size_y,
    )

    surface_series.set_start(x=0, z=0)
    surface_series.set_end(x=grid_size_x, z=grid_size_y)

    surface_series.set_step(x=1, z=1)
    surface_series.set_intensity_interpolation(True)
    surface_series.invalidate_intensity_values(slice_data.tolist())

    # Invalidate height map
    surface_series.invalidate_height_map(slice_data.tolist())

    surface_series.hide_wireframe()

    # Define custom palette
    surface_series.set_palette_colors(
        steps=[
            {"value": np.nanmin(slice_data), "color": lc.Color(0, 0, 255)},       # Blue for lower values
            {"value": np.nanpercentile(slice_data, 25), "color": lc.Color(0, 255, 255)},  # Cyan for lower mid values
            {"value": np.nanmedian(slice_data), "color": lc.Color(0, 255, 0)},   # Green for median values
            {"value": np.nanpercentile(slice_data, 75), "color": lc.Color(255, 255, 0)},  # Yellow for upper mid values
            {"value": np.nanmax(slice_data), "color": lc.Color(255, 0, 0)}       # Red for higher values
        ],
        look_up_property='value',
        percentage_values=False
    )

    # Invalidate intensity values (for color mapping)
    surface_series.invalidate_intensity_values(slice_data.tolist())

    chart.get_default_x_axis().set_title('X')
    chart.get_default_y_axis().set_title('Intensity')
    chart.get_default_z_axis().set_title('Y')

    chart.add_legend(data=surface_series)

    chart.open()

plot_slice_lc(array_3d, slice_index=55, axis=0)
plot_slice_lc(array_3d, slice_index=55, axis=1)
plot_slice_lc(array_3d, slice_index=55, axis=2)

