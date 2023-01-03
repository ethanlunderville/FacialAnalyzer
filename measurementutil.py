
import cv2
class Measurementutil:  

    @classmethod
    def line_drawer(self, face, coord1, coord2):

        cv2.line(face.image, coord1, coord2, (255,255,255), 1) 

    @classmethod
    def align_face(self, coord1, coord2):
        
        leftEyeX,leftEyeY = eyePoints[0]
        rightEyeX, rightEyeY = eyePoints[1]

