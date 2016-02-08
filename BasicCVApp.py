import SimpleCV

# init camera
cam = SimpleCV.Camera()

# for constant photo taking:
#   sudo apt-get install cron
#   then use the command "crontab -e"
#   add the following line (without the '#' to the end)
#   * * * * * /usr/bin/python /path/to/BasicCVApp.py

# take a picture
img = cam.getImage()
img2 = img.copy()
img3 = img.copy()
img4 = img.copy()

# the following samples of things you can do to the pictures below
# were found based on documentation and samples from the SimpleCV website

# facial recognition, use haarcascades_cuda (SimpleCV compatible)
faces = img2.findHaarFeatures("/home/linaro/Desktop/haarcascade_frontalface_alt.xml")
	
# draw green boxes around faces
green = (0, 255, 0)	
for f in faces:
    print "face at", str(f.coordinates()) # prints the location of a face
    f.draw(green)

# white line drawings
img3 = img3.edges(t1=125)

# grayscale
img4 = img4.grayscale()

img.save("/home/linaro/Pictures/my_image.png")
img2.save("/home/linaro/Pictures/my_faces.png")
img3.save("/home/linaro/Pictures/my_edges.png")
img4.save("/home/linaro/Pictures/my_grayscale.png")