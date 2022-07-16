from multiapp import MultiApp
from interfaces import home, equalization, segmentation, noise, histogram, apply_filter, brightness


app = MultiApp()

# add all apps
# app.add_app("Home", home.app)
app.add_app("Image Segmentation Tool", segmentation.app)
app.add_app("Reduce Periodic Noise Tool", noise.app)
app.add_app("Histogram Equalization Tool", equalization.app)
app.add_app("laplacian Filter Tool", apply_filter.app)
app.add_app("Show Image Histogram", histogram.app)
app.add_app("Brightness Adjustment Tool", brightness.app)

app.run()
