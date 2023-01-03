import os
import cv2
import mediapipe as mp
from dotutility import DotUtility


class Face():

    def __init__(self, image):
        
        self.image = cv2.imread(f'{os.environ["FACEPROJECTDIR"]}/faces/{image}')
        self.height, self.width, nan = self.image.shape
        self.rgb_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)

        self.MOUTH_LEFT_TUPLE = []
        self.MOUTH_TOP_TUPLE = []
        self.MOUTH_BOTTOM_TUPLE = []
        self.MOUTH_RIGHT_TUPLE = []
        self.NOSE_BRIDGE_CENTER_TUPLE = []
        self.NOSE_CENTER_TUPLE = []
        self.NOSE_LEFT_TUPLE = []
        self.NOSE_RIGHT_TUPLE = []
        #self.LEFT_CHEEK_CENTER_TUPLE = []
        #self.LEFT_CHEEKBONE_TUPLE = []
        #self.LEFT_JAW_CORNER_TUPLE = []
        #self.LEFT_JAW_CENTER_TUPLE = []
        #self.RIGHT_CHEEK_CENTER_TUPLE = []
        #self.RIGHT_CHEEKBONE_TUPLE = []
        #self.RIGHT_JAW_CORNER_TUPLE = []
        #self.RIGHT_JAW_CENTER_TUPLE = []
        #self.LEFT_CHIN_TUPLE = []
        #self.RIGHT_CHIN_TUPLE = []
        #self.BOTTOM_CHIN_TUPLE = []
        self.CHIN_CENTER_TUPLE = []
        self.EYEBROW_MIDPOINT_TUPLE = []
        self.EYE_MIDPOINT_TUPLE = []
        self.CENTER_FOREHEAD_TUPLE = []
        #self.LEFT_TEMPLE_HAIRLINE_TUPLE = []
        #self.RIGHT_TEMPLE_HAIRLINE_TUPLE = []
        self.LEFT_EYEBROW_RIGHT_POINT_TUPLE = []
        self.LEFT_EYEBROW_TRANSITION_POINT_TUPLE = []
        self.LEFT_EYEBROW_LEFT_POINT_TUPLE = []
        self.RIGHT_EYEBROW_LEFT_POINT_TUPLE = []
        self.RIGHT_EYEBROW_TRANSITION_POINT_TUPLE = []
        self.RIGHT_EYEBROW_RIGHT_POINT_TUPLE = []
        self.RIGHT_EYE_LEFT_POINT_TUPLE = []
        self.RIGHT_EYE_RIGHT_POINT_TUPLE = []
        self.RIGHT_EYE_BOTTOM_POINT_TUPLE = []
        self.RIGHT_EYE_TOP_POINT_TUPLE = []
        self.LEFT_EYE_LEFT_POINT_TUPLE = []
        self.LEFT_EYE_RIGHT_POINT_TUPLE = []
        self.LEFT_EYE_BOTTOM_POINT_TUPLE = []
        self.LEFT_EYE_TOP_POINT_TUPLE = []

        # NOTE : COORDINATES MUST BE GENERATED BEFORE LIST INSERTION
        DotUtility.generate_coordinates(self)
        self.coordinates = [ self.MOUTH_LEFT_TUPLE, self.MOUTH_TOP_TUPLE, self.MOUTH_BOTTOM_TUPLE, self.MOUTH_RIGHT_TUPLE, self.NOSE_BRIDGE_CENTER_TUPLE, 
                                self.NOSE_CENTER_TUPLE, self.NOSE_LEFT_TUPLE, self.NOSE_RIGHT_TUPLE, self.LEFT_CHEEK_CENTER_TUPLE, self.LEFT_CHEEKBONE_TUPLE, self.LEFT_JAW_CORNER_TUPLE, 
                                self.LEFT_JAW_CENTER_TUPLE, self.RIGHT_CHEEK_CENTER_TUPLE, self.RIGHT_CHEEKBONE_TUPLE, self.RIGHT_JAW_CORNER_TUPLE, self.RIGHT_JAW_CENTER_TUPLE, self.LEFT_CHIN_TUPLE, 
                                self.RIGHT_CHIN_TUPLE, self.BOTTOM_CHIN_TUPLE, self.CHIN_CENTER_TUPLE, self.EYEBROW_MIDPOINT_TUPLE, self.EYE_MIDPOINT_TUPLE, self.CENTER_FOREHEAD_TUPLE, 
                                self.LEFT_TEMPLE_HAIRLINE_TUPLE, self.RIGHT_TEMPLE_HAIRLINE_TUPLE, self.LEFT_EYEBROW_RIGHT_POINT_TUPLE, self.LEFT_EYEBROW_TRANSITION_POINT_TUPLE, self.LEFT_EYEBROW_LEFT_POINT_TUPLE, 
                                self.RIGHT_EYEBROW_LEFT_POINT_TUPLE, self.RIGHT_EYEBROW_TRANSITION_POINT_TUPLE, self.RIGHT_EYEBROW_RIGHT_POINT_TUPLE, self.RIGHT_EYE_LEFT_POINT_TUPLE, self.RIGHT_EYE_RIGHT_POINT_TUPLE, 
                                self.RIGHT_EYE_BOTTOM_POINT_TUPLE, self.RIGHT_EYE_TOP_POINT_TUPLE, self.LEFT_EYE_LEFT_POINT_TUPLE, self.LEFT_EYE_RIGHT_POINT_TUPLE, self.LEFT_EYE_BOTTOM_POINT_TUPLE, self.LEFT_EYE_TOP_POINT_TUPLE ]
        DotUtility.draw_coordinates(self)
        
    def show_coordinates(self):
 
        cv2.imshow("Image", self.image)
        cv2.waitKey(0)

x = Face("image3.jpeg")
x.show_coordinates()