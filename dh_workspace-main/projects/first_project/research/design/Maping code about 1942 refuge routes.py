<!-- ...existing code... -->
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>1942年河南饥荒难民逃难路线地图</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" />
    <script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js"></script>
    <style>
        #map { height: 600px; width: 100%; }
    </style>
</head>
<body>
    <h1>1942年河南饥荒难民逃难路线地图</h1>
    <p>此地图基于历史记录展示1942年河南大饥荒期间难民的主要逃难路线，主要从河南省向陕西省方向逃荒，途径陇海铁路等路径。数据来源于历史报道，如难民爬火车逃往陕西。</p>
    <div id="map"></div>
    <script>
        // 在 DOM 完成加载后再初始化地图，避免 "map container not found" 错误
        document.addEventListener('DOMContentLoaded', function () {
            var map = L.map('map').setView([34.5, 111.5], 6);  // 中心于河南/陕豫交界附近

            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                maxZoom: 19,
                attribution: '&copy; OpenStreetMap contributors'
            }).addTo(map).on('tileerror', function (err) {
                console.error('Tile load error:', err);
            });

            // 标记主要地点
            L.marker([34.7466, 113.6254]).addTo(map).bindPopup('郑州：饥荒中心，难民聚集地');
            L.marker([34.3416, 108.9398]).addTo(map).bindPopup('西安：主要逃荒目的地，在陕西');

            // 绘制逃难路线（简化路径：郑州 -> 洛阳 -> 三门峡/灵宝 -> 潼关 -> 西安）
            var refugeePath = [
                [34.7466, 113.6254],  // 郑州
                [34.6578, 112.4475],  // 洛阳（更精确）
                [34.7746, 111.2006],  // 三门峡/灵宝（近似）
                [34.5134, 110.2423],  // 潼关（近似）
                [34.3416, 108.9398]   // 西安
            ];

            var polyline = L.polyline(refugeePath, {color: 'red', weight: 3, opacity: 0.8}).addTo(map);
            polyline.bindPopup('难民逃难路线：从河南向陕西，主要沿陇海铁路西逃');

            map.fitBounds(polyline.getBounds());
        });
    </script>
</body>
</html>
<!-- ...existing code... -->