import trimesh
import open3d as o3d
import numpy as np

model_path = r"C:\Users\ASUS\Documents\3_course\1_trimak\DataViz\fish\13001_Ryukin_Goldfish_v1_L3.obj"

# === 1. ЗАГРУЗКА МОДЕЛИ С ТРИАНГУЛЯЦИЕЙ ===
tm = trimesh.load(model_path, force='mesh', process=True)

print(f"Trimesh vertices: {tm.vertices.shape}")
print(f"Trimesh faces: {tm.faces.shape}")

# Конвертируем в Open3D
mesh = o3d.geometry.TriangleMesh(
    vertices=o3d.utility.Vector3dVector(tm.vertices),
    triangles=o3d.utility.Vector3iVector(tm.faces)
)

if not mesh.has_vertex_normals():
    mesh.compute_vertex_normals()

print("1) ИНФОРМАЦИЯ О МОДЕЛИ")
print(f"Количество вершин: {len(mesh.vertices)}")
print(f"Количество треугольников: {len(mesh.triangles)}")
print(f"Наличие цветов: {mesh.has_vertex_colors()}")
print(f"Наличие нормалей: {mesh.has_vertex_normals()}")

o3d.visualization.draw_geometries([mesh], window_name="Исходная модель")



# === 2. Преобразование в облако точек ===
pcd = mesh.sample_points_uniformly(number_of_points=5000)  # берём 5000 точек (можно изменить)

print("2) Преобразование в облако точек")
print(f"Количество точек: {len(pcd.points)}")
print(f"Наличие цвета: {pcd.has_colors()}")

o3d.visualization.draw_geometries([pcd], window_name="Облако точек")


# === 3. Реконструкция поверхности Poisson ===
pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.05, max_nn=30))

mesh_poisson, densities = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pcd, depth=8)
print(f"[INFO] Mesh Poisson создан с {len(mesh_poisson.vertices)} вершинами и {len(mesh_poisson.triangles)} треугольниками")

densities = np.asarray(densities)
density_threshold = np.quantile(densities, 0.05)  # убираем самые редкие точки
vertices_to_keep = densities > density_threshold
mesh_clean = mesh_poisson.select_by_index(np.where(vertices_to_keep)[0])

print("3) Реконструкция поверхности")
print(f"Количество вершин: {len(mesh_clean.vertices)}")
print(f"Количество треугольников: {len(mesh_clean.triangles)}")
print(f"Наличие цвета: {mesh_clean.has_vertex_colors()}")

o3d.visualization.draw_geometries([mesh_clean], window_name="Реконструированный Mesh")


# === 4. Вокселизация ===
voxel_size = 0.05  # размер одной ячейки
voxel_grid = o3d.geometry.VoxelGrid.create_from_point_cloud(pcd, voxel_size=voxel_size)

print("4) Вокселизация")
print(f"Количество вокселей: {len(voxel_grid.get_voxels())}")
print(f"Наличие цвета: {voxel_grid.has_colors()}")

o3d.visualization.draw_geometries([voxel_grid], window_name="Воксельная сетка")


# --- 5. Создание "плоскости" через тонкий box ---
plane_width = 12.0
plane_height = 12.0
plane_thickness = 0.01  # очень тонкий, будет выглядеть как плоскость
plane = o3d.geometry.TriangleMesh.create_box(width=plane_width, height=plane_height, depth=plane_thickness)

plane.translate((-plane_width/2, -plane_height/2, -0.5))  # сдвиг, чтобы центр совпадал с объектом

plane.paint_uniform_color([0.7, 0.7, 0.7])  # светло-серый

o3d.visualization.draw_geometries([mesh, plane], window_name="5) Добавление плоскости")


# --- 6. Клиппинг: оставляем вершины ниже плоскости z <= 0 ---
vertices = np.asarray(mesh.vertices)
triangles = np.asarray(mesh.triangles)

mask = vertices[:, 2] <= 0
old_to_new = -np.ones(len(vertices), dtype=int)
old_to_new[np.where(mask)[0]] = np.arange(np.sum(mask))

cropped_vertices = vertices[mask]
cropped_triangles = triangles[np.all(mask[triangles], axis=1)]
cropped_triangles = old_to_new[cropped_triangles]

cropped_mesh = o3d.geometry.TriangleMesh(
    vertices=o3d.utility.Vector3dVector(cropped_vertices),
    triangles=o3d.utility.Vector3iVector(cropped_triangles)
)

if not cropped_mesh.has_vertex_normals():
    cropped_mesh.compute_vertex_normals()

print("6) Обрезка по поверхности (клиппинг)")
print(f"Количество вершин: {len(cropped_mesh.vertices)}")
print(f"Количество треугольников: {len(cropped_mesh.triangles)}")
print(f"Наличие цветов: {cropped_mesh.has_vertex_colors()}")
print(f"Наличие нормалей: {cropped_mesh.has_vertex_normals()}")

o3d.visualization.draw_geometries([cropped_mesh], window_name="Модель после клиппинга")



# --- 7.Работа с цветом и экстремумами ---
# Задаём градиент по оси Z 
vertices = np.asarray(mesh.vertices)
z_min = vertices[:, 2].min()
z_max = vertices[:, 2].max()

colors = (vertices[:, 2] - z_min) / (z_max - z_min)
colors_rgb = np.zeros((len(vertices), 3))
colors_rgb[:, 0] = colors        # красный канал
colors_rgb[:, 2] = 1 - colors    # синий канал
mesh.vertex_colors = o3d.utility.Vector3dVector(colors_rgb)

z_idx_min = np.argmin(vertices[:, 2])
z_idx_max = np.argmax(vertices[:, 2])
min_point = vertices[z_idx_min]
max_point = vertices[z_idx_max]

print("7) Работа с цветом и экстремумами")
print(f"Минимум по Z: {min_point}")
print(f"Максимум по Z: {max_point}")

sphere_min = o3d.geometry.TriangleMesh.create_sphere(radius=0.05)
sphere_min.translate(min_point)
sphere_min.paint_uniform_color([0, 1, 0])  # зелёная сфера

sphere_max = o3d.geometry.TriangleMesh.create_sphere(radius=0.05)
sphere_max.translate(max_point)
sphere_max.paint_uniform_color([1, 0, 0])  # красная сфера

o3d.visualization.draw_geometries([mesh, sphere_min, sphere_max], window_name="Градиент и экстремумы")
