import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point

# 气象站：俄语名称 + 经纬度
station_coords = {
    "Пекин": (116.4074, 39.9042), "Шанхай": (121.4737, 31.2304), "Тяньцзинь": (117.3616, 39.3434),
    "Шицзячжуан": (114.5149, 38.0428), "Баодин": (115.4646, 38.8744), "Цанчжоу": (116.8709, 38.3044),
    "Лаотин": (118.9113, 39.4210), "Вэйчан": (119.1071, 36.7093), "Синтай": (114.5048, 37.0706),
    "Таншань": (118.1802, 39.6309), "Циндао": (120.3826, 36.0671), "Вэйфан": (119.1618, 36.7069),
    "Яньчжоу": (116.8336, 35.5520), "Цзинань": (117.0009, 36.6758), "Хуэйминь": (117.5150, 37.4880),
    "Хайян": (121.1684, 36.7764), "Чжэнчжоу": (113.6254, 34.7466), "Аньян": (114.3931, 36.0977),
    "Синьсян": (113.9268, 35.3030), "Гуши": (115.6540, 32.1711), "Наньян": (112.5283, 32.9907),
    "Сихуа": (114.5240, 33.7758), "Нанкин": (118.7969, 32.0603), "Сюйчжоу": (117.2906, 34.2127),
    "Ганьюй": (119.1305, 34.8392), "Лиян": (119.4860, 31.4168), "Бэнбу": (117.3893, 32.9155),
    "Фуянь": (115.8142, 32.8970), "Хэфэй": (117.2272, 31.8206), "Лиши": (111.1342, 36.8555),
    "Тайюань": (112.5492, 37.8570), "Цзесю": (111.9125, 37.0276), "Юйсянь": (113.4126, 38.2892),
    "Юйшэ": (112.9794, 36.8418), "Юньчэн": (111.0069, 35.0263), "Яньчэн": (120.1616, 33.3474)
}

# 转为 GeoDataFrame
df = gpd.GeoDataFrame(
    {"name": list(station_coords.keys())},
    geometry=[Point(lon, lat) for lon, lat in station_coords.values()],
    crs="EPSG:4326"
)

# 读取中国地图边界
world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
china = world[world["name"] == "China"]

# 绘图
fig, ax = plt.subplots(figsize=(12, 10))
china.plot(ax=ax, color="white", edgecolor="black")
df.plot(ax=ax, color="red", markersize=40)

# 添加城市名称标注（俄语）
for x, y, label in zip(df.geometry.x, df.geometry.y, df["name"]):
    ax.text(x + 0.2, y, label, fontsize=8, fontname='DejaVu Sans')

# 设定显示区域
ax.set_xlim(105, 125)
ax.set_ylim(30, 42)
ax.set_title("Карта метеостанций Китая", fontsize=14)
ax.axis("off")

# 保存图像
plt.savefig("china_meteostations_ru.png", dpi=300)
plt.savefig("china_meteostations_ru.pdf", dpi=300)
plt.show()
