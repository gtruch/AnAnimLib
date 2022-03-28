# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 11:33:09 2021

@author: gtruch
"""
# START
import ananimlib as al

rect = al.Rectangle([1,1])

al.Animate(
    al.AddAnObject(rect),
    al.MoveTo(rect,[-3.0,0.0]),
    al.RunParallel(
        al.Move(rect, [6,0], duration=1.0),
        al.Rotate(rect, 2*3.1415, duration=1.0),
    ),
    al.Wait(1.0)
)
        
al.play_movie()
# END
