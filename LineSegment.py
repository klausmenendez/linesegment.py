# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Point:

    def __init__(self, x_coord,y_coord):
        '''
        initial point

        :param x_coord: x coordinate of point
        :param y_coord: y coordinate of point
        '''
        self._x_coord=x_coord
        self._y_coord=y_coord
        

    def get_x_coord(self):
       return self._x_coord
    '''
    returns x coordinate of point
    '''
    def get_y_coord(self):
       return self._y_coord
    '''
    returns y coordinate of point
    '''
    def distance_to(self, point_object2):
        '''
        creates a point object and the finds its distance to another point the function is called on

        :param point_object2: 2nd point object
        :return:
        '''
        x2=point_object2.get_x_coord()
        y2=point_object2.get_y_coord()
        x1=self._x_coord
        y1=self._y_coord
        distance=((y2-y1)**(2)+(x2-x1)**(2))**(0.5)
        print(distance)


class LineSegment:
    def __init__(self, endpoint_1, endpoint_2):
        '''
        initial method
        :param endpoint_1: first point object
        :param endpoint_2: second point object
        '''
        self._endpoint_1 = endpoint_1
        self._endpoint_2 = endpoint_2

    def get_endpoint_1(self):
        return self._endpoint_1
    '''
    returns first endppoint
    '''

    def get_endpoint_2(self):
        return self._endpoint_2
    '''
    returns 2nd endpoint
    '''

    def length(self):
        return self._endpoint_1.distance_to(self._endpoint_2)
    '''
    Returns length of line segment from endpoint 1 to endpoint 2
    '''

    def slope(self):
        '''
        Finds slope of line segment between endpoint1 and endpoint2
        :return:
        '''
        x1=self._endpoint_1.get_x_coord()
        y1=self._endpoint_1.get_y_coord()
        x2=self._endpoint_2.get_x_coord()
        y2=self._endpoint_2.get_y_coord()
        slope = float((y2 - y1) / (x2 - x1))
        print(slope)

    def is_parallel_to(self,lseg1):
        '''
        Checks to see if 2 lines have the same slope and are parallel
        :param lseg1: line segment object passed as parameter
        :return:
        '''
        self._pair1=lseg1.get_endpoint_2()
        self._pair2=lseg1.get_endpoint_1()
        num2=(self._endpoint_2.get_y_coord()-self._endpoint_1.get_y_coord())/(self._endpoint_2.get_x_coord()-self._endpoint_1.get_x_coord())
        if (abs((float(self._pair1.get_y_coord()-self._pair2.get_y_coord())/(self._pair1.get_x_coord()-self._pair2.get_x_coord())-num2))<0.000001):
            print("true")
        else:
            print("false")
#endpoint1=Point(5,2)
#endpoint2=Point(6,4)
#endpoint3=Point(8,4)
#endpoint4=Point(9,2)
#new_line=LineSegment(endpoint1, endpoint2)
#new_Line1=LineSegment(endpoint3, endpoint4)
#new_Line1.is_parallel_to(new_line)





