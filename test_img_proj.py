from georef.operators import Georef, Projector, ProjectionGrid
import cv2
from pathlib import Path


# camera parameters
f_camera_parameters = 'camera_parameters_cam39.json'

# read camera georef parameters
georef_params = Georef.from_param_file(f_camera_parameters)

# read image to project
# f_img = Path('/home/florent/Projects/St_tropez/Garonnette_2/images/no_blurry_stab_edited_luigi/A_Garonnette_2_2fps_600s_20250620_04_00.jpg')
f_img = Path('A_CAM39_20250620_040000_d10a4849aebf_raw.jpeg')
img = cv2.imread(f_img)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# z
# z = 0.2
z = 0.0

# projection grid
projection_grid = ProjectionGrid(12, 230, 0.5, -45, 35, 0.5, z)

# projector
projector = Projector(georef_params, projection_grid)

# project image
img_proj = projector.project_image(img, z=z)

# save image
# projector.to_jpeg('PA_Garonnette_2_2fps_600s_20250620_04_00.jpg')
projector.to_png('PA_Garonnette_2_2fps_600s_20250620_04_00.png')