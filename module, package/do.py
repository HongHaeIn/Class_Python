import my_module as mm

mm.해인이1()
mm.해인이2()
print(mm.date)

import travel.gangreung as ga
gp = ga.GangreungPackage()
print(gp)

from travel import gangreung
gp = gangreung.GangreungPackage()
print(gp)

from travel.gangreung import GangreungPackage
gp = GangreungPackage()


from travel import ilsan
ilsan.이지()

import travel.ilsan
travel.ilsan.이지()

from travel.ilsan import 이지
이지()

from travel import *
ilsan.이지()
gp = gangreung.GangreungPackage()
print(gp)
