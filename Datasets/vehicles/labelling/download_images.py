from simple_image_download import simple_image_download as simp

response = simp.simple_image_download

path_to_save = "C:\\Users\\pylko\\Repo_YOLO_project\\Object-detection-project\\Datasets\\vehicles\\labelling\\simple_image\\"
keywords = ["trucks in the traffic"]

for kw in keywords:
    response().download(kw, 150)
