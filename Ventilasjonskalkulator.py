import math
from decimal import *


class Duct:

    def __init__(self, airflow):

        try:
            airflow = int(airflow)
        except ValueError:
            airflow = 0

        self._airflow = airflow/3600

    def flowsetter(self, newflow):

        try:
            newflow = int(newflow)
        except ValueError:
            print("Luftmengde må være heltall")

        self.airflow = newflow


class RoundDuct(Duct):

    def __init__(self, airflow, diameter):

        try:
            diameter = int(diameter)/1000
        except ValueError:
            diameter = None

        self._diameter = diameter

        if self._diameter is not None:
            self._radius = diameter / 2
            self._airflow = int(airflow) / 3600
            self._area = math.pi * (self._radius**2)
            self._ductspeed = self._airflow/self._area
        else:
            self._radius = None

        self._isturbulent = False
        self._pressureGradient = None

        super(RoundDuct, self).__init__(airflow)

    def dimsetter_round(self, diameter):
        try:
            diameter = int(diameter)
        except ValueError:
            print("Dimensjon må være et heltall")

        self._diameter = diameter/1000
        self._radius = diameter/2000

    def flowcalc(self):

        if self._radius > 0:
            return '{0:.2f}'.format(self._ductspeed) + ' m/s'

        else:
            return "Feil med kanal"

    def pressureCalc(self):

        reynoldsnumber = (self._ductspeed * self._diameter) / (15.1 * (10 ** -6))

        if reynoldsnumber > 2300:
            self._isturbulent = True
            frictionfactor = 0.02

        else:
            frictionfactor = 64/reynoldsnumber

        self._pressureGradient = frictionfactor * ((1.2 * (self._ductspeed ** 2)) / (self._diameter * 2))

        return '{0:.2f}'.format(self._pressureGradient) + ' Pa/m'

    def returnTurbulent(self):

        if self._isturbulent:
            return "Turbulent"

        else:
            return "Laminær"


class RectDuct(Duct):

    def __init__(self, airflow, dim_x, dim_y):

        try:
            dim_x = int(dim_x)
            dim_y = int(dim_y)
        except ValueError:
            dim_x = None
            dim_y = None

        self._dim_x = dim_x
        self._dim_y = dim_y
        self._ductspeed_hydraulic = None
        self._hydraulic_rad = None
        self._airflow = airflow

        super(RectDuct, self).__init__(airflow)

    def dimsetter_rect(self, dim_x, dim_y):
        try:
            dim_x = int(dim_x)
            dim_y = int(dim_y)
        except ValueError:
            print("Dimensjoner må være heltall")

        self._dim_x = dim_x
        self._dim_y = dim_y

    def flowcalc(self):

        if self._dim_x > 0 and self._dim_y > 0:
            self._area = (self._dim_x / 1000)*(self._dim_y / 1000)
            self._ductspeed = self._airflow/self.area
            self._hydraulic_rad = ((2 * self._dim_x * self._dim_y) / (self._dim_x + self._dim_y)) / 2000
            self._ductspeed_hydraulic = self._airflow / (math.pi * (self._hydraulic_rad ** 2))
            self._ductspeed = self._airflow / self.area

            return self._ductspeed

        else:
            return "Feil med Kanal"


