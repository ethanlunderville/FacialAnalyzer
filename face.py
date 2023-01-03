import os
import cv2
from measurementutil import Measurementutil
from dotutil import DotUtility


class Face():

    def __init__(self, image):
        
        self.image = cv2.imread(f'{os.environ["FACEPROJECTDIR"]}/faces/{image}')
        self.height, self.width, nan = self.image.shape
        self.rgb_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)

        self.MOUTH_LEFT_COORD = []
        self.MOUTH_TOP_COORD = []
        self.MOUTH_BOTTOM_COORD = []
        self.MOUTH_RIGHT_COORD = []
        self.NOSE_BRIDGE_CENTER_COORD = []
        self.NOSE_CENTER_COORD = []
        self.NOSE_LEFT_COORD = []
        self.NOSE_RIGHT_COORD = []
        self.CHIN_CENTER_COORD = []
        self.EYEBROW_MIDPOINT_COORD = []
        self.EYE_MIDPOINT_COORD = []
        self.CENTER_FOREHEAD_COORD = []
        self.RIGHT_EYE_LEFT_POINT_COORD = []
        self.RIGHT_EYE_RIGHT_POINT_COORD = []
        self.RIGHT_EYE_BOTTOM_POINT_COORD = []
        self.RIGHT_EYE_TOP_POINT_COORD = []
        self.LEFT_EYE_LEFT_POINT_COORD = []
        self.LEFT_EYE_RIGHT_POINT_COORD = []
        self.LEFT_EYE_BOTTOM_POINT_COORD = []
        self.LEFT_EYE_TOP_POINT_COORD = []

        self.LEFT_BROW_1_COORD = []
        self.LEFT_BROW_2_COORD = []
        self.LEFT_BROW_3_COORD = []
        self.LEFT_BROW_4_COORD = []
        self.LEFT_BROW_5_COORD = []

        self.RIGHT_BROW_1_COORD = []
        self.RIGHT_BROW_2_COORD = []
        self.RIGHT_BROW_3_COORD = []
        self.RIGHT_BROW_4_COORD = []
        self.RIGHT_BROW_5_COORD = []

        self.FACE_OUTLINE = {}
        # NOTE : COORDINATES MUST BE GENERATED BEFORE LIST INSERTION
        DotUtility.generate_coordinates(self)

        self.coordinates = [    
                                self.MOUTH_LEFT_COORD, self.MOUTH_TOP_COORD, self.MOUTH_BOTTOM_COORD, self.MOUTH_RIGHT_COORD, self.NOSE_BRIDGE_CENTER_COORD, 
                                self.NOSE_CENTER_COORD, self.NOSE_LEFT_COORD, self.NOSE_RIGHT_COORD, self.CHIN_CENTER_COORD, self.EYEBROW_MIDPOINT_COORD, 
                                self.EYE_MIDPOINT_COORD, self.CENTER_FOREHEAD_COORD, self.RIGHT_EYE_LEFT_POINT_COORD, self.RIGHT_EYE_RIGHT_POINT_COORD, 
                                self.RIGHT_EYE_BOTTOM_POINT_COORD, self.RIGHT_EYE_TOP_POINT_COORD, self.LEFT_EYE_LEFT_POINT_COORD, self.LEFT_EYE_RIGHT_POINT_COORD,
                                self.LEFT_EYE_BOTTOM_POINT_COORD, self.LEFT_EYE_TOP_POINT_COORD, self.LEFT_BROW_1_COORD,self.LEFT_BROW_2_COORD,self.LEFT_BROW_3_COORD,
                                self.LEFT_BROW_4_COORD, self.LEFT_BROW_5_COORD, self.RIGHT_BROW_1_COORD, self.RIGHT_BROW_2_COORD, self.RIGHT_BROW_3_COORD,
                                self.RIGHT_BROW_4_COORD,self.RIGHT_BROW_5_COORD
                            ]

    def draw_coordinates(self):
        DotUtility.draw_coordinates(self)
    def draw_line(self, coord1, coord2):
        Measurementutil.line_drawer(self, coord1, coord2)

        
    def show_face(self):
 
        cv2.imshow("Image", self.image)
        cv2.waitKey(0)

x = Face("image207.jpeg")

x.draw_line(x.EYE_MIDPOINT_COORD, x.NOSE_CENTER_COORD)
x.draw_coordinates()
x.show_face()