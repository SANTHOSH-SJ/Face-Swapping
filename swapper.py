import cv2
from face_swap import swap_faces

# Read images
source_image = cv2.imread("assets/image.jpg")
dest_image = cv2.imread("assets/image1.jpg") 

# Swap faces
img_changed_face, img2_changed_face = swap_faces(source_image, dest_image)

# write output to file
cv2.imwrite('results/result.png', img2_changed_face)
